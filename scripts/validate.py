"""Check the catalogue before a change merges.

The JSON Schemas check each file's shape. This also checks what a schema
cannot: that each entry's id matches its file name, that its type, scope,
tags and professions come from vocabularies.yml, that every id
the catalogue refers to exists, and that each hosted source's directory has a
guidance.yml.

Exits 1 and lists every problem it finds.
"""

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
VOCABULARY_NAMES = ("types", "scope", "professions", "tags")
LAYOUTS = ("requirements", "policy", "guide", "steps", "tool", "media")


def load_yaml(path: Path, errors: list[str]):
    try:
        with path.open(encoding="utf-8") as file:
            return yaml.safe_load(file)
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot read: {exc}")
        return None


def validator(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((ROOT / "schema" / name).read_text(encoding="utf-8")))


def schema_errors(check: Draft202012Validator, data, name: str) -> list[str]:
    found = sorted(check.iter_errors(data), key=lambda e: [str(p) for p in e.absolute_path])
    return [
        f"{name}: {'/'.join(str(p) for p in error.absolute_path) or '(top level)'}: {error.message}"
        for error in found
    ]


def check_vocabularies(vocabularies, errors: list[str]) -> dict[str, set[str]]:
    if not isinstance(vocabularies, dict):
        errors.append("vocabularies: expected a mapping of types, scope, professions and tags")
        return {name: set() for name in VOCABULARY_NAMES}
    known = {}
    for name in VOCABULARY_NAMES:
        values = vocabularies.get(name)
        if not isinstance(values, dict) or not values:
            errors.append(f"vocabularies: '{name}' must list at least one value")
            known[name] = set()
            continue
        for key, value in values.items():
            if not isinstance(value, dict) or not value.get("label"):
                errors.append(f"vocabularies: {name}.{key} needs a label")
            if name == "types" and isinstance(value, dict) and value.get("layout") not in LAYOUTS:
                errors.append(
                    f"vocabularies: types.{key} needs a layout of {', '.join(LAYOUTS)}"
                )
        known[name] = set(values)
    return known


def main() -> int:
    errors: list[str] = []

    catalogue = load_yaml(ROOT / "catalogue.yml", errors)
    if catalogue is None:
        return report(errors)
    errors += schema_errors(validator("catalogue.schema.json"), catalogue, "catalogue.yml")
    if errors:
        return report(errors)

    known = check_vocabularies(load_yaml(ROOT / catalogue["vocabularies"], errors), errors)

    entry_check = validator("entry.schema.json")
    # Every entry file's id is its file name, so a reference to it resolves
    # even when the file itself has problems: one broken entry is reported
    # once, not again by every entry that relates to it.
    entry_ids = set()
    entries = {}
    for path in sorted((ROOT / catalogue["entries"]).glob("*.yml")):
        name = str(path.relative_to(ROOT))
        entry_ids.add(path.stem)
        entry = load_yaml(path, errors)
        if entry is None:
            continue
        problems = schema_errors(entry_check, entry, name)
        errors += problems
        if problems:
            continue
        if entry["id"] != path.stem:
            errors.append(f"{name}: id '{entry['id']}' must match the file name '{path.stem}'")
        entries[path.stem] = (name, entry)

    if not entry_ids:
        errors.append(f"{catalogue['entries']}: no entries found")

    for entry_id, (name, entry) in entries.items():
        if entry["type"] not in known["types"]:
            errors.append(f"{name}: type '{entry['type']}' is not in vocabularies.yml")
        if entry["scope"] not in known["scope"]:
            errors.append(f"{name}: scope '{entry['scope']}' is not in vocabularies.yml")
        for field in ("tags", "professions"):
            for value in entry[field]:
                if value not in known[field]:
                    errors.append(f"{name}: {field} value '{value}' is not in vocabularies.yml")
        for related in entry.get("related", []):
            if related == entry_id:
                errors.append(f"{name}: an entry cannot be related to itself")
            elif related not in entry_ids:
                errors.append(f"{name}: related entry '{related}' does not exist")
        source = entry["source"]
        if source["type"] == "hosted" and not (ROOT / source["path"] / "guidance.yml").is_file():
            errors.append(f"{name}: {source['path']}/guidance.yml does not exist")

    for featured in catalogue.get("featured", []):
        if featured not in entry_ids:
            errors.append(f"catalogue.yml: featured entry '{featured}' does not exist")

    return report(errors, count=len(entry_ids))


def report(errors: list[str], count: int = 0) -> int:
    if errors:
        print(f"{len(errors)} problem(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"Catalogue is valid: {count} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
