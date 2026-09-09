# Databricks SDK + Claude Code Playground 
> Built and documented with hands-on Claude Code workflows. 

A hands-on project demonstrating the capabilities of the **Databricks Python SDK** through practical examples, reusable SDK wrapper modules, end-to-end automation workflows, and basic unit testing.

The repository was built to explore how the Databricks Python SDK can be used to automate common workspace operations programmatically while following a clean and maintainable Python project structure.

---

## Solution Architecture

```text
                    Local Development (VS Code)
                              │
                              ▼
                  Databricks Python SDK Wrapper
                              │
                              ▼
                     Databricks Python SDK
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
  Unity Catalog         Workspace APIs         Jobs APIs
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    Databricks Workspace
```

---

# Objectives

The primary objectives of this repository are to:

- Learn the Databricks Python SDK through practical implementation.
- Build reusable Python modules on top of the SDK.
- Automate common Databricks workspace operations.
- Demonstrate an end-to-end SDK automation workflow.
- Organise the project using a scalable Python package structure.
- Validate reusable components using `pytest`.

---

# Repository Structure

```text
databricks-python-sdk-playground/
│
├── docs/
│   ├── 01_Getting_Started.md
│   ├── 02_Listing_Catalogs.md
│   ├── 03_Listing_Schemas.md
│   ├── 04_Listing_Tables.md
│   └── 05_Listing_Jobs.md
│
├── examples/
│   ├── 01_connect.py
│   ├── 02_list_catalogs.py
│   ├── 03_list_schemas.py
│   ├── 04_list_tables.py
│   └── 05_list_jobs.py
│
├── notebooks/
│   └── sample_notebook.py
│
├── use_cases/
│   ├── deploy_notebook.py
│   ├── create_job.py
│   ├── trigger_job.py
│   ├── monitor_job_run.py
│   └── monitor_jobs.py
│
├── src/
│   └── databricks_sdk_playground/
│       ├── __init__.py
│       ├── client.py
│       ├── catalogs.py
│       ├── schemas.py
│       ├── tables.py
│       ├── jobs.py
│       └── workspace.py
│
├── tests/
│   ├── test_client.py
│   ├── test_catalogs.py
│   ├── test_schemas.py
│   ├── test_tables.py
│   ├── test_jobs.py
│   └── test_workspace.py
│
└── README.md
```

---

# Implemented Features

## Authentication

- Authenticate using a Databricks CLI profile.
- Create a reusable `WorkspaceClient` for SDK operations.

---

## Unity Catalog Operations

Implemented SDK examples for:

- Listing available Catalogs
- Listing Schemas within a Catalog
- Listing Tables and Views within a Schema

---

## Databricks Jobs

Implemented examples for:

- Listing existing Jobs
- Retrieving Job metadata

---

# End-to-End SDK Automation

An end-to-end automation workflow has been implemented using the Databricks Python SDK.

## Deploy Notebook

Programmatically:

- Create a Workspace folder
- Import a local notebook into the Databricks Workspace

---

## Create Job

Programmatically create a Databricks Job that executes the deployed notebook.

---

## Trigger Job

Execute the Job directly from a local Python script.

---

## Monitor Job Execution

Retrieve and monitor the Job run status until completion.

---

# Reusable SDK Wrapper

To improve maintainability and encourage code reuse, reusable wrapper modules have been implemented under:

```text
src/databricks_sdk_playground/
```

These modules encapsulate commonly used SDK operations.

| Module | Purpose |
|----------|---------|
| `client.py` | Create and manage the Databricks Workspace client |
| `catalogs.py` | Unity Catalog operations |
| `schemas.py` | Schema operations |
| `tables.py` | Table operations |
| `jobs.py` | Databricks Job operations |
| `workspace.py` | Workspace management operations |

This lightweight scaffold provides a foundation that can be extended for additional Databricks SDK automation scenarios.

---

# Unit Testing

A basic unit testing structure has been implemented using **pytest**.

Current test coverage includes:

- Workspace client creation
- Catalog retrieval
- Schema retrieval
- Table retrieval
- Job retrieval
- Workspace folder creation

Run the tests:

```powershell
$env:PYTHONPATH="src"

pytest
```

Sample output:

```text
==============================
6 passed in 35.00s
==============================
```

---

# Technologies Used

- Python 3.12
- Databricks Python SDK
- Databricks CLI
- Unity Catalog
- Databricks Jobs API
- Pytest
- Visual Studio Code

---

# Key Learning Outcomes

This implementation provided hands-on experience with:

- Databricks Python SDK authentication
- Unity Catalog APIs
- Workspace APIs
- Jobs APIs
- Programmatic notebook deployment
- Job creation using the SDK
- Job execution and monitoring
- Building reusable SDK wrapper modules
- Python package organisation using the `src` layout
- Basic unit testing with `pytest`

---

# Future Enhancements

Potential improvements include:

- Mock-based unit testing for SDK interactions
- GitHub Actions CI/CD pipeline
- Async SDK implementation
- Structured logging
- OpenTelemetry integration
- SQL Warehouse automation
- Cluster lifecycle management
- Unity Catalog privilege management
- Secrets management
- Databricks Asset Bundle integration

---

# Summary

This repository demonstrates practical usage of the Databricks Python SDK through incremental examples, reusable wrapper modules, automation workflows, and unit tests.

The implementation follows a modular project structure and establishes a lightweight SDK scaffold that can be extended to support more advanced Databricks automation and Data Engineering use cases.

---

# AI-Assisted Development Workflow

This repository is configured to work with **Claude Code**, with project-specific context, guardrails, and reusable commands rather than relying on default, generic behavior.

## Project Memory (`CLAUDE.md`)

Two `CLAUDE.md` files give Claude Code persistent context about this project:

- **Root `CLAUDE.md`** — documents the stack, module conventions, the exact test command, naming patterns, and explicit "never touch without confirmation" rules (notably: `use_cases/` scripts and the test suite itself both make real calls against a live Databricks workspace).
- **`src/databricks_sdk_playground/CLAUDE.md`** — a directory-level override demonstrating that more specific, closer-to-the-code instructions take precedence over the root file when they conflict.

## Custom Commands

Two reusable slash commands live in `.claude/commands/`:

| Command | Purpose |
|---------|---------|
| `/safe-test-check` | Runs test *collection* only (`pytest --collect-only`), never the live suite, and explicitly reminds that the full suite hits a real Databricks workspace |
| `/review-changes` | Reviews uncommitted changes against this repo's conventions - checks for missing test updates, misplaced business logic in `examples/`, and any risky edits under `use_cases/` |

## Scoped Tool Access

External tool access (MCP) is explicitly scoped in `.claude/settings.json` rather than left at default breadth - only read-only search is allowed, with write/create operations explicitly denied, since this project has no legitimate need for them.

## Author Built by [Sandarsh M](https://github.com/Sandarsh-M) 