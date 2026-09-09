"""
Client module for creating a Databricks Workspace client.

This is the single entry point for authentication: every other wrapper module
(catalogs, schemas, tables, jobs, workspace) obtains its WorkspaceClient from
here rather than constructing one directly. Auth is resolved from a Databricks
CLI profile (default "playground").
"""

from databricks.sdk import WorkspaceClient


def get_workspace_client(profile: str = "playground") -> WorkspaceClient:
    """
    Create and return a Databricks WorkspaceClient.

    Args:
        profile: Databricks CLI authentication profile.

    Returns:
        WorkspaceClient instance.
    """

    return WorkspaceClient(profile=profile)