"""Ergonomic entry points for the generated Atlas SDK."""

from __future__ import annotations

import os
import time
from urllib.parse import urljoin
from typing import Any

import httpx

from atlas_sdk import *  # noqa: F403
from atlas_sdk import AtlasClient as _GeneratedAtlasClient
from atlas_sdk.core.request_options import RequestOptions
from atlas_sdk.types.advanced_auto_scaling_settings import AdvancedAutoScalingSettings
from atlas_sdk.types.disk_gb_auto_scaling import DiskGbAutoScaling

DEFAULT_BASE_URL = "https://cloud.mongodb.com"
DEFAULT_ACCEPT_HEADER = "application/vnd.atlas.2025-03-12+json"

class AtlasClient(_GeneratedAtlasClient):
    """Atlas Admin API client with service account authentication helpers."""

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        _install_auto_accept_header(self._client_wrapper.httpx_client)

    @classmethod
    def from_service_account(
        cls,
        *,
        client_id: str,
        client_secret: str,
        base_url: str = DEFAULT_BASE_URL,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> "AtlasClient":
        """Create a client using Atlas OAuth service account credentials."""
        client_headers = {"Accept": DEFAULT_ACCEPT_HEADER, **(headers or {})}
        return cls(
            base_url=base_url,
            token=fetch_service_account_token(
                client_id=client_id,
                client_secret=client_secret,
                base_url=base_url,
            ),
            headers=client_headers,
            **kwargs,
        )

    @classmethod
    def from_env(cls, **kwargs) -> "AtlasClient":
        """Create a client from MONGODB_ATLAS_* environment variables."""
        return cls.from_service_account(
            client_id=_required_env("MONGODB_ATLAS_CLIENT_ID"),
            client_secret=_required_env("MONGODB_ATLAS_CLIENT_SECRET"),
            base_url=get_base_url(),
            **kwargs,
        )

    def cluster(self, project_id: str, cluster_name: str) -> "ClusterManager":
        """Return a helper for common cluster management operations."""
        return ClusterManager(client=self, project_id=project_id, cluster_name=cluster_name)


class ClusterManager:
    """Convenience helper for common Atlas cluster mutation workflows."""

    def __init__(
        self,
        *,
        client: AtlasClient,
        project_id: str,
        cluster_name: str,
        poll_interval_seconds: float = 30.0,
        timeout_seconds: float = 1800.0,
    ):
        self.client = client
        self.project_id = project_id
        self.cluster_name = cluster_name
        self.poll_interval_seconds = poll_interval_seconds
        self.timeout_seconds = timeout_seconds

    def get(self) -> Any:
        """Fetch the current cluster."""
        return self.client.clusters.get_cluster(self.project_id, self.cluster_name)

    def pause(self, *, wait: bool = True) -> Any:
        """Pause the cluster."""
        return self._update(wait=wait, paused=True)

    def resume(self, *, wait: bool = True) -> Any:
        """Resume the cluster."""
        return self._update(wait=wait, paused=False)

    def change_instance_size(self, instance_size: str, *, wait: bool = True) -> Any:
        """Change the instance size for all configured node types."""
        cluster = self.get()
        return self._update(
            wait=wait,
            replication_specs=_replication_specs_with_hardware_updates(
                cluster.replication_specs,
                {"instance_size": instance_size},
            ),
        )

    def set_disk_autoscaling(self, enabled: bool, *, wait: bool = True) -> Any:
        """Enable or disable disk auto-scaling for all configured regions."""
        cluster = self.get()
        return self._update(
            wait=wait,
            replication_specs=_replication_specs_with_disk_auto_scaling(
                cluster.replication_specs,
                enabled,
            ),
        )

    def set_disk_auto_scaling(self, enabled: bool, *, wait: bool = True) -> Any:
        """Enable or disable disk auto-scaling for all configured regions."""
        return self.set_disk_autoscaling(enabled, wait=wait)

    def change_disk_size(self, disk_size_gb: float, *, wait: bool = True) -> Any:
        """Change disk size for all configured node types."""
        cluster = self.get()
        return self._update(
            wait=wait,
            replication_specs=_replication_specs_with_hardware_updates(
                cluster.replication_specs,
                {"disk_size_gb": disk_size_gb},
            ),
        )

    def increase_disk_size(
        self,
        *,
        gb: float | None = None,
        percent: float | None = None,
        wait: bool = True,
    ) -> Any:
        """Increase disk size by an absolute GB amount or a percentage."""
        if (gb is None) == (percent is None):
            raise ValueError("Provide exactly one of gb or percent.")

        cluster = self.get()
        current_size = _disk_size_gb(cluster.replication_specs)
        if gb is not None:
            new_size = current_size + gb
        else:
            new_size = current_size * (1 + percent / 100)
        return self._update(
            wait=wait,
            replication_specs=_replication_specs_with_hardware_updates(
                cluster.replication_specs,
                {"disk_size_gb": round(new_size, 1)},
            ),
        )

    def wait_until_idle(self) -> Any:
        """Wait until the cluster reaches IDLE."""
        return self.wait_for_state("IDLE")

    def wait_for_state(self, target_state: str) -> Any:
        """Wait until the cluster reaches the requested state."""
        deadline = time.monotonic() + self.timeout_seconds
        while True:
            cluster = self.get()
            if cluster.state_name == target_state:
                return cluster
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"Timed out waiting for {self.cluster_name} to reach {target_state}; "
                    f"last state was {cluster.state_name}."
                )
            time.sleep(self.poll_interval_seconds)

    def _update(self, *, wait: bool, **kwargs: Any) -> Any:
        updated = self.client.clusters.update_cluster(
            group_id_=self.project_id,
            cluster_name=self.cluster_name,
            **kwargs,
        )
        if wait:
            return self.wait_until_idle()
        return updated


def get_base_url() -> str:
    """Return the configured Atlas base URL."""
    return os.environ.get("MONGODB_ATLAS_BASE_URL", DEFAULT_BASE_URL)


def fetch_service_account_token(*, client_id: str, client_secret: str, base_url: str) -> str:
    """Fetch a bearer token using OAuth2 client credentials flow."""
    response = httpx.post(
        urljoin(base_url, "/api/oauth/token"),
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    response.raise_for_status()
    return response.json()["access_token"]


def _replication_specs_with_hardware_updates(
    replication_specs: list[Any],
    updates: dict[str, Any],
) -> list[Any]:
    if not replication_specs:
        raise ValueError("Cluster has no replication specs to update.")

    return [
        _copy_model(
            spec,
            region_configs=[
                _region_config_with_hardware_updates(region_config, updates)
                for region_config in spec.region_configs or []
            ],
        )
        for spec in replication_specs
    ]


def _region_config_with_hardware_updates(region_config: Any, updates: dict[str, Any]) -> Any:
    return _copy_model(
        region_config,
        electable_specs=_copy_optional_model(region_config.electable_specs, updates),
        read_only_specs=_copy_optional_model(region_config.read_only_specs, updates),
        analytics_specs=_copy_optional_model(region_config.analytics_specs, updates),
    )


def _replication_specs_with_disk_auto_scaling(
    replication_specs: list[Any],
    enabled: bool,
) -> list[Any]:
    if not replication_specs:
        raise ValueError("Cluster has no replication specs to update.")

    return [
        _copy_model(
            spec,
            region_configs=[
                _region_config_with_disk_auto_scaling(region_config, enabled)
                for region_config in spec.region_configs or []
            ],
        )
        for spec in replication_specs
    ]


def _region_config_with_disk_auto_scaling(region_config: Any, enabled: bool) -> Any:
    auto_scaling = region_config.auto_scaling or AdvancedAutoScalingSettings()
    return _copy_model(
        region_config,
        auto_scaling=_copy_model(
            auto_scaling,
            disk_gb=DiskGbAutoScaling(enabled=enabled),
        ),
    )


def _copy_optional_model(model: Any, updates: dict[str, Any]) -> Any:
    if model is None:
        return None
    return _copy_model(model, **updates)


def _copy_model(model: Any, **updates: Any) -> Any:
    if hasattr(model, "model_copy"):
        return model.model_copy(update=updates)
    return model.copy(update=updates)


def _disk_size_gb(replication_specs: list[Any]) -> float:
    if not replication_specs:
        raise ValueError("Cluster has no replication specs to update.")

    for spec in replication_specs:
        for region_config in spec.region_configs or []:
            for hardware_spec in (
                region_config.electable_specs,
                region_config.read_only_specs,
                region_config.analytics_specs,
            ):
                if hardware_spec is not None and hardware_spec.disk_size_gb is not None:
                    return hardware_spec.disk_size_gb
    raise ValueError("Cluster has no disk size to increase.")


def _install_auto_accept_header(http_client: Any) -> None:
    request = http_client.request

    def request_with_matching_accept(*args: Any, **kwargs: Any) -> httpx.Response:
        kwargs["request_options"] = _with_matching_accept(
            headers=kwargs.get("headers"),
            request_options=kwargs.get("request_options"),
        )
        return request(*args, **kwargs)

    http_client.request = request_with_matching_accept


def _with_matching_accept(
    *,
    headers: dict[str, Any] | None,
    request_options: RequestOptions | None,
) -> RequestOptions | None:
    content_type = _header_value(headers, "content-type")
    if (
        content_type is None
        or _header_value(headers, "accept")
        or _header_value(_additional_headers(request_options), "accept")
    ):
        return request_options

    updated_options: RequestOptions = dict(request_options or {})
    additional_headers = dict(_additional_headers(request_options))
    additional_headers["Accept"] = content_type
    updated_options["additional_headers"] = additional_headers
    return updated_options


def _additional_headers(request_options: RequestOptions | None) -> dict[str, Any]:
    if request_options is None:
        return {}
    return dict(request_options.get("additional_headers", {}) or {})


def _header_value(headers: dict[str, Any] | None, name: str) -> str | None:
    if headers is None:
        return None
    for key, value in headers.items():
        if key.lower() == name.lower() and isinstance(value, str):
            return value
    return None


def _required_env(name: str) -> str:
    try:
        return os.environ[name]
    except KeyError:
        raise RuntimeError(f"Set {name} before creating an Atlas client.") from None
