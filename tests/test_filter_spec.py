import os
import sys
import tempfile
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scripts.filter_spec import HTTP_METHODS, filter_spec

INPUT = os.path.join(os.path.dirname(__file__), "..", "openapi", "atlas-api-transformed.yaml")


def test_all_operations_remain():
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w") as tmp:
        out_path = tmp.name
    filter_spec(INPUT, out_path)
    with open(out_path) as f:
        spec = yaml.safe_load(f)

    with open(INPUT) as f:
        source_spec = yaml.safe_load(f)

    assert _operation_ids(spec) == _operation_ids(source_spec)
    os.unlink(out_path)


def test_all_operation_tags_remain():
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w") as tmp:
        out_path = tmp.name
    filter_spec(INPUT, out_path)
    with open(out_path) as f:
        spec = yaml.safe_load(f)

    with open(INPUT) as f:
        source_spec = yaml.safe_load(f)

    assert _operation_tags(spec) == _operation_tags(source_spec)
    os.unlink(out_path)


def test_components_schemas_kept():
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w") as tmp:
        out_path = tmp.name
    filter_spec(INPUT, out_path)
    with open(out_path) as f:
        spec = yaml.safe_load(f)
    assert len(spec.get("components", {}).get("schemas", {})) > 100, (
        "Expected all schemas to be retained for referenced types"
    )
    os.unlink(out_path)


def _operation_ids(spec):
    return {
        op.get("operationId") or f"{method.upper()} {path}"
        for path, path_item in spec["paths"].items()
        for method, op in path_item.items()
        if method in HTTP_METHODS
    }


def _operation_tags(spec):
    return {
        tag
        for path_item in spec["paths"].values()
        for method, op in path_item.items()
        if method in HTTP_METHODS
        for tag in op.get("tags", [])
    }
