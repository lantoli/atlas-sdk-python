import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.compare_coverage import compare_specs, format_report


PYTHON_SPEC = {
    "paths": {
        "/api/atlas/v2/groups": {
            "get": {"operationId": "listGroups", "tags": ["Projects"]},
        },
        "/api/atlas/v2/groups/{groupId}/clusters": {
            "post": {"operationId": "createCluster", "tags": ["Clusters"]},
        },
    }
}

GO_SPEC = {
    "paths": {
        "/api/atlas/v2/groups": {
            "get": {"operationId": "listGroups", "tags": ["Projects"]},
        },
        "/api/atlas/v2/groups/{groupId}/clusters": {
            "post": {"operationId": "createCluster", "tags": ["Clusters"]},
        },
        "/api/atlas/v2/groups/{groupId}/backup/snapshots": {
            "get": {"operationId": "listSnapshots", "tags": ["Cloud Backups"]},
        },
    }
}


def test_compare_specs_counts_tags_operations_and_gaps():
    coverage = compare_specs(PYTHON_SPEC, GO_SPEC)

    assert coverage.python_operation_count == 2
    assert coverage.go_operation_count == 3
    assert coverage.python_tag_count == 2
    assert coverage.go_tag_count == 3
    assert coverage.shared_operation_count == 2
    assert coverage.missing_tag_counts == {"Cloud Backups": 1}
    assert coverage.python_tag_counts == {"Clusters": 1, "Projects": 1}
    assert coverage.go_tag_counts == {"Cloud Backups": 1, "Clusters": 1, "Projects": 1}


def test_format_report_summarizes_coverage():
    coverage = compare_specs(PYTHON_SPEC, GO_SPEC)

    report = format_report(coverage)

    assert "Python SDK: 2 operations across 2 tags." in report
    assert "Atlas Go SDK: 3 operations across 3 tags." in report
    assert "Shared operations: 2." in report
    assert "Missing operations by tag:" in report
    assert "Cloud Backups: 1 operation." in report
