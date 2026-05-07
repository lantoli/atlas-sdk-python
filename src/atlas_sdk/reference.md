# Reference
## Root
<details><summary><code>client.root.<a href="src/atlas_sdk/root/client.py">get_system_status</a>() -> SystemStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This resource returns information about the MongoDB application along with API key meta data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.root.get_system_status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.root.<a href="src/atlas_sdk/root/client.py">list_control_plane_addresses</a>() -> ControlPlaneIpAddresses</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all control plane IP addresses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.root.list_control_plane_addresses()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Alert Configurations
<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">list_matcher_field_names</a>() -> typing.List[MatcherField]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all field names that the `matchers.fieldName` parameter accepts when you create or update an Alert Configuration. You can successfully call this endpoint with any assigned role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.list_matcher_field_names()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">list_alert_configs</a>(...) -> PaginatedAlertConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all alert configurations for one project. These alert configurations apply to any component in the project. Alert configurations define the triggers and notification methods for alerts. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.list_alert_configs(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">create_alert_config</a>(...) -> GroupAlertsConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one alert configuration for the specified project. Alert configurations define the triggers and notification methods for alerts. To use this resource, the requesting Service Account or API Key must have the Project Alerts Manager, Project Monitoring Admin, Organization Owner, or Project Owner role.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.create_alert_config(
    group_id_="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupAlertsConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">get_alert_config</a>(...) -> GroupAlertsConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified alert configuration from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Use the Return All Alert Configurations for One Project endpoint to retrieve all alert configurations to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.get_alert_config(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_config_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_config_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">update_alert_config</a>(...) -> GroupAlertsConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one alert configuration in the specified project. Alert configurations define the triggers and notification methods for alerts. To use this resource, the requesting Service Account or API Key must have the Project Alerts Manager, Project Monitoring Admin, Organization Owner, or Project Owner role.

**NOTE**: To enable or disable the alert configuration, see Toggle One State of One Alert Configuration in One Project.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.update_alert_config(
    group_id_="32b6e34b3d91647abb20e7b8",
    alert_config_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_config_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupAlertsConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">delete_alert_config</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one alert configuration from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Alerts Manager, Project Monitoring Admin, Organization Owner, or Project Owner role. Use the Return All Alert Configurations for One Project endpoint to retrieve all alert configurations to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.delete_alert_config(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_config_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_config_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">toggle_alert_config</a>(...) -> GroupAlertsConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables or disables the specified alert configuration in the specified project. The resource enables the specified alert configuration if currently enabled. The resource disables the specified alert configuration if currently disabled. To use this resource, the requesting Service Account or API Key must have the Project Alerts Manager, Project Monitoring Admin, Organization Owner, or Project Owner role.

**NOTE**: This endpoint updates only the enabled/disabled state for the alert configuration. To update more than just this configuration, see Update One Alert Configuration.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.toggle_alert_config(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_config_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_config_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert configuration that triggered this alert.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Flag that indicates whether to enable or disable the specified alert configuration in the specified project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alert_configurations.<a href="src/atlas_sdk/alert_configurations/client.py">get_alert_configs</a>(...) -> PaginatedAlertConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all alert configurations set for the specified alert. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Use the Return All Alerts from One Project endpoint to retrieve all alerts to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alert_configurations.get_alert_configs(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_id="alertId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clusters
<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">list_cluster_details</a>(...) -> PaginatedOrgGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details for all clusters in all projects to which you have access. Clusters contain a group of hosts that maintain the same data set. The response does not include multi-cloud clusters. To use this resource, the requesting Service Account or API Key can have any cluster-level role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.list_cluster_details()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">list_clusters</a>(...) -> PaginatedClusterDescription20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details for all clusters in the specific project to which you have access. Clusters contain a group of hosts that maintain the same data set. The response includes clusters with asymmetrically-sized shards. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. This feature is not  available for serverless clusters.

This endpoint can also be used on Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) endpoint or former M2/M5 clusters that have been migrated to Flex clusters until January 2026. Please use the List Flex Clusters endpoint for Flex clusters instead. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.list_clusters(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_with_retained_backups:** `typing.Optional[bool]` — Flag that indicates whether to return Clusters with retain backups.
    
</dd>
</dl>

<dl>
<dd>

**use_effective_instance_fields:** `typing.Optional[bool]` — Controls how hardware specification fields are returned in the response. When set to true, returns the original client-specified values and provides separate effective fields showing current operational values. When false (default), hardware specification fields show current operational values directly. Primarily used for autoscaling compatibility.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">create_cluster</a>(...) -> ClusterDescription20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. This resource can create clusters with asymmetrically-sized shards. Each project supports up to 25 database deployments. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Cluster Creator role. This feature is not available for serverless clusters.

Please note that using an `instanceSize` of M2 or M5 will create a Flex cluster instead. Support for the `instanceSize` of M2 or M5 will be discontinued in January 2026. We recommend using the Create Flex Cluster API for such configurations moving forward. Deprecated versions: v2-{2024-08-05}, v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ReplicationSpec20240805, CloudRegionConfig20240805, HardwareSpec20240805, AdvancedAutoScalingSettings, AdvancedComputeAutoScaling, DiskGbAutoScaling, DedicatedHardwareSpec20240805
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.create_cluster(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_type="SHARDED",
    name="myCluster",
    replication_specs=[
        ReplicationSpec20240805(
            region_configs=[
                CloudRegionConfig20240805(
                    electable_specs=HardwareSpec20240805(
                        disk_size_gb=10,
                        instance_size="M60",
                        node_count=3,
                    ),
                    priority=7,
                    provider_name="AWS",
                    region_name="US_EAST_1",
                    analytics_auto_scaling=AdvancedAutoScalingSettings(
                        compute=AdvancedComputeAutoScaling(
                            enabled=True,
                            max_instance_size="M40",
                            min_instance_size="M30",
                            scale_down_enabled=True,
                        ),
                        disk_gb=DiskGbAutoScaling(
                            enabled=True,
                        ),
                    ),
                    analytics_specs=DedicatedHardwareSpec20240805(
                        disk_size_gb=10,
                        node_count=0,
                        instance_size="M40",
                    ),
                    auto_scaling=AdvancedAutoScalingSettings(
                        compute=AdvancedComputeAutoScaling(
                            enabled=True,
                            max_instance_size="M60",
                            min_instance_size="M30",
                            scale_down_enabled=True,
                        ),
                        disk_gb=DiskGbAutoScaling(
                            enabled=True,
                        ),
                    ),
                    read_only_specs=DedicatedHardwareSpec20240805(
                        disk_size_gb=10,
                        node_count=0,
                        instance_size="M60",
                    ),
                )
            ],
            zone_name="Zone 1",
        ),
        ReplicationSpec20240805(
            region_configs=[
                CloudRegionConfig20240805(
                    electable_specs=HardwareSpec20240805(
                        disk_size_gb=10,
                        instance_size="M40",
                        node_count=3,
                    ),
                    priority=7,
                    provider_name="AWS",
                    region_name="US_EAST_1",
                    analytics_auto_scaling=AdvancedAutoScalingSettings(
                        compute=AdvancedComputeAutoScaling(
                            enabled=True,
                            max_instance_size="M40",
                            min_instance_size="M30",
                            scale_down_enabled=True,
                        ),
                        disk_gb=DiskGbAutoScaling(
                            enabled=True,
                        ),
                    ),
                    analytics_specs=DedicatedHardwareSpec20240805(
                        disk_size_gb=10,
                        node_count=0,
                        instance_size="M30",
                    ),
                    auto_scaling=AdvancedAutoScalingSettings(
                        compute=AdvancedComputeAutoScaling(
                            enabled=True,
                            max_instance_size="M60",
                            min_instance_size="M30",
                            scale_down_enabled=True,
                        ),
                        disk_gb=DiskGbAutoScaling(
                            enabled=True,
                        ),
                    ),
                    read_only_specs=DedicatedHardwareSpec20240805(
                        disk_size_gb=10,
                        node_count=0,
                        instance_size="M40",
                    ),
                )
            ],
            zone_name="Zone 1",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ClusterDescription20240805` 
    
</dd>
</dl>

<dl>
<dd>

**use_effective_instance_fields:** `typing.Optional[bool]` — Controls how hardware specification fields are returned in the response after cluster creation. When set to true, returns the original client-specified values and provides separate effective fields showing current operational values. When false (default), hardware specification fields show current operational values directly. Primarily used for autoscaling compatibility.
    
</dd>
</dl>

<dl>
<dd>

**use_effective_fields_replication_specs:** `typing.Optional[bool]` — Controls how `replicationSpecs` fields are returned in the response. When set to `true`, stores the client's view of `replicationSpecs` and returns it in `replicationSpecs`, while the actual cluster state (including auto-scaled hardware and auto-added shards) is returned in `effectiveReplicationSpecs`. When `false` (default), `replicationSpecs` contains the actual cluster state.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">get_cluster</a>(...) -> ClusterDescription20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. The response includes clusters with asymmetrically-sized shards. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. This feature is not available for serverless clusters.

This endpoint can also be used on Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) endpoint or former M2/M5 clusters that have been migrated to Flex clusters until January 2026. Please use the Get Flex Cluster endpoint for Flex clusters instead. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.get_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**use_effective_instance_fields:** `typing.Optional[bool]` — Controls how hardware specification fields are returned in the response. When set to true, returns the original client-specified values and provides separate effective fields showing current operational values. When false (default), hardware specification fields show current operational values directly. Primarily used for autoscaling compatibility.
    
</dd>
</dl>

<dl>
<dd>

**use_effective_fields_replication_specs:** `typing.Optional[bool]` — Controls how `replicationSpecs` are returned in the response. When set to `true`, returns the client-specified view in `replicationSpecs` and the actual cluster state in `effectiveReplicationSpecs`. When `false` (default), `replicationSpecs` contains the actual cluster state.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">delete_cluster</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one cluster from the specified project. The cluster must have termination protection disabled in order to be deleted. To use this resource, the requesting Service Account or API Key must have the Project Owner role. This feature is not available for serverless clusters.

This endpoint can also be used on Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) endpoint or former M2/M5 clusters that have been migrated to Flex clusters until January 2026. Please use the Delete Flex Cluster endpoint for Flex clusters instead. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.delete_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**retain_backups:** `typing.Optional[bool]` — Flag that indicates whether to retain backup snapshots for the deleted dedicated cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">update_cluster</a>(...) -> ClusterDescription20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. This resource can update clusters with asymmetrically-sized shards. To update a cluster's termination protection, the requesting Service Account or API Key must have the Project Owner role. For all other updates, the requesting Service Account or API Key must have the Project Cluster Manager role or the Project Replica Set Manager role. You can't modify a paused cluster (`paused : true`). You must call this endpoint to set `paused : false`. After this endpoint responds with `paused : false`, you can call it again with the changes you want to make to the cluster. This feature is not available for serverless clusters. Deprecated versions: v2-{2024-08-05}, v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.update_cluster(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ClusterDescription20240805` 
    
</dd>
</dl>

<dl>
<dd>

**use_effective_instance_fields:** `typing.Optional[bool]` — Controls how hardware specification fields are returned in the response after cluster updates. When set to true, returns the original client-specified values and provides separate effective fields showing current operational values. When false (default), hardware specification fields show current operational values directly. Note: When using this header with autoscaling enabled, MongoDB ignores `replicationSpecs` changes during updates. To intentionally override the `replicationSpecs`, disable this header.
    
</dd>
</dl>

<dl>
<dd>

**use_effective_fields_replication_specs:** `typing.Optional[bool]` — Controls how `replicationSpecs` fields are returned in the response. When set to `true`, stores the client's view of `replicationSpecs` and returns it in `replicationSpecs`, while the actual cluster state (including auto-scaled hardware and auto-added shards) is returned in `effectiveReplicationSpecs`. When `false` (default), `replicationSpecs` contains the actual cluster state.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">auto_scaling_configuration</a>(...) -> ClusterDescriptionAutoScalingModeConfiguration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the internal configuration of AutoScaling for sharded clusters. This endpoint can be used for diagnostic purposes to ensure that sharded clusters updated from older APIs have gained support for AutoScaling each shard independently.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.auto_scaling_configuration(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">get_process_args</a>(...) -> ClusterDescriptionProcessArgs20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings. This feature isn't available for `M0` free clusters, `M2` and `M5` shared-tier clusters, flex clusters, or serverless clusters. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.get_process_args(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">update_process_args</a>(...) -> ClusterDescriptionProcessArgs20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role. This feature isn't available for `M0` free clusters, `M2` and `M5` shared-tier clusters, flex clusters, or serverless clusters. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.update_process_args(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ClusterDescriptionProcessArgs20240805` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">restart_primaries</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a failover test for the specified cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. A failover test checks how MongoDB Cloud handles the failure of the cluster's primary node. During the test, MongoDB Cloud shuts down the primary node and elects a new primary. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.restart_primaries(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">get_cluster_status</a>(...) -> ClusterStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of all changes that you made to the specified cluster in the specified project. Use this resource to check the progress MongoDB Cloud has made in processing your changes. The response does not include the deployment of new dedicated clusters. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.get_cluster_status(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">grant_mongo_employee_access</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Grants MongoDB employee cluster access for the given duration and at the specified level for one cluster. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Support Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment
import datetime

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.grant_mongo_employee_access(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    expiration_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    grant_type="grantType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EmployeeAccessGrant` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">pin_feature_compatibility_version</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pins the Feature Compatibility Version (FCV) to the current MongoDB version and sets the pin expiration date. If an FCV pin already exists for the cluster, calling this method will only update the expiration date of the existing pin and will not re-pin the FCV.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.pin_feature_compatibility_version(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[datetime.datetime]` — Expiration date of the fixed FCV. If not specified, the expiration date will default to 4 weeks from the date FCV was originally pinned. Note that this field cannot exceed 4 weeks from the pinned date. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">revoke_mongo_employee_access</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes a previously granted MongoDB employee cluster access. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Support Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.revoke_mongo_employee_access(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">unpin_feature_compatibility_version</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpins the current fixed Feature Compatibility Version (FCV). This feature is not available for clusters on rapid release.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.unpin_feature_compatibility_version(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">list_cluster_provider_regions</a>(...) -> PaginatedApiAtlasProviderRegions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of regions available for the specified cloud provider at the specified tier. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.list_cluster_provider_regions(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**providers:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Cloud providers whose regions to retrieve. When you specify multiple providers, the response can return only tiers and regions that support multi-cloud clusters.
    
</dd>
</dl>

<dl>
<dd>

**tier:** `typing.Optional[str]` — Cluster tier for which to retrieve the regions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">upgrade_tenant_upgrade</a>(...) -> LegacyAtlasCluster</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrades a shared-tier cluster to a Flex or Dedicated (M10+) cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role. Each project supports up to 25 clusters. 

This endpoint can also be used to upgrade Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) API or former M2/M5 clusters that have been migrated to Flex clusters, using `instanceSizeName` to “M2” or “M5” until January 2026. This functionality will be available until January 22, 2026, after which it will only be available for M0 clusters. Please use the Upgrade Flex Cluster endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.upgrade_tenant_upgrade(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**accept_data_risks_and_force_replica_set_reconfig:** `typing.Optional[datetime.datetime]` — If reconfiguration is necessary to regain a primary due to a regional outage, submit this field alongside your topology reconfiguration to request a new regional outage resistant topology. Forced reconfigurations during an outage of the majority of electable nodes carry a risk of data loss if replicated writes (even majority committed writes) have not been replicated to the new primary node. MongoDB Atlas docs contain more information. To proceed with an operation which carries that risk, set `acceptDataRisksAndForceReplicaSetReconfig` to the current date. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**advanced_configuration:** `typing.Optional[ApiAtlasClusterAdvancedConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_scaling:** `typing.Optional[ClusterAutoScalingSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**backup_enabled:** `typing.Optional[bool]` — Flag that indicates whether the cluster can perform backups. If set to `true`, the cluster can perform backups. You must set this value to `true` for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to `false`, the cluster doesn't use MongoDB Cloud backups.
    
</dd>
</dl>

<dl>
<dd>

**bi_connector:** `typing.Optional[BiConnector]` 
    
</dd>
</dl>

<dl>
<dd>

**cluster_type:** `typing.Optional[str]` — Configuration of nodes that comprise the cluster.
    
</dd>
</dl>

<dl>
<dd>

**config_server_management_mode:** `typing.Optional[str]` — Config Server Management Mode for creating or updating a sharded cluster. When configured as `ATLAS_MANAGED`, Atlas may automatically switch the cluster's config server type for optimal performance and savings. When configured as `FIXED_TO_DEDICATED`, the cluster will always use a dedicated config server.
    
</dd>
</dl>

<dl>
<dd>

**delete_after_creation_hours:** `typing.Optional[int]` 

Number of hours after cluster creation that this cluster will be automatically deleted.

This field is used to derive `deleteAfterDate` relative to `createDate`.

When set to null or zero on cluster creation, the cluster will not be automatically deleted.

When set to a positive value on cluster creation, the cluster will be automatically deleted after the specified number of hours.

When updating this field on an existing (non-deleted) cluster, and this is set to null, then existing values are preserved for this & `deleteAfterDate`.

When updating this field on an existing (non-deleted) cluster, and this is set to zero, then `deleteAfterDate` is reset to null (disable auto deletion) regardless of previous configurations.

When updating this field on an existing (non-deleted) cluster, and this is set to a positive value, then `createDate` + `deleteAfterCreationHours` must be later than now else the field update is ignored and existing values are preserved for this & `deleteAfterDate`.
    
</dd>
</dl>

<dl>
<dd>

**disk_size_gb:** `typing.Optional[float]` 

Storage capacity of instance data volumes expressed in gigabytes. Increase this number to add capacity.

 This value is not configurable on M0/M2/M5 clusters.

 MongoDB Cloud requires this parameter if you set `replicationSpecs`.

 If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. 

 Storage charge calculations depend on whether you choose the default value or a custom value.

 The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.
    
</dd>
</dl>

<dl>
<dd>

**disk_warming_mode:** `typing.Optional[str]` — Disk warming mode selection.
    
</dd>
</dl>

<dl>
<dd>

**encryption_at_rest_provider:** `typing.Optional[str]` — Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster `replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize` setting must be `M10` or higher and `"backupEnabled" : false` or omitted entirely.
    
</dd>
</dl>

<dl>
<dd>

**global_cluster_self_managed_sharding:** `typing.Optional[bool]` 

Set this field to configure the Sharding Management Mode when creating a new Global Cluster.

When set to false, the management mode is set to Atlas-Managed Sharding. This mode fully manages the sharding of your Global Cluster and is built to provide a seamless deployment experience.

When set to true, the management mode is set to Self-Managed Sharding. This mode leaves the management of shards in your hands and is built to provide an advanced and flexible deployment experience.

This setting cannot be changed once the cluster is deployed.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.List[ComponentLabel]]` 

Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.

Cluster labels are deprecated and will be removed in a future release. We strongly recommend that you use Resource Tags instead.
    
</dd>
</dl>

<dl>
<dd>

**mongo_db_employee_access_grant:** `typing.Optional[EmployeeAccessGrant]` 
    
</dd>
</dl>

<dl>
<dd>

**mongo_db_major_version:** `typing.Optional[str]` 

MongoDB major version of the cluster.

On creation: Choose from the available versions of MongoDB, or leave unspecified for the current recommended default in the MongoDB Cloud platform. The recommended version is a recent Long Term Support version. The default is not guaranteed to be the most recently released version throughout the entire release cycle. For versions available in a specific project, see the linked documentation or use the API endpoint for [project LTS versions endpoint](#tag/Projects/operation/getProjectLTSVersions).

 On update: Increase version only by 1 major version at a time. If the cluster is pinned to a MongoDB feature compatibility version exactly one major version below the current MongoDB version, the MongoDB version can be downgraded to the previous major version.
    
</dd>
</dl>

<dl>
<dd>

**mongo_db_version:** `typing.Optional[str]` — Version of MongoDB that the cluster runs.
    
</dd>
</dl>

<dl>
<dd>

**num_shards:** `typing.Optional[int]` — Number of shards up to 50 to deploy for a sharded cluster. The resource returns `1` to indicate a replica set and values of `2` and higher to indicate a sharded cluster. The returned value equals the number of shards in the cluster.
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Flag that indicates whether the cluster is paused.
    
</dd>
</dl>

<dl>
<dd>

**pit_enabled:** `typing.Optional[bool]` — Flag that indicates whether the cluster uses continuous cloud backups.
    
</dd>
</dl>

<dl>
<dd>

**provider_backup_enabled:** `typing.Optional[bool]` — Flag that indicates whether the M10 or higher cluster can perform Cloud Backups. If set to `true`, the cluster can perform backups. If this and `backupEnabled` are set to `false`, the cluster doesn't use MongoDB Cloud backups.
    
</dd>
</dl>

<dl>
<dd>

**provider_settings:** `typing.Optional[ClusterProviderSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**replica_set_scaling_strategy:** `typing.Optional[str]` 

Set this field to configure the replica set scaling mode for your cluster.

By default, Atlas scales under `WORKLOAD_TYPE`. This mode allows Atlas to scale your analytics nodes in parallel to your operational nodes.

When configured as `SEQUENTIAL`, Atlas scales all nodes sequentially. This mode is intended for steady-state workloads and applications performing latency-sensitive secondary reads.

When configured as `NODE_TYPE`, Atlas scales your electable nodes in parallel with your read-only and analytics nodes. This mode is intended for large, dynamic workloads requiring frequent and timely cluster tier scaling. This is the fastest scaling strategy, but it might impact latency of workloads when performing extensive secondary reads.
    
</dd>
</dl>

<dl>
<dd>

**replication_factor:** `typing.Optional[int]` — Number of members that belong to the replica set. Each member retains a copy of your databases, providing high availability and data redundancy. Use `replicationSpecs` instead.
    
</dd>
</dl>

<dl>
<dd>

**replication_spec:** `typing.Optional[typing.Dict[str, RegionSpec]]` — Physical location where MongoDB Cloud provisions cluster nodes.
    
</dd>
</dl>

<dl>
<dd>

**replication_specs:** `typing.Optional[typing.List[LegacyReplicationSpec]]` 

List of settings that configure your cluster regions.

- For Global Clusters, each object in the array represents one zone where MongoDB Cloud deploys your clusters nodes.
- For non-Global sharded clusters and replica sets, the single object represents where MongoDB Cloud deploys your clusters nodes.
    
</dd>
</dl>

<dl>
<dd>

**root_cert_type:** `typing.Optional[str]` — Root Certificate Authority that MongoDB Atlas cluster uses. MongoDB Cloud supports Internet Security Research Group.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[ResourceTag]]` — List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster.
    
</dd>
</dl>

<dl>
<dd>

**termination_protection_enabled:** `typing.Optional[bool]` — Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.
    
</dd>
</dl>

<dl>
<dd>

**version_release_system:** `typing.Optional[str]` — Method by which the cluster maintains the MongoDB versions. If value is `CONTINUOUS`, you must not specify `mongoDBMajorVersion`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">upgrade_cluster_to_serverless</a>(...) -> ServerlessInstanceDescription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint has been deprecated as of February 2025 as we no longer support the creation of new serverless instances. Please use the Upgrade Flex Cluster endpoint to upgrade Flex clusters.

 Upgrades a shared-tier cluster to a serverless instance in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ServerlessProviderSettings
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.upgrade_cluster_to_serverless(
    group_id_="32b6e34b3d91647abb20e7b8",
    provider_settings=ServerlessProviderSettings(
        backing_provider_name="backingProviderName",
        region_name="regionName",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ServerlessInstanceDescription` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">request_sample_dataset_load</a>(...) -> SampleDatasetStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests loading the MongoDB sample dataset into the specified cluster. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.request_sample_dataset_load(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the cluster into which you load the sample dataset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/atlas_sdk/clusters/client.py">get_sample_dataset_load</a>(...) -> SampleDatasetStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks the progress of loading the sample dataset into one cluster. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.clusters.get_sample_dataset_load(
    group_id="32b6e34b3d91647abb20e7b8",
    sample_dataset_id="sampleDatasetId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**sample_dataset_id:** `str` — Unique 24-hexadecimal digit string that identifies the loaded sample dataset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/atlas_sdk/events/client.py">list_event_types</a>(...) -> PaginatedEventTypeDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all event types, along with a description and additional metadata about each event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.events.list_event_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/atlas_sdk/events/client.py">list_group_events</a>(...) -> GroupPaginatedEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns events for the specified project. Events identify significant database, billing, or security activities or status changes. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.events.list_group_events(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**cluster_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[typing.Union[EventTypeForNdsGroup, typing.Sequence[EventTypeForNdsGroup]]]` 

Category of incident recorded at this moment in time.

**IMPORTANT**: The complete list of event type values changes frequently.
    
</dd>
</dl>

<dl>
<dd>

**excluded_event_type:** `typing.Optional[typing.Union[EventTypeForNdsGroup, typing.Sequence[EventTypeForNdsGroup]]]` 

Category of event that you would like to exclude from query results, such as `CLUSTER_CREATED`.

**IMPORTANT**: Event type names change frequently. Verify that you specify the event type correctly by checking the complete list of event types.
    
</dd>
</dl>

<dl>
<dd>

**include_raw:** `typing.Optional[bool]` — Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
    
</dd>
</dl>

<dl>
<dd>

**max_date:** `typing.Optional[datetime.datetime]` — Date and time from when MongoDB Cloud stops returning events. This parameter uses the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**min_date:** `typing.Optional[datetime.datetime]` — Date and time from when MongoDB Cloud starts returning events. This parameter uses the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/atlas_sdk/events/client.py">get_group_event</a>(...) -> EventViewForNdsGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one event for the specified project. Events identify significant database, billing, or security activities or status changes. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Use the Return Events from One Project endpoint to retrieve all events to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.events.get_group_event(
    group_id="32b6e34b3d91647abb20e7b8",
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique 24-hexadecimal digit string that identifies the event that you want to return.
    
</dd>
</dl>

<dl>
<dd>

**include_raw:** `typing.Optional[bool]` — Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/atlas_sdk/events/client.py">list_org_events</a>(...) -> OrgPaginatedEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns events for the specified organization. Events identify significant database, billing, or security activities or status changes. To use this resource, the requesting Service Account or API Key must have the Organization Member role.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.events.list_org_events(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[typing.Union[EventTypeForOrg, typing.Sequence[EventTypeForOrg]]]` 

Category of incident recorded at this moment in time.

**IMPORTANT**: The complete list of event type values changes frequently.
    
</dd>
</dl>

<dl>
<dd>

**include_raw:** `typing.Optional[bool]` — Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
    
</dd>
</dl>

<dl>
<dd>

**max_date:** `typing.Optional[datetime.datetime]` — Date and time from when MongoDB Cloud stops returning events. This parameter uses the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**min_date:** `typing.Optional[datetime.datetime]` — Date and time from when MongoDB Cloud starts returning events. This parameter uses the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/atlas_sdk/events/client.py">get_org_event</a>(...) -> EventViewForOrg</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one event for the specified organization. Events identify significant database, billing, or security activities or status changes. To use this resource, the requesting Service Account or API Key must have the Organization Member role. Use the Return Events from One Organization endpoint to retrieve all events to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.events.get_org_event(
    org_id="4888442a3354817a7320eb61",
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique 24-hexadecimal digit string that identifies the event that you want to return.
    
</dd>
</dl>

<dl>
<dd>

**include_raw:** `typing.Optional[bool]` — Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Federated Authentication
<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">delete_federation_setting</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the federation settings instance and all associated data, including identity providers and domains. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in the last remaining connected organization. **Note**: requests to this resource will fail if there is more than one connected organization in the federation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.delete_federation_setting(
    federation_settings_id="55fa922fb343282757d9554e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">list_connected_org_configs</a>(...) -> PaginatedConnectedOrgConfigs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all connected organization configurations in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.list_connected_org_configs(
    federation_settings_id="55fa922fb343282757d9554e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">get_connected_org_config</a>(...) -> ConnectedOrgConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified connected organization configuration from the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in the connected organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.get_connected_org_config(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the connected organization configuration to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">remove_connected_org_config</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one connected organization configuration from the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role. Note: This request fails if only one connected organization exists in the federation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.remove_connected_org_config(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the connected organization configuration to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">update_connected_org_config</a>(...) -> ConnectedOrgConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one connected organization configuration from the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role. 

**Note** If the organization configuration has no associated identity provider, you can't use this resource to update role mappings or post authorization role grants.  

**Note**: The `domainRestrictionEnabled` field defaults to false if not provided in the request. 

**Note**: If the `identityProviderId` field is not provided, you will disconnect the organization and the identity provider. 

**Note**: Currently connected data access identity providers missing from the `dataAccessIdentityProviderIds` field will be disconnected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.update_connected_org_config(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id_="32b6e34b3d91647abb20e7b8",
    domain_restriction_enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the connected organization configuration to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ConnectedOrgConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">list_role_mappings</a>(...) -> PaginatedRoleMapping</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all role mappings from the specified organization in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.list_role_mappings(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">create_role_mapping</a>(...) -> AuthFederationRoleMapping</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one role mapping to the specified organization in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ConnectedOrgConfigRoleAssignment
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.create_role_mapping(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="4888442a3354817a7320eb61",
    external_group_name="externalGroupName",
    role_assignments=[
        ConnectedOrgConfigRoleAssignment()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AuthFederationRoleMapping` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">get_role_mapping</a>(...) -> AuthFederationRoleMapping</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one role mapping from the specified organization in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.get_role_mapping(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="4888442a3354817a7320eb61",
    id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique 24-hexadecimal digit string that identifies the role mapping that you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">update_role_mapping</a>(...) -> AuthFederationRoleMapping</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one role mapping in the specified organization in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ConnectedOrgConfigRoleAssignment
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.update_role_mapping(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="4888442a3354817a7320eb61",
    id_="32b6e34b3d91647abb20e7b8",
    external_group_name="externalGroupName",
    role_assignments=[
        ConnectedOrgConfigRoleAssignment()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique 24-hexadecimal digit string that identifies the role mapping that you want to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AuthFederationRoleMapping` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">delete_role_mapping</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one role mapping in the specified organization from the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.delete_role_mapping(
    federation_settings_id="55fa922fb343282757d9554e",
    org_id="4888442a3354817a7320eb61",
    id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique 24-hexadecimal digit string that identifies the role mapping that you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">list_identity_providers</a>(...) -> PaginatedFederationIdentityProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all identity providers with the provided protocol and type in the specified federation. If no protocol is specified, only SAML identity providers will be returned. If no `idpType` is specified, only WORKFORCE identity providers will be returned. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.list_identity_providers(
    federation_settings_id="55fa922fb343282757d9554e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The protocols of the target identity providers.
    
</dd>
</dl>

<dl>
<dd>

**idp_type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The types of the target identity providers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">create_identity_provider</a>(...) -> FederationOidcIdentityProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one identity provider within the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

**Note**: This resource only supports the creation of OIDC identity providers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.create_identity_provider(
    federation_settings_id="55fa922fb343282757d9554e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[str]` — Identifier of the intended recipient of the token.
    
</dd>
</dl>

<dl>
<dd>

**authorization_type:** `typing.Optional[str]` — Indicates whether authorization is granted based on group membership or user ID.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Human-readable label that identifies the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**groups_claim:** `typing.Optional[str]` — Identifier of the claim which contains IdP Group IDs in the token.
    
</dd>
</dl>

<dl>
<dd>

**idp_type:** `typing.Optional[str]` — String enum that indicates the type of the identity provider. Default is WORKFORCE.
    
</dd>
</dl>

<dl>
<dd>

**issuer_uri:** `typing.Optional[str]` — Unique string that identifies the issuer of the SAML Assertion or OIDC metadata/discovery document URL.
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `typing.Optional[str]` — String enum that indicates the protocol of the identity provider. Either SAML or OIDC.
    
</dd>
</dl>

<dl>
<dd>

**user_claim:** `typing.Optional[str]` — Identifier of the claim which contains the user ID in the token.
    
</dd>
</dl>

<dl>
<dd>

**associated_domains:** `typing.Optional[typing.List[str]]` — List that contains the domains associated with the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client identifier that is assigned to an application by the Identity Provider.
    
</dd>
</dl>

<dl>
<dd>

**requested_scopes:** `typing.Optional[typing.List[str]]` — Scopes that MongoDB applications will request from the authorization endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">get_identity_provider</a>(...) -> FederationIdentityProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one identity provider in the specified federation by the identity provider's id. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.get_identity_provider(
    federation_settings_id="55fa922fb343282757d9554e",
    identity_provider_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**identity_provider_id:** `str` — Unique string that identifies the identity provider to connect. If using an API version before 11-15-2023, use the legacy 20-hexadecimal digit id. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider. For all other versions, use the 24-hexadecimal digit id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">delete_identity_provider</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one identity provider in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role for the connected organization. 

**Note**: Requests to this resource will fail if the identity provider is connected to more than one organization or is connected to an organization unowned by the requesting Service Account or API key. Before deleting an identity provider, confirm that no organization in your federation uses this identity provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.delete_identity_provider(
    federation_settings_id="55fa922fb343282757d9554e",
    identity_provider_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**identity_provider_id:** `str` — Unique 24-hexadecimal digit string that identifies the identity provider to connect.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">update_identity_provider</a>(...) -> FederationIdentityProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one identity provider in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

**Note**: Changing authorization types and/or updating authorization claims can prevent current users and/or groups from accessing the database.

**Note**: When deactivating a SAML identity provider connected to an organization, the requesting Service Account or API key must have the Organization Owner role for the organization. If the identity provider is connected to multiple organizations, the request will fail. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.update_identity_provider(
    federation_settings_id="55fa922fb343282757d9554e",
    identity_provider_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**identity_provider_id:** `str` — Unique string that identifies the identity provider to connect. If using an API version before 11-15-2023, use the legacy 20-hexadecimal digit id. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider. For all other versions, use the 24-hexadecimal digit id.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Human-readable label that identifies the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**idp_type:** `typing.Optional[str]` — String enum that indicates the type of the identity provider. Default is WORKFORCE.
    
</dd>
</dl>

<dl>
<dd>

**issuer_uri:** `typing.Optional[str]` — Unique string that identifies the issuer of the SAML Assertion or OIDC metadata/discovery document URL.
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `typing.Optional[str]` — String enum that indicates the protocol of the identity provider. Either SAML or OIDC.
    
</dd>
</dl>

<dl>
<dd>

**associated_domains:** `typing.Optional[typing.List[str]]` — List that contains the domains associated with the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**pem_file_info:** `typing.Optional[PemFileInfoUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_binding:** `typing.Optional[str]` — SAML Authentication Request Protocol HTTP method binding (POST or REDIRECT) that Federated Authentication uses to send the authentication request.
    
</dd>
</dl>

<dl>
<dd>

**response_signature_algorithm:** `typing.Optional[str]` — Signature algorithm that Federated Authentication uses to encrypt the identity provider signature.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — Custom SSO URL for the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**sso_debug_enabled:** `typing.Optional[bool]` — Flag that indicates whether the identity provider has SSO debug enabled.
    
</dd>
</dl>

<dl>
<dd>

**sso_url:** `typing.Optional[str]` — URL that points to the receiver of the SAML authentication request.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — String enum that indicates whether the identity provider is active.
    
</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[str]` — Identifier of the intended recipient of the token.
    
</dd>
</dl>

<dl>
<dd>

**authorization_type:** `typing.Optional[str]` — Indicates whether authorization is granted based on group membership or user ID.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Client identifier that is assigned to an application by the Identity Provider.
    
</dd>
</dl>

<dl>
<dd>

**groups_claim:** `typing.Optional[str]` — Identifier of the claim which contains IdP Group IDs in the token.
    
</dd>
</dl>

<dl>
<dd>

**requested_scopes:** `typing.Optional[typing.List[str]]` — Scopes that MongoDB applications will request from the authorization endpoint.
    
</dd>
</dl>

<dl>
<dd>

**user_claim:** `typing.Optional[str]` — Identifier of the claim which contains the user ID in the token.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">revoke_identity_provider_jwks</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes the JWKS tokens from the requested OIDC identity provider. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations. 

**Note**: Revoking your JWKS tokens immediately refreshes your IdP public keys from all your Atlas clusters, invalidating previously signed access tokens and logging out all users. You may need to restart your MongoDB clients. All organizations connected to the identity provider will be affected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.revoke_identity_provider_jwks(
    federation_settings_id="55fa922fb343282757d9554e",
    identity_provider_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**identity_provider_id:** `str` — Unique 24-hexadecimal digit string that identifies the identity provider to connect.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">get_identity_provider_metadata</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the metadata of one identity provider in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.get_identity_provider_metadata(
    federation_settings_id="55fa922fb343282757d9554e",
    identity_provider_id="c2777a9eca931f29fc2f",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**federation_settings_id:** `str` — Unique 24-hexadecimal digit string that identifies your federation.
    
</dd>
</dl>

<dl>
<dd>

**identity_provider_id:** `str` — Legacy 20-hexadecimal digit string that identifies the identity provider. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.federated_authentication.<a href="src/atlas_sdk/federated_authentication/client.py">get_federation_settings</a>(...) -> OrgFederationSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the federation settings for the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in the connected organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.federated_authentication.get_federation_settings(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Projects
<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">list_groups</a>(...) -> PaginatedAtlasGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about all projects. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings. To use this resource, the requesting Service Account or API Key must have the Organization Read Only role or higher.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.list_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">create_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings. To use this resource, the requesting Service Account or API Key must have the Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.create_group(
    name="name",
    org_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Group` 
    
</dd>
</dl>

<dl>
<dd>

**project_owner_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user to whom to grant the Project Owner role on the specified project. If you set this parameter, it overrides the default value of the oldest Organization Owner.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the specified project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_group(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">delete_group</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings. You can delete a project only if there are no Online Archives for the clusters in the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.delete_group(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">update_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the human-readable label that identifies the specified project, or the tags associated with the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.update_group(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable label that identifies the project included in the MongoDB Cloud organization.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[ResourceTag]]` — List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the project.
    
</dd>
</dl>

<dl>
<dd>

**with_default_alerts_settings:** `typing.Optional[bool]` — Flag that indicates whether the project can automatically create default alerts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">add_group_user</a>(...) -> OrganizationInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one MongoDB Cloud user to the specified project. If the MongoDB Cloud user is not a member of the project's organization, then the user must accept their invitation to the organization to access information within the specified project. If the MongoDB Cloud User is already a member of the project's organization, then they will be added to the project immediately and an invitation will not be returned by this resource. To use this resource, the requesting Service Account or API Key must have the Group User Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.add_group_user(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupInvitationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">list_group_invites</a>(...) -> typing.List[GroupInvitation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all pending invitations to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.list_group_invites(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Email address of the user account invited to this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">create_group_invite</a>(...) -> GroupInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invites one MongoDB Cloud user to join the specified project. The MongoDB Cloud user must accept the invitation to access information within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.create_group_invite(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupInvitationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">update_group_invites</a>(...) -> GroupInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of one pending invitation to the specified project. To specify which invitation to update, provide the username of the invited user. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.update_group_invites(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupInvitationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_group_invite</a>(...) -> GroupInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one pending invitation to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_group_invite(
    group_id="32b6e34b3d91647abb20e7b8",
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — Unique 24-hexadecimal digit string that identifies the invitation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">delete_group_invite</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels one pending invitation sent to the specified MongoDB Cloud user to join a project. You can't cancel an invitation that the user accepted. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Note: deleting a project invitation does not delete an organization invitation even if they were created together.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.delete_group_invite(
    group_id="32b6e34b3d91647abb20e7b8",
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — Unique 24-hexadecimal digit string that identifies the invitation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">update_invite_by_id</a>(...) -> GroupInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of one pending invitation to the specified project. To specify which invitation to update, provide the unique identification string for that invitation. Use the Return All Project Invitations endpoint to retrieve IDs for all pending project invitations. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.update_invite_by_id(
    group_id="32b6e34b3d91647abb20e7b8",
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — Unique 24-hexadecimal digit string that identifies the invitation.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — One or more project-level roles to assign to the MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_group_ip_addresses</a>(...) -> GroupIpAddresses</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all IP addresses for this project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_group_ip_addresses(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">list_group_limits</a>(...) -> typing.List[DataFederationLimit]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all the limits for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.list_group_limits(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_group_limit</a>(...) -> DataFederationLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified limit for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_group_limit(
    group_id="32b6e34b3d91647abb20e7b8",
    limit_name="limitName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**limit_name:** `str` 

Human-readable label that identifies this project limit.

| Limit Name | Description | Default | API Override Limit |
| --- | --- | --- | --- |
| `atlas.project.deployment.clusters` | Limit on the number of clusters in this project | 25 | 100 |
| `atlas.project.deployment.nodesPerPrivateLinkRegion` | Limit on the number of nodes per Private Link region in this project | 50 | 90 |
| `atlas.project.security.databaseAccess.customRoles` | Limit on the number of custom roles in this project | 100 | 1400 |
| `atlas.project.security.databaseAccess.users` | Limit on the number of database users in this project | 100 | 100 |
| `atlas.project.security.networkAccess.crossRegionEntries` | Limit on the number of cross-region network access entries in this project | 40 | 220 |
| `atlas.project.security.networkAccess.entries` | Limit on the number of network access entries in this project | 200 | 20 |
| `dataFederation.bytesProcessed.query` | Limit on the number of bytes processed during a single Data Federation query | N/A | N/A |
| `dataFederation.bytesProcessed.daily` | Limit on the number of bytes processed across all Data Federation tenants for the current day | N/A | N/A |
| `dataFederation.bytesProcessed.weekly` | Limit on the number of bytes processed across all Data Federation tenants for the current week | N/A | N/A |
| `dataFederation.bytesProcessed.monthly` | Limit on the number of bytes processed across all Data Federation tenants for the current month | N/A | N/A |
| `atlas.project.deployment.privateServiceConnectionsPerRegionGroup` | Number of Private Service Connections per Region Group | 50 | 100|
| `atlas.project.deployment.privateServiceConnectionsSubnetMask` | Subnet mask for GCP PSC Networks. Has lower limit of 20. | 27 | 27|
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">delete_group_limit</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified project limit. Depending on the limit, Atlas either resets the limit to its default value or removes the limit entirely. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.delete_group_limit(
    group_id="32b6e34b3d91647abb20e7b8",
    limit_name="limitName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**limit_name:** `str` 

Human-readable label that identifies this project limit.

| Limit Name | Description | Default | API Override Limit |
| --- | --- | --- | --- |
| `atlas.project.deployment.clusters` | Limit on the number of clusters in this project | 25 | 100 |
| `atlas.project.deployment.nodesPerPrivateLinkRegion` | Limit on the number of nodes per Private Link region in this project | 50 | 90 |
| `atlas.project.security.databaseAccess.customRoles` | Limit on the number of custom roles in this project | 100 | 1400 |
| `atlas.project.security.databaseAccess.users` | Limit on the number of database users in this project | 100 | 100 |
| `atlas.project.security.networkAccess.crossRegionEntries` | Limit on the number of cross-region network access entries in this project | 40 | 220 |
| `atlas.project.security.networkAccess.entries` | Limit on the number of network access entries in this project | 200 | 20 |
| `dataFederation.bytesProcessed.query` | Limit on the number of bytes processed during a single Data Federation query | N/A | N/A |
| `dataFederation.bytesProcessed.daily` | Limit on the number of bytes processed across all Data Federation tenants for the current day | N/A | N/A |
| `dataFederation.bytesProcessed.weekly` | Limit on the number of bytes processed across all Data Federation tenants for the current week | N/A | N/A |
| `dataFederation.bytesProcessed.monthly` | Limit on the number of bytes processed across all Data Federation tenants for the current month | N/A | N/A |
| `atlas.project.deployment.privateServiceConnectionsPerRegionGroup` | Number of Private Service Connections per Region Group | 50 | 100|
| `atlas.project.deployment.privateServiceConnectionsSubnetMask` | Subnet mask for GCP PSC Networks. Has lower limit of 20. | 27 | 27|
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">set_group_limit</a>(...) -> DataFederationLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the specified project limit. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

**NOTE**: Increasing the following configuration limits might lead to slower response times in the MongoDB Cloud UI or increased user management overhead leading to authentication or authorization re-architecture. If possible, we recommend that you create additional projects to gain access to more of these resources for a more sustainable growth pattern.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.set_group_limit(
    group_id="32b6e34b3d91647abb20e7b8",
    limit_name="limitName",
    value=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**limit_name:** `str` 

Human-readable label that identifies this project limit.

| Limit Name | Description | Default | API Override Limit |
| --- | --- | --- | --- |
| `atlas.project.deployment.clusters` | Limit on the number of clusters in this project | 25 | 100 |
| `atlas.project.deployment.nodesPerPrivateLinkRegion` | Limit on the number of nodes per Private Link region in this project | 50 | 90 |
| `atlas.project.security.databaseAccess.customRoles` | Limit on the number of custom roles in this project | 100 | 1400 |
| `atlas.project.security.databaseAccess.users` | Limit on the number of database users in this project | 100 | 100 |
| `atlas.project.security.networkAccess.crossRegionEntries` | Limit on the number of cross-region network access entries in this project | 40 | 220 |
| `atlas.project.security.networkAccess.entries` | Limit on the number of network access entries in this project | 200 | 20 |
| `dataFederation.bytesProcessed.query` | Limit on the number of bytes processed during a single Data Federation query | N/A | N/A |
| `dataFederation.bytesProcessed.daily` | Limit on the number of bytes processed across all Data Federation tenants for the current day | N/A | N/A |
| `dataFederation.bytesProcessed.weekly` | Limit on the number of bytes processed across all Data Federation tenants for the current week | N/A | N/A |
| `dataFederation.bytesProcessed.monthly` | Limit on the number of bytes processed across all Data Federation tenants for the current month | N/A | N/A |
| `atlas.project.deployment.privateServiceConnectionsPerRegionGroup` | Number of Private Service Connections per Region Group | 50 | 100|
| `atlas.project.deployment.privateServiceConnectionsSubnetMask` | Subnet mask for GCP PSC Networks. Has lower limit of 20. | 27 | 27|
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataFederationLimit` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_mongo_db_versions</a>(...) -> PaginatedAvailableVersion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the MongoDB Long Term Support Major Versions available to new clusters in this project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_mongo_db_versions(
    group_id="32b6e34b3d91647abb20e7b8",
    instance_size="M10",
    items_per_page=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `typing.Optional[str]` — Filter results to only one cloud provider.
    
</dd>
</dl>

<dl>
<dd>

**instance_size:** `typing.Optional[str]` — Filter results to only one instance size.
    
</dd>
</dl>

<dl>
<dd>

**default_status:** `typing.Optional[str]` — Filter results to only the default values per tier. This value must be DEFAULT.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_group_settings</a>(...) -> GroupSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the specified project's settings. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_group_settings(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">update_group_settings</a>(...) -> GroupSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the settings of the specified project. You can update any of the options available. MongoDB cloud only updates the options provided in the request. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.update_group_settings(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupSettings` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">update_group_user_roles</a>(...) -> UpdateGroupRolesForUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the roles of the specified user in the specified project. To specify the user to update, provide the unique 24-hexadecimal digit string that identifies the user in the specified project. To use this resource, the requesting Service Account or API Key must have the Group User Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.update_group_user_roles(
    group_id="32b6e34b3d91647abb20e7b8",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the user to modify.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateGroupRolesForUser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">migrate_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrates a project from its current organization to another organization. All project users and their roles will be copied to the same project in the destination organization. You must include an organization API key with the Organization Owner role for the destination organization to verify access to the destination organization when you authenticate with Programmatic API Keys. Otherwise, the requesting user must have the Organization Owner role in both organizations. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.migrate_group(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**destination_org_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the organization to move the specified project to.
    
</dd>
</dl>

<dl>
<dd>

**destination_org_private_api_key:** `typing.Optional[str]` — Unique string that identifies the private part of the API Key used to verify access to the destination organization. This parameter is required only when you authenticate with Programmatic API Keys.
    
</dd>
</dl>

<dl>
<dd>

**destination_org_public_api_key:** `typing.Optional[str]` — Unique string that identifies the public part of the API Key used to verify access to the destination organization. This parameter is required only when you authenticate with Programmatic API Keys.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/atlas_sdk/projects/client.py">get_group_by_name</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the specified project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.projects.get_group_by_name(
    group_name="groupName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_name:** `str` — Human-readable label that identifies this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Project IP Access List
<details><summary><code>client.project_ip_access_list.<a href="src/atlas_sdk/project_ip_access_list/client.py">list_access_list_entries</a>(...) -> PaginatedNetworkAccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all access list entries from the specified project's IP access list. Each entry in the project's IP access list contains either one IP address or one CIDR-notated block of IP addresses. MongoDB Cloud only allows client connections to the cluster from entries in the project's IP access list. To use this resource, the requesting Service Account or API Key must have the Project Read Only or Project Charts Admin roles. This resource replaces the whitelist resource. MongoDB Cloud removed whitelists in July 2021. Update your applications to use this new resource. The `/groups/{GROUP-ID}/accessList` endpoint manages the database IP access list. This endpoint is distinct from the `orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accesslist` endpoint, which manages the access list for MongoDB Cloud organizations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.project_ip_access_list.list_access_list_entries(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_ip_access_list.<a href="src/atlas_sdk/project_ip_access_list/client.py">create_access_list_entry</a>(...) -> PaginatedNetworkAccess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one or more access list entries to the specified project. MongoDB Cloud only allows client connections to the cluster from entries in the project's IP access list. Write each entry as either one IP address or one CIDR-notated block of IP addresses. To use this resource, the requesting Service Account or API Key must have the Project Owner role, Project Charts Admin role, or Project Network Access Manager role. This resource replaces the whitelist resource. MongoDB Cloud removed whitelists in July 2021. Update your applications to use this new resource. The `/groups/{GROUP-ID}/accessList` endpoint manages the database IP access list. This endpoint is distinct from the `orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accesslist` endpoint, which manages the access list for MongoDB Cloud organizations. This endpoint doesn't support concurrent `POST` requests. You must submit multiple `POST` requests synchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, NetworkPermissionEntry
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.project_ip_access_list.create_access_list_entry(
    group_id="32b6e34b3d91647abb20e7b8",
    request=[
        NetworkPermissionEntry()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[NetworkPermissionEntry]` 
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_ip_access_list.<a href="src/atlas_sdk/project_ip_access_list/client.py">get_access_list_entry</a>(...) -> NetworkPermissionEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one access list entry from the specified project's IP access list. Each entry in the project's IP access list contains either one IP address or one CIDR-notated block of IP addresses. MongoDB Cloud only allows client connections to the cluster from entries in the project's IP access list. To use this resource, the requesting Service Account or API Key must have the Project Read Only or Project Charts Admin roles. This resource replaces the whitelist resource. MongoDB Cloud removed whitelists in July 2021. Update your applications to use this new resource. This endpoint (`/groups/{GROUP-ID}/accessList`) manages the Project IP Access List. It doesn't manage the access list for MongoDB Cloud organizations. The Programmatic API Keys endpoint (`/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accesslist`) manages those access lists.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.project_ip_access_list.get_access_list_entry(
    group_id="32b6e34b3d91647abb20e7b8",
    entry_value="IPv4: 192.0.2.0%2F24 or IPv6: 2001:db8:85a3:8d3:1319:8a2e:370:7348 or IPv4 CIDR: 198.51.100.0%2f24 or IPv6 CIDR: 2001:db8::%2f58 or AWS SG: sg-903004f8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**entry_value:** `str` — Access list entry that you want to return from the project's IP access list. This value can use one of the following: one AWS security group ID, one IP address, or one CIDR block of addresses. For CIDR blocks that use a subnet mask, replace the forward slash (`/`) with its URL-encoded value (`%2F`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_ip_access_list.<a href="src/atlas_sdk/project_ip_access_list/client.py">delete_access_list_entry</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one access list entry from the specified project's IP access list. Each entry in the project's IP access list contains one IP address, one CIDR-notated block of IP addresses, or one AWS Security Group ID. MongoDB Cloud only allows client connections to the cluster from entries in the project's IP access list. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Network Access Manager role. This resource replaces the whitelist resource. MongoDB Cloud removed whitelists in July 2021. Update your applications to use this new resource. The `/groups/{GROUP-ID}/accessList` endpoint manages the database IP access list. This endpoint is distinct from the `orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accesslist` endpoint, which manages the access list for MongoDB Cloud organizations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.project_ip_access_list.delete_access_list_entry(
    group_id="32b6e34b3d91647abb20e7b8",
    entry_value="IPv4: 192.0.2.0%2F24 or IPv6: 2001:db8:85a3:8d3:1319:8a2e:370:7348 or IPv4 CIDR: 198.51.100.0%2f24 or IPv6 CIDR: 2001:db8::%2f58 or AWS SG: sg-903004f8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**entry_value:** `str` 

Access list entry that you want to remove from the project's IP access list. This value can use one of the following: one AWS security group ID, one IP address, or one CIDR block of addresses. For CIDR blocks that use a subnet mask, replace the forward slash (`/`) with its URL-encoded value (`%2F`). When you remove an entry from the IP access list, existing connections from the removed address or addresses may remain open for a variable amount of time. The amount of time it takes MongoDB Cloud to close the connection depends upon several factors, including:

- how your application established the connection,
- how MongoDB Cloud or the driver using the address behaves, and
- which protocol (like TCP or UDP) the connection uses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_ip_access_list.<a href="src/atlas_sdk/project_ip_access_list/client.py">get_access_list_status</a>(...) -> NetworkPermissionEntryStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of one project IP access list entry. This resource checks if the provided project IP access list entry applies to all cloud providers serving clusters from the specified project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.project_ip_access_list.get_access_list_status(
    group_id="32b6e34b3d91647abb20e7b8",
    entry_value="IPv4: 192.0.2.0%2F24 or IPv6: 2001:db8:85a3:8d3:1319:8a2e:370:7348 or IPv4 CIDR: 198.51.100.0%2f24 or IPv6 CIDR: 2001:db8::%2f58 or AWS SG: sg-903004f8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**entry_value:** `str` — Network address or cloud provider security construct that identifies which project access list entry to be verified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Activity Feed
<details><summary><code>client.activity_feed.<a href="src/atlas_sdk/activity_feed/client.py">get_group_activity_feed</a>(...) -> ActivityFeedLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a pre-filtered activity feed link for the specified project based on the provided date range and event types. The returned link can be shared and opened to view the activity feed with the same filters applied. To use this resource, the requesting Service Account or API Key must have the Project Read Only role or higher.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.activity_feed.get_group_activity_feed(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[typing.Union[EventTypeForNdsGroup, typing.Sequence[EventTypeForNdsGroup]]]` 

Category of incident recorded at this moment in time.

**IMPORTANT**: The complete list of event type values changes frequently.
    
</dd>
</dl>

<dl>
<dd>

**max_date:** `typing.Optional[datetime.datetime]` — End date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**min_date:** `typing.Optional[datetime.datetime]` — Start date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activity_feed.<a href="src/atlas_sdk/activity_feed/client.py">get_org_activity_feed</a>(...) -> ActivityFeedLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a pre-filtered activity feed link for the specified organization based on the provided date range and event types. The returned link can be shared and opened to view the activity feed with the same filters applied. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.activity_feed.get_org_activity_feed(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[typing.Union[EventTypeForOrg, typing.Sequence[EventTypeForOrg]]]` 

Category of incident recorded at this moment in time.

**IMPORTANT**: The complete list of event type values changes frequently.
    
</dd>
</dl>

<dl>
<dd>

**max_date:** `typing.Optional[datetime.datetime]` — End date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**min_date:** `typing.Optional[datetime.datetime]` — Start date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Alerts
<details><summary><code>client.alerts.<a href="src/atlas_sdk/alerts/client.py">get_alert_config_alerts</a>(...) -> PaginatedAlert</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all open alerts that the specified alert configuration triggers. These alert configurations apply to the specified project only. Alert configurations define the triggers and notification methods for alerts. Open alerts have been triggered but remain unacknowledged. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Use the Return All Alert Configurations for One Project endpoint to retrieve all alert configurations to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alerts.get_alert_config_alerts(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_config_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_config_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alerts.<a href="src/atlas_sdk/alerts/client.py">list_alerts</a>(...) -> PaginatedAlert</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all alerts. These alerts apply to all components in one project. You receive an alert when a monitored component meets or exceeds a value you set. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alerts.list_alerts(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Status of the alerts to return. Omit this parameter to return all alerts in all statuses. TRACKING indicates the alert condition exists but has not persisted for the minimum notification delay. OPEN indicates the alert condition currently exists. CLOSED indicates the alert condition has been resolved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alerts.<a href="src/atlas_sdk/alerts/client.py">get_alert</a>(...) -> AlertViewForNdsGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one alert. This alert applies to any component in one project. You receive an alert when a monitored component meets or exceeds a value you set. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Use the Return All Alerts from One Project endpoint to retrieve all alerts to which the authenticated user has access.

This resource remains under revision and may change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alerts.get_alert(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_id="alertId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alerts.<a href="src/atlas_sdk/alerts/client.py">acknowledge_alert</a>(...) -> AlertViewForNdsGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirms receipt of one existing alert. This alert applies to any component in one project. Acknowledging an alert prevents successive notifications. You receive an alert when a monitored component meets or exceeds a value you set until you acknowledge the alert. To use this resource, the requesting Service Account or API Key must have the Project Alerts Manager, Project Monitoring Admin, Organization Owner, or Project Owner role. Use the Return All Alerts from One Project endpoint to retrieve all alerts to which the authenticated user has access.

This resource remains under revision and may change. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.alerts.acknowledge_alert(
    group_id="32b6e34b3d91647abb20e7b8",
    alert_id="alertId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**alert_id:** `str` — Unique 24-hexadecimal digit string that identifies the alert.
    
</dd>
</dl>

<dl>
<dd>

**acknowledged_until:** `typing.Optional[datetime.datetime]` — Date and time until which this alert has been acknowledged. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter if a MongoDB User previously acknowledged this alert.
    
</dd>
</dl>

<dl>
<dd>

**acknowledgement_comment:** `typing.Optional[str]` — Comment that a MongoDB Cloud user submitted when acknowledging the alert.
    
</dd>
</dl>

<dl>
<dd>

**unacknowledge_alert:** `typing.Optional[bool]` — Flag that indicates to unacknowledge a previously acknowledged alert. By default this value is set to false. If set to true, it will override the `acknowledgedUntil` parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Programmatic API Keys
<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">list_group_api_keys</a>(...) -> PaginatedApiApiUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all organization API keys that you assigned to the specified project. Users with the Project Owner role in the project associated with the API key can use the organization API key to access the resources. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.list_group_api_keys(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">create_group_api_key</a>(...) -> ApiKeyUserDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates and assigns the specified organization API key to the specified project. Users with the Project Owner role in the project associated with the API key can use the organization API key to access the resources. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.create_group_api_key(
    group_id="32b6e34b3d91647abb20e7b8",
    desc="desc",
    roles=[
        "roles"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**desc:** `str` — Purpose or explanation provided when someone created this project API key.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">add_group_api_key</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns the specified organization API key to the specified project. Users with the Project Owner role in the project associated with the API key can then use the organization API key to access the resources. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, UserAccessRoleAssignment
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.add_group_api_key(
    group_id="32b6e34b3d91647abb20e7b8",
    api_user_id="apiUserId",
    request=[
        UserAccessRoleAssignment()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key that you want to assign to one project.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[UserAccessRoleAssignment]` — Explanatory text that describes this API key, the list of roles to grant this API key, or both.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">remove_group_api_key</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one organization API key from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.remove_group_api_key(
    group_id="32b6e34b3d91647abb20e7b8",
    api_user_id="apiUserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key that you want to unassign from one project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">update_api_key_roles</a>(...) -> ApiKeyUserDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the roles of the organization API key that you specify for the project that you specify. You must specify at least one valid role for the project. The application removes any roles that you do not include in this request if they were previously set in the organization API key that you specify for the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.update_api_key_roles(
    group_id="32b6e34b3d91647abb20e7b8",
    api_user_id="apiUserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key that you want to unassign from one project.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` — Purpose or explanation provided when someone creates this project API key.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">list_org_api_keys</a>(...) -> PaginatedApiApiUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all organization API keys for the specified organization. The organization API keys grant programmatic access to an organization. You can't use the API key to log into MongoDB Cloud through the console. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.list_org_api_keys(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">create_org_api_key</a>(...) -> ApiKeyUserDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one API key for the specified organization. An organization API key grants programmatic access to an organization. You can't use the API key to log into the console. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.create_org_api_key(
    org_id="4888442a3354817a7320eb61",
    desc="desc",
    roles=[
        "roles"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateAtlasOrganizationApiKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">get_org_api_key</a>(...) -> ApiKeyUserDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one organization API key. The organization API keys grant programmatic access to an organization. You can't use the API key to log into MongoDB Cloud through the user interface. To use this resource, the requesting Service Account or API Key must have the  Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.get_org_api_key(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key that  you want to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">delete_org_api_key</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one organization API key from the specified organization. When you remove an API key from an organization, MongoDB Cloud also removes that key from any projects that use that key. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.delete_org_api_key(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">update_org_api_key</a>(...) -> ApiKeyUserDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one organization API key in the specified organization. The organization API keys  grant programmatic access to an organization. To use this resource, the requesting  API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.update_org_api_key(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key you  want to update.
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` — Purpose or explanation provided when someone creates this organization API key.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">list_org_access_entries</a>(...) -> PaginatedApiUserAccessListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all access list entries that you configured for the specified organization API key. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.list_org_access_entries(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key for which you want to return access list entries.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">create_org_access_entry</a>(...) -> PaginatedApiUserAccessListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates the access list entries for the specified organization API key. Resources require all API requests originate from IP addresses on the API access list. To use this resource, the requesting Service Account or API Key must have the Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, UserAccessListRequest
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.create_org_access_entry(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
    request=[
        UserAccessListRequest()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key for which you want to create a new access list entry.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[UserAccessListRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">get_org_access_entry</a>(...) -> UserAccessListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one access list entry for the specified organization API key. Resources require  all API requests originate from IP addresses on the API access list. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.get_org_access_entry(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
    ip_address="192.0.2.0%2F24",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key for  which you want to return access list entries.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `str` — One IP address or multiple IP addresses represented as one CIDR block to limit  requests to API resources in the specified organization. When adding a CIDR block with a subnet mask, such as  192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programmatic_api_keys.<a href="src/atlas_sdk/programmatic_api_keys/client.py">delete_access_entry</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified access list entry from the specified organization API key. Resources require all API requests originate from the IP addresses on the API access list. To use this resource, the requesting Service Account or API Key must have the Read Write role. In addition, you cannot remove the requesting IP address from the requesting organization API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.programmatic_api_keys.delete_access_entry(
    org_id="4888442a3354817a7320eb61",
    api_user_id="apiUserId",
    ip_address="192.0.2.0%2F24",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**api_user_id:** `str` — Unique 24-hexadecimal digit string that identifies this organization API key for which you want to remove access list entries.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `str` — One IP address or multiple IP addresses represented as one CIDR block to limit requests to API resources in the specified organization. When adding a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auditing
<details><summary><code>client.auditing.<a href="src/atlas_sdk/auditing/client.py">get_group_audit_log</a>(...) -> AuditLog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the auditing configuration for the specified project. The auditing configuration defines the events that MongoDB Cloud records in the audit log. To use this resource, the requesting Service Account or API Key must have the Project Owner role. This feature isn't available for `M0`, `M2`, `M5`, or serverless clusters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.auditing.get_group_audit_log(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auditing.<a href="src/atlas_sdk/auditing/client.py">update_audit_log</a>(...) -> AuditLog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the auditing configuration for the specified project. The auditing configuration defines the events that MongoDB Cloud records in the audit log. To use this resource, the requesting Service Account or API Key must have the Project Owner role. This feature isn't available for `M0`, `M2`, `M5`, or serverless clusters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.auditing.update_audit_log(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AuditLog` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AWS Clusters DNS
<details><summary><code>client.aws_clusters_dns.<a href="src/atlas_sdk/aws_clusters_dns/client.py">get_aws_custom_dns</a>(...) -> AwsCustomDnsEnabled</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the custom DNS configuration for AWS clusters in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.aws_clusters_dns.get_aws_custom_dns(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aws_clusters_dns.<a href="src/atlas_sdk/aws_clusters_dns/client.py">toggle_aws_custom_dns</a>(...) -> AwsCustomDnsEnabled</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables or disables the custom DNS configuration for AWS clusters in the specified project. Enable custom DNS if you use AWS VPC peering and use your own DNS servers. To use this resource, the requesting Service Account or API Key must have the Project Atlas Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.aws_clusters_dns.toggle_aws_custom_dns(
    group_id="32b6e34b3d91647abb20e7b8",
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AwsCustomDnsEnabled` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cloud Backups
<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_backup_private_endpoints</a>(...) -> PaginatedApiAtlasObjectStoragePrivateEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the private endpoints of the specified cloud provider for object storage backup operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_backup_private_endpoints(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider for the private endpoints to return.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">create_backup_private_endpoint</a>(...) -> ObjectStoragePrivateEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a private endpoint in the specified region for secure, private connectivity between Atlas and cloud provider object storage services for backup operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.create_backup_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider for the private endpoint to create.
    
</dd>
</dl>

<dl>
<dd>

**object_storage_private_endpoint_request_cloud_provider:** `typing.Optional[str]` — Human-readable label that identifies the cloud provider.
    
</dd>
</dl>

<dl>
<dd>

**region_name:** `typing.Optional[str]` — Cloud provider region in which the Object Storage private endpoint is located.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_backup_private_endpoint</a>(...) -> ObjectStoragePrivateEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one private endpoint, identified by its ID, for object storage backup operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_backup_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider of the private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">delete_backup_private_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one private endpoint, identified by its ID, for object storage backup operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.delete_backup_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider of the private endpoint to delete.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_export_buckets</a>(...) -> PaginatedBackupSnapshotExportBuckets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Export Buckets associated with the specified Project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_export_buckets(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">create_export_bucket</a>(...) -> DiskBackupSnapshotExportBucketResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Snapshot Export Bucket for an AWS S3 Bucket, Azure Blob Storage Container, or Google Cloud Storage Bucket. Once created, an snapshots can be exported to the Export Bucket and its referenced AWS S3 Bucket, Azure Blob Storage Container, or Google Cloud Storage Bucket. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.create_export_bucket(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="AWS",
    bucket_name="export-bucket",
    iam_role_id="668c5f0ed436263134491592",
    require_private_networking=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider.
    
</dd>
</dl>

<dl>
<dd>

**bucket_name:** `typing.Optional[str]` — Human-readable label that identifies the Google Cloud Storage Bucket that the role is authorized to export to.
    
</dd>
</dl>

<dl>
<dd>

**iam_role_id:** `typing.Optional[str]` — Unique 24-hexadecimal character string that identifies the Unified AWS Access role ID that MongoDB Cloud uses to access the AWS S3 bucket.
    
</dd>
</dl>

<dl>
<dd>

**require_private_networking:** `typing.Optional[bool]` — Indicates whether to do exports over PrivateLink as opposed to public IPs. Defaults to False.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the GCP Cloud Provider Access Role that MongoDB Cloud uses to access the Google Cloud Storage Bucket.
    
</dd>
</dl>

<dl>
<dd>

**service_url:** `typing.Optional[str]` — URL of the Azure Storage Account to export to. For example: `https://examplestorageaccount.blob.core.windows.net/exportcontainer`. Only standard endpoints (with `blob.core.windows.net`) are supported.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — UUID that identifies the Azure Active Directory Tenant ID. Deprecated: this field is ignored; the `tenantId` of the Cloud Provider Access role (from `roleId`) is used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_export_bucket</a>(...) -> DiskBackupSnapshotExportBucketResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Export Bucket associated with the specified Project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_export_bucket(
    group_id="32b6e34b3d91647abb20e7b8",
    export_bucket_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**export_bucket_id:** `str` — Unique 24-hexadecimal character string that identifies the Export Bucket.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">delete_export_bucket</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an Export Bucket. Auto export must be disabled on all clusters in this Project exporting to this Export Bucket before revoking access. To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.delete_export_bucket(
    group_id="32b6e34b3d91647abb20e7b8",
    export_bucket_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**export_bucket_id:** `str` — Unique 24-hexadecimal character string that identifies the Export Bucket.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">update_backup_export_bucket</a>(...) -> DiskBackupSnapshotAwsExportBucketResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the private networking settings for one snapshot export bucket in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.update_backup_export_bucket(
    group_id="32b6e34b3d91647abb20e7b8",
    export_bucket_id="32b6e34b3d91647abb20e7b8",
    require_private_networking=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**export_bucket_id:** `str` — Unique 24-hexadecimal character string that identifies the snapshot export bucket.
    
</dd>
</dl>

<dl>
<dd>

**require_private_networking:** `bool` — True to require private networking; false to disable it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_compliance_policy</a>(...) -> DataProtectionSettings20231001</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Backup Compliance Policy settings with the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_compliance_policy(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">update_compliance_policy</a>(...) -> DataProtectionSettings20231001</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the Backup Compliance Policy settings for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.update_compliance_policy(
    group_id="32b6e34b3d91647abb20e7b8",
    authorized_email="authorizedEmail",
    authorized_user_first_name="authorizedUserFirstName",
    authorized_user_last_name="authorizedUserLastName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataProtectionSettings20231001` 
    
</dd>
</dl>

<dl>
<dd>

**overwrite_backup_policies:** `typing.Optional[bool]` — Flag that indicates whether to overwrite non complying backup policies with the new data protection settings or not.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">disable_compliance_policy</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the Backup Compliance Policy settings with the specified project. As a prerequisite, a support ticket needs to be file first, instructions in https://www.mongodb.com/docs/atlas/backup/cloud-backup/backup-compliance-policy/. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.disable_compliance_policy(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_backup_exports</a>(...) -> PaginatedApiAtlasDiskBackupExportJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Cloud Backup Snapshot Export Jobs associated with the specified Atlas cluster. To use this resource, the requesting Service Account or API Key must have the Project Atlas Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_backup_exports(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">create_backup_export</a>(...) -> DiskBackupExportJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports one backup Snapshot for dedicated Atlas cluster using Cloud Backups to an Export Bucket. To use this resource, the requesting Service Account or API Key must have the Project Backup Export Operator role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.create_backup_export(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    export_bucket_id="32b6e34b3d91647abb20e7b8",
    snapshot_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**export_bucket_id:** `str` — Unique 24-hexadecimal character string that identifies the Export Bucket.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal character string that identifies the Cloud Backup Snapshot to export.
    
</dd>
</dl>

<dl>
<dd>

**custom_data:** `typing.Optional[typing.List[BackupLabel]]` — Collection of key-value pairs that represent custom data to add to the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_backup_export</a>(...) -> DiskBackupExportJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Cloud Backup Snapshot Export Job associated with the specified Atlas cluster. To use this resource, the requesting Service Account or API Key must have the Project Atlas Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_backup_export(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    export_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**export_id:** `str` — Unique 24-hexadecimal character string that identifies the Export Job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_backup_restore_jobs</a>(...) -> PaginatedCloudBackupRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all cloud backup restore jobs for one cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_backup_restore_jobs(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the restore jobs you want to return.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">create_backup_restore_job</a>(...) -> DiskBackupSnapshotRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores one snapshot of one cluster from the specified project. Atlas takes on-demand snapshots immediately and scheduled snapshots at regular intervals. If an on-demand snapshot with a status of `queued` or `inProgress` exists, before taking another snapshot, wait until Atlas completes processing the previously taken on-demand snapshot.

 To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role, Project Backup Export Operator role, or Project Backup Recovery Operator role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.create_backup_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    delivery_type="deliveryType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DiskBackupSnapshotRestoreJob` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_backup_restore_job</a>(...) -> DiskBackupSnapshotRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one cloud backup restore job for one cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_backup_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    restore_job_id="restoreJobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the restore jobs you want to return.
    
</dd>
</dl>

<dl>
<dd>

**restore_job_id:** `str` — Unique 24-hexadecimal digit string that identifies the restore job to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">cancel_backup_restore_job</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels one cloud backup restore job of one cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role, Project Backup Export Operator role, or Project Backup Recovery Operator role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.cancel_backup_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    restore_job_id="restoreJobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**restore_job_id:** `str` — Unique 24-hexadecimal digit string that identifies the restore job to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_backup_schedule</a>(...) -> DiskBackupSnapshotSchedule20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the cloud backup schedule for the specified cluster within the specified project. This schedule defines when MongoDB Cloud takes scheduled snapshots and how long it stores those snapshots. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_backup_schedule(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">delete_cluster_backup_schedule</a>(...) -> DiskBackupSnapshotSchedule20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes all cloud backup schedules for the specified cluster. This schedule defines when MongoDB Cloud takes scheduled snapshots and how long it stores those snapshots. To use this resource, the requesting Service Account or API Key must have the Project Atlas Admin role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.delete_cluster_backup_schedule(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">update_backup_schedule</a>(...) -> DiskBackupSnapshotSchedule20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the cloud backup schedule for one cluster within the specified project. This schedule defines when MongoDB Cloud takes scheduled snapshots and how long it stores those snapshots. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, AdvancedDiskBackupSnapshotSchedulePolicy, DiskBackupApiPolicyItem
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.update_backup_schedule(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name_="clusterName",
    policies=[
        AdvancedDiskBackupSnapshotSchedulePolicy(
            policy_items=[
                DiskBackupApiPolicyItem(
                    frequency_interval=1,
                    frequency_type="frequencyType",
                    retention_unit="retentionUnit",
                    retention_value=1,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DiskBackupSnapshotSchedule20240805` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_backup_snapshots</a>(...) -> PaginatedCloudBackupReplicaSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all snapshots of one cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role or Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_backup_snapshots(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**point_in_time_utc_seconds:** `typing.Optional[int]` — Desired point in time, expressed as the number of seconds that have elapsed since the UNIX epoch. If specified, returns the closest snapshot created before that point in time. Mutually exclusive with `oplogTs` and `oplogInc`.
    
</dd>
</dl>

<dl>
<dd>

**oplog_ts:** `typing.Optional[int]` — Oplog timestamp that represents the desired point in time. This is the first part of an Oplog timestamp. Must be used with `oplogInc`. Mutually exclusive with `pointInTimeUtcSeconds`.
    
</dd>
</dl>

<dl>
<dd>

**oplog_inc:** `typing.Optional[int]` — Oplog operation number that represents the desired point in time. This is the second part of an Oplog timestamp. Must be used with `oplogTs`. Mutually exclusive with `pointInTimeUtcSeconds`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">take_snapshots</a>(...) -> DiskBackupSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Takes one on-demand snapshot for the specified cluster. Atlas takes on-demand snapshots immediately and scheduled snapshots at regular intervals. If an on-demand snapshot with a status of `queued` or `inProgress` exists, before taking another snapshot, wait until Atlas completes processing the previously taken on-demand snapshot.

 To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role or Project Backup Creator role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.take_snapshots(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when `"status" : "onDemand"`.
    
</dd>
</dl>

<dl>
<dd>

**retention_in_days:** `typing.Optional[int]` — Number of days that MongoDB Cloud should retain the on-demand snapshot. Must be at least **1**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_cluster_backup_snapshot</a>(...) -> DiskBackupReplicaSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one snapshot from the specified cluster. To use this resource, the requesting Service Account or API Key must have the Project Read Only role or Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_cluster_backup_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">delete_cluster_backup_snapshot</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified snapshot. To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.delete_cluster_backup_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">update_backup_snapshot</a>(...) -> DiskBackupReplicaSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes the expiration date for one cloud backup snapshot for one cluster in the specified project, the requesting Service Account or API Key must have the Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.update_backup_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
    retention_unit="retentionUnit",
    retention_value=5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**retention_unit:** `str` — Quantity of time in which MongoDB Cloud measures snapshot retention.
    
</dd>
</dl>

<dl>
<dd>

**retention_value:** `int` — Number that indicates the amount of days, weeks, months, or years that MongoDB Cloud retains the snapshot. For less frequent policy items, MongoDB Cloud requires that you specify a value greater than or equal to the value specified for more frequent policy items. If the hourly policy item specifies a retention of two days, specify two days or greater for the retention of the weekly policy item.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_backup_sharded_cluster</a>(...) -> DiskBackupShardedClusterSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one snapshot of one sharded cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role or Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_backup_sharded_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">delete_backup_sharded_cluster</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one snapshot of one sharded cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.delete_backup_sharded_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_backup_sharded_clusters</a>(...) -> PaginatedCloudBackupShardedClusterSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all snapshots of one sharded cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role or Project Backup Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_backup_sharded_clusters(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_serverless_restore_jobs</a>(...) -> PaginatedApiAtlasServerlessBackupRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all restore jobs for one serverless instance from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

This API can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or Flex clusters that were migrated from Serverless instances. This endpoint will be sunset on January 22, 2026. Please use the List Flex Backup Restore Jobs endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_serverless_restore_jobs(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the serverless instance.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">create_serverless_restore_job</a>(...) -> ServerlessBackupRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores one snapshot of one serverless instance from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

This API can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or Flex clusters that were migrated from Serverless instances. This endpoint will be sunset on January 22, 2026. Please use the Create Flex Backup Restore Job endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.create_serverless_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    delivery_type="deliveryType",
    target_cluster_name="targetClusterName",
    target_group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the serverless instance whose snapshot you want to restore.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ServerlessBackupRestoreJob` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_serverless_restore_job</a>(...) -> ServerlessBackupRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one restore job for one serverless instance from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

This API can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or Flex clusters that were migrated from Serverless instances. This endpoint will be sunset on January 22, 2026. Please use the Get Flex Backup Restore Job endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_serverless_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    restore_job_id="restoreJobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the serverless instance.
    
</dd>
</dl>

<dl>
<dd>

**restore_job_id:** `str` — Unique 24-hexadecimal digit string that identifies the restore job to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">list_serverless_backup_snapshots</a>(...) -> PaginatedApiAtlasServerlessBackupSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all snapshots of one serverless instance from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This API can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or Flex clusters that were migrated from Serverless instances. This endpoint will be sunset on January 22, 2026. Please use the List Flex Backups endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.list_serverless_backup_snapshots(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the serverless instance.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_backups.<a href="src/atlas_sdk/cloud_backups/client.py">get_serverless_backup_snapshot</a>(...) -> ServerlessBackupSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one snapshot of one serverless instance from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This endpoint can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) API or Flex clusters that were migrated from Serverless instances. This endpoint will be sunset on January 22, 2026. Please use the Get Flex Backup endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_backups.get_serverless_backup_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the serverless instance.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cloud Provider Access
<details><summary><code>client.cloud_provider_access.<a href="src/atlas_sdk/cloud_provider_access/client.py">list_cloud_provider_access</a>(...) -> CloudProviderAccessRoles</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all cloud provider access roles with access to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_provider_access.list_cloud_provider_access(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_provider_access.<a href="src/atlas_sdk/cloud_provider_access/client.py">create_cloud_provider_access</a>(...) -> CloudProviderAccessRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one access role for the specified cloud provider. Some MongoDB Cloud features use these cloud provider access roles for authentication. To use this resource, the requesting Service Account or API Key must have the Project Owner role. For the GCP provider, if the project folder is not yet provisioned, Atlas will now create the role asynchronously. An intermediate role with status `IN_PROGRESS` will be returned, and the final service account will be provisioned. Once the GCP project is set up, subsequent requests will create the service account synchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_provider_access.create_cloud_provider_access(
    group_id="32b6e34b3d91647abb20e7b8",
    provider_name="providerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `str` — Human-readable label that identifies the cloud provider of the role.
    
</dd>
</dl>

<dl>
<dd>

**atlas_azure_app_id:** `typing.Optional[str]` — Azure Active Directory Application ID of Atlas. This field is optional and will be derived from the Azure subscription if not provided.
    
</dd>
</dl>

<dl>
<dd>

**service_principal_id:** `typing.Optional[str]` — UUID string that identifies the Azure Service Principal.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — UUID String that identifies the Azure Active Directory Tenant ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_provider_access.<a href="src/atlas_sdk/cloud_provider_access/client.py">deauthorize_provider_access_role</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes access to the specified project for the specified access role. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_provider_access.deauthorize_provider_access_role(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    role_id="roleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider of the role to deauthorize.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — Unique 24-hexadecimal digit string that identifies the role.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_provider_access.<a href="src/atlas_sdk/cloud_provider_access/client.py">get_cloud_provider_access</a>(...) -> CloudProviderAccessRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the access role with the specified id and with access to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_provider_access.get_cloud_provider_access(
    group_id="32b6e34b3d91647abb20e7b8",
    role_id="roleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — Unique 24-hexadecimal digit string that identifies the role.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_provider_access.<a href="src/atlas_sdk/cloud_provider_access/client.py">authorize_provider_access_role</a>(...) -> CloudProviderAccessRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Grants access to the specified project for the specified access role. To use this resource, the requesting Service Account or API Key must have the Project Owner role. This API endpoint is one step in a procedure to create unified access for MongoDB Cloud services. This is not required for GCP service account access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_provider_access.authorize_provider_access_role(
    group_id="32b6e34b3d91647abb20e7b8",
    role_id="roleId",
    provider_name="providerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `str` — Unique 24-hexadecimal digit string that identifies the role.
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `str` — Human-readable label that identifies the cloud provider of the role.
    
</dd>
</dl>

<dl>
<dd>

**iam_assumed_role_arn:** `typing.Optional[str]` — Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.
    
</dd>
</dl>

<dl>
<dd>

**atlas_azure_app_id:** `typing.Optional[str]` — Azure Active Directory Application ID of Atlas. This field is optional and will be derived from the Azure subscription if not provided.
    
</dd>
</dl>

<dl>
<dd>

**service_principal_id:** `typing.Optional[str]` — UUID string that identifies the Azure Service Principal.
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` — UUID String that identifies the Azure Active Directory Tenant ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collection Level Metrics
<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">list_coll_stat_measurements</a>(...) -> MeasurementsCollStatsLatencyCluster</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of the Coll Stats Latency cluster-level measurements for the given namespace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.list_coll_stat_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    cluster_view="clusterView",
    database_name="mydb",
    collection_name="mycoll",
    period="PT10H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to retrieve metrics for.
    
</dd>
</dl>

<dl>
<dd>

**cluster_view:** `str` — Human-readable label that identifies the cluster topology to retrieve metrics for.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Human-readable label that identifies the collection.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List that contains the metrics that you want to retrieve for the associated data series. If you don't set this parameter, this resource returns data series for all Coll Stats Latency metrics.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">get_cluster_namespaces</a>(...) -> CollStatsRankedNamespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the subset of namespaces from the given cluster sorted by highest total execution time (descending) within the given time window.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.get_cluster_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    cluster_view="clusterView",
    period="PT10H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to pin namespaces to.
    
</dd>
</dl>

<dl>
<dd>

**cluster_view:** `str` — Human-readable label that identifies the cluster topology to retrieve metrics for.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">list_pinned_namespaces</a>(...) -> PinnedNamespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of given cluster's pinned namespaces, a set of namespaces manually selected by users to collect query latency metrics on.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.list_pinned_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to retrieve pinned namespaces for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">pin_namespaces</a>(...) -> PinnedNamespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pin provided list of namespaces for collection-level latency metrics collection for the given Group and Cluster. This initializes a pinned namespaces list or replaces any existing pinned namespaces list for the Group and Cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.pin_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to pin namespaces to.
    
</dd>
</dl>

<dl>
<dd>

**request:** `NamespacesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">update_pinned_namespaces</a>(...) -> PinnedNamespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add provided list of namespaces to existing pinned namespaces list for collection-level latency metrics collection for the given Group and Cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.update_pinned_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to pin namespaces to.
    
</dd>
</dl>

<dl>
<dd>

**request:** `NamespacesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">unpin_namespaces</a>(...) -> PinnedNamespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpin provided list of namespaces for collection-level latency metrics collection for the given Group and Cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.unpin_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to unpin namespaces from.
    
</dd>
</dl>

<dl>
<dd>

**request:** `NamespacesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">list_coll_stat_metrics</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all available Coll Stats Latency metric names and their respective units for the specified project at the time of request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.list_coll_stat_metrics(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">list_process_measurements</a>(...) -> MeasurementsCollStatsLatencyHost</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of the Coll Stats Latency process-level measurements for the given namespace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.list_process_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="my.host.name.com:27017",
    database_name="mydb",
    collection_name="mycoll",
    period="PT10H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Human-readable label that identifies the collection.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List that contains the metrics that you want to retrieve for the associated data series. If you don't set this parameter, this resource returns data series for all Coll Stats Latency metrics.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_level_metrics.<a href="src/atlas_sdk/collection_level_metrics/client.py">get_process_namespaces</a>(...) -> CollStatsRankedNamespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the subset of namespaces from the given process ranked by highest total execution time (descending) within the given time window.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.collection_level_metrics.get_process_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="my.host.name.com:27017",
    period="PT10H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Legacy Backup
<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">list_cluster_backup_checkpoints</a>(...) -> PaginatedApiAtlasCheckpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all legacy backup checkpoints for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.list_cluster_backup_checkpoints(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the checkpoints that you want to return.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">get_cluster_backup_checkpoint</a>(...) -> ApiAtlasCheckpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one legacy backup checkpoint for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.get_cluster_backup_checkpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    checkpoint_id="checkpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the checkpoints that you want to return.
    
</dd>
</dl>

<dl>
<dd>

**checkpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the checkpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">list_cluster_restore_jobs</a>(...) -> PaginatedRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all legacy backup restore jobs for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

 Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation. If you use the `BATCH-ID` query parameter, you can retrieve all restore jobs in the specified batch. When creating a restore job for a sharded cluster, MongoDB Cloud creates a separate job for each shard, plus another for the config server. Each of those jobs are part of a batch. However, a batch can't include a restore job for a replica set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.list_cluster_restore_jobs(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the snapshot you want to return.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the batch of restore jobs to return. Timestamp in ISO 8601 date and time format in UTC when creating a restore job for a sharded cluster, Application creates a separate job for each shard, plus another for the config host. Each of these jobs comprise one batch. A restore job for a replica set can't be part of a batch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">create_cluster_restore_job</a>(...) -> PaginatedRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores one legacy backup for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation. This endpoint doesn't support creating checkpoint restore jobs for sharded clusters, or creating restore jobs for queryable backup snapshots. If you create an automated restore job by specifying `delivery.methodName` of `AUTOMATED_RESTORE` in your request body, MongoDB Cloud removes all existing data on the target cluster prior to the restore.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, BackupRestoreJobDelivery
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.create_cluster_restore_job(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_name_="clusterName",
    delivery=BackupRestoreJobDelivery(
        method_name="methodName",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the snapshot you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BackupRestoreJob` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">get_cluster_restore_job</a>(...) -> BackupRestoreJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one legacy backup restore job for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

 Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.get_cluster_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the snapshot you want to return.
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — Unique 24-hexadecimal digit string that identifies the restore job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">get_cluster_snapshot_schedule</a>(...) -> ApiAtlasSnapshotSchedule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the snapshot schedule for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

 Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.get_cluster_snapshot_schedule(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the snapshot you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">update_cluster_snapshot_schedule</a>(...) -> ApiAtlasSnapshotSchedule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the snapshot schedule for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

 Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.update_cluster_snapshot_schedule(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    cluster_checkpoint_interval_min=1,
    cluster_id="32b6e34b3d91647abb20e7b8",
    daily_snapshot_retention_days=1,
    monthly_snapshot_retention_months=1,
    point_in_time_window_hours=1,
    snapshot_interval_hours=1,
    snapshot_retention_days=1,
    weekly_snapshot_retention_weeks=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster with the snapshot you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiAtlasSnapshotSchedule` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">list_cluster_snapshots</a>(...) -> PaginatedSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all legacy backup snapshots for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.list_cluster_snapshots(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[str]` — Human-readable label that specifies whether to return only completed, incomplete, or all snapshots. By default, MongoDB Cloud only returns completed snapshots.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">get_cluster_snapshot</a>(...) -> BackupSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one legacy backup snapshot for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.get_cluster_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">delete_cluster_snapshot</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one legacy backup snapshot for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.delete_cluster_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_backup.<a href="src/atlas_sdk/legacy_backup/client.py">update_cluster_snapshot</a>(...) -> BackupSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes the expiration date for one legacy backup snapshot for one cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.legacy_backup.update_cluster_snapshot(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_name_="clusterName",
    snapshot_id="snapshotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BackupSnapshot` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Atlas Search
<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">create_cluster_fts_index</a>(...) -> ClusterSearchIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one Atlas Search index on the specified collection. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. Only clusters running MongoDB v4.2 or later can use Atlas Search. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.create_cluster_fts_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    collection_name="collectionName",
    database="database",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection on which to create an Atlas Search index.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ClusterSearchIndex` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">list_cluster_fts_index</a>(...) -> typing.List[ClusterSearchIndex]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Atlas Search indexes on the specified collection. Atlas Search indexes contain the indexed fields and the analyzers used to create the indexes. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.list_cluster_fts_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    database_name="databaseName",
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Name of the collection that contains one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">get_cluster_fts_index</a>(...) -> ClusterSearchIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Atlas Search index in the specified project. You identify this index using its unique ID. Atlas Search index contains the indexed fields and the analyzers used to create the index. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.get_cluster_fts_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    index_id="indexId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `str` — Unique 24-hexadecimal digit string that identifies the Application Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Application Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Application Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">delete_cluster_fts_index</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one Atlas Search index that you identified with its unique ID. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.delete_cluster_fts_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    index_id="indexId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the database and collection with one or more Application Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `str` — Unique 24-hexadecimal digit string that identifies the Atlas Search index. Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">update_cluster_fts_index</a>(...) -> ClusterSearchIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one Atlas Search index that you identified with its unique ID. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.update_cluster_fts_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    index_id_="indexId",
    collection_name="collectionName",
    database="database",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection whose Atlas Search index to update.
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `str` — Unique 24-hexadecimal digit string that identifies the Atlas Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ClusterSearchIndex` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">get_cluster_search_deployment</a>(...) -> ApiSearchDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Search Nodes for the specified cluster. Deprecated versions: v2-{2024-05-30}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.get_cluster_search_deployment(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Label that identifies the cluster to return the Search Nodes for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">create_cluster_search_deployment</a>(...) -> ApiSearchDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates Search Nodes for the specified cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ApiSearchDeploymentSpec
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.create_cluster_search_deployment(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    specs=[
        ApiSearchDeploymentSpec(
            instance_size="instanceSize",
            node_count=2,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Label that identifies the cluster to create Search Nodes for.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiSearchDeploymentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">delete_cluster_search_deployment</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the Search Nodes for the specified cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.delete_cluster_search_deployment(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Label that identifies the cluster to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">update_cluster_search_deployment</a>(...) -> ApiSearchDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the Search Nodes for the specified cluster. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ApiSearchDeploymentSpec
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.update_cluster_search_deployment(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    specs=[
        ApiSearchDeploymentSpec(
            instance_size="instanceSize",
            node_count=2,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Label that identifies the cluster to update the Search Nodes for.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiSearchDeploymentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">list_cluster_search_indexes</a>(...) -> typing.List[SearchIndexResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Atlas Search indexes on the specified cluster. Atlas Search indexes contain the indexed fields and the analyzers used to create the indexes. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.list_cluster_search_indexes(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">create_cluster_search_index</a>(...) -> SearchIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one Atlas Search index on the specified collection. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. Only clusters running MongoDB v4.2 or later can use Atlas Search. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.create_cluster_search_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    collection_name="collectionName",
    database="database",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection on which to create an Atlas Search index.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Label that identifies the collection to create an Atlas Search index in.
    
</dd>
</dl>

<dl>
<dd>

**database:** `str` — Label that identifies the database that contains the collection to create an Atlas Search index in.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Label that identifies this index. Within each namespace, names of all indexes in the namespace must be unique.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Type of the index. The default type is search.
    
</dd>
</dl>

<dl>
<dd>

**definition:** `typing.Optional[BaseSearchIndexCreateRequestDefinition]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">list_search_index</a>(...) -> typing.List[SearchIndexResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Atlas Search indexes on the specified collection. Atlas Search indexes contain the indexed fields and the analyzers used to create the indexes. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.list_search_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    database_name="databaseName",
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Label that identifies the database that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Name of the collection that contains one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">get_index_by_name</a>(...) -> SearchIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Atlas Search index in the specified project. You identify this index using its database, collection and name. Atlas Search index contains the indexed fields and the analyzers used to create the index. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.get_index_by_name(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    database_name="databaseName",
    collection_name="collectionName",
    index_name="indexName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Label that identifies the database that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Name of the collection that contains one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — Name of the Atlas Search index to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">delete_index_by_name</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one Atlas Search index that you identified with its database, collection, and name. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role. This deletion is eventually consistent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.delete_index_by_name(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    database_name="databaseName",
    collection_name="collectionName",
    index_name="indexName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the database and collection with one or more Application Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Label that identifies the database that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Name of the collection that contains one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — Name of the Atlas Search index to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">update_index_by_name</a>(...) -> SearchIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one Atlas Search index that you identified with its database, collection name, and index name. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, SearchIndexUpdateRequestDefinition
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.update_index_by_name(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    database_name="databaseName",
    collection_name="collectionName",
    index_name="indexName",
    definition=SearchIndexUpdateRequestDefinition(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection whose Atlas Search index you want to update.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Label that identifies the database that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Name of the collection that contains one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — Name of the Atlas Search index to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchIndexUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">get_cluster_search_index</a>(...) -> SearchIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Atlas Search index in the specified project. You identify this index using its unique ID. Atlas Search index contains the indexed fields and the analyzers used to create the index. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Write role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.get_cluster_search_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    index_id="indexId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection with one or more Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `str` — Unique 24-hexadecimal digit string that identifies the Application Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Application Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Application Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">delete_cluster_search_index</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one Atlas Search index that you identified with its unique ID. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role. This deletion is eventually consistent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.delete_cluster_search_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    index_id="indexId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the database and collection with one or more Application Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `str` — Unique 24-hexadecimal digit string that identifies the Atlas Search index. Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.atlas_search.<a href="src/atlas_sdk/atlas_search/client.py">update_cluster_search_index</a>(...) -> SearchIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one Atlas Search index that you identified with its unique ID. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, SearchIndexUpdateRequestDefinition
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.atlas_search.update_cluster_search_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    index_id="indexId",
    definition=SearchIndexUpdateRequestDefinition(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Name of the cluster that contains the collection whose Atlas Search index you want to update.
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `str` — Unique 24-hexadecimal digit string that identifies the Atlas Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchIndexUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Global Clusters
<details><summary><code>client.global_clusters.<a href="src/atlas_sdk/global_clusters/client.py">get_cluster_global_writes</a>(...) -> GeoSharding20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one managed namespace within the specified global cluster. A managed namespace identifies a collection using the database name, the dot separator, and the collection name. To use this resource, the requesting Service Account or API Key must have the Project Read Only role. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.global_clusters.get_cluster_global_writes(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_clusters.<a href="src/atlas_sdk/global_clusters/client.py">create_custom_zone_mapping</a>(...) -> GeoSharding20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one custom zone mapping for the specified global cluster. A custom zone mapping matches one ISO 3166-2 location code to a zone in your global cluster. By default, MongoDB Cloud maps each location code to the closest geographical zone. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ZoneMapping
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.global_clusters.create_custom_zone_mapping(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    custom_zone_mappings=[
        ZoneMapping(
            location="location",
            zone="zone",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**custom_zone_mappings:** `typing.List[ZoneMapping]` 

List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings.

This parameter returns an empty object if no custom zones exist.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_clusters.<a href="src/atlas_sdk/global_clusters/client.py">delete_custom_zone_mapping</a>(...) -> GeoSharding20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes all custom zone mappings for the specified global cluster. A custom zone mapping matches one ISO 3166-2 location code to a zone in your global cluster. Removing the custom zone mappings restores the default mapping. By default, MongoDB Cloud maps each location code to the closest geographical zone. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.global_clusters.delete_custom_zone_mapping(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_clusters.<a href="src/atlas_sdk/global_clusters/client.py">create_managed_namespace</a>(...) -> GeoSharding20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one managed namespace within the specified global cluster. A managed namespace identifies a collection using the database name, the dot separator, and the collection name. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.global_clusters.create_managed_namespace(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    collection="collection",
    custom_shard_key="customShardKey",
    db="db",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ManagedNamespaces` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_clusters.<a href="src/atlas_sdk/global_clusters/client.py">delete_managed_namespaces</a>(...) -> GeoSharding20240805</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one managed namespace within the specified global cluster. A managed namespace identifies a collection using the database name, the dot separator, and the collection name. Deleting a managed namespace does not remove the associated collection or data. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.global_clusters.delete_managed_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies this cluster.
    
</dd>
</dl>

<dl>
<dd>

**db:** `typing.Optional[str]` — Human-readable label that identifies the database that contains the collection.
    
</dd>
</dl>

<dl>
<dd>

**collection:** `typing.Optional[str]` — Human-readable label that identifies the collection associated with the managed namespace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rolling Index
<details><summary><code>client.rolling_index.<a href="src/atlas_sdk/rolling_index/client.py">create_rolling_index</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an index on the cluster identified by its name in a rolling manner. Creating the index in this way allows index builds on one replica set member as a standalone at a time, starting with the secondary members. Creating indexes in this way requires at least one replica set election. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role or the Project Index Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, Collation, IndexOptions
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.rolling_index.create_rolling_index(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    collation=Collation(
        alternate="non-ignorable",
        backwards=False,
        case_first="lower",
        case_level=False,
        locale="af",
        max_variable="punct",
        normalization=False,
        numeric_ordering=False,
        strength=3,
    ),
    collection="accounts",
    db="sample_airbnb",
    keys=[
        {
            "property_type": "1"
        }
    ],
    options=IndexOptions(
        name="PartialIndexTest",
        partial_filter_expression={
            "limit": {"$gt": 900}
        },
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster on which MongoDB Cloud creates an index.
    
</dd>
</dl>

<dl>
<dd>

**collection:** `str` — Human-readable label of the collection for which MongoDB Cloud creates an index.
    
</dd>
</dl>

<dl>
<dd>

**db:** `str` — Human-readable label of the database that holds the collection on which MongoDB Cloud creates an index.
    
</dd>
</dl>

<dl>
<dd>

**keys:** `typing.List[typing.Dict[str, str]]` — List that contains one or more objects that describe the parameters that you want to index.
    
</dd>
</dl>

<dl>
<dd>

**collation:** `typing.Optional[Collation]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[IndexOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Online Archive
<details><summary><code>client.online_archive.<a href="src/atlas_sdk/online_archive/client.py">list_online_archives</a>(...) -> PaginatedOnlineArchive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details of all online archives. This archive stores data from one cluster within one project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.online_archive.list_online_archives(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the collection for which you want to return the online archives.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.online_archive.<a href="src/atlas_sdk/online_archive/client.py">create_online_archive</a>(...) -> BackupOnlineArchive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one online archive. This archive stores data from one cluster within one project. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, Criteria
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.online_archive.create_online_archive(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    coll_name="collName",
    criteria=Criteria(),
    db_name="dbName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the collection for which you want to create one online archive.
    
</dd>
</dl>

<dl>
<dd>

**coll_name:** `str` — Human-readable label that identifies the collection for which you created the online archive.
    
</dd>
</dl>

<dl>
<dd>

**criteria:** `Criteria` 
    
</dd>
</dl>

<dl>
<dd>

**db_name:** `str` — Human-readable label of the database that contains the collection that contains the online archive.
    
</dd>
</dl>

<dl>
<dd>

**collection_type:** `typing.Optional[str]` 

Classification of MongoDB database collection that you want to return.

If you set this parameter to `TIMESERIES`, set `"criteria.type" : "date"` and `"criteria.dateFormat" : "ISODATE"`.
    
</dd>
</dl>

<dl>
<dd>

**data_expiration_rule:** `typing.Optional[DataExpirationRule]` 
    
</dd>
</dl>

<dl>
<dd>

**data_process_region:** `typing.Optional[CreateDataProcessRegion]` 
    
</dd>
</dl>

<dl>
<dd>

**partition_fields:** `typing.Optional[typing.List[PartitionField]]` — List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify parameters that you frequently query. If you specified `criteria.type`: `DATE` in the Create One Online Archive endpoint, then you can specify up to three parameters by which to query. One of these parameters must be the `DATE` value, which is required in this case. If you specified `criteria.type`: `CUSTOM` in the Create One Online Archive endpoint, then you can specify up to two parameters by which to query. Queries that don't use `criteria.type`: `DATE` or `criteria.type`: `CUSTOM` parameters cause MongoDB to scan a full collection of all archived documents. This takes more time and increases your costs.
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Flag that indicates whether this online archive exists in the paused state. A request to resume fails if the collection has another active online archive. To pause an active online archive or resume a paused online archive, you must include this parameter. To pause an active archive, set this to **true**. To resume a paused archive, set this to **false**.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[OnlineArchiveSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.online_archive.<a href="src/atlas_sdk/online_archive/client.py">get_online_archive</a>(...) -> BackupOnlineArchive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one online archive for one cluster. This archive stores data from one cluster within one project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.online_archive.get_online_archive(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    archive_id="archiveId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the specified collection from which Application created the online archive.
    
</dd>
</dl>

<dl>
<dd>

**archive_id:** `str` — Unique 24-hexadecimal digit string that identifies the online archive to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.online_archive.<a href="src/atlas_sdk/online_archive/client.py">delete_online_archive</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one online archive. This archive stores data from one cluster within one project. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.online_archive.delete_online_archive(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    archive_id="archiveId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the collection from which you want to remove an online archive.
    
</dd>
</dl>

<dl>
<dd>

**archive_id:** `str` — Unique 24-hexadecimal digit string that identifies the online archive to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.online_archive.<a href="src/atlas_sdk/online_archive/client.py">update_online_archive</a>(...) -> BackupOnlineArchive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates, pauses, or resumes one online archive. This archive stores data from one cluster within one project. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.online_archive.update_online_archive(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_name_="clusterName",
    archive_id="archiveId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the specified collection from which Application created the online archive.
    
</dd>
</dl>

<dl>
<dd>

**archive_id:** `str` — Unique 24-hexadecimal digit string that identifies the online archive to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BackupOnlineArchive` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.online_archive.<a href="src/atlas_sdk/online_archive/client.py">download_query_logs</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads query logs for the specified online archive. To use this resource, the requesting Service Account or API Key must have the Project Data Access Read Only or higher role. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.online_archive.download_query_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that contains the collection for which you want to return the query logs from one online archive.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Date and time that specifies the starting point for the range of log messages to return. This resource expresses this value in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — Date and time that specifies the end point for the range of log messages to return. This resource expresses this value in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).
    
</dd>
</dl>

<dl>
<dd>

**archive_only:** `typing.Optional[bool]` — Flag that indicates whether to download logs for queries against your online archive only or both your online archive and cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cluster Outage Simulation
<details><summary><code>client.cluster_outage_simulation.<a href="src/atlas_sdk/cluster_outage_simulation/client.py">get_outage_simulation</a>(...) -> ClusterOutageSimulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one outage simulation for one cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cluster_outage_simulation.get_outage_simulation(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that is undergoing outage simulation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cluster_outage_simulation.<a href="src/atlas_sdk/cluster_outage_simulation/client.py">start_outage_simulation</a>(...) -> ClusterOutageSimulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a cluster outage simulation. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role, Project Cluster Resilience Tester role, or Project Replica Set Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cluster_outage_simulation.start_outage_simulation(
    group_id_="32b6e34b3d91647abb20e7b8",
    cluster_name_="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster to undergo an outage simulation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ClusterOutageSimulation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cluster_outage_simulation.<a href="src/atlas_sdk/cluster_outage_simulation/client.py">end_outage_simulation</a>(...) -> ClusterOutageSimulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ends a cluster outage simulation. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role, Project Cluster Resilience Tester role, or Project Replica Set Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cluster_outage_simulation.end_outage_simulation(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster that is undergoing outage simulation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Performance Advisor
<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">list_drop_index_suggestions</a>(...) -> DropIndexSuggestionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the indexes that the Performance Advisor suggests to drop. The Performance Advisor suggests dropping unused, redundant, and hidden indexes to improve write performance and increase storage space. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.list_drop_index_suggestions(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">list_schema_advice</a>(...) -> SchemaAdvisorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the schema suggestions that the Performance Advisor detects. The Performance Advisor provides holistic schema recommendations for your cluster by sampling documents in your most active collections and collections with slow-running queries. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.list_schema_advice(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">list_cluster_suggested_indexes</a>(...) -> PerformanceAdvisorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the indexes that the Performance Advisor suggests. The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.list_cluster_suggested_indexes(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**process_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Process IDs from which to retrieve suggested indexes. A `processId` is a combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests. To include multiple `processIds`, pass the parameter multiple times delimited with an ampersand (`&`) between each `processId`.
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Namespaces from which to retrieve suggested indexes. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` 

Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you don't specify the **until** parameter, the endpoint returns data covering from the **since** value and the current time.
- If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[int]` 

Date and time up until which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you specify the **until** parameter, you must specify the **since** parameter.
- If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">get_managed_slow_ms</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get whether the Managed Slow MS feature is enabled.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.get_managed_slow_ms(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">disable_managed_slow_ms</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the slow operation threshold that MongoDB Cloud calculated for the specified project. The threshold determines which operations the Performance Advisor and Query Profiler considers slow. When enabled, MongoDB Cloud uses the average execution time for operations on your cluster to determine slow-running queries. As a result, the threshold is more pertinent to your cluster workload. The slow operation threshold is enabled by default for dedicated clusters (M10+). When disabled, MongoDB Cloud considers any operation that takes longer than 100 milliseconds to be slow. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.disable_managed_slow_ms(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">enable_managed_slow_ms</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables MongoDB Cloud to use its slow operation threshold for the specified project. The threshold determines which operations the Performance Advisor and Query Profiler considers slow. When enabled, MongoDB Cloud uses the average execution time for operations on your cluster to determine slow-running queries. As a result, the threshold is more pertinent to your cluster workload. The slow operation threshold is enabled by default for dedicated clusters (M10+). When disabled, MongoDB Cloud considers any operation that takes longer than 100 milliseconds to be slow. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.enable_managed_slow_ms(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">list_performance_advisor_namespaces</a>(...) -> Namespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns up to 20 namespaces for collections experiencing slow queries on the specified host. If you specify a secondary member of a replica set that hasn't received any database read operations, the endpoint doesn't return any namespaces. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.list_performance_advisor_namespaces(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="processId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` 

Length of time expressed during which the query finds suggested indexes among the managed namespaces in the cluster. This parameter expresses its value in milliseconds.

- If you don't specify the **since** parameter, the endpoint returns data covering the duration before the current time.
- If you specify neither the **duration** nor **since** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` 

Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you don't specify the **duration** parameter, the endpoint returns data covering from the **since** value and the current time.
- If you specify neither the **duration** nor the **since** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">list_slow_query_logs</a>(...) -> PerformanceAdvisorSlowQueryList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns log lines for slow queries that the Performance Advisor and Query Profiler identified. The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance. MongoDB Cloud bases the threshold for slow queries on the average time of operations on your cluster. This enables workload-relevant recommendations. To use this resource, the requesting Service Account or API Key must have any Project Data Access role or the Project Observability Viewer role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.list_slow_query_logs(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="processId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` 

Length of time expressed during which the query finds slow queries among the managed namespaces in the cluster. This parameter expresses its value in milliseconds.

- If you don't specify the **since** parameter, the endpoint returns data covering the duration before the current time.
- If you specify neither the **duration** nor **since** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Namespaces from which to retrieve slow queries. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**n_logs:** `typing.Optional[int]` — Maximum number of lines from the log to return.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` 

Date and time from which the query retrieves the slow queries. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you don't specify the **duration** parameter, the endpoint returns data covering from the **since** value and the current time.
- If you specify neither the **duration** nor the **since** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**include_metrics:** `typing.Optional[bool]` — Whether or not to include metrics extracted from the slow query log as separate fields.
    
</dd>
</dl>

<dl>
<dd>

**include_replica_state:** `typing.Optional[bool]` — Whether or not to include the replica state of the host when the slow query log was generated as a separate field.
    
</dd>
</dl>

<dl>
<dd>

**include_op_type:** `typing.Optional[bool]` — Whether or not to include the operation type (read/write/command) extracted from the slow query log as a separate field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">list_suggested_indexes</a>(...) -> PerformanceAdvisorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the indexes that the Performance Advisor suggests. The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.list_suggested_indexes(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="processId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` 

Length of time expressed during which the query finds suggested indexes among the managed namespaces in the cluster. This parameter expresses its value in milliseconds.

- If you don't specify the **since** parameter, the endpoint returns data covering the duration before the current time.
- If you specify neither the **duration** nor **since** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Namespaces from which to retrieve suggested indexes. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**n_examples:** `typing.Optional[int]` — Maximum number of example queries that benefit from the suggested index.
    
</dd>
</dl>

<dl>
<dd>

**n_indexes:** `typing.Optional[int]` — Number that indicates the maximum indexes to suggest.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` 

Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you don't specify the **duration** parameter, the endpoint returns data covering from the **since** value and the current time.
- If you specify neither the **duration** nor the **since** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">get_serverless_auto_indexing</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get whether the Serverless Auto Indexing feature is enabled. This endpoint returns a value for Flex clusters that were created with the Create Serverless Instance endpoint or Flex clusters that were migrated from Serverless instances. However, the value returned is not indicative of the Auto Indexing state as Auto Indexing is unavailable for Flex clusters. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.get_serverless_auto_indexing(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.performance_advisor.<a href="src/atlas_sdk/performance_advisor/client.py">set_serverless_auto_indexing</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set whether the Serverless Auto Indexing feature is enabled. This endpoint sets a value for Flex clusters that were created with the Create Serverless Instance endpoint or Flex clusters that were migrated from Serverless instances. However, the value returned is not indicative of the Auto Indexing state as Auto Indexing is unavailable for Flex clusters. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.performance_advisor.set_serverless_auto_indexing(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    enable=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**enable:** `bool` — Value that we want to set for the Serverless Auto Indexing toggle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## QueryShapeInsights
<details><summary><code>client.query_shape_insights.<a href="src/atlas_sdk/query_shape_insights/client.py">get_query_shape_details</a>(...) -> QueryStatsDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the metadata and statistics summary for a given query shape hash.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.query_shape_insights.get_query_shape_details(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    query_shape_hash="queryShapeHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**query_shape_hash:** `str` — A SHA256 hash of a query shape, output by MongoDB commands like `$queryStats` and `$explain` or slow query logs.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` 

Date and time from which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you don't specify the **until** parameter, the endpoint returns data covering from the **since** value and the current time.
- If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[int]` 

Date and time up until which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you specify the **until** parameter, you must specify the **since** parameter.
- If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**process_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Process IDs from which to retrieve query shape statistics. A `processId` is a combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests. To include multiple `processIds`, pass the parameter multiple times delimited with an ampersand (`&`) between each `processId`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_shape_insights.<a href="src/atlas_sdk/query_shape_insights/client.py">list_query_shape_summaries</a>(...) -> QueryStatsSummaryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of query shape statistics summaries for a given cluster. Query shape statistics provide performance insights about MongoDB queries, helping users identify problematic query patterns and potential optimizations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.query_shape_insights.list_query_shape_summaries(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` 

Date and time from which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you don't specify the **until** parameter, the endpoint returns data covering from the **since** value and the current time.
- If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[int]` 

Date and time up until which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).

- If you specify the **until** parameter, you must specify the **since** parameter.
- If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**process_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Process IDs from which to retrieve query shape statistics. A `processId` is a combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests. To include multiple `processId`, pass the parameter multiple times delimited with an ampersand (`&`) between each `processId`.
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Namespaces from which to retrieve query shape statistics. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**commands:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve query shape statistics matching specified MongoDB commands. To include multiple commands, pass the parameter multiple times delimited with an ampersand (`&`) between each command. The currently supported parameters are find, distinct, and aggregate. Omit this parameter to return results for all supported commands.
    
</dd>
</dl>

<dl>
<dd>

**n_summaries:** `typing.Optional[int]` — Maximum number of query statistic summaries to return.
    
</dd>
</dl>

<dl>
<dd>

**series:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Query shape statistics data series to retrieve. A series represents a specific metric about query execution. To include multiple series, pass the parameter multiple times delimited with an ampersand (`&`) between each series. Omit this parameter to return results for all available series.
    
</dd>
</dl>

<dl>
<dd>

**query_shape_hashes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of SHA256 hashes of desired query shapes, output by MongoDB commands like `$queryStats` and $explain or slow query logs. To include multiple series, pass the parameter multiple times delimited with an ampersand (`&`) between each series. Omit this parameter to return results for all available series.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_shape_insights.<a href="src/atlas_sdk/query_shape_insights/client.py">list_cluster_query_shapes</a>(...) -> PaginatedQueryShapes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of query shapes for one cluster. Query shapes may be filtered by their status; at present, this endpoint supports only the REJECTED status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.query_shape_insights.list_cluster_query_shapes(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The status of query shapes to retrieve. Only REJECTED status is supported. If omitted, defaults to REJECTED.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_shape_insights.<a href="src/atlas_sdk/query_shape_insights/client.py">get_cluster_query_shape</a>(...) -> QueryShapeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details for a single query shape. This endpoint only returns query shapes with REJECTED status. If the specified query shape hash does not correspond to a rejected query shape, a 404 Not Found error is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.query_shape_insights.get_cluster_query_shape(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    query_shape_hash="queryShapeHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**query_shape_hash:** `str` — A SHA256 hash of a query shape, output by MongoDB commands like `$queryStats` and `$explain` or slow query logs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_shape_insights.<a href="src/atlas_sdk/query_shape_insights/client.py">update_cluster_query_shape</a>(...) -> QueryShapeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the rejection status of a query shape. Use this endpoint to reject a query shape (preventing it from executing on the cluster) or to unreject a previously rejected query shape (allowing it to execute again). This operation is idempotent: rejecting an already rejected query shape or unrejecting an already unrejected query shape will return 200 OK.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.query_shape_insights.update_cluster_query_shape(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
    query_shape_hash="queryShapeHash",
    status="status",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**query_shape_hash:** `str` — A SHA256 hash of a query shape, output by MongoDB commands like `$queryStats` and `$explain` or slow query logs.
    
</dd>
</dl>

<dl>
<dd>

**status:** `str` — The rejection status of a query shape. Use REJECTED to prevent the query shape from executing on the cluster, or UNREJECTED to allow it to execute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitoring and Logs
<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">download_cluster_log</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a compressed (.gz) log file that contains a range of log messages for the specified host for the specified project. MongoDB updates process and audit logs from the cluster backend infrastructure every five minutes. Logs are stored in chunks approximately five minutes in length, but this duration may vary. If you poll the API for log files, we recommend polling every five minutes even though consecutive polls could contain some overlapping logs. This feature isn't available for `M0` free clusters, `M2`, `M5`, flex, or serverless clusters. To use this resource, the requesting Service Account or API Key must have the Project Cluster Log Viewer role or Project Data Access Read Only role. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.download_cluster_log()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**host_name:** `str` — Human-readable label that identifies the host that stores the log files that you want to download.
    
</dd>
</dl>

<dl>
<dd>

**log_name:** `str` — Human-readable label that identifies the log file that you want to return. To return audit logs, enable *Database Auditing* for the specified project.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — Specifies the date and time for the ending point of the range of log messages to retrieve, in the number of seconds that have elapsed since the UNIX epoch. This value will default to 24 hours after the start date. If the start date is also unspecified, the value will default to the time of the request.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Specifies the date and time for the starting point of the range of log messages to retrieve, in the number of seconds that have elapsed since the UNIX epoch. This value will default to 24 hours prior to the end date. If the end date is also unspecified, the value will default to 24 hours prior to the time of the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">list_host_fts_metrics</a>(...) -> CloudSearchMetrics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Atlas Search metric types available for one process in the specified project. You must have the Project Read Only or higher role to view the Atlas Search metric types.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.list_host_fts_metrics(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="my.host.name.com:27017",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_index_measurements</a>(...) -> MeasurementsIndexes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Atlas Search metrics data series within the provided time range for one namespace and index name on the specified process. You must have the Project Read Only or higher role to view the Atlas Search metric types.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_index_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="my.host.name.com:27017",
    database_name="mydb",
    collection_name="mycoll",
    index_name="myindex",
    granularity="PT1M",
    period="PT10H",
    metrics=[
        "metrics"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Human-readable label that identifies the collection.
    
</dd>
</dl>

<dl>
<dd>

**index_name:** `str` — Human-readable label that identifies the index.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `str` — Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List that contains the measurements that MongoDB Atlas reports for the associated data series.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">list_index_measurements</a>(...) -> MeasurementsIndexes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Atlas Search index metrics within the specified time range for one namespace in the specified process.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.list_index_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="my.host.name.com:27017",
    database_name="mydb",
    collection_name="mycoll",
    granularity="PT1M",
    period="PT10H",
    metrics=[
        "metrics"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database.
    
</dd>
</dl>

<dl>
<dd>

**collection_name:** `str` — Human-readable label that identifies the collection.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `str` — Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List that contains the measurements that MongoDB Atlas reports for the associated data series.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">list_measurements</a>(...) -> MeasurementsNonIndex</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Atlas Search hardware and status data series within the provided time range for one process in the specified project. You must have the Project Read Only or higher role to view the Atlas Search metric types.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.list_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="my.host.name.com:27017",
    granularity="PT1M",
    period="PT10H",
    metrics=[
        "metrics"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `str` — Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List that contains the metrics that you want MongoDB Atlas to report for the associated data series. If you don't set this parameter, this resource returns all hardware and status metrics for the associated data series.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">list_group_processes</a>(...) -> PaginatedHostViewAtlas</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details of all processes for the specified project. A MongoDB process can be either a `mongod` or `mongos`. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.list_group_processes(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_group_process</a>(...) -> ApiHostViewAtlas</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the processes for the specified host for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_group_process(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">list_databases</a>(...) -> PaginatedDatabase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of databases running on the specified host for the specified project. `M0` free clusters, `M2`, `M5`, serverless, and Flex clusters have some operational limits. The MongoDB Cloud process must be a `mongod`. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.list_databases(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_database</a>(...) -> MesurementsDatabase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one database running on the specified host for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_database(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
    database_name="databaseName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database that the specified MongoDB process serves.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_database_measurements</a>(...) -> ApiMeasurementsGeneralViewAtlas</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the measurements of one database for the specified host for the specified project. Returns the database's on-disk storage space based on the MongoDB `dbStats` command output. To calculate some metric series, Atlas takes the rate between every two adjacent points. For these metric series, the first data point has a null value because Atlas can't calculate a rate for the first data point given the query time range. Atlas retrieves database metrics every 20 minutes but reduces frequency when necessary to optimize database performance. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_database_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
    database_name="databaseName",
    granularity="PT1M",
    period="PT10H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — Human-readable label that identifies the database that the specified MongoDB process serves.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `str` — Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**m:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One or more types of measurement to request for this MongoDB process. If omitted, the resource returns all measurements. To specify multiple values for `m`, repeat the `m` parameter for each value. Specify measurements that apply to the specified host. MongoDB Cloud returns an error if you specified any invalid measurements.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">list_process_disks</a>(...) -> PaginatedDiskPartition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of disks or partitions for the specified host for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.list_process_disks(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_process_disk</a>(...) -> MeasurementDiskPartition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns measurement details for one disk or partition for the specified host for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_process_disk(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
    partition_name="partitionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `str` — Human-readable label of the disk or partition to which the measurements apply.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_process_disk_measurements</a>(...) -> ApiMeasurementsGeneralViewAtlas</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the measurements of one disk or partition for the specified host for the specified project. Returned value can be one of the following:
- Throughput of I/O operations for the disk partition used for the MongoDB process
- Percentage of time during which requests the partition issued and serviced
- Latency per operation type of the disk partition used for the MongoDB process
- Amount of free and used disk space on the disk partition used for the MongoDB process

To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_process_disk_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
    partition_name="partitionName",
    granularity="PT1M",
    period="PT10H",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**partition_name:** `str` — Human-readable label of the disk or partition to which the measurements apply.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `str` — Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**m:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One or more types of measurement to request for this MongoDB process. If omitted, the resource returns all measurements. To specify multiple values for `m`, repeat the `m` parameter for each value. Specify measurements that apply to the specified host. MongoDB Cloud returns an error if you specified any invalid measurements.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitoring_and_logs.<a href="src/atlas_sdk/monitoring_and_logs/client.py">get_process_measurements</a>(...) -> ApiMeasurementsGeneralViewAtlas</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns disk, partition, or host measurements per process for the specified host for the specified project. Returned value can be one of the following:
- Throughput of I/O operations for the disk partition used for the MongoDB process
- Percentage of time during which requests the partition issued and serviced
- Latency per operation type of the disk partition used for the MongoDB process
- Amount of free and used disk space on the disk partition used for the MongoDB process
- Measurements for the host, such as CPU usage or number of I/O operations

To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.monitoring_and_logs.get_process_measurements(
    group_id="32b6e34b3d91647abb20e7b8",
    process_id="mongodb.example.com:27017",
    period="PT10H",
    granularity="PT1M",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` — Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `str` — Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**m:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One or more types of measurement to request for this MongoDB process. If omitted, the resource returns all measurements. To specify multiple values for `m`, repeat the `m` parameter for each value. Specify measurements that apply to the specified host. MongoDB Cloud returns an error if you specified any invalid measurements.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Network Peering
<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">list_group_containers</a>(...) -> PaginatedCloudProviderContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about all network peering containers in the specified project for the specified cloud provider. If you do not specify the cloud provider, MongoDB Cloud returns details about all network peering containers in the project for Amazon Web Services (AWS). To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.list_group_containers(
    group_id="32b6e34b3d91647abb20e7b8",
    provider_name="providerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `str` — Cloud service provider that serves the desired network peering containers.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">create_group_container</a>(...) -> CloudProviderContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one new network peering container in the specified project. MongoDB Cloud can deploy Network Peering connections in a network peering container. GCP can have one container per project. AWS and Azure can have one container per cloud provider region. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.create_group_container(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CloudProviderContainer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">get_group_container</a>(...) -> CloudProviderContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about one network peering container in one specified project. Network peering containers contain network peering connections. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.get_group_container(
    group_id="32b6e34b3d91647abb20e7b8",
    container_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**container_id:** `str` — Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">delete_group_container</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one network peering container in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.delete_group_container(
    group_id="32b6e34b3d91647abb20e7b8",
    container_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**container_id:** `str` — Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">update_group_container</a>(...) -> CloudProviderContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the network details and labels of one specified network peering container in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.update_group_container(
    group_id="32b6e34b3d91647abb20e7b8",
    container_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**container_id:** `str` — Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CloudProviderContainer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">list_group_container_all</a>(...) -> PaginatedCloudProviderContainer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about all network peering containers in the specified project. Network peering containers contain network peering connections. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.list_group_container_all(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">list_group_peers</a>(...) -> PaginatedContainerPeer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about all network peering connections in the specified project. Network peering allows multiple cloud-hosted applications to securely connect to the same project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.list_group_peers(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `typing.Optional[str]` — Cloud service provider to use for this VPC peering connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">create_group_peer</a>(...) -> BaseNetworkPeeringConnectionSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one new network peering connection in the specified project. Network peering allows multiple cloud-hosted applications to securely connect to the same project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Network Access Manager role. To learn more about considerations and prerequisites, see the Network Peering Documentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.create_group_peer(
    group_id="32b6e34b3d91647abb20e7b8",
    container_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BaseNetworkPeeringConnectionSettings` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">get_group_peer</a>(...) -> BaseNetworkPeeringConnectionSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about one specified network peering connection in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.get_group_peer(
    group_id="32b6e34b3d91647abb20e7b8",
    peer_id="peerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**peer_id:** `str` — Unique 24-hexadecimal digit string that identifies the network peering connection that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">delete_group_peer</a>(...) -> RequestAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one network peering connection in the specified project. If you remove the last network peering connection associated with a project, MongoDB Cloud also removes any AWS security groups from the project IP access list. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Network Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.delete_group_peer(
    group_id="32b6e34b3d91647abb20e7b8",
    peer_id="peerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**peer_id:** `str` — Unique 24-hexadecimal digit string that identifies the network peering connection that you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">update_group_peer</a>(...) -> BaseNetworkPeeringConnectionSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one specified network peering connection in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Network Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.update_group_peer(
    group_id="32b6e34b3d91647abb20e7b8",
    peer_id="peerId",
    container_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**peer_id:** `str` — Unique 24-hexadecimal digit string that identifies the network peering connection that you want to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BaseNetworkPeeringConnectionSettings` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">verify_private_ip_mode</a>(...) -> PrivateIpMode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies if someone set the specified project to **Connect via Peering Only** mode. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.verify_private_ip_mode(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_peering.<a href="src/atlas_sdk/network_peering/client.py">disable_peering</a>(...) -> PrivateIpMode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables Connect via Peering Only mode for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.network_peering.disable_peering(
    group_id="32b6e34b3d91647abb20e7b8",
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PrivateIpMode` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Custom Database Roles
<details><summary><code>client.custom_database_roles.<a href="src/atlas_sdk/custom_database_roles/client.py">list_custom_db_roles</a>(...) -> typing.List[UserCustomDbRole]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom roles for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.custom_database_roles.list_custom_db_roles(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_database_roles.<a href="src/atlas_sdk/custom_database_roles/client.py">create_custom_db_role</a>(...) -> UserCustomDbRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one custom role in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role, Project Stream Processing Owner role, or the Project Database Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.custom_database_roles.create_custom_db_role(
    group_id="32b6e34b3d91647abb20e7b8",
    role_name="roleName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserCustomDbRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_database_roles.<a href="src/atlas_sdk/custom_database_roles/client.py">get_custom_db_role</a>(...) -> UserCustomDbRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one custom role for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.custom_database_roles.get_custom_db_role(
    group_id="32b6e34b3d91647abb20e7b8",
    role_name="roleName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**role_name:** `str` — Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_database_roles.<a href="src/atlas_sdk/custom_database_roles/client.py">delete_custom_db_role</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one custom role from the specified project. You can't remove a custom role that would leave one or more child roles with no parent roles or actions. You also can't remove a custom role that would leave one or more database users without roles. To use this resource, the requesting Service Account or API Key must have the Project Owner role, Project Stream Processing Owner role, or the Project Database Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.custom_database_roles.delete_custom_db_role(
    group_id="32b6e34b3d91647abb20e7b8",
    role_name="roleName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**role_name:** `str` — Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_database_roles.<a href="src/atlas_sdk/custom_database_roles/client.py">update_custom_db_role</a>(...) -> UserCustomDbRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one custom role in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role, the Project Stream Processing Owner role, or the Project Database Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.custom_database_roles.update_custom_db_role(
    group_id="32b6e34b3d91647abb20e7b8",
    role_name="roleName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**role_name:** `str` — Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.List[DatabasePrivilegeAction]]` — List of the individual privilege actions that the role grants.
    
</dd>
</dl>

<dl>
<dd>

**inherited_roles:** `typing.Optional[typing.List[DatabaseInheritedRole]]` — List of the built-in roles that this custom role inherits.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Federation
<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">list_data_federation</a>(...) -> typing.List[DataLakeTenant]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of all federated database instances in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only or higher role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.list_data_federation(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Type of Federated Database Instances to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">create_data_federation</a>(...) -> DataLakeTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one federated database instance in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Charts Admin roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.create_data_federation(
    group_id_="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataLakeTenant` 
    
</dd>
</dl>

<dl>
<dd>

**skip_role_validation:** `typing.Optional[bool]` — Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket. AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">get_data_federation</a>(...) -> DataLakeTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one federated database instance within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only or Project Charts Admin roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.get_data_federation(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the Federated Database to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">delete_data_federation</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one federated database instance from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Charts Admin roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.delete_data_federation(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">update_data_federation</a>(...) -> DataLakeTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of one federated database instance in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner or higher role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.update_data_federation(
    group_id_="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    skip_role_validation=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance to update.
    
</dd>
</dl>

<dl>
<dd>

**skip_role_validation:** `bool` — Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket. AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataLakeTenant` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">list_data_federation_limits</a>(...) -> typing.List[DataFederationTenantQueryLimit]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns query limits for a federated databases instance in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.list_data_federation_limits(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance for which you want to retrieve query limits.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">get_data_federation_limit</a>(...) -> DataFederationTenantQueryLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one query limit for the specified federated database instance in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.get_data_federation_limit(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    limit_name="limitName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance to which the query limit applies.
    
</dd>
</dl>

<dl>
<dd>

**limit_name:** `str` 

Human-readable label that identifies this data federation instance limit.

| Limit Name | Description | Default |
| --- | --- | --- |
| `bytesProcessed.query` | Limit on the number of bytes processed during a single data federation query | N/A |
| `bytesProcessed.daily` | Limit on the number of bytes processed for the data federation instance for the current day | N/A |
| `bytesProcessed.weekly` | Limit on the number of bytes processed for the data federation instance for the current week | N/A |
| `bytesProcessed.monthly` | Limit on the number of bytes processed for the data federation instance for the current month | N/A |
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">delete_data_federation_limit</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one query limit for one federated database instance. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.delete_data_federation_limit(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    limit_name="limitName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance to which the query limit applies.
    
</dd>
</dl>

<dl>
<dd>

**limit_name:** `str` 

Human-readable label that identifies this data federation instance limit.

| Limit Name | Description | Default |
| --- | --- | --- |
| `bytesProcessed.query` | Limit on the number of bytes processed during a single data federation query | N/A |
| `bytesProcessed.daily` | Limit on the number of bytes processed for the data federation instance for the current day | N/A |
| `bytesProcessed.weekly` | Limit on the number of bytes processed for the data federation instance for the current week | N/A |
| `bytesProcessed.monthly` | Limit on the number of bytes processed for the data federation instance for the current month | N/A |
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">set_data_federation_limit</a>(...) -> DataFederationTenantQueryLimit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates one query limit for one federated database instance. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.set_data_federation_limit(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name_="tenantName",
    limit_name="limitName",
    value=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance to which the query limit applies.
    
</dd>
</dl>

<dl>
<dd>

**limit_name:** `str` 

Human-readable label that identifies this data federation instance limit.

| Limit Name | Description | Default |
| --- | --- | --- |
| `bytesProcessed.query` | Limit on the number of bytes processed during a single data federation query | N/A |
| `bytesProcessed.daily` | Limit on the number of bytes processed for the data federation instance for the current day | N/A |
| `bytesProcessed.weekly` | Limit on the number of bytes processed for the data federation instance for the current week | N/A |
| `bytesProcessed.monthly` | Limit on the number of bytes processed for the data federation instance for the current month | N/A |
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataFederationTenantQueryLimit` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">download_federation_query_logs</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the query logs for the specified federated database instance. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Data Access Read Write roles. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.download_federation_query_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Human-readable label that identifies the federated database instance for which you want to download query logs.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — Timestamp that specifies the end point for the range of log messages to download.  MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Timestamp that specifies the starting point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">list_private_endpoint_ids</a>(...) -> PaginatedPrivateNetworkEndpointIdEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all private endpoints for Federated Database Instances and Online Archives in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only or Project Charts Admin roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.list_private_endpoint_ids(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">create_private_endpoint_id</a>(...) -> PaginatedPrivateNetworkEndpointIdEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one private endpoint for Federated Database Instances and Online Archives to the specified projects. If the endpoint ID already exists and the associated comment is unchanged, Atlas Data Federation makes no change to the endpoint ID list. If the endpoint ID already exists and the associated comment is changed, Atlas Data Federation updates the comment value only in the endpoint ID list. If the endpoint ID doesn't exist, Atlas Data Federation appends the new endpoint to the list of endpoints in the endpoint ID list. Each region has an associated service name for the various endpoints. For the latest list of supported regions and their service names, see the external documentation. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Charts Admin roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.create_private_endpoint_id(
    group_id="32b6e34b3d91647abb20e7b8",
    endpoint_id="vpce-3bf78b0ddee411ba1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PrivateNetworkEndpointIdEntry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">get_private_endpoint_id</a>(...) -> PrivateNetworkEndpointIdEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified private endpoint for Federated Database Instances or Online Archives in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only or Project Charts Admin roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.get_private_endpoint_id(
    group_id="32b6e34b3d91647abb20e7b8",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 22-character alphanumeric string that identifies the private endpoint to return. Atlas Data Federation supports AWS private endpoints using the AWS PrivateLink feature.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_federation.<a href="src/atlas_sdk/data_federation/client.py">delete_private_endpoint_id</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one private endpoint for Federated Database Instances and Online Archives in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_federation.delete_private_endpoint_id(
    group_id="32b6e34b3d91647abb20e7b8",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 22-character alphanumeric string that identifies the private endpoint to remove. Atlas Data Federation supports AWS private endpoints using the AWS PrivateLink feature.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Database Users
<details><summary><code>client.database_users.<a href="src/atlas_sdk/database_users/client.py">list_database_users</a>(...) -> PaginatedApiAtlasDatabaseUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all database users that belong to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.database_users.list_database_users(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database_users.<a href="src/atlas_sdk/database_users/client.py">create_database_user</a>(...) -> CloudDatabaseUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one database user in the specified project. This MongoDB Cloud supports a maximum of 100 database users per project. If you require more than 100 database users on a project, contact Support. To use this resource, the requesting Service Account or API Key must have the Project Owner role, the Project Charts Admin role, Project Stream Processing Owner role, or the Project Database Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, DatabaseUserRole, UserScope
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.database_users.create_database_user(
    group_id_="32b6e34b3d91647abb20e7b8",
    aws_iam_type="USER",
    database_name="$external",
    group_id="32b6e34b3d91647abb20e7b8",
    roles=[
        DatabaseUserRole(
            database_name="sales",
            role_name="readWrite",
        ),
        DatabaseUserRole(
            database_name="marketing",
            role_name="read",
        )
    ],
    scopes=[
        UserScope(
            name="myCluster",
            type="CLUSTER",
        )
    ],
    username="arn:aws:iam::358363220050:user/mongodb-aws-iam-auth-test-user",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CloudDatabaseUser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database_users.<a href="src/atlas_sdk/database_users/client.py">get_database_user</a>(...) -> CloudDatabaseUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one database user that belong to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.database_users.get_database_user(
    group_id="32b6e34b3d91647abb20e7b8",
    database_name="databaseName",
    username="SCRAM-SHA: dylan or AWS IAM: arn:aws:iam::123456789012:user/sales/enterprise/DylanBloggs or x.509/LDAP: CN=Dylan Bloggs,OU=Enterprise,OU=Sales,DC=Example,DC=COM or OIDC: IdPIdentifier/IdPGroupName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — The database against which the database user authenticates. Database users must provide both a username and authentication database to log into MongoDB. If the user authenticates with AWS IAM, x.509, LDAP, or OIDC Workload this value should be `$external`. If the user authenticates with SCRAM-SHA or OIDC Workforce, this value should be `admin`.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 

Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication:

| Authentication Method | Parameter Needed | Parameter Value | username Format |
|---|---|---|---|
| AWS IAM | `awsIAMType` | `ROLE` | <abbr title="Amazon Resource Name">ARN</abbr> |
| AWS IAM | `awsIAMType` | `USER` | <abbr title="Amazon Resource Name">ARN</abbr> |
| x.509 | `x509Type` | `CUSTOMER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| x.509 | `x509Type` | `MANAGED` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| LDAP | `ldapAuthType` | `USER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| LDAP | `ldapAuthType` | `GROUP` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| OIDC Workforce | `oidcAuthType` | `IDP_GROUP` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP group name |
| OIDC Workload | `oidcAuthType` | `USER` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP user name |
| SCRAM-SHA | `awsIAMType`, `x509Type`, `ldapAuthType`, `oidcAuthType` | `NONE` | Alphanumeric string |
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database_users.<a href="src/atlas_sdk/database_users/client.py">delete_database_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one database user from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role, the Project Stream Processing Owner role, or the Project Database Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.database_users.delete_database_user(
    group_id="32b6e34b3d91647abb20e7b8",
    database_name="databaseName",
    username="SCRAM-SHA: dylan or AWS IAM: arn:aws:iam::123456789012:user/sales/enterprise/DylanBloggs or x.509/LDAP: CN=Dylan Bloggs,OU=Enterprise,OU=Sales,DC=Example,DC=COM or OIDC: IdPIdentifier/IdPGroupName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — The database against which the database user authenticates. Database users must provide both a username and authentication database to log into MongoDB. If the user authenticates with AWS IAM, x.509, LDAP, or OIDC Workload this value should be `$external`. If the user authenticates with SCRAM-SHA or OIDC Workforce, this value should be `admin`.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 

Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication:

| Authentication Method | Parameter Needed | Parameter Value | username Format |
|---|---|---|---|
| AWS IAM | `awsIAMType` | `ROLE` | <abbr title="Amazon Resource Name">ARN</abbr> |
| AWS IAM | `awsIAMType` | `USER` | <abbr title="Amazon Resource Name">ARN</abbr> |
| x.509 | `x509Type` | `CUSTOMER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| x.509 | `x509Type` | `MANAGED` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| LDAP | `ldapAuthType` | `USER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| LDAP | `ldapAuthType` | `GROUP` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| OIDC Workforce | `oidcAuthType` | `IDP_GROUP` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP group name |
| OIDC Workload | `oidcAuthType` | `USER` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP user name |
| SCRAM-SHA | `awsIAMType`, `x509Type`, `ldapAuthType`, `oidcAuthType` | `NONE` | Alphanumeric string |
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database_users.<a href="src/atlas_sdk/database_users/client.py">update_database_user</a>(...) -> CloudDatabaseUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one database user that belongs to the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role, Project Charts Admin role, Project Stream Processing Owner role, or the Project Database Access Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, DatabaseUserRole
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.database_users.update_database_user(
    group_id_="32b6e34b3d91647abb20e7b8",
    database_name_="databaseName",
    username_="SCRAM-SHA: dylan or AWS IAM: arn:aws:iam::123456789012:user/sales/enterprise/DylanBloggs or x.509/LDAP: CN=Dylan Bloggs,OU=Enterprise,OU=Sales,DC=Example,DC=COM or OIDC: IdPIdentifier/IdPGroupName",
    database_name="databaseName",
    group_id="groupId",
    roles=[
        DatabaseUserRole(
            database_name="databaseName",
            role_name="roleName",
        )
    ],
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**database_name:** `str` — The database against which the database user authenticates. Database users must provide both a username and authentication database to log into MongoDB. If the user authenticates with AWS IAM, x.509, LDAP, or OIDC Workload this value should be `$external`. If the user authenticates with SCRAM-SHA or OIDC Workforce, this value should be `admin`.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 

Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication:

| Authentication Method | Parameter Needed | Parameter Value | username Format |
|---|---|---|---|
| AWS IAM | `awsIAMType` | `ROLE` | <abbr title="Amazon Resource Name">ARN</abbr> |
| AWS IAM | `awsIAMType` | `USER` | <abbr title="Amazon Resource Name">ARN</abbr> |
| x.509 | `x509Type` | `CUSTOMER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| x.509 | `x509Type` | `MANAGED` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| LDAP | `ldapAuthType` | `USER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| LDAP | `ldapAuthType` | `GROUP` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |
| OIDC Workforce | `oidcAuthType` | `IDP_GROUP` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP group name |
| OIDC Workload | `oidcAuthType` | `USER` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP user name |
| SCRAM-SHA | `awsIAMType`, `x509Type`, `ldapAuthType`, `oidcAuthType` | `NONE` | Alphanumeric string |
    
</dd>
</dl>

<dl>
<dd>

**request:** `CloudDatabaseUser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## X.509 Authentication
<details><summary><code>client.x509authentication.<a href="src/atlas_sdk/x509authentication/client.py">list_database_user_certs</a>(...) -> PaginatedUserCert</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all unexpired X.509 certificates for the specified MongoDB user. This MongoDB user belongs to one project. Atlas manages these certificates and the MongoDB user. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.x509authentication.list_database_user_certs(
    group_id="32b6e34b3d91647abb20e7b8",
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Human-readable label that represents the MongoDB database user account whose certificates you want to return.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.x509authentication.<a href="src/atlas_sdk/x509authentication/client.py">create_database_user_cert</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates one X.509 certificate for the specified MongoDB user. Atlas manages the certificate and MongoDB user that belong to one project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

To get MongoDB Cloud to generate a managed certificate for a database user, set `"x509Type" : "MANAGED"` on the desired MongoDB Database User.

If you are managing your own Certificate Authority (CA) in Self-Managed X.509 mode, you must generate certificates for database users using your own CA.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.x509authentication.create_database_user_cert(
    group_id_="32b6e34b3d91647abb20e7b8",
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Human-readable label that represents the MongoDB database user account for whom to create a certificate.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserCert` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.x509authentication.<a href="src/atlas_sdk/x509authentication/client.py">disable_security_customer_x509</a>(...) -> UserSecurity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clears the customer-managed X.509 settings on a project, including the uploaded Certificate Authority, which disables self-managed X.509.

 Updating this configuration triggers a rolling restart of the database. You must have the Project Owner role to use this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.x509authentication.disable_security_customer_x509(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Access Tracking
<details><summary><code>client.access_tracking.<a href="src/atlas_sdk/access_tracking/client.py">get_access_history_cluster</a>(...) -> MongoDbAccessLogsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the access logs of one cluster identified by the cluster's name. Access logs contain a list of authentication requests made against your cluster. You can't use this feature on tenant-tier clusters (M0, M2, M5). To use this resource, the requesting Service Account or API Key must have the Project Monitoring Admin role, the Project Database Access Admin role, or the Project Cluster Log Viewer role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.access_tracking.get_access_history_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    cluster_name="clusterName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**auth_result:** `typing.Optional[bool]` — Flag that indicates whether the response returns the successful authentication attempts only.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[int]` — Date and time when to stop retrieving database history. If you specify **end**, you must also specify **start**. This parameter uses UNIX epoch time in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — One Internet Protocol address that attempted to authenticate with the database.
    
</dd>
</dl>

<dl>
<dd>

**n_logs:** `typing.Optional[int]` — Maximum number of lines from the log to return.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[int]` — Date and time when MongoDB Cloud begins retrieving database history. If you specify **start**, you must also specify **end**. This parameter uses UNIX epoch time in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.access_tracking.<a href="src/atlas_sdk/access_tracking/client.py">get_access_history_process</a>(...) -> MongoDbAccessLogsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the access logs of one cluster identified by the cluster's hostname. Access logs contain a list of authentication requests made against your clusters. You can't use this feature on tenant-tier clusters (M0, M2, M5). To use this resource, the requesting Service Account or API Key must have the Project Monitoring Admin role, the Project Database Access Admin role, or the Project Cluster Log Viewer role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.access_tracking.get_access_history_process(
    group_id="32b6e34b3d91647abb20e7b8",
    hostname="hostname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**hostname:** `str` — Fully qualified domain name or IP address of the MongoDB host that stores the log files that you want to download.
    
</dd>
</dl>

<dl>
<dd>

**auth_result:** `typing.Optional[bool]` — Flag that indicates whether the response returns the successful authentication attempts only.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[int]` — Date and time when to stop retrieving database history. If you specify **end**, you must also specify **start**. This parameter uses UNIX epoch time in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — One Internet Protocol address that attempted to authenticate with the database.
    
</dd>
</dl>

<dl>
<dd>

**n_logs:** `typing.Optional[int]` — Maximum number of lines from the log to return.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[int]` — Date and time when MongoDB Cloud begins retrieving database history. If you specify **start**, you must also specify **end**. This parameter uses UNIX epoch time in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Encryption at Rest using Customer Key Management
<details><summary><code>client.encryption_at_rest_using_customer_key_management.<a href="src/atlas_sdk/encryption_at_rest_using_customer_key_management/client.py">get_encryption_at_rest</a>(...) -> EncryptionAtRest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the configuration for encryption at rest using the keys you manage through your cloud provider. MongoDB Cloud encrypts all storage even if you don't use your own key management. This resource requires the requesting Service Account or API Key to have the Project Owner role.

**LIMITED TO M10 OR GREATER:** MongoDB Cloud limits this feature to dedicated cluster tiers of M10 and greater.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.encryption_at_rest_using_customer_key_management.get_encryption_at_rest(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encryption_at_rest_using_customer_key_management.<a href="src/atlas_sdk/encryption_at_rest_using_customer_key_management/client.py">update_encryption_at_rest</a>(...) -> EncryptionAtRest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration for encryption at rest using the keys you manage through your cloud provider. MongoDB Cloud encrypts all storage even if you don't use your own key management. This resource requires the requesting Service Account or API Key to have the Project Owner role. This feature isn't available for `M0` free clusters, `M2`, `M5`, or serverless clusters.

 After you configure at least one Encryption at Rest using a Customer Key Management provider for the MongoDB Cloud project, Project Owners can enable Encryption at Rest using Customer Key Management for each MongoDB Cloud cluster for which they require encryption. The Encryption at Rest using Customer Key Management provider doesn't have to match the cluster cloud service provider. MongoDB Cloud doesn't automatically rotate user-managed encryption keys. Defer to your preferred Encryption at Rest using Customer Key Management provider's documentation and guidance for best practices on key rotation. MongoDB Cloud automatically creates a 90-day key rotation alert when you configure Encryption at Rest using Customer Key Management using your Key Management in an MongoDB Cloud project. MongoDB Cloud encrypts all storage whether or not you use your own key management.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.encryption_at_rest_using_customer_key_management.update_encryption_at_rest(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EncryptionAtRest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encryption_at_rest_using_customer_key_management.<a href="src/atlas_sdk/encryption_at_rest_using_customer_key_management/client.py">list_rest_private_endpoints</a>(...) -> PaginatedApiAtlasEarPrivateEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the private endpoints of the specified cloud provider for encryption at rest using customer key management.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.encryption_at_rest_using_customer_key_management.list_rest_private_endpoints(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider for the private endpoints to return.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encryption_at_rest_using_customer_key_management.<a href="src/atlas_sdk/encryption_at_rest_using_customer_key_management/client.py">create_rest_private_endpoint</a>(...) -> EarPrivateEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a private endpoint in the specified region for encryption at rest using customer key management.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.encryption_at_rest_using_customer_key_management.create_rest_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider_="cloudProvider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider for the private endpoint to create.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EarPrivateEndpoint` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encryption_at_rest_using_customer_key_management.<a href="src/atlas_sdk/encryption_at_rest_using_customer_key_management/client.py">get_rest_private_endpoint</a>(...) -> EarPrivateEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one private endpoint, identified by its ID, for encryption at rest using Customer Key Management.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.encryption_at_rest_using_customer_key_management.get_rest_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider of the private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encryption_at_rest_using_customer_key_management.<a href="src/atlas_sdk/encryption_at_rest_using_customer_key_management/client.py">request_private_endpoint_deletion</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one private endpoint, identified by its ID, for encryption at rest using Customer Key Management.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.encryption_at_rest_using_customer_key_management.request_private_endpoint_deletion(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud provider of the private endpoint to delete.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flex Clusters
<details><summary><code>client.flex_clusters.<a href="src/atlas_sdk/flex_clusters/client.py">list_flex_clusters</a>(...) -> PaginatedFlexClusters20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for all flex clusters in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_clusters.list_flex_clusters(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_clusters.<a href="src/atlas_sdk/flex_clusters/client.py">create_flex_cluster</a>(...) -> FlexClusterDescription20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one flex cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, FlexProviderSettingsCreate20241113
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_clusters.create_flex_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
    provider_settings=FlexProviderSettingsCreate20241113(
        backing_provider_name="backingProviderName",
        region_name="regionName",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the instance.
    
</dd>
</dl>

<dl>
<dd>

**provider_settings:** `FlexProviderSettingsCreate20241113` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[ResourceTag]]` — List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the instance.
    
</dd>
</dl>

<dl>
<dd>

**termination_protection_enabled:** `typing.Optional[bool]` — Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_clusters.<a href="src/atlas_sdk/flex_clusters/client.py">get_flex_cluster</a>(...) -> FlexClusterDescription20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for one flex cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_clusters.get_flex_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_clusters.<a href="src/atlas_sdk/flex_clusters/client.py">delete_flex_cluster</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one flex cluster from the specified project. The flex cluster must have termination protection disabled in order to be deleted. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_clusters.delete_flex_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_clusters.<a href="src/atlas_sdk/flex_clusters/client.py">update_flex_cluster</a>(...) -> FlexClusterDescription20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one flex cluster in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_clusters.update_flex_cluster(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[ResourceTag]]` — List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the instance.
    
</dd>
</dl>

<dl>
<dd>

**termination_protection_enabled:** `typing.Optional[bool]` — Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_clusters.<a href="src/atlas_sdk/flex_clusters/client.py">tenant_upgrade</a>(...) -> FlexClusterDescription20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrades a flex cluster to a dedicated cluster (M10+) in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Cluster Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_clusters.tenant_upgrade(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the cluster.
    
</dd>
</dl>

<dl>
<dd>

**accept_data_risks_and_force_replica_set_reconfig:** `typing.Optional[datetime.datetime]` — If reconfiguration is necessary to regain a primary due to a regional outage, submit this field alongside your topology reconfiguration to request a new regional outage resistant topology. Forced reconfigurations during an outage of the majority of electable nodes carry a risk of data loss if replicated writes (even majority committed writes) have not been replicated to the new primary node. MongoDB Atlas docs contain more information. To proceed with an operation which carries that risk, set `acceptDataRisksAndForceReplicaSetReconfig` to the current date. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**advanced_configuration:** `typing.Optional[ApiAtlasClusterAdvancedConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**backup_enabled:** `typing.Optional[bool]` — Flag that indicates whether the cluster can perform backups. If set to `true`, the cluster can perform backups. You must set this value to `true` for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and [Shared Cluster Backups](https://docs.atlas.mongodb.com/backup/shared-tier/overview/) for tenant clusters. If set to `false`, the cluster doesn't use backups.
    
</dd>
</dl>

<dl>
<dd>

**bi_connector:** `typing.Optional[BiConnector]` 
    
</dd>
</dl>

<dl>
<dd>

**cluster_type:** `typing.Optional[str]` — Configuration of nodes that comprise the cluster.
    
</dd>
</dl>

<dl>
<dd>

**config_server_management_mode:** `typing.Optional[str]` — Config Server Management Mode for creating or updating a sharded cluster. When configured as `ATLAS_MANAGED`, Atlas may automatically switch the cluster's config server type for optimal performance and savings. When configured as `FIXED_TO_DEDICATED`, the cluster will always use a dedicated config server.
    
</dd>
</dl>

<dl>
<dd>

**disk_warming_mode:** `typing.Optional[str]` — Disk warming mode selection.
    
</dd>
</dl>

<dl>
<dd>

**encryption_at_rest_provider:** `typing.Optional[str]` — Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster `replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize` setting must be `M10` or higher and `"backupEnabled" : false` or omitted entirely.
    
</dd>
</dl>

<dl>
<dd>

**global_cluster_self_managed_sharding:** `typing.Optional[bool]` 

Set this field to configure the Sharding Management Mode when creating a new Global Cluster.

When set to false, the management mode is set to Atlas-Managed Sharding. This mode fully manages the sharding of your Global Cluster and is built to provide a seamless deployment experience.

When set to true, the management mode is set to Self-Managed Sharding. This mode leaves the management of shards in your hands and is built to provide an advanced and flexible deployment experience.

This setting cannot be changed once the cluster is deployed.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.List[ComponentLabel]]` 

Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.

Cluster labels are deprecated and will be removed in a future release. We strongly recommend that you use Resource Tags instead.
    
</dd>
</dl>

<dl>
<dd>

**mongo_db_employee_access_grant:** `typing.Optional[EmployeeAccessGrant]` 
    
</dd>
</dl>

<dl>
<dd>

**mongo_db_major_version:** `typing.Optional[str]` 

MongoDB major version of the cluster. Set to the binary major version. 

On creation: Choose from the available versions of MongoDB, or leave unspecified for the current recommended default in the MongoDB Cloud platform. The recommended version is a recent Long Term Support version. The default is not guaranteed to be the most recently released version throughout the entire release cycle. For versions available in a specific project, see the linked documentation or use the API endpoint for [project LTS versions endpoint](#tag/Projects/operation/getProjectLtsVersions).

 On update: Increase version only by 1 major version at a time. If the cluster is pinned to a MongoDB feature compatibility version exactly one major version below the current MongoDB version, the MongoDB version can be downgraded to the previous major version.
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Flag that indicates whether the cluster is paused.
    
</dd>
</dl>

<dl>
<dd>

**pit_enabled:** `typing.Optional[bool]` — Flag that indicates whether the cluster uses continuous cloud backups.
    
</dd>
</dl>

<dl>
<dd>

**redact_client_log_data:** `typing.Optional[bool]` 

Enable or disable log redaction.

This setting configures the ``mongod`` or ``mongos`` to redact any document field contents from a message accompanying a given log event before logging. This prevents the program from writing potentially sensitive data stored on the database to the diagnostic log. Metadata such as error or operation codes, line numbers, and source file names are still visible in the logs.

Use ``redactClientLogData`` in conjunction with Encryption at Rest and TLS/SSL (Transport Encryption) to assist compliance with regulatory requirements.

*Note*: changing this setting on a cluster will trigger a rolling restart as soon as the cluster is updated.
    
</dd>
</dl>

<dl>
<dd>

**replica_set_scaling_strategy:** `typing.Optional[str]` 

Set this field to configure the replica set scaling mode for your cluster.

By default, Atlas scales under `WORKLOAD_TYPE`. This mode allows Atlas to scale your analytics nodes in parallel to your operational nodes.

When configured as `SEQUENTIAL`, Atlas scales all nodes sequentially. This mode is intended for steady-state workloads and applications performing latency-sensitive secondary reads.

When configured as `NODE_TYPE`, Atlas scales your electable nodes in parallel with your read-only and analytics nodes. This mode is intended for large, dynamic workloads requiring frequent and timely cluster tier scaling. This is the fastest scaling strategy, but it might impact latency of workloads when performing extensive secondary reads.
    
</dd>
</dl>

<dl>
<dd>

**replication_specs:** `typing.Optional[typing.List[ReplicationSpec20240805]]` — List of settings that configure your cluster regions. This array has one object per shard representing node configurations in each shard. For replica sets there is only one object representing node configurations.
    
</dd>
</dl>

<dl>
<dd>

**retain_backups:** `typing.Optional[bool]` — Flag that indicates whether the cluster retains backups.
    
</dd>
</dl>

<dl>
<dd>

**root_cert_type:** `typing.Optional[str]` — Root Certificate Authority that MongoDB Atlas cluster uses. MongoDB Cloud supports Internet Security Research Group.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[ResourceTag]]` — List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster.
    
</dd>
</dl>

<dl>
<dd>

**termination_protection_enabled:** `typing.Optional[bool]` — Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.
    
</dd>
</dl>

<dl>
<dd>

**use_aws_time_based_snapshot_copy_for_fast_initial_sync:** `typing.Optional[bool]` — Flag that indicates whether AWS time-based snapshot copies will be used instead of slower standard snapshot copies during fast Atlas cross-region initial syncs. This flag is only relevant for clusters containing AWS nodes.
    
</dd>
</dl>

<dl>
<dd>

**version_release_system:** `typing.Optional[str]` — Method by which the cluster maintains the MongoDB versions. If value is `CONTINUOUS`, you must not specify `mongoDBMajorVersion`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flex Snapshots
<details><summary><code>client.flex_snapshots.<a href="src/atlas_sdk/flex_snapshots/client.py">download_flex_backup</a>(...) -> FlexBackupRestoreJob20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests one snapshot for the specified flex cluster. This resource returns a `snapshotURL` that you can use to download the snapshot. This `snapshotURL` remains active for four hours after you make the request. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Backup Export Operator role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_snapshots.download_flex_backup(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
    snapshot_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the snapshot to download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_snapshots.<a href="src/atlas_sdk/flex_snapshots/client.py">list_flex_backup_snapshots</a>(...) -> PaginatedApiAtlasFlexBackupSnapshot20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all snapshots of one flex cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_snapshots.list_flex_backup_snapshots(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_snapshots.<a href="src/atlas_sdk/flex_snapshots/client.py">get_flex_backup_snapshot</a>(...) -> FlexBackupSnapshot20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one snapshot of one flex cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_snapshots.get_flex_backup_snapshot(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
    snapshot_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the desired snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flex Restore Jobs
<details><summary><code>client.flex_restore_jobs.<a href="src/atlas_sdk/flex_restore_jobs/client.py">list_flex_restore_jobs</a>(...) -> PaginatedApiAtlasFlexBackupRestoreJob20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all restore jobs for one flex cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_restore_jobs.list_flex_restore_jobs(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_restore_jobs.<a href="src/atlas_sdk/flex_restore_jobs/client.py">create_flex_restore_job</a>(...) -> FlexBackupRestoreJob20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores one snapshot of one flex cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Backup Recovery Operator role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_restore_jobs.create_flex_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
    snapshot_id="32b6e34b3d91647abb20e7b8",
    target_deployment_item_name="targetDeploymentItemName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster whose snapshot you want to restore.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal digit string that identifies the snapshot to restore.
    
</dd>
</dl>

<dl>
<dd>

**target_deployment_item_name:** `str` — Human-readable label that identifies the instance or cluster on the target project to which you want to restore the snapshot. You can restore the snapshot to another flex cluster or dedicated cluster tier.
    
</dd>
</dl>

<dl>
<dd>

**target_project_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the project that contains the instance or cluster to which you want to restore the snapshot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flex_restore_jobs.<a href="src/atlas_sdk/flex_restore_jobs/client.py">get_flex_restore_job</a>(...) -> FlexBackupRestoreJob20241113</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one restore job for one flex cluster from the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.flex_restore_jobs.get_flex_restore_job(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
    restore_job_id="restoreJobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the flex cluster.
    
</dd>
</dl>

<dl>
<dd>

**restore_job_id:** `str` — Unique 24-hexadecimal digit string that identifies the restore job to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Third-Party Integrations
<details><summary><code>client.third_party_integrations.<a href="src/atlas_sdk/third_party_integrations/client.py">list_group_integrations</a>(...) -> PaginatedIntegration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the settings that permit integrations with all configured third-party services. These settings apply to all databases managed in one MongoDB Cloud project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.third_party_integrations.list_group_integrations(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_integrations.<a href="src/atlas_sdk/third_party_integrations/client.py">get_group_integration</a>(...) -> ThirdPartyIntegration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the settings for configuring integration with one third-party service. These settings apply to all databases managed in one MongoDB Cloud project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.third_party_integrations.get_group_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    integration_type="integrationType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `str` — Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_integrations.<a href="src/atlas_sdk/third_party_integrations/client.py">create_group_integration</a>(...) -> PaginatedIntegration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds the settings for configuring one third-party service integration. These settings apply to all databases managed in the specified MongoDB Cloud project. Each project can have only one configuration per `{INTEGRATION-TYPE}`. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.third_party_integrations.create_group_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    integration_type="integrationType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `str` — Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ThirdPartyIntegration` 
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_integrations.<a href="src/atlas_sdk/third_party_integrations/client.py">update_group_integration</a>(...) -> PaginatedIntegration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the settings for configuring integration with one third-party service. These settings apply to all databases managed in one MongoDB Cloud project. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.third_party_integrations.update_group_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    integration_type="integrationType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `str` — Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ThirdPartyIntegration` 
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_integrations.<a href="src/atlas_sdk/third_party_integrations/client.py">delete_group_integration</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the settings that permit configuring one third-party service integration. These settings apply to all databases managed in one MongoDB Cloud project. If you delete an integration from a project, you remove that integration configuration only for that project. This action doesn't affect any other project or organization's configured `{INTEGRATION-TYPE}` integrations. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.third_party_integrations.delete_group_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    integration_type="integrationType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `str` — Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cloud Migration Service
<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">create_group_live_migration</a>(...) -> LiveMigrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrate one cluster that Cloud or Ops Manager manages to MongoDB Atlas.

 Please make sure to validate your migration before initiating it.

 You can use this API endpoint for push live migrations only. Your API Key must have the Organization Owner role to successfully call this resource.

 **NOTE**: Migrating time-series collections is not yet supported on MongoDB 6.0 or higher. Migrations on MongoDB 6.0 or higher will skip any time-series collections on the source cluster. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, Destination, Source
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.create_group_live_migration(
    group_id="32b6e34b3d91647abb20e7b8",
    destination=Destination(
        cluster_name="clusterName",
        group_id="32b6e34b3d91647abb20e7b8",
        hostname_schema_type="hostnameSchemaType",
    ),
    migration_hosts=[
        "vm001.example.com"
    ],
    source=Source(
        cluster_name="clusterName",
        group_id="32b6e34b3d91647abb20e7b8",
        managed_authentication=True,
        ssl=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `LiveMigrationRequest20240530` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">get_group_live_migration</a>(...) -> LiveMigrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return details of one cluster migration job. Each push live migration job uses one migration host. Your API Key must have the Organization Member role to successfully call this resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.get_group_live_migration(
    group_id="32b6e34b3d91647abb20e7b8",
    live_migration_id="6296fb4c7c7aa997cf94e9a8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**live_migration_id:** `str` — Unique 24-hexadecimal digit string that identifies the migration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">cutover_migration</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cut over the migrated cluster to MongoDB Atlas. Confirm when the cut over completes. When the cut over completes, MongoDB Atlas completes the live migration process and stops synchronizing with the source cluster. Your API Key must have the Organization Owner role to successfully call this resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.cutover_migration(
    group_id="32b6e34b3d91647abb20e7b8",
    live_migration_id="6296fb4c7c7aa997cf94e9a8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**live_migration_id:** `str` — Unique 24-hexadecimal digit string that identifies the migration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">validate_live_migrations</a>(...) -> LiveImportValidation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies whether the provided credentials, available disk space, MongoDB versions, and so on meet the requirements of the migration request. If the check passes, the migration can proceed. Your API Key must have the Organization Owner role to successfully call this resource. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, Destination, Source
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.validate_live_migrations(
    group_id="32b6e34b3d91647abb20e7b8",
    destination=Destination(
        cluster_name="clusterName",
        group_id="32b6e34b3d91647abb20e7b8",
        hostname_schema_type="hostnameSchemaType",
    ),
    migration_hosts=[
        "vm001.example.com"
    ],
    source=Source(
        cluster_name="clusterName",
        group_id="32b6e34b3d91647abb20e7b8",
        managed_authentication=True,
        ssl=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `LiveMigrationRequest20240530` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">get_migration_validate_status</a>(...) -> LiveImportValidation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the status of one migration validation job. Your API Key must have the Organization Owner role to successfully call this resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.get_migration_validate_status(
    group_id="32b6e34b3d91647abb20e7b8",
    validation_id="507f1f77bcf86cd799439011",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**validation_id:** `str` — Unique 24-hexadecimal digit string that identifies the validation job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">list_available_projects</a>(...) -> typing.List[LiveImportAvailableProject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all projects that you can migrate to the specified organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.list_available_projects(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">create_link_token</a>(...) -> TargetOrg</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one link-token that contains all the information required to complete the link. MongoDB Atlas uses the link-token for push live migrations only. Live migration (push) allows you to securely push data from Cloud Manager or Ops Manager into MongoDB Atlas. Your API Key must have the Organization Owner role to successfully call this resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.create_link_token(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**access_list_ips:** `typing.Optional[typing.List[str]]` — IP address access list entries associated with the API key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_migration_service.<a href="src/atlas_sdk/cloud_migration_service/client.py">delete_link_tokens</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one organization link and its associated public API key. MongoDB Atlas uses the link-token for push live migrations only. Live migrations (push) let you securely push data from Cloud Manager or Ops Manager into MongoDB Atlas. Your API Key must have the Organization Owner role to successfully call this resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.cloud_migration_service.delete_link_tokens(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Push-Based Log Export
<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">list_group_log_integrations</a>(...) -> PaginatedLogIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all log integration configurations for the project. Optionally filter by integration type. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.list_group_log_integrations(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `typing.Optional[str]` — Optional filter by integration type (e.g., `S3_LOG_EXPORT`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">create_group_log_integration</a>(...) -> LogIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new log integration configuration identified by a unique ID. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.create_group_log_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    log_types=[
        "MONGOD",
        "MONGOS"
    ],
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `LogIntegrationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">get_group_log_integration</a>(...) -> LogIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the configuration for one log integration identified by its unique ID. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.get_group_log_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique identifier of the log integration configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">update_group_log_integration</a>(...) -> LogIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration for one log integration identified by its unique ID. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.update_group_log_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    id="id",
    log_types=[
        "MONGOD",
        "MONGOS"
    ],
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique identifier of the log integration configuration.
    
</dd>
</dl>

<dl>
<dd>

**request:** `LogIntegrationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">delete_group_log_integration</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the configuration for one log integration identified by its unique ID. To use this resource, the requesting Service Account or API Key must have the Organization Owner or Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.delete_group_log_integration(
    group_id="32b6e34b3d91647abb20e7b8",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique identifier of the log integration configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">get_log_export</a>(...) -> PushBasedLogExportProject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches the current project level settings for the push-based log export feature.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.get_log_export(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">create_log_export</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configures the project level settings for the push-based log export feature.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.create_log_export(
    group_id="32b6e34b3d91647abb20e7b8",
    bucket_name="bucketName",
    iam_role_id="32b6e34b3d91647abb20e7b8",
    prefix_path="prefixPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**bucket_name:** `str` — The name of the bucket to which the agent will send the logs to.
    
</dd>
</dl>

<dl>
<dd>

**iam_role_id:** `str` — ID of the AWS IAM role that will be used to write to the S3 bucket.
    
</dd>
</dl>

<dl>
<dd>

**prefix_path:** `str` — S3 directory in which vector will write to in order to store the logs. An empty string denotes the root directory.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">delete_log_export</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the push-based log export feature by resetting the project level settings to its default configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.delete_log_export(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.push_based_log_export.<a href="src/atlas_sdk/push_based_log_export/client.py">update_log_export</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the project level settings for the push-based log export feature.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.push_based_log_export.update_log_export(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PushBasedLogExportProject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Maintenance Windows
<details><summary><code>client.maintenance_windows.<a href="src/atlas_sdk/maintenance_windows/client.py">get_maintenance_window</a>(...) -> GroupMaintenanceWindow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the maintenance window for the specified project. MongoDB Cloud starts those maintenance activities when needed. You can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.maintenance_windows.get_maintenance_window(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance_windows.<a href="src/atlas_sdk/maintenance_windows/client.py">reset_maintenance_window</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets the maintenance window for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. Urgent maintenance activities such as security patches can't wait for your chosen window. MongoDB Cloud starts those maintenance activities when needed. After you schedule maintenance for your cluster, you can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.maintenance_windows.reset_maintenance_window(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance_windows.<a href="src/atlas_sdk/maintenance_windows/client.py">update_maintenance_window</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the maintenance window for the specified project. Urgent maintenance activities such as security patches can't wait for your chosen window. MongoDB Cloud starts those maintenance activities when needed. After you schedule maintenance for your cluster, you can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time. Updating the maintenance window will reset any maintenance deferrals for this project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.maintenance_windows.update_maintenance_window(
    group_id="32b6e34b3d91647abb20e7b8",
    day_of_week=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GroupMaintenanceWindow` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance_windows.<a href="src/atlas_sdk/maintenance_windows/client.py">toggle_maintenance_auto_defer</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Toggles automatic deferral of the maintenance window for the specified project. When automatic deferral is enabled, all maintenance windows are deferred for one week. This endpoint controls the same underlying feature as the `autoDeferOnceEnabled` field in the PATCH `/maintenanceWindow` endpoint. The difference is that this endpoint toggles the current value (switches from enabled to disabled or vice versa), while the `autoDeferOnceEnabled` field allows you to set a specific value. For most use cases, the PATCH endpoint with `autoDeferOnceEnabled` is recommended because it allows setting an explicit value rather than toggling. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.maintenance_windows.toggle_maintenance_auto_defer(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance_windows.<a href="src/atlas_sdk/maintenance_windows/client.py">defer_maintenance_window</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Defers the maintenance window for the specified project. Urgent maintenance activities such as security patches can't wait for your chosen window. MongoDB Cloud starts those maintenance activities when needed. After you schedule maintenance for your cluster, you can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.maintenance_windows.defer_maintenance_window(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Lake Pipelines
<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">list_pipelines</a>(...) -> typing.List[DataLakeIngestionPipeline]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Data Lake Pipelines. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.list_pipelines(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">create_pipeline</a>(...) -> DataLakeIngestionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one Data Lake Pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.create_pipeline(
    group_id_="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataLakeIngestionPipeline` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">get_pipeline</a>(...) -> DataLakeIngestionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one Data Lake Pipeline within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.get_pipeline(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">delete_pipeline</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one Data Lake Pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.delete_pipeline(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">update_pipeline</a>(...) -> DataLakeIngestionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one Data Lake Pipeline.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.update_pipeline(
    group_id_="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DataLakeIngestionPipeline` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">get_available_pipeline_schedules</a>(...) -> typing.List[DiskBackupApiPolicyItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of backup schedule policy items that you can use as a Data Lake Pipeline source. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.get_available_pipeline_schedules(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">get_available_pipeline_snapshots</a>(...) -> PaginatedBackupSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of backup snapshots that you can use to trigger an on demand pipeline run. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.get_available_pipeline_snapshots(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**completed_after:** `typing.Optional[datetime.datetime]` — Date and time after which MongoDB Cloud created the snapshot. If specified, MongoDB Cloud returns available backup snapshots created after this time and date only. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">pause_pipeline</a>(...) -> DataLakeIngestionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pauses ingestion for a Data Lake Pipeline within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.pause_pipeline(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">resume_pipeline</a>(...) -> DataLakeIngestionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resumes ingestion for a Data Lake Pipeline within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.resume_pipeline(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">list_pipeline_runs</a>(...) -> PaginatedPipelineRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of past Data Lake Pipeline runs. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.list_pipeline_runs(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — If specified, Atlas returns only Data Lake Pipeline runs initiated before this time and date.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">get_pipeline_run</a>(...) -> IngestionPipelineRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one Data Lake Pipeline run within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.get_pipeline_run(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
    pipeline_run_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_run_id:** `str` — Unique 24-hexadecimal character string that identifies a Data Lake Pipeline run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">delete_pipeline_run</a>(...) -> RequestAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes dataset that Atlas generated during the specified pipeline run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.delete_pipeline_run(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
    pipeline_run_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_run_id:** `str` — Unique 24-hexadecimal character string that identifies a Data Lake Pipeline run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_lake_pipelines.<a href="src/atlas_sdk/data_lake_pipelines/client.py">trigger_pipeline</a>(...) -> IngestionPipelineRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers a Data Lake Pipeline ingestion of a specified snapshot.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.data_lake_pipelines.trigger_pipeline(
    group_id="32b6e34b3d91647abb20e7b8",
    pipeline_name="pipelineName",
    snapshot_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_name:** `str` — Human-readable label that identifies the Data Lake Pipeline.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `str` — Unique 24-hexadecimal character string that identifies the snapshot.
    
</dd>
</dl>

<dl>
<dd>

**dataset_retention_policy:** `typing.Optional[DatasetRetentionPolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Private Endpoint Services
<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">list_private_endpoint_service</a>(...) -> typing.List[EndpointService]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the name, interfaces, and state of all private endpoint services for the specified cloud service provider. This cloud service provider manages the private endpoint service for the project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.list_private_endpoint_service(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Cloud service provider that manages this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">get_private_endpoint_service</a>(...) -> EndpointService</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the name, interfaces, and state of the specified private endpoint service from one project. The cloud service provider hosted this private endpoint service that belongs to the project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.get_private_endpoint_service(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_service_id="endpointServiceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Cloud service provider that manages this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_service_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint service that you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">delete_private_endpoint_service</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one private endpoint service from the specified project. This cloud service provider manages the private endpoint service that belongs to the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.delete_private_endpoint_service(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_service_id="endpointServiceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Cloud service provider that manages this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_service_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint service that you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">create_private_endpoint</a>(...) -> PrivateLinkEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one private endpoint for the specified cloud service provider. This cloud service provider manages the private endpoint service, which in turn manages the private endpoints for the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role. To learn more about considerations, limitations, and prerequisites, see the MongoDB documentation for setting up a private endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.create_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_service_id="endpointServiceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Cloud service provider that manages this private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_service_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint service for which you want to create a private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique string that identifies the private endpoint's network interface that someone added to this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**private_endpoint_ip_address:** `typing.Optional[str]` — IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_group_name:** `typing.Optional[str]` — Human-readable label that identifies a set of endpoints. If this private endpoint belongs to a port-mapped endpoint service, this field is still required but ignored.
    
</dd>
</dl>

<dl>
<dd>

**endpoints:** `typing.Optional[typing.List[CreateGcpForwardingRuleRequest]]` — List of individual private endpoints that comprise this endpoint group. If this endpoint belongs to a port-mapped endpoint service, this field will only take in a list of one private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**gcp_project_id:** `typing.Optional[str]` — Unique string that identifies the Google Cloud project in which you created the endpoints.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">get_private_endpoint</a>(...) -> PrivateLinkEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the connection state of the specified private endpoint. The private endpoint service manages this private endpoint which belongs to one project hosted from one cloud service provider. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.get_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_service_id="endpointServiceId",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Cloud service provider that manages this private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_service_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint service for which you want to return a private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique string that identifies the private endpoint you want to return. The format of the `endpointId` parameter differs for AWS and Azure. You must URL encode the `endpointId` for Azure private endpoints.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">delete_private_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one private endpoint from the specified project and private endpoint service, as managed by the specified cloud service provider. When the last private endpoint is removed from a given private endpoint service, that private endpoint service is also removed. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.delete_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    endpoint_service_id="endpointServiceId",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Cloud service provider that manages this private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_service_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint service from which you want to delete a private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique string that identifies the private endpoint you want to delete. The format of the `endpointId` parameter differs for AWS and Azure. You must URL encode the `endpointId` for Azure private endpoints.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">create_private_endpoint_service</a>(...) -> EndpointService</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one private endpoint service for the specified cloud service provider. This cloud service provider manages the private endpoint service for the project. When you create a private endpoint service, MongoDB Cloud creates a network container in the project for the cloud provider for which you create the private endpoint service if one doesn't already exist. To learn more about private endpoint terminology in MongoDB Cloud, see Private Endpoint Concepts. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.create_private_endpoint_service(
    group_id="32b6e34b3d91647abb20e7b8",
    provider_name="providerName",
    region="region",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `str` — Human-readable label that identifies the cloud service provider for which you want to create the private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` — Cloud provider region in which you want to create the private endpoint service. Regions accepted as values differ for [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/), [Google Cloud Platform](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Microsoft Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).
    
</dd>
</dl>

<dl>
<dd>

**port_mapping_enabled:** `typing.Optional[bool]` — Flag that indicates whether this endpoint service uses PSC port-mapping. This is only applicable for GCP Private Endpoint Services.
    
</dd>
</dl>

<dl>
<dd>

**supported_remote_regions:** `typing.Optional[typing.List[str]]` — List of regions that the endpoint service supports. Native cross region support is implemented for AWS only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">update_private_endpoint_service</a>(...) -> EndpointService</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified private endpoint service for the project. The cloud service provider manages the private endpoint service that belongs to the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.update_private_endpoint_service(
    group_id="32b6e34b3d91647abb20e7b8",
    endpoint_service_id="endpointServiceId",
    cloud_provider="cloudProvider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_service_id:** `str` — Unique 24-hexadecimal digit string that identifies the private endpoint service that you want to update.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — Human-readable label that identifies the cloud service provider for the private endpoint service which you want to update.
    
</dd>
</dl>

<dl>
<dd>

**supported_remote_regions:** `typing.Optional[typing.List[str]]` — List of regions that the endpoint service supports. Native cross region support is implemented for AWS only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">get_regional_endpoint_mode</a>(...) -> ProjectSettingItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks whether each region in the specified cloud service provider can create multiple private endpoints per region. The cloud service provider manages the private endpoint for the project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.get_regional_endpoint_mode(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.private_endpoint_services.<a href="src/atlas_sdk/private_endpoint_services/client.py">toggle_regional_endpoint_mode</a>(...) -> ProjectSettingItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables or disables the ability to create multiple private endpoints per region in all cloud service providers in one project. The cloud service provider manages the private endpoints for the project. Connection strings to existing multi-region and global sharded clusters change when you enable this setting. You must update your applications to use the new connection strings. This might cause downtime. To use this resource, the requesting Service Account or API Key must have the Project Owner role and all clusters in the deployment must be sharded clusters. Once enabled, you cannot create replica sets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.private_endpoint_services.toggle_regional_endpoint_mode(
    group_id="32b6e34b3d91647abb20e7b8",
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ProjectSettingItem` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Serverless Private Endpoints
<details><summary><code>client.serverless_private_endpoints.<a href="src/atlas_sdk/serverless_private_endpoints/client.py">list_serverless_private_endpoint</a>(...) -> typing.List[ServerlessTenantEndpoint]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all private endpoints for one serverless instance. You must have at least the Project Read Only role for the project to successfully call this resource.

This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_private_endpoints.list_serverless_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    instance_name="instanceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**instance_name:** `str` — Human-readable label that identifies the serverless instance associated with the tenant endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.serverless_private_endpoints.<a href="src/atlas_sdk/serverless_private_endpoints/client.py">create_serverless_private_endpoint</a>(...) -> ServerlessTenantEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one private endpoint for one serverless instance. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

 A new endpoint won't be immediately available after creation.  Read the steps in the linked tutorial for detailed guidance.

This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_private_endpoints.create_serverless_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    instance_name="instanceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**instance_name:** `str` — Human-readable label that identifies the serverless instance for which the tenant endpoint will be created.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Human-readable comment associated with the private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.serverless_private_endpoints.<a href="src/atlas_sdk/serverless_private_endpoints/client.py">get_serverless_private_endpoint</a>(...) -> ServerlessTenantEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return one private endpoint for one serverless instance. Identify this endpoint using its unique ID. You must have at least the Project Read Only role for the project to successfully call this resource.

This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_private_endpoints.get_serverless_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    instance_name="instanceName",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**instance_name:** `str` — Human-readable label that identifies the serverless instance associated with the tenant endpoint.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the tenant endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.serverless_private_endpoints.<a href="src/atlas_sdk/serverless_private_endpoints/client.py">delete_serverless_private_endpoint</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one private endpoint from one serverless instance. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_private_endpoints.delete_serverless_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    instance_name="instanceName",
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**instance_name:** `str` — Human-readable label that identifies the serverless instance from which the tenant endpoint will be removed.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the tenant endpoint which will be removed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.serverless_private_endpoints.<a href="src/atlas_sdk/serverless_private_endpoints/client.py">update_serverless_private_endpoint</a>(...) -> ServerlessTenantEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one private endpoint for one serverless instance. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_private_endpoints.update_serverless_private_endpoint(
    group_id="32b6e34b3d91647abb20e7b8",
    instance_name="instanceName",
    endpoint_id="endpointId",
    provider_name="providerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**instance_name:** `str` — Human-readable label that identifies the serverless instance associated with the tenant endpoint that will be updated.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` — Unique 24-hexadecimal digit string that identifies the tenant endpoint which will be updated.
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `str` — Human-readable label that identifies the cloud provider of the tenant endpoint.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Human-readable comment associated with the private endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider_endpoint_id:** `typing.Optional[str]` — Unique string that identifies the Azure private endpoint's network interface for this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**private_endpoint_ip_address:** `typing.Optional[str]` — IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Serverless Instances
<details><summary><code>client.serverless_instances.<a href="src/atlas_sdk/serverless_instances/client.py">list_serverless_instances</a>(...) -> PaginatedServerlessInstanceDescription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for all serverless instances in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This endpoint also lists Flex clusters that were created using the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or former Serverless instances that have been migrated to Flex clusters, until January 15, 2026 after which this endpoint will begin returning an empty list. The endpoint will be removed entirely on January 15, 2027. Continuous backups are not supported and `serverlessContinuousBackupEnabled` will not take effect on these clusters. Please use the List Flex Clusters endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_instances.list_serverless_instances(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.serverless_instances.<a href="src/atlas_sdk/serverless_instances/client.py">get_serverless_instance</a>(...) -> ServerlessInstanceDescription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for one serverless instance in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

This API can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or Flex clusters that were migrated from Serverless instances. Continuous backups are not supported and `serverlessContinuousBackupEnabled` will not take effect on these clusters. This endpoint will be sunset on January 15, 2027. Please use the Get Flex Cluster endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.serverless_instances.get_serverless_instance(
    group_id="32b6e34b3d91647abb20e7b8",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the serverless instance.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Service Accounts
<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">list_group_service_accounts</a>(...) -> PaginatedGroupServiceAccounts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Service Accounts for the specified Project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.list_group_service_accounts(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">create_group_service_account</a>(...) -> GroupServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one Service Account for the specified Project. The Service Account will automatically be added as an Organization Member to the Organization that the specified Project is a part of.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.create_group_service_account(
    group_id="32b6e34b3d91647abb20e7b8",
    description="description",
    name="name",
    roles=[
        "roles"
    ],
    secret_expires_after_hours=8,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Human readable description for the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for the Service Account. The name is modifiable and does not have to be unique.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — A list of project-level roles for the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**secret_expires_after_hours:** `int` — The expiration time of the new Service Account secret, provided in hours. The minimum and maximum allowed expiration times are subject to change and are controlled by the organization's settings.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">get_group_service_account</a>(...) -> GroupServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Service Account in the specified Project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.get_group_service_account(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">delete_group_service_account</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified Service Account from the specified project. The Service Account will still be a part of the Organization it was created in, and the credentials will remain active until expired or manually revoked.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.delete_group_service_account(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">update_group_service_account</a>(...) -> GroupServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one Service Account in the specified Project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.update_group_service_account(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Human readable description for the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable name for the Service Account. The name is modifiable and does not have to be unique.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — A list of Project roles associated with the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">list_access_list</a>(...) -> PaginatedServiceAccountIpAccessEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all access list entries that you configured for the specified Service Account for the project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.list_access_list(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">create_access_list</a>(...) -> PaginatedServiceAccountIpAccessEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add Access List Entries for the specified Service Account for the project. Resources require all API requests to originate from IP addresses on the API access list. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ServiceAccountIpAccessListEntry
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.create_access_list(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    request=[
        ServiceAccountIpAccessListEntry()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[ServiceAccountIpAccessListEntry]` 
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">delete_group_access_entry</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified access list entry from the specified Service Account for the project. You can't remove the requesting IP address from the access list. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.delete_group_access_entry(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    ip_address="192.0.2.0%2F24",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `str` — One IP address or multiple IP addresses represented as one CIDR block. When specifying a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">create_group_secret</a>(...) -> ServiceAccountSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a secret for the specified Service Account in the specified Project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.create_group_secret(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    secret_expires_after_hours=8,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ServiceAccountSecretRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">delete_group_secret</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified Service Account secret.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.delete_group_secret(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    secret_id="secretId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**secret_id:** `str` — Unique 24-hexadecimal digit string that identifies the secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">invite_group_service_account</a>(...) -> GroupServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns the specified Service Account to the specified Project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.invite_group_service_account(
    group_id="32b6e34b3d91647abb20e7b8",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    roles=[
        "roles"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — The Project permissions for the Service Account in the specified Project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">list_org_service_accounts</a>(...) -> PaginatedOrgServiceAccounts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Service Accounts for the specified Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.list_org_service_accounts(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">create_org_service_account</a>(...) -> OrgServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one Service Account for the specified Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.create_org_service_account(
    org_id="4888442a3354817a7320eb61",
    description="description",
    name="name",
    roles=[
        "roles"
    ],
    secret_expires_after_hours=8,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrgServiceAccountRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">get_org_service_account</a>(...) -> OrgServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified Service Account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.get_org_service_account(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">delete_org_service_account</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified Service Account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.delete_org_service_account(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">update_org_service_account</a>(...) -> OrgServiceAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified Service Account in the specified Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.update_org_service_account(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Human readable description for the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable name for the Service Account. The name is modifiable and does not have to be unique.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — A list of organization-level roles for the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">list_org_access_list</a>(...) -> PaginatedServiceAccountIpAccessEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all access list entries that you configured for the specified Service Account for the organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.list_org_access_list(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">create_org_access_list</a>(...) -> PaginatedServiceAccountIpAccessEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add Access List Entries for the specified Service Account for the organization. Resources require all API requests to originate from IP addresses on the API access list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ServiceAccountIpAccessListEntry
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.create_org_access_list(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    request=[
        ServiceAccountIpAccessListEntry()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[ServiceAccountIpAccessListEntry]` 
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">delete_org_access_entry</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the specified access list entry from the specified Service Account for the organization. You can't remove the requesting IP address from the access list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.delete_org_access_entry(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    ip_address="192.0.2.0%2F24",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `str` — One IP address or multiple IP addresses represented as one CIDR block. When specifying a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">get_service_account_groups</a>(...) -> PaginatedServiceAccountGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all projects the specified Service Account is a part of.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.get_service_account_groups(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">create_org_secret</a>(...) -> ServiceAccountSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a secret for the specified Service Account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.create_org_secret(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    secret_expires_after_hours=8,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ServiceAccountSecretRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_accounts.<a href="src/atlas_sdk/service_accounts/client.py">delete_org_secret</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified Service Account secret.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.service_accounts.delete_org_secret(
    org_id="4888442a3354817a7320eb61",
    client_id="mdb_sa_id_1234567890abcdef12345678",
    secret_id="secretId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The Client ID of the Service Account.
    
</dd>
</dl>

<dl>
<dd>

**secret_id:** `str` — Unique 24-hexadecimal digit string that identifies the secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Streams
<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">list_stream_workspaces</a>(...) -> PaginatedApiStreamsTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all stream workspaces for the specified project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.list_stream_workspaces(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">create_stream_workspace</a>(...) -> StreamsTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one stream workspace in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.create_stream_workspace(
    group_id_="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `StreamsTenant` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">get_stream_workspace</a>(...) -> StreamsTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one stream workspace within the specified project. To use this resource, the requesting Service Account or API Key must have the Project Data Access roles, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.get_stream_workspace(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace to return.
    
</dd>
</dl>

<dl>
<dd>

**include_connections:** `typing.Optional[bool]` — Flag to indicate whether connections information should be included in the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">delete_stream_workspace</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one stream workspace in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.delete_stream_workspace(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">update_stream_workspace</a>(...) -> StreamsTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one stream workspace in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Data Access Admin role, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.update_stream_workspace(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace to update.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `typing.Optional[str]` — Human-readable label that identifies the cloud provider.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[BaseStreamsRegion]` 
    
</dd>
</dl>

<dl>
<dd>

**stream_config:** `typing.Optional[StreamConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">download_audit_logs</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the audit logs for the specified Atlas Streams Processing workspace or stream processor. By default, logs cover periods of 30 days. To use this resource, the requesting Service Account or API Key must have the Project Data Access roles, Project Owner role or Project Stream Processing Owner role. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.download_audit_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — Timestamp that specifies the end point for the range of log messages to download.  MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Timestamp that specifies the starting point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
    
</dd>
</dl>

<dl>
<dd>

**sp_name:** `typing.Optional[str]` — Name of the stream processor to download logs for. An empty string will download logs for all stream processors in the workspace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">list_stream_connections</a>(...) -> PaginatedApiStreamsConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all connections of the stream workspace for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Data Access roles, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.list_stream_connections(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">create_stream_connection</a>(...) -> StreamsConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one connection for a stream workspace in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.create_stream_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**request:** `StreamsConnection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">get_stream_connection</a>(...) -> StreamsConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one stream connection within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.get_stream_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    connection_name="connectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace to return.
    
</dd>
</dl>

<dl>
<dd>

**connection_name:** `str` — Label that identifies the stream connection to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">delete_stream_connection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one connection of the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.delete_stream_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    connection_name="connectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**connection_name:** `str` — Label that identifies the stream connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">update_stream_connection</a>(...) -> StreamsConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one connection for the specified stream workspace in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.update_stream_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    connection_name="connectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**connection_name:** `str` — Label that identifies the stream connection.
    
</dd>
</dl>

<dl>
<dd>

**request:** `StreamsConnection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">create_stream_processor</a>(...) -> StreamsProcessor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.create_stream_processor(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**request:** `StreamsProcessor` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">get_stream_processor</a>(...) -> StreamsProcessorWithStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.get_stream_processor(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    processor_name="processorName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**processor_name:** `str` — Label that identifies the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">delete_stream_processor</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.delete_stream_processor(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    processor_name="processorName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**processor_name:** `str` — Label that identifies the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">update_stream_processor</a>(...) -> StreamsProcessorWithStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify one existing Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.update_stream_processor(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    processor_name="processorName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**processor_name:** `str` — Label that identifies the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name for the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[StreamsModifyStreamProcessorOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**pipeline:** `typing.Optional[typing.List[Document]]` — New pipeline for the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">start_stream_processor</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.start_stream_processor(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    processor_name="processorName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**processor_name:** `str` — Label that identifies the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">start_stream_processor_with</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.start_stream_processor_with(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    processor_name="processorName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**processor_name:** `str` — Label that identifies the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**resume_from_checkpoint:** `typing.Optional[bool]` — When true or not specified, the stream processor resumes from its last checkpoint. When false, the stream processor starts fresh.
    
</dd>
</dl>

<dl>
<dd>

**start_at_operation_time:** `typing.Optional[datetime.datetime]` — The operation time after which the change stream source should begin reporting. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
    
</dd>
</dl>

<dl>
<dd>

**tier:** `typing.Optional[str]` — Selected tier for the Stream Workspace. Configures Memory / VCPU allowances.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">stop_stream_processor</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop a Stream Processor within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.stop_stream_processor(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
    processor_name="processorName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**processor_name:** `str` — Label that identifies the stream processor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">get_stream_processors</a>(...) -> PaginatedApiStreamsStreamProcessorWithStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Stream Processors within the specified stream workspace. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.get_stream_processors(
    group_id="32b6e34b3d91647abb20e7b8",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">download_operational_logs</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the operational logs for the specified Atlas Streams Processing workspace or stream processor. By default, logs cover periods of 30 days. To use this resource, the requesting Service Account or API Key must have the Project Data Access roles, Project Owner role or Project Stream Processing Owner role. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: "Accept: application/vnd.atlas.2025-03-12+gzip".
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.download_operational_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `str` — Label that identifies the stream workspace.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — Timestamp that specifies the end point for the range of log messages to download.  MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Timestamp that specifies the starting point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
    
</dd>
</dl>

<dl>
<dd>

**sp_name:** `typing.Optional[str]` — Name of the stream processor to download logs for. An empty string will download logs for all stream processors in the workspace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">get_account_details</a>(...) -> AccountDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Account ID, and the VPC ID for the group and region specified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.get_account_details(
    group_id="32b6e34b3d91647abb20e7b8",
    cloud_provider="cloudProvider",
    region_name="regionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**cloud_provider:** `str` — One of "aws", "azure" or "gcp".
    
</dd>
</dl>

<dl>
<dd>

**region_name:** `str` — The cloud provider specific region name, i.e. "US_EAST_1" for cloud provider "aws".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">list_active_peering_connections</a>(...) -> PaginatedApiStreamsVpcPeeringConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of active incoming VPC Peering Connections.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.list_active_peering_connections(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">list_private_link_connections</a>(...) -> PaginatedApiStreamsPrivateLink</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Private Link connections for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role, Project Data Access roles, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.list_private_link_connections(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">create_private_link_connection</a>(...) -> StreamsPrivateLinkConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one Private Link in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.create_private_link_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `StreamsPrivateLinkConnection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">get_private_link_connection</a>(...) -> StreamsPrivateLinkConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one Private Link connection within the project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.get_private_link_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Unique ID that identifies the Private Link connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">delete_private_link_connection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one Private Link in the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.delete_private_link_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Unique ID that identifies the Private Link connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">list_vpc_peering_connections</a>(...) -> PaginatedApiStreamsVpcPeeringConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of incoming VPC Peering Connections.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.list_vpc_peering_connections(
    group_id="32b6e34b3d91647abb20e7b8",
    requester_account_id="requesterAccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**requester_account_id:** `str` — The Account ID of the VPC Peering connection/s.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">delete_vpc_peering_connection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an incoming VPC Peering connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.delete_vpc_peering_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The VPC Peering Connection id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">accept_vpc_peering_connection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests the acceptance of an incoming VPC Peering connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.accept_vpc_peering_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The VPC Peering Connection id.
    
</dd>
</dl>

<dl>
<dd>

**requester_account_id:** `typing.Optional[str]` — The AWS requester account ID.
    
</dd>
</dl>

<dl>
<dd>

**requester_vpc_id:** `typing.Optional[str]` — The AWS requester VPC ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">reject_vpc_peering_connection</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests the rejection of an incoming VPC Peering connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.reject_vpc_peering_connection(
    group_id="32b6e34b3d91647abb20e7b8",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The VPC Peering Connection id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.streams.<a href="src/atlas_sdk/streams/client.py">with_stream_sample_connections</a>(...) -> StreamsTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one stream workspace in the specified project with sample connections. To use this resource the requesting Service Account or API Key must have the Project Data Access Admin role, Project Owner role or Project Stream Processing Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.streams.with_stream_sample_connections(
    group_id="32b6e34b3d91647abb20e7b8",
    request={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TenantWithSampleConnections` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Teams
<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">list_group_teams</a>(...) -> PaginatedTeamRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all teams to which the authenticated user has access in the project specified using its unique 24-hexadecimal digit identifier. All members of the team share the same project access. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.list_group_teams(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">add_group_teams</a>(...) -> PaginatedTeamRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds multiple teams to the specified project. All members of a team share the same project access. MongoDB Cloud limits the number of users to a maximum of 100 teams per project and a maximum of 250 teams per organization. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, TeamRole
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.add_group_teams(
    group_id="32b6e34b3d91647abb20e7b8",
    request=[
        TeamRole(
            role_names=[
                "roleNames"
            ],
            team_id="32b6e34b3d91647abb20e7b8",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[TeamRole]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">get_group_team</a>(...) -> TeamRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one team to which the authenticated user has access in the project specified using its unique 24-hexadecimal digit identifier. All members of the team share the same project access. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.get_group_team(
    group_id="32b6e34b3d91647abb20e7b8",
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team for which you want to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">remove_group_team</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one team specified using its unique 24-hexadecimal digit identifier from the project specified using its unique 24-hexadecimal digit identifier. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.remove_group_team(
    group_id="32b6e34b3d91647abb20e7b8",
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team that you want to remove from the specified project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">update_group_team</a>(...) -> PaginatedTeamRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the project roles assigned to the specified team. You can grant team roles for specific projects and grant project access roles to users in the team. All members of the team share the same project access. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.update_group_team(
    group_id="32b6e34b3d91647abb20e7b8",
    team_id_="teamId",
    role_names=[
        "roleNames"
    ],
    team_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team for which you want to update roles.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TeamRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">list_org_teams</a>(...) -> PaginatedTeam</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all teams that belong to the specified organization. Teams enable you to grant project access roles to MongoDB Cloud users. MongoDB Cloud only returns teams for which you have access. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.list_org_teams(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">create_org_team</a>(...) -> Team</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one team in the specified organization. Teams enable you to grant project access roles to MongoDB Cloud users. MongoDB Cloud limits the number of teams to a maximum of 250 teams per organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.create_org_team(
    org_id="4888442a3354817a7320eb61",
    name="name",
    usernames=[
        "usernames"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Team` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">get_org_team</a>(...) -> TeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one team that you identified using its unique 24-hexadecimal digit ID. This team belongs to one organization. Teams enable you to grant project access roles to MongoDB Cloud users. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.get_org_team(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team whose information you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">delete_org_team</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one team specified using its unique 24-hexadecimal digit identifier from the organization specified using its unique 24-hexadecimal digit identifier. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.delete_org_team(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team that you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">rename_org_team</a>(...) -> TeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Renames one team in the specified organization. Teams enable you to grant project access roles to MongoDB Cloud users. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.rename_org_team(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team that you want to rename.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the team.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">add_team_users</a>(...) -> PaginatedApiAppUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one or more MongoDB Cloud users from the specified organization to the specified team. Teams enable you to grant project access roles to MongoDB Cloud users. You can assign up to 250 MongoDB Cloud users from one organization to one team. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This endpoint is deprecated. Use [Add One MongoDB Cloud User to One Team](#tag/MongoDB-Cloud-Users/operation/addUserToTeam) to add an active or pending user to a team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, AddUserToTeam
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.add_team_users(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
    request=[
        AddUserToTeam(
            id="32b6e34b3d91647abb20e7b8",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal character string that identifies the team to which you want to add MongoDB Cloud users.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[AddUserToTeam]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">remove_user_from_team</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one MongoDB Cloud user from the specified team. This team belongs to one organization. Teams enable you to grant project access roles to MongoDB Cloud users. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This endpoint is deprecated. Use [Remove One MongoDB Cloud User from One Team](#tag/MongoDB-Cloud-Users/operation/removeUserFromTeam) to remove an active or pending user from a team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.remove_user_from_team(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team from which you want to remove one database application user.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies MongoDB Cloud user that you want to remove from the specified team.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/atlas_sdk/teams/client.py">get_team_by_name</a>(...) -> TeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one team that you identified using its human-readable name. This team belongs to one organization. Teams enable you to grant project access roles to MongoDB Cloud users. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.teams.get_team_by_name(
    org_id="4888442a3354817a7320eb61",
    team_name="teamName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_name:** `str` — Name of the team whose information you want to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LDAP Configuration
<details><summary><code>client.ldap_configuration.<a href="src/atlas_sdk/ldap_configuration/client.py">get_user_security</a>(...) -> UserSecurity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current LDAP configuration for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.ldap_configuration.get_user_security(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ldap_configuration.<a href="src/atlas_sdk/ldap_configuration/client.py">update_user_security</a>(...) -> UserSecurity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edits the LDAP configuration for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

Updating this configuration triggers a rolling restart of the database.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.ldap_configuration.update_user_security(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserSecurity` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ldap_configuration.<a href="src/atlas_sdk/ldap_configuration/client.py">delete_ldap_user_mapping</a>(...) -> UserSecurity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the current LDAP Distinguished Name mapping captured in the ``userToDNMapping`` document from the LDAP configuration for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.ldap_configuration.delete_ldap_user_mapping(
    group_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ldap_configuration.<a href="src/atlas_sdk/ldap_configuration/client.py">verify_user_security_ldap</a>(...) -> LdapVerifyConnectivityJobRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies the LDAP configuration for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.ldap_configuration.verify_user_security_ldap(
    group_id="32b6e34b3d91647abb20e7b8",
    bind_password="bindPassword",
    bind_username="CN=BindUser,CN=Users,DC=myldapserver,DC=mycompany,DC=com",
    hostname="hostname",
    port=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request:** `LdapVerifyConnectivityJobRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ldap_configuration.<a href="src/atlas_sdk/ldap_configuration/client.py">get_user_security_verify</a>(...) -> LdapVerifyConnectivityJobRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of one request to verify one LDAP configuration for the specified project. To use this resource, the requesting Service Account or API Key must have the Project Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.ldap_configuration.get_user_security_verify(
    group_id="32b6e34b3d91647abb20e7b8",
    request_id="requestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` — Unique string that identifies the request to verify an Lightweight Directory Access Protocol (LDAP) configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MongoDB Cloud Users
<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">list_group_users</a>(...) -> PaginatedGroupUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the pending and active MongoDB Cloud users associated with the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

**Note**: This resource cannot be used to view details about users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

**Note**: To return both pending and active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users will be returned. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.list_group_users(
    group_id="32b6e34b3d91647abb20e7b8",
    org_membership_status="ACTIVE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**flatten_teams:** `typing.Optional[bool]` — Flag that indicates whether the returned list should include users who belong to a team with a role in this project. You might not have assigned the individual users a role in this project. If `"flattenTeams" : false`, this resource returns only users with a role in the project.  If `"flattenTeams" : true`, this resource returns both users with roles in the project and users who belong to teams with roles in the project.
    
</dd>
</dl>

<dl>
<dd>

**include_org_users:** `typing.Optional[bool]` — Flag that indicates whether the returned list should include users with implicit access to the project, the Organization Owner or Organization Read Only role. You might not have assigned the individual users a role in this project. If `"includeOrgUsers": false`, this resource returns only users with a role in the project. If `"includeOrgUsers": true`, this resource returns both users with roles in the project and users who have implicit access to the project through their organization role.
    
</dd>
</dl>

<dl>
<dd>

**org_membership_status:** `typing.Optional[str]` — Flag that indicates whether to filter the returned list by users organization membership status. If you exclude this parameter, this resource returns both pending and active users. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Email address to filter users by. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">add_group_users</a>(...) -> GroupUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one MongoDB Cloud user to one project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role. 
- If the user has a pending invitation to join the project's organization, MongoDB Cloud modifies it and grants project access. 
- If the user doesn't have an invitation to join the organization, MongoDB Cloud sends a new invitation that grants the user organization and project access. 
- If the user is already active in the project's organization, MongoDB Cloud grants access to the project. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.add_group_users(
    group_id="32b6e34b3d91647abb20e7b8",
    roles=[
        "roles"
    ],
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — One or more project-level roles to assign the MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Email address that represents the username of the MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">get_group_user</a>(...) -> GroupUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the specified MongoDB Cloud user within the context of the specified project. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

**Note**: You can only use this resource to fetch information about MongoDB Cloud human users. To return information about an API Key, use the [Return One Organization API Key](#tag/Programmatic-API-Keys/operation/getApiKey) endpoint.

**Note**: This resource does not return information about pending users invited via the deprecated [Invite One MongoDB Cloud User to Join One Project](#tag/Projects/operation/createProjectInvitation) endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.get_group_user(
    group_id="32b6e34b3d91647abb20e7b8",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Project resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">remove_group_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one MongoDB Cloud user from the specified project. You can remove an active user or a user that has not yet accepted the invitation to join the organization. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.

**Note**: This resource cannot be used to remove pending users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

**Note**: To remove pending or active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users can be removed. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.remove_group_user(
    group_id="32b6e34b3d91647abb20e7b8",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the [Return All MongoDB Cloud Users in One Project](#tag/MongoDB-Cloud-Users/operation/listProjectUsers) resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">add_group_user_role</a>(...) -> GroupUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one project-level role to the MongoDB Cloud user. You can add a role to an active user or a user that has been invited to join the project. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.

**Note**: This resource cannot be used to add a role to users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.add_group_user_role(
    group_id="32b6e34b3d91647abb20e7b8",
    user_id="userId",
    group_role="groupRole",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Project resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddOrRemoveGroupRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">remove_group_user_role</a>(...) -> GroupUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one project-level role from the MongoDB Cloud user. You can remove a role from an active user or a user that has been invited to join the project. To replace a user's only role, add the new role before removing the old role. A user must have at least one role at all times. To use this resource, the requesting Service Account or API Key must have the Project Owner role or Project Access Manager role.

**Note**: This resource cannot be used to remove a role from users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.remove_group_user_role(
    group_id="32b6e34b3d91647abb20e7b8",
    user_id="userId",
    group_role="groupRole",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 

Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access.

**NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Project resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddOrRemoveGroupRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">list_team_users</a>(...) -> PaginatedOrgUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the pending and active MongoDB Cloud users associated with the specified team in the organization. Teams enable you to grant project access roles to MongoDB Cloud users. To use this resource, the requesting Service Account or API Key must have the Organization Member role.

**Note**: This resource cannot be used to view details about users invited via the deprecated [Invite One MongoDB Cloud User to Join One Project](#tag/Projects/operation/createProjectInvitation) endpoint.

**Note**: To return both pending and active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users will be returned. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.list_team_users(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
    org_membership_status="ACTIVE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team whose application users you want to return.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Email address to filter users by. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**org_membership_status:** `typing.Optional[str]` — Organization membership status to filter users by. If you exclude this parameter, this resource returns both pending and active users. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string to filter users by. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">add_org_team_user</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one MongoDB Cloud user to one team. You can add an active user or a user that has not yet accepted the invitation to join the organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This resource cannot be used to add a user invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.add_org_team_user(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
    id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team to add the MongoDB Cloud user to.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddOrRemoveUserFromTeam` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">remove_org_team_user</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one MongoDB Cloud user from one team. You can remove an active user or a user that has not yet accepted the invitation to join the organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This resource cannot be used to remove a user invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.remove_org_team_user(
    org_id="4888442a3354817a7320eb61",
    team_id="teamId",
    id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `str` — Unique 24-hexadecimal digit string that identifies the team to remove the MongoDB user from.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddOrRemoveUserFromTeam` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">list_org_users</a>(...) -> PaginatedOrgUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the pending and active MongoDB Cloud users associated with the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Member role.

**Note**: This resource cannot be used to view details about users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

**Note**: To return both pending and active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users will be returned. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.list_org_users(
    org_id="4888442a3354817a7320eb61",
    org_membership_status="ACTIVE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Email address to filter users by. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**org_membership_status:** `typing.Optional[str]` — Organization membership status to filter users by. If you exclude this parameter, this resource returns both pending and active users. Not supported in deprecated versions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">create_org_user</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invites one new or existing MongoDB Cloud user to join the organization. The invitation to join the organization will be sent to the username provided and must be accepted within 30 days. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: If the user does not have an existing MongoDB Cloud account, they will be prompted to finish setting up an account upon accepting the invitation. If the user already has an account, they will still receive an invitation to access the organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, OrgUserRolesRequest
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.create_org_user(
    org_id="4888442a3354817a7320eb61",
    roles=OrgUserRolesRequest(
        org_roles=[
            "orgRoles"
        ],
    ),
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `OrgUserRolesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Email address that represents the username of the MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**team_ids:** `typing.Optional[typing.List[str]]` — List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">get_org_user</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the specified MongoDB Cloud user within the context of the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Member role.

**Note**: This resource can only be used to fetch information about MongoDB Cloud human users. To return information about an API Key, use the [Return One Organization API Key](#tag/Programmatic-API-Keys/operation/getApiKey) endpoint.

**Note**: This resource does not return information about pending users invited via the deprecated [Invite One MongoDB Cloud User to Join One Project](#tag/Projects/operation/createProjectInvitation) endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.get_org_user(
    org_id="4888442a3354817a7320eb61",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">remove_org_user</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one MongoDB Cloud user in the specified organization. You can remove an active user or a user that has not yet accepted the invitation to join the organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This resource cannot be used to remove pending users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

**Note**: To remove pending or active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users can be removed. Deprecated versions: v2-{2023-01-01}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.remove_org_user(
    org_id="4888442a3354817a7320eb61",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the [Return All MongoDB Cloud Users in One Organization](#tag/MongoDB-Cloud-Users/operation/listOrganizationUsers) resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">update_org_user</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one MongoDB Cloud user in the specified organization. You can update an active user or a user that has not yet accepted the invitation to join the organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: Only include the fields you wish to update in the request body. Supplying a field with an empty value will reset that field on the user.

**Note**: This resource cannot be used to update pending users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.update_org_user(
    org_id="4888442a3354817a7320eb61",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[OrgUserRolesRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**team_ids:** `typing.Optional[typing.List[str]]` — List of unique 24-hexadecimal digit strings that identifies the teams to assign the MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">add_org_role</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one organization-level role to the MongoDB Cloud user. You can add a role to an active user or a user that has not yet accepted the invitation to join the organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This operation is atomic.

**Note**: This resource cannot be used to add a role to users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.add_org_role(
    org_id="4888442a3354817a7320eb61",
    user_id="userId",
    org_role="orgRole",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddOrRemoveOrgRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">remove_org_role</a>(...) -> OrgUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one organization-level role from the MongoDB Cloud user. You can remove a role from an active user or a user that has not yet accepted the invitation to join the organization. To replace a user's only role, add the new role before removing the old role. A user must have at least one role at all times. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: This operation is atomic.

**Note**: This resource cannot be used to remove a role from users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.remove_org_role(
    org_id="4888442a3354817a7320eb61",
    user_id="userId",
    org_role="orgRole",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddOrRemoveOrgRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">create_user</a>(...) -> CloudAppUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one MongoDB Cloud user account. A MongoDB Cloud user account grants access to only the MongoDB Cloud application. To grant database access, create a database user. MongoDB Cloud sends an email to the users you specify, inviting them to join the project. Invited users don't have access to the project until they accept the invitation. Invitations expire after 30 days.

 MongoDB Cloud limits MongoDB Cloud user membership to a maximum of 250 MongoDB Cloud users per team. MongoDB Cloud limits MongoDB Cloud user membership to 500 MongoDB Cloud users per project and 500 MongoDB Cloud users per organization, which includes the combined membership of all projects in the organization. MongoDB Cloud raises an error if an operation exceeds these limits. For example, if you have an organization with five projects, and each project has 100 MongoDB Cloud users, and each MongoDB Cloud user belongs to only one project, you can't add any MongoDB Cloud users to this organization without first removing existing MongoDB Cloud users from the organization.

 To use this resource, the requesting Service Account or API Key can have any role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, CloudAccessRoleAssignment
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.create_user(
    country="country",
    first_name="firstName",
    last_name="lastName",
    mobile_number="mobileNumber",
    password="password",
    roles=[
        CloudAccessRoleAssignment()
    ],
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CloudAppUser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">get_user</a>(...) -> CloudAppUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details for one MongoDB Cloud user account with the specified unique identifier for the user. You can't use this endpoint to return information on an API Key. To return information about an API Key, use the Return One Organization API Key endpoint. You can always retrieve your own user account. If you are the owner of a MongoDB Cloud organization or project, you can also retrieve the user profile for any user with membership in that organization or project. To use this resource, the requesting Service Account or API Key can have any role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.get_user(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mongo_db_cloud_users.<a href="src/atlas_sdk/mongo_db_cloud_users/client.py">get_user_by_name</a>(...) -> CloudAppUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details for one MongoDB Cloud user account with the specified username. You can't use this endpoint to return information about an API Key. To return information about an API Key, use the Return One Organization API Key endpoint. To use this resource, the requesting Service Account or API Key can have any role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.mongo_db_cloud_users.get_user_by_name(
    user_name="userName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_name:** `str` — Email address that belongs to the MongoDB Cloud user account. You cannot modify this address after creating the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations
<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">list_orgs</a>(...) -> PaginatedOrganization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all organizations to which the requesting Service Account or API Key has access. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.list_orgs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable label of the organization to use to filter the returned list. Performs a case-insensitive search for an organization that starts with the specified name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">create_org</a>(...) -> CreateOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one organization in MongoDB Cloud and links it to the requesting Service Account's or API Key's organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role. The requesting Service Account's or API Key's organization must be a paying organization. To learn more, see Configure a Paying Organization in the MongoDB Atlas documentation. Optionally, if `federationSettingsId` is provided, the new Organization will be linked to the federation. The requesting Service Account or API Key must be an Organization Owner in the federation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.create_org(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable label that identifies the organization.
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[CreateAtlasOrganizationApiKey]` 
    
</dd>
</dl>

<dl>
<dd>

**federation_settings_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the federation to link the newly created organization to. If specified, the proposed Organization Owner of the new organization must have the Organization Owner role in an organization associated with the federation.
    
</dd>
</dl>

<dl>
<dd>

**org_owner_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user that you want to assign the Organization Owner role. This user must be a member of the same organization as the calling API key. If you provide `federationSettingsId`,  this user must instead have the Organization Owner role on an organization in the specified federation. This parameter is required only when you authenticate with Programmatic API Keys.
    
</dd>
</dl>

<dl>
<dd>

**service_account:** `typing.Optional[OrgServiceAccountRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_default_alerts_settings:** `typing.Optional[bool]` — Disables automatic alert creation. When set to true, no organization level alerts will be created automatically.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">get_org</a>(...) -> AtlasOrganization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one organization to which the requesting Service Account or API Key has access. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.get_org(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">delete_org</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one specified organization. MongoDB Cloud imposes the following limits on this resource:

 - Organizations with active projects cannot be removed.
 - All projects in the organization must be removed before you can remove the organization.
 To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.delete_org(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">update_org</a>(...) -> AtlasOrganization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.update_org(
    org_id="4888442a3354817a7320eb61",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AtlasOrganization` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">get_org_groups</a>(...) -> PaginatedAtlasGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns multiple projects in the specified organization. Each organization can have multiple projects. Use projects to:

- Isolate different environments, such as development, test, or production environments, from each other.
- Associate different MongoDB Cloud users or teams with different environments, or give different permission to MongoDB Cloud users in different environments.
- Maintain separate cluster security configurations.
- Create different alert settings.

To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.get_org_groups(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable label of the project to use to filter the returned list. Performs a case-insensitive search for a project within the organization which is prefixed by the specified name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">list_org_invites</a>(...) -> typing.List[OrganizationInvitation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all pending invitations to the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: Invitation management APIs are deprecated. Use Return All MongoDB Cloud Users in One Organization and filter by `orgMembershipStatus` to return all pending users.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.list_org_invites(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Email address of the user account invited to this organization. If you exclude this parameter, this resource returns all pending invitations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">create_org_invite</a>(...) -> OrganizationInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invites one MongoDB Cloud user to join the specified organization. The user must accept the invitation to access information within the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: Invitation management APIs are deprecated. Use Add One MongoDB Cloud User to One Organization to invite a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.create_org_invite(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationInvitationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">update_org_invites</a>(...) -> OrganizationInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of one pending invitation to the specified organization. To specify which invitation, provide the username of the invited user. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**:  Invitation management are deprecated. Use Update One MongoDB Cloud User in One Organization to update a pending user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.update_org_invites(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationInvitationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">get_org_invite</a>(...) -> OrganizationInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of one pending invitation to the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: Invitation management APIs are deprecated. Use Return One MongoDB Cloud User in One Organization to return a pending user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.get_org_invite(
    org_id="4888442a3354817a7320eb61",
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — Unique 24-hexadecimal digit string that identifies the invitation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">delete_org_invite</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels one pending invitation sent to the specified MongoDB Cloud user to join an organization. You can't cancel an invitation that the user accepted. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: Invitation management APIs are deprecated. Use Remove One MongoDB Cloud User From One Organization to remove a pending user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.delete_org_invite(
    org_id="4888442a3354817a7320eb61",
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — Unique 24-hexadecimal digit string that identifies the invitation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">update_org_invite_by_id</a>(...) -> OrganizationInvitation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of one pending invitation to the specified organization. To specify which invitation, provide the unique identification string for that invitation. Use the Return All Organization Invitations endpoint to retrieve IDs for all pending organization invitations. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.

**Note**: Invitation management APIs are deprecated. Use Update One MongoDB Cloud User in One Organization to update a pending user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.update_org_invite_by_id(
    org_id="4888442a3354817a7320eb61",
    invitation_id="invitationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — Unique 24-hexadecimal digit string that identifies the invitation.
    
</dd>
</dl>

<dl>
<dd>

**group_role_assignments:** `typing.Optional[typing.List[OrganizationInvitationGroupRoleAssignmentsRequest]]` — List of projects that the user will be added to when they accept their invitation to the organization.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` — One or more organization level roles to assign to the MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**team_ids:** `typing.Optional[typing.List[str]]` — List of teams to which you want to invite the desired MongoDB Cloud user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">get_org_settings</a>(...) -> OrganizationSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about the specified organization's settings. To use this resource, the requesting Service Account or API Key must have the Organization Member role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.get_org_settings(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">update_org_settings</a>(...) -> OrganizationSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the organization's settings. To use this resource, the requesting Service Account or API Key must have the Organization Owner role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.update_org_settings(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationSettings` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/atlas_sdk/organizations/client.py">update_org_user_roles</a>(...) -> UpdateOrgRolesForUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the roles of the specified user in the specified organization. To specify the user to update, provide the unique 24-hexadecimal digit string that identifies the user in the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization User Admin role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.organizations.update_org_user_roles(
    org_id="4888442a3354817a7320eb61",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique 24-hexadecimal digit string that identifies the user to modify.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateOrgRolesForUser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoices
<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">create_cost_explorer_process</a>(...) -> CostExplorerFilterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a query process within the Cost Explorer for the given parameters. A token is returned that can be used to poll the status of the query and eventually retrieve the results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment
import datetime

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.create_cost_explorer_process(
    org_id="4888442a3354817a7320eb61",
    end_date=datetime.date.fromisoformat("2023-01-15"),
    start_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — The exclusive ending date for the Cost Explorer query. The date must be the start of a month.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — The inclusive starting date for the Cost Explorer query. The date must be the start of a month.
    
</dd>
</dl>

<dl>
<dd>

**clusters:** `typing.Optional[typing.List[str]]` — The list of clusters to be included in the Cost Explorer Query.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[str]` — The dimension to group the returned usage results by. At least one filter value needs to be provided for a dimension to be used.
    
</dd>
</dl>

<dl>
<dd>

**include_partial_matches:** `typing.Optional[bool]` — Flag to control whether usage that matches the filter criteria, but does not have values for all filter criteria is included in response. Default is false, which excludes the partially matching data.
    
</dd>
</dl>

<dl>
<dd>

**organizations:** `typing.Optional[typing.List[str]]` — The list of organizations to be included in the Cost Explorer Query.
    
</dd>
</dl>

<dl>
<dd>

**projects:** `typing.Optional[typing.List[str]]` — The list of projects to be included in the Cost Explorer Query.
    
</dd>
</dl>

<dl>
<dd>

**services:** `typing.Optional[typing.List[str]]` — The list of SKU services to be included in the Cost Explorer Query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">get_cost_explorer_usage</a>(...) -> CostExplorerQueryResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the usage details for a Cost Explorer query, if the query is finished and the data is ready to be viewed. If the data is not ready, a 'processing' response will indicate that another request should be sent later to view the data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.get_cost_explorer_usage(
    org_id="4888442a3354817a7320eb61",
    token="4ABBE973862346D40F3AE859D4BE96E0F895764EB14EAB039E7B82F9D638C05C",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — Unique 64 digit string that identifies the Cost Explorer query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">list_invoices</a>(...) -> PaginatedApiInvoiceMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all invoices that MongoDB issued to the specified organization. This list includes all invoices regardless of invoice status. To use this resource, the requesting Service Account or API Key must have the Organization Billing Viewer, Organization Billing Admin, or Organization Owner role. If you have a cross-organization setup, you can view linked invoices if you have the Organization Billing Admin or Organization Owner role.
To compute the total owed amount of the invoices - sum up total owed of each invoice. It could be computed as a sum of owed amount of each payment included into the invoice. To compute payment's owed amount - use formula `totalBilledCents` * `unitPrice` + `salesTax` - `startingBalanceCents`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.list_invoices(
    org_id="4888442a3354817a7320eb61",
    order_by="desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**view_linked_invoices:** `typing.Optional[bool]` — Flag that indicates whether to return linked invoices in the `linkedInvoices` field.
    
</dd>
</dl>

<dl>
<dd>

**status_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Statuses of the invoice to be retrieved. Omit to return invoices of all statuses.
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.date]` — Retrieve the invoices the `startDates` of which are greater than or equal to the `fromDate`. If omit, the invoices return will go back to earliest `startDate`.
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[datetime.date]` — Retrieve the invoices the `endDates` of which are smaller than or equal to the `toDate`. If omit, the invoices return will go further to latest `endDate`.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Field used to sort the returned invoices by. Use in combination with `orderBy` parameter to control the order of the result.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field used to order the returned invoices by. Use in combination of `sortBy` parameter to control the order of the result.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">get_invoice</a>(...) -> BillingInvoice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one invoice that MongoDB issued to the specified organization. A unique 24-hexadecimal digit string identifies the invoice. You can choose to receive this invoice in JSON or CSV format. To use this resource, the requesting Service Account or API Key must have the Organization Billing Viewer, Organization Billing Admin, or Organization Owner role. If you have a cross-organization setup, you can query for a linked invoice if you have the Organization Billing Admin or Organization Owner role.
To compute the total owed amount of the invoice - sum up total owed amount of each payment included into the invoice. To compute payment's owed amount - use formula `totalBilledCents` * `unitPrice` + `salesTax` - `startingBalanceCents`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.get_invoice(
    org_id="4888442a3354817a7320eb61",
    invoice_id="invoiceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `str` — Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">get_invoice_csv</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one invoice that MongoDB issued to the specified organization in CSV format. A unique 24-hexadecimal digit string identifies the invoice. To use this resource, the requesting Service Account or API Key have at least the Organization Billing Viewer, Organization Billing Admin, or Organization Owner role. If you have a cross-organization setup, you can query for a linked invoice if you have the Organization Billing Admin or Organization Owner Role.
 To compute the total owed amount of the invoice - sum up total owed amount of each payment included into the invoice. To compute payment's owed amount - use formula `totalBilledCents` * `unitPrice` + `salesTax` - `startingBalanceCents`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.get_invoice_csv(
    org_id="4888442a3354817a7320eb61",
    invoice_id="invoiceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `str` — Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">search_invoice_line_items</a>(...) -> PaginatedPublicApiUsageDetailsLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query the `lineItems` of the specified invoice and return the result JSON. A unique 24-hexadecimal digit string identifies the invoice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.search_invoice_line_items(
    org_id="4888442a3354817a7320eb61",
    invoice_id="invoiceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `str` — Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">list_invoice_pending</a>(...) -> PaginatedApiInvoice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all invoices accruing charges for the current billing cycle for the specified organization. To use this resource, the requesting Service Account or API Key must have the Organization Billing Viewer, Organization Billing Admin, or Organization Owner role. If you have a cross-organization setup, you can view linked invoices if you have the Organization Billing Admin or Organization Owner Role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.list_invoice_pending(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">list_skus</a>(...) -> PaginatedApiSku</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all available SKUs (Stock Keeping Units) that can appear on MongoDB invoices. SKUs represent different products and services offered by MongoDB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.list_skus()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — Flag that indicates whether the response returns the total number of items (`totalCount`) in the response.
    
</dd>
</dl>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/atlas_sdk/invoices/client.py">get_sku</a>(...) -> SkuResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about a single SKU (Stock Keeping Unit) by its identifier. SKUs represent different products and services offered by MongoDB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.invoices.get_sku(
    sku_id="ATLAS_AWS_INSTANCE_M10",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sku_id:** `str` — Unique identifier of the SKU to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Resource Policies
<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">get_non_compliant_resources</a>(...) -> typing.List[ApiAtlasNonCompliantResource]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all non-compliant resources for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.get_non_compliant_resources(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">list_org_resource_policies</a>(...) -> typing.List[ApiAtlasResourcePolicy]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all Atlas Resource Policies for the organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.list_org_resource_policies(
    org_id="4888442a3354817a7320eb61",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">create_org_resource_policy</a>(...) -> ApiAtlasResourcePolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one Atlas Resource Policy for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ApiAtlasPolicyCreate
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.create_org_resource_policy(
    org_id="4888442a3354817a7320eb61",
    name="name",
    policies=[
        ApiAtlasPolicyCreate(
            body="  forbid (\n    principal,\n    action == cloud::Action::\"cluster.createEdit\",\n    resource\n  ) when {\n   context.cluster.regions.contains(cloud::region::\"aws:us-east-1\")\n  };\n",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiAtlasResourcePolicyCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">get_org_resource_policy</a>(...) -> ApiAtlasResourcePolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return one Atlas Resource Policy for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.get_org_resource_policy(
    org_id="4888442a3354817a7320eb61",
    resource_policy_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**resource_policy_id:** `str` — Unique 24-hexadecimal digit string that identifies an atlas resource policy.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">delete_org_resource_policy</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one Atlas Resource Policy for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.delete_org_resource_policy(
    org_id="4888442a3354817a7320eb61",
    resource_policy_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**resource_policy_id:** `str` — Unique 24-hexadecimal digit string that identifies an atlas resource policy.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">update_org_resource_policy</a>(...) -> ApiAtlasResourcePolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one Atlas Resource Policy for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.update_org_resource_policy(
    org_id="4888442a3354817a7320eb61",
    resource_policy_id="32b6e34b3d91647abb20e7b8",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**resource_policy_id:** `str` — Unique 24-hexadecimal digit string that identifies an atlas resource policy.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the atlas resource policy.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable label that describes the atlas resource policy.
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.List[ApiAtlasPolicyCreate]]` — List of policies that make up the atlas resource policy.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_policies.<a href="src/atlas_sdk/resource_policies/client.py">validate_resource_policies</a>(...) -> ApiAtlasResourcePolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate one Atlas Resource Policy for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient, ApiAtlasPolicyCreate
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.resource_policies.validate_resource_policies(
    org_id="4888442a3354817a7320eb61",
    name="name",
    policies=[
        ApiAtlasPolicyCreate(
            body="  forbid (\n    principal,\n    action == cloud::Action::\"cluster.createEdit\",\n    resource\n  ) when {\n   context.cluster.regions.contains(cloud::region::\"aws:us-east-1\")\n  };\n",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiAtlasResourcePolicyCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rate Limiting
<details><summary><code>client.rate_limiting.<a href="src/atlas_sdk/rate_limiting/client.py">list_rate_limits</a>(...) -> PaginatedRateLimitEndpointSets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all rate limits for all v2 Atlas Administration API endpoint sets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.rate_limiting.list_rate_limits(
    group_id="32b6e34b3d91647abb20e7b8",
    org_id="32b6e34b3d91647abb20e7b8",
    user_id="mdb_sa_id_1234567890abcdef12345678",
    ip_address="127.0.0.1",
    name="Rate Limits Inspection",
    endpoint_path="/api/atlas/v2/clusters",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**items_per_page:** `typing.Optional[int]` — Number of items that the response returns per page.
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` — Number of the page that displays the current set of the total objects that the response returns.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the Atlas Project to request rate limits for. When this parameter is provided, only group scoped endpoint sets are returned and the limits returned are applicable to the specified project. The requesting user must have the Project Read Only role for the specified project.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the Atlas Organization to request rate limits for. When this parameter is provided, only organization scoped endpoint sets are returned and the limits returned are applicable to the specified organization. The requesting user must have the Organization Read Only role for the specified organization.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — A string that identifies the Atlas user to request rate limits for. The ID can for example be the Service Account Client ID or the API Public Key. When this parameter is provided, only user scoped endpoint sets are returned and the limits returned are applicable to the specified user. The requesting user must be the same as the specified user.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — An IP address to request rate limits for. When this parameter is provided, only IP scoped endpoint sets are returned and the limits returned are applicable to the specified IP address. The requesting user must have the same IP address as the one provided in the request.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filters the returned endpoint sets by the provided endpoint set name. Multiple names may be provided, for example `/rateLimits?name=Name1&name=Name2`. For names that use spaces, replace the space with its URL-encoded value (`%20`).
    
</dd>
</dl>

<dl>
<dd>

**endpoint_path:** `typing.Optional[str]` — Filters the returned endpoint sets by the provided endpoint path. Multiple paths may be provided, for example `/rateLimits?endpointPath=%2Fapi%2Fatlas%2Fv2%2Fclusters&endpointPath=%2Fapi%2Fatlas%2Fv2%2Fgroups%2F%7BgroupId%7D%2F`. Replace `/`, `{` and `}` with their URL-encoded values (`%2F`, `%7B` and `%7D` respectively).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rate_limiting.<a href="src/atlas_sdk/rate_limiting/client.py">get_rate_limit</a>(...) -> RateLimitEndpointSetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one rate limit endpoint set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from atlas_sdk import AtlasClient
from atlas_sdk.environment import AtlasClientEnvironment

client = AtlasClient(
    token="<token>",
    environment=AtlasClientEnvironment.DEFAULT,
)

client.rate_limiting.get_rate_limit(
    endpoint_set_id="rateLimitsInspection_group",
    group_id="32b6e34b3d91647abb20e7b8",
    org_id="32b6e34b3d91647abb20e7b8",
    user_id="mdb_sa_id_1234567890abcdef12345678",
    ip_address="127.0.0.1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**endpoint_set_id:** `str` — The ID of the rate limit endpoint set.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the Atlas Project to request rate limits for. When this parameter is provided, the limits returned are applicable to the specified project. The requesting user must have the Project Read Only role for the specified project.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — Unique 24-hexadecimal digit string that identifies the Atlas Organization to request rate limits for. When this parameter is provided, the limits returned are applicable to the specified organization. The requesting user must have the Organization Read Only role for the specified organization.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — A string that identifies the Atlas user to request rate limits for. The ID can for example be the Service Account Client ID or the API Public Key. When this parameter is provided, the limits returned are applicable to the specified  user. The requesting user must be the same as the specified user.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — An IP address to request rate limits for. When this parameter is provided, the limits returned are applicable to the specified IP address. The requesting user must have the same IP address as the one provided in the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

