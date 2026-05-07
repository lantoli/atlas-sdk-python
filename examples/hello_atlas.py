"""List up to 10 Atlas projects accessible to the service account.

Required env vars:
    MONGODB_ATLAS_CLIENT_ID
    MONGODB_ATLAS_CLIENT_SECRET
"""

from _atlas import get_client

client = get_client()
result = client.projects.list_groups(items_per_page=10, page_num=1)

for project in result.results or []:
    print(f"{project.id}  {project.name}")
