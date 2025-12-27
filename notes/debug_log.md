## Debug #001 — JSON serialization failure (set)

- Trigger: Added a Python `set` into `metrics` (e.g. `{"bad": {1,2,3}}`).
- Symptom: Program crashed at `json.dump(...)` and `metrics.json` was not written/updated.
- Error: `TypeError: Object of type set is not JSON serializable`
- Fix: Converted the `set` to a JSON-serializable type (`list`, e.g. `[1,2,3]`).
- Lesson: Only store JSON-serializable types in `metrics` (dict/list/str/int/float/bool/null).

## Debug #002 — Metrics history structure mismatch
- Trigger: Manually edited `metrics.json` to `{}` (JSON root became an object, not a list).
- Symptom: No crash, but previous history was discarded and a new history list was created.
- Error: None (schema check prevented `append` on a non-list type).
- Fix: After `json.load`, validate `history` with `isinstance(history, list)`. If not a list, reset `history = []` before appending.
- Lesson: Never assume persisted JSON schema is correct. Always validate root type (list vs dict) before mutating metrics history.
