"""Check this example bundle's links, source fidelity, and yield arithmetic.

Run with Python 3 and PyYAML: python docs/ontology-examples/check.py
This is an example checker, not a complete OKF or ontology validator.
"""

import json
import math
import re
from pathlib import Path
from urllib.parse import urlsplit

import yaml


ROOT = Path(__file__).resolve().parent / "bundle"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def resolve(target, origin):
    parts = urlsplit(target)
    if parts.scheme:
        require(parts.scheme == "https", f"Unexpected external scheme: {target}")
        return None
    path = (ROOT / parts.path.lstrip("/") if parts.path.startswith("/")
            else origin.parent / parts.path).resolve()
    require(path.is_relative_to(ROOT), f"Link escapes bundle: {target}")
    require(path.is_file(), f"Missing target from {origin.name}: {target}")
    return path


def close(actual, expected, label):
    require(math.isclose(actual, expected, rel_tol=0, abs_tol=0.000001), label)


def main():
    docs = {}
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text()
        require(text.startswith("---\n"), f"Missing frontmatter: {path}")
        _, frontmatter, body = text.split("---", 2)
        meta = yaml.safe_load(frontmatter)
        for target in re.findall(r"\]\(([^)]+)\)", body):
            resolve(target, path)
        if path.name == "index.md":
            require(meta == {"okf_version": "0.2"}, "Unexpected index metadata")
            continue
        docs[path.resolve()] = meta
        require(meta.get("type") and meta.get("title"), f"Missing type/title: {path}")
        require(meta.get("status") == "draft", f"Unexpected lifecycle: {path}")
        st = meta["steelthumb"]
        require(st["ontology_version"] == "0.2", f"Wrong profile version: {path}")
        source_rows = meta.get("sources", [])
        sources = {s["id"]: s for s in source_rows}
        require(len(sources) == len(source_rows), f"Duplicate source ID: {path}")
        for source in sources.values():
            resolve(source["resource"], path)
        claim_ids = set()
        for claim in st.get("claims", []):
            require(claim["id"] not in claim_ids, f"Duplicate claim ID: {path}")
            claim_ids.add(claim["id"])
            for evidence in claim["evidence"]:
                require(evidence["source_id"] in sources, f"Unknown evidence source: {path}")
        for label in re.findall(r"\[\^([^]]+)\]", body):
            require(label in sources, f"Unknown footnote source: {label}")
            require(f"[^{label}]:" in body, f"Missing footnote definition: {label}")
        for edge in st.get("relations", []):
            resolve(edge["target"], path)

    nutrient_count = 0
    for path, meta in docs.items():
        if meta["type"] != "FoodProfile":
            continue
        food = meta["steelthumb"]["food"]
        snapshot = json.loads(resolve(food["snapshot"], path).read_text())["record"]
        require(snapshot["fdcId"] == food["fdc_id"], "Wrong FDC identity")
        require(snapshot["description"] == food["source_food_name"], "Food description drift")
        require(food["basis"]["mass"] == 100 and food["basis"]["unit"] == "g", "Wrong USDA basis")
        require(food["cultivar_scope"] == "unspecified in source", "Unsupported cultivar scope")
        originals = {f"usda:{n['nutrient']['id']}": n for n in snapshot["foodNutrients"]}
        ids = set()
        for row in food["nutrients"]:
            require(row["id"] not in ids, "Duplicate nutrient")
            ids.add(row["id"])
            original = originals.get(row["id"])
            if original is None:
                require(row["value"] is None and row["availability"] == "not_reported", "Absent nutrient presented as measured")
                require(f"| {row['name']} | not reported | {row['unit']} |" in path.read_text(), "Missing-data table drift")
                nutrient_count += 1
                continue
            require(row["value"] == original.get("amount"), f"Value differs from USDA: {row['id']}")
            require(row["unit"] == original["nutrient"]["unitName"], "Unit drift")
            require(row["name"] == original["nutrient"]["name"], "Nutrient identity drift")
            expected = "reported" if row["value"] is not None else "not_reported"
            require(row["availability"] == expected, "Missingness confused with zero")
            require(row["source_id"] in {s["id"] for s in meta["sources"]}, "Unknown nutrient source")
            rendered = str(row["value"]) if row["value"] is not None else "not reported"
            require(f"| {row['name']} | {rendered} | {row['unit']} |" in path.read_text(), "Nutrition table drift")
            nutrient_count += 1

    yield_count = 0
    for path, meta in docs.items():
        if meta["type"] != "YieldEstimate":
            continue
        estimate = meta["steelthumb"]["yield"]
        require(estimate["basis_kind"] == "scenario", "Synthetic harvest mislabeled")
        food = docs[resolve(estimate["food_profile"], path)]["steelthumb"]["food"]
        require(estimate["food_state"] == food["preparation"], "Mass/preparation mismatch")
        inputs = estimate["inputs"]
        mass = inputs["harvested_mass_g"]
        fraction = inputs["edible_fraction"]["value"]
        area = inputs["growing_area_m2"]["value"]
        days = inputs["period_days"]["value"]
        require(0 <= fraction <= 1 and area > 0 and days > 0, "Invalid yield denominator or fraction")
        require(0 <= mass["min"] <= mass["max"], "Invalid mass range")
        require(all(i["origin"] in {"source", "assumption"} for i in inputs.values()), "Reference examples require sourced or assumed inputs; live observations belong to SteelThumb")
        if mass["origin"] == "source":
            require(mass["source_id"] in {s["id"] for s in meta["sources"]}, "Unknown harvest source")
            for bound in ("min", "max"):
                close(mass[bound], mass["original"][bound] * mass["grams_per_lb"], "Mass conversion failed")
            geometry = inputs["growing_area_m2"]["geometry"]
            close(area, geometry["row_length_m"] * geometry["row_spacing_m"], "Area conversion failed")
        nutrients = {n["id"]: n for n in food["nutrients"] if n["value"] is not None}
        require(len(estimate["results"]) == len(nutrients), "Missing or duplicate yield rows")
        require({r["nutrient_id"] for r in estimate["results"]} == set(nutrients), "Unknown yield nutrient")
        for result in estimate["results"]:
            nutrient = nutrients[result["nutrient_id"]]
            require(result["unit"] == nutrient["unit"], "Yield unit mismatch")
            for bound in ("min", "max"):
                total = mass[bound] * fraction / food["basis"]["mass"] * nutrient["value"]
                for field, expected in (("total", total), ("per_m2", total / area), ("per_m2_day", total / area / days)):
                    close(result[field][bound], expected, f"Yield arithmetic failed: {path.name}, {field}")
        yield_count += 1

    crops = {p for p, d in docs.items() if d["type"] == "Crop"}
    for crop in crops:
        cultivars = [d for p, d in docs.items() if d["type"] == "Cultivar" and any(
            e["predicate"] == "cultivar_of" and resolve(e["target"], p) == crop
            for e in d["steelthumb"]["relations"])]
        procedures = [d for p, d in docs.items() if d["type"] == "Procedure" and any(
            e["predicate"] == "applies_to" and resolve(e["target"], p) == crop
            for e in d["steelthumb"]["relations"])]
        require(len(cultivars) >= 3 and len(procedures) >= 2, f"Insufficient coverage: {crop}")
    print(f"PASS: {len(docs)} concepts; links/evidence; {nutrient_count} nutrient rows match USDA snapshots; {yield_count} yield scenarios recomputed; crop/cultivar/procedure coverage.")


if __name__ == "__main__":
    main()
