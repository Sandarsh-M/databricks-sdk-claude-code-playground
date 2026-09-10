# Project: databricks-python-sdk-playground

## Stack
- Python (repo originally documented as 3.12 - VERIFY against your actual
  environment before relying on this; discovered via Claude Code that a
  fresh machine may have 3.14 as the default python3, with no `python`
  alias on PATH at all - this file drifted out of sync with reality)
- Databricks Python SDK (authenticated via Databricks CLI profile)
- Unity Catalog, Workspace APIs, Jobs APIs
- pytest for testing
- Developed in VS Code


## Conventions
- `src` layout: all real code lives under `src/databricks_sdk_playground/`
- One module per domain concept: `client.py`, `catalogs.py`, `schemas.py`,
  `tables.py`, `jobs.py`, `workspace.py` - each wraps a related set of SDK calls
- `examples/` holds numbered, standalone scripts (01_connect.py, 02_list_catalogs.py...)
  that demonstrate one SDK capability each - not production code, don't add
  business logic here
- `use_cases/` holds end-to-end automation scripts that call the real SDK
  wrapper modules together - see "Never touch" below
- Use single quotes for all string literals in Python code, not double quotes

## Test command
First install dependencies (once per environment - note `python` may not be on
PATH, only `python3`, and a Homebrew `python3` is externally managed so a venv
is required):
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```
Then run the test commands below with `.venv/bin/pytest` (or activate the venv
first: `source .venv/bin/activate`).

Windows (PowerShell):
```powershell
$env:PYTHONPATH="src"
pytest
```
Mac/Linux:
```bash
PYTHONPATH=src pytest
```

## Never touch
- Do not run any script in `use_cases/` (trigger_job.py, deploy_notebook.py,
  monitor_job_run.py, etc.) without explicit confirmation first - these
  create real jobs and trigger real runs against a live Databricks workspace,
  not a local sandbox
- Do not edit `.venv/` or `.pytest_cache/` - both are auto-generated
- Running the full test suite is NOT side-effect-free: tests call the real
  Databricks SDK against a live workspace (auth profile "playground"), and
  test_workspace.py specifically creates a real workspace folder. Don't run
  the full suite casually - confirm the Databricks profile/environment first,
  or use `pytest --collect-only` to check test discovery without executing anything

## Naming
- Every file in `src/databricks_sdk_playground/` has a matching test file in
  `tests/` with the same name prefixed `test_` (client.py -> test_client.py)
- `examples/` and `docs/` share the same numeric prefix scheme
  (01_connect.py <-> 01_Getting_Started.md) - keep these in sync if you add a new one
- Branch names should be lowercase-with-hyphens (e.g. feature/add-logging) 