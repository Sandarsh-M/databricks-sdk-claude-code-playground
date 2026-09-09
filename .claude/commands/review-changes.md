---
description: Review my uncommitted changes against this repo's conventions
allowed-tools: Read, Grep, Glob, Bash
---

Look at the current uncommitted changes (git diff and git status).

Check specifically:
- If a file was added/changed under src/databricks_sdk_playground/, is there
  a matching test_<name>.py update in tests/? Flag it if not.
- If a new example was added to examples/, does it follow the numbered
  prefix convention, and is there a matching numbered doc in docs/?
- Does anything touch use_cases/ - if so, flag loudly that those scripts
  have real side effects against a live Databricks workspace and should
  not be run casually.
- Any hardcoded credentials, workspace URLs, or tokens that should come
  from the Databricks CLI profile instead?

Report as a short punch list. Do not make any edits yourself - review only.
