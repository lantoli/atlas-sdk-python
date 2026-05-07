# atlas-sdk-python

Experimental Python SDK for the [MongoDB Atlas Admin API](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/), generated with [Fern](https://www.buildwithfern.com/) from the same OpenAPI spec used by the official [atlas-sdk-go](https://github.com/mongodb/atlas-sdk-go).

> **This is an experimental project and is not officially supported by MongoDB.**

## Motivation

Python users working in automation scripts, Jupyter notebooks, data and ML pipelines, and AI-assisted code often hand-roll `requests` calls against the raw Atlas Admin API. That means each script has to handle OAuth, pagination, versioned headers, PATCH payload shape, and untyped responses on its own.

This project explores what an official Python SDK for Atlas could look like: generated from the same transformed OpenAPI spec as the Go SDK, but with Python-native models, examples, and helper workflows.

## Status

This is an experimental SDK, not published to PyPI, and not officially supported by MongoDB.

Current deliverables:

- Full generated Atlas Admin API coverage from the transformed spec: 468 operations across 51 tags and 293 paths.
- Hand-written `mongodb_atlas` wrapper with service account auth helpers and common cluster workflows.
- Eleven SDK examples covering project listing, cluster provisioning, cluster mutation, disk usage, invoices, and monthly spend.
- Focused tests for spec filtering, coverage comparison, auth, versioned headers, examples, and cluster helper behavior.
- Fern generation for the Python package in `src/atlas_sdk`.

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

This installs the SDK in editable mode along with its runtime dependencies (`httpx`, `pydantic`, `typing-extensions`) and dev dependencies (`pytest`, `pyyaml`).

Export your Atlas [Service Account](https://www.mongodb.com/docs/atlas/api/service-accounts-overview/) credentials:

```bash
export MONGODB_ATLAS_CLIENT_ID=your-client-id
export MONGODB_ATLAS_CLIENT_SECRET=your-client-secret
```

Optionally override the Atlas base URL (defaults to `https://cloud.mongodb.com`):

```bash
export MONGODB_ATLAS_BASE_URL=https://cloud.mongodb.com
```

## Quick start

```python
from mongodb_atlas import AtlasClient

client = AtlasClient.from_env()

for project in client.projects.list_groups().results or []:
    print(project.id, project.name)
```

The `mongodb_atlas` package is a small hand-written wrapper around the generated `atlas_sdk` client. It adds service account authentication helpers, automatically matches Atlas versioned `Accept` headers for generated mutating operations, and re-exports generated models while keeping generated code untouched.

For common cluster changes, use the cluster manager helper:

```python
cluster = client.cluster("PROJECT_ID", "CLUSTER_NAME")

cluster.pause()
cluster.resume()
cluster.change_instance_size("M20")
cluster.set_disk_autoscaling(True)
cluster.change_disk_size(40.0)
cluster.increase_disk_size(gb=10.0)
cluster.increase_disk_size(percent=10.0)
```

You can also pass credentials directly:

```python
from mongodb_atlas import AtlasClient

client = AtlasClient.from_service_account(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
)
```

## Examples

The original five examples have been run successfully against a live Atlas org. All examples read `MONGODB_ATLAS_CLIENT_ID` and `MONGODB_ATLAS_CLIENT_SECRET`. Additional vars per example:

| File | What it does | Additional env vars |
|---|---|---|
| `examples/hello_atlas.py` | Authenticates, lists all projects | (none) |
| `examples/provision_cluster.py` | End-to-end: project, cluster, db user, IP | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME` (optional) |
| `examples/provision_big_cluster.py` | Provision geosharded multi-cloud cluster | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME` |
| `examples/pause_cluster.py` | Pause and unpause a cluster (PATCH demo) | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME` |
| `examples/scale_cluster.py` | Scale cluster instance size up or down | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME`, `MONGODB_ATLAS_INSTANCE_SIZE` |
| `examples/update_autoscaling.py` | Toggle compute and disk autoscaling | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME`, `MONGODB_ATLAS_AUTOSCALING_ENABLED`, plus bounds when enabling |
| `examples/manage_cluster.py` | Show common `ClusterManager` demo commands | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME` (optional) |
| `examples/disk_usage.py` | Show configured disk size and used/free disk metrics | `MONGODB_ATLAS_PROJECT_ID`, `MONGODB_ATLAS_CLUSTER_NAME` |
| `examples/get_invoice.py` | Show the latest 12 invoices in a table | (none) |
| `examples/monthly_spend.py` | Summarize the last 12 months by month and service | (none) |

`examples_ai/` contains standalone direct-REST scripts produced during the experiment for AI-agent style workflows. The SDK examples in `examples/` are the primary user-facing examples.

`examples/provision_cluster.py` calls `https://api.ipify.org` to add your public egress IP to the project IP access list.

`examples/provision_big_cluster.py` creates a larger geosharded cluster with AWS and Azure nodes across two zones. Expect higher cost than the basic M10 replica set example.

Run any example:

```bash
uv run python examples/hello_atlas.py
```

## Next focus

The generated SDK now exposes the full Atlas Admin API surface from the transformed OpenAPI spec. Customer usage data still points to cluster updates as the most important workflows to smooth with hand-written helpers and examples:

- Pause and unpause clusters (`toggle_pause`), especially via the public API.
- Scale instance size up or down, including multi-region clusters.
- Toggle auto-scaling and adjust disk size or disk IOPS.
- Change replication specs and labels.
- Upgrade MongoDB major version.

This repo now includes examples for pause/unpause, instance size scaling, and autoscaling toggles. The `mongodb_atlas.ClusterManager` helper smooths pause/resume, instance size changes, disk auto-scaling toggles, and absolute or relative disk size changes. Remaining high-value helper gaps are disk IOPS, labels, replication spec changes, and MongoDB major version upgrades.

## Why Fern over openapi-generator-cli

The Go SDK uses `openapi-generator-cli`. Here is the same project list operation in both:

**Go (openapi-generator-cli output):**

```go
request := sdk.ProjectsApi.ListGroupsWithParams(ctx,
    &admin.ListGroupsApiParams{
        ItemsPerPage: admin.PtrInt(1),
        IncludeCount: admin.PtrBool(true),
        PageNum:      admin.PtrInt(1),
    })
projects, response, err := request.IncludeCount(true).PageNum(1).Execute()
if err != nil {
    log.Fatal(err)
}
for _, p := range projects.GetResults() {
    fmt.Println(p.GetId(), p.GetName())
}
```

**Python (this SDK, Fern output):**

```python
for project in client.projects.list_groups().results or []:
    print(project.id, project.name)
```

Fern generates Pydantic v2 models (no `GetXxx()` accessor methods), httpx-backed sync and async clients, and typed errors, none of which `openapi-generator-cli` provides for Python.

## Coverage

The SDK now generates every operation in the transformed Atlas Admin API spec used by the local Atlas Go SDK checkout: 468 operations across 51 tags and 293 paths, generated from `openapi/atlas-api-filtered.yaml`.

Compared with the local Atlas Go SDK spec, this SDK currently covers 468 of 468 operations (100.0%) and 51 of 51 tags (100.0%). There are no operation gaps by tag.

Compare this SDK with a local `atlas-sdk-go` checkout:

```bash
uv run python scripts/compare_coverage.py
```

By default, the script looks for a sibling `atlas-sdk-go` checkout at `../atlas-sdk-go/openapi/atlas-api-transformed.yaml`. Pass `--go-spec` to compare against a different Go SDK checkout.

## Regenerating

After changes to the OpenAPI spec:

```bash
uv run python scripts/filter_spec.py \
  openapi/atlas-api-transformed.yaml \
  openapi/atlas-api-filtered.yaml
echo "y" | npx --yes fern-api generate --local
uv sync
```

The Fern Python generator wipes the output directory (`src/atlas_sdk/`) on every regeneration; do not edit generated files manually.

The generator also writes scaffold tests under `src/atlas_sdk/tests` that reference a placeholder package name. Project pytest discovery is limited to `tests/`, where the repo's hand-written tests live.

This repo generates the Python SDK into `src/atlas_sdk`.

