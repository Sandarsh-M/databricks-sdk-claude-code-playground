---
description: Safely check test status without hitting the live Databricks workspace
allowed-tools: Bash, Read
---

Run test collection ONLY first, never the full live suite automatically:

PYTHONPATH=src pytest --collect-only

Report how many tests were found and whether collection succeeded cleanly.

Do NOT run the full test suite (plain `pytest` or `pytest tests/`) even if
collection succeeds - remind me that doing so calls the real Databricks SDK
against the "playground" workspace profile, and that test_workspace.py
creates a real workspace folder. Only run the full suite if I explicitly
say so in this same conversation after seeing this report.
