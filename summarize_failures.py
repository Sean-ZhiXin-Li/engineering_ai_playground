import json
from collections import Counter

METRICS_PATH = "metrics.json"

with open(METRICS_PATH, "r") as f:
    data = json.load(f)

reasons = []
for rec in data:
    passed = rec.get("passed", None)
    if passed is False:
        reasons.append(rec.get("failure_reason", None))

counts = Counter(reasons)

for reason, cnt in counts.items():
    print(f"{reason}: {cnt}")