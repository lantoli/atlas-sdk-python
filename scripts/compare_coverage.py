#!/usr/bin/env python3
"""Compare Python SDK coverage with the Atlas Go SDK OpenAPI spec."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

HTTP_METHODS = frozenset(["get", "post", "put", "patch", "delete"])
REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PYTHON_SPEC = REPO_ROOT / "openapi" / "atlas-api-filtered.yaml"
DEFAULT_GO_SPEC = REPO_ROOT.parent / "atlas-sdk-go" / "openapi" / "atlas-api-transformed.yaml"


@dataclass(frozen=True)
class Operation:
    operation_id: str
    method: str
    path: str
    tags: tuple[str, ...]


@dataclass(frozen=True)
class Coverage:
    python_operation_count: int
    go_operation_count: int
    python_tag_count: int
    go_tag_count: int
    shared_operation_count: int
    python_tag_counts: dict[str, int]
    go_tag_counts: dict[str, int]
    missing_tag_counts: dict[str, int]

    @property
    def operation_coverage_percent(self) -> float:
        if self.go_operation_count == 0:
            return 100.0
        return self.shared_operation_count / self.go_operation_count * 100

    @property
    def tag_coverage_percent(self) -> float:
        if self.go_tag_count == 0:
            return 100.0
        return self.python_tag_count / self.go_tag_count * 100


def load_spec(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return yaml.safe_load(f)


def collect_operations(spec: dict[str, Any]) -> list[Operation]:
    operations: list[Operation] = []
    for path, path_item in spec.get("paths", {}).items():
        for method, op in path_item.items():
            if method not in HTTP_METHODS:
                continue
            operation_id = op.get("operationId") or f"{method.upper()} {path}"
            operations.append(
                Operation(
                    operation_id=operation_id,
                    method=method.upper(),
                    path=path,
                    tags=tuple(op.get("tags", [])),
                )
            )
    return operations


def count_operations_by_tag(operations: list[Operation]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for operation in operations:
        for tag in operation.tags:
            counts[tag] += 1
    return dict(sorted(counts.items()))


def compare_specs(python_spec: dict[str, Any], go_spec: dict[str, Any]) -> Coverage:
    python_operations = collect_operations(python_spec)
    go_operations = collect_operations(go_spec)

    python_operation_ids = {operation.operation_id for operation in python_operations}
    go_operation_ids = {operation.operation_id for operation in go_operations}

    python_tag_counts = count_operations_by_tag(python_operations)
    go_tag_counts = count_operations_by_tag(go_operations)

    missing_operations = [
        operation for operation in go_operations if operation.operation_id not in python_operation_ids
    ]
    missing_tag_counts = count_operations_by_tag(missing_operations)

    return Coverage(
        python_operation_count=len(python_operation_ids),
        go_operation_count=len(go_operation_ids),
        python_tag_count=len(python_tag_counts),
        go_tag_count=len(go_tag_counts),
        shared_operation_count=len(python_operation_ids & go_operation_ids),
        python_tag_counts=python_tag_counts,
        go_tag_counts=go_tag_counts,
        missing_tag_counts=missing_tag_counts,
    )


def format_report(coverage: Coverage) -> str:
    lines = [
        "Atlas SDK coverage comparison",
        "",
        f"Python SDK: {coverage.python_operation_count} operations across {coverage.python_tag_count} tags.",
        f"Atlas Go SDK: {coverage.go_operation_count} operations across {coverage.go_tag_count} tags.",
        f"Shared operations: {coverage.shared_operation_count}.",
        f"Operation coverage: {coverage.operation_coverage_percent:.1f}%.",
        f"Tag coverage: {coverage.tag_coverage_percent:.1f}%.",
        "",
        "Tag counts:",
    ]

    all_tags = sorted(set(coverage.python_tag_counts) | set(coverage.go_tag_counts))
    for tag in all_tags:
        python_count = coverage.python_tag_counts.get(tag, 0)
        go_count = coverage.go_tag_counts.get(tag, 0)
        gap = max(go_count - python_count, 0)
        lines.append(f"- {tag}: Python {python_count}, Go {go_count}, gap {gap}.")

    if coverage.missing_tag_counts:
        lines.extend(["", "Missing operations by tag:"])
        for tag, count in coverage.missing_tag_counts.items():
            lines.append(f"- {tag}: {count} {_operation_label(count)}.")
    else:
        lines.extend(["", "Missing operations by tag: none."])

    return "\n".join(lines)


def _operation_label(count: int) -> str:
    return "operation" if count == 1 else "operations"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare this Python SDK's Atlas OpenAPI coverage with atlas-sdk-go."
    )
    parser.add_argument(
        "--python-spec",
        type=Path,
        default=DEFAULT_PYTHON_SPEC,
        help=f"Path to this SDK's OpenAPI spec. Defaults to {DEFAULT_PYTHON_SPEC}.",
    )
    parser.add_argument(
        "--go-spec",
        type=Path,
        default=DEFAULT_GO_SPEC,
        help=f"Path to atlas-sdk-go's transformed OpenAPI spec. Defaults to {DEFAULT_GO_SPEC}.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    coverage = compare_specs(load_spec(args.python_spec), load_spec(args.go_spec))
    print(format_report(coverage))


if __name__ == "__main__":
    main()
