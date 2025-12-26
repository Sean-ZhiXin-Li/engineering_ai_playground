## Debug #001 — JSON serialization failure (set)

- Trigger: Added a Python `set` into `metrics` (e.g. `{"bad": {1,2,3}}`).
- Symptom: Program crashed at `json.dump(...)` and `metrics.json` was not written/updated.
- Error: `TypeError: Object of type set is not JSON serializable`
- Fix: Converted the `set` to a JSON-serializable type (`list`, e.g. `[1,2,3]`).
- Lesson: Only store JSON-serializable types in `metrics` (dict/list/str/int/float/bool/null).
