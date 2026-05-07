#!/usr/bin/env python3
"""Prepare the Atlas OpenAPI spec for SDK generation."""

import sys
import yaml

HTTP_METHODS = frozenset(["get", "post", "put", "patch", "delete"])


def filter_spec(input_path: str, output_path: str) -> None:
    with open(input_path) as f:
        spec = yaml.safe_load(f)

    kept_paths: dict = {}
    kept_tags: set[str] = set()
    for path, path_item in spec.get("paths", {}).items():
        kept_ops: dict = {}
        for method, op in path_item.items():
            if method not in HTTP_METHODS:
                kept_ops[method] = op
                continue
            kept_ops[method] = op
            kept_tags.update(op.get("tags", []))
        if kept_ops:
            kept_paths[path] = kept_ops

    spec["paths"] = kept_paths
    spec["tags"] = [t for t in spec.get("tags", []) if t.get("name") in kept_tags]

    with open(output_path, "w") as f:
        yaml.dump(spec, f, allow_unicode=True, sort_keys=False)

    print(f"Prepared: {len(kept_paths)} paths retained across {len(kept_tags)} tags.")


if __name__ == "__main__":
    filter_spec(sys.argv[1], sys.argv[2])
