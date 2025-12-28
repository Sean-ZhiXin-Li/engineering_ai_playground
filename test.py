import json
from datetime import datetime
import os

passed = False
failure_reason = None
param =float( input())
a = 12
b = 123
c = 135
if param > 1:
	print(abs(param - 1))
	passed = True
else:
	failure_reason = "param <= 1"

if a + b == c:
	print("Hello Engineering World!!!")
else:
	print("Well, you need to check your numbers, ensure you can into a real engineering world")

timestamp = datetime.now().isoformat()
metrics ={
	"param": param,
	"value": abs(param - 1),
	"passed": passed,
	"timestamp": timestamp,
	"bad": [1, 2, 3],
	"failure_reason": failure_reason
}

metrics_path = "metrics.json"

if os.path.exists(metrics_path):
	with open(metrics_path, 'r') as f:
		history = json.load(f)
else:
	history = []

if not isinstance(history, list):
	history = []

for rec in history:
	if "failure_reason" not in rec:
		rec["failure_reason"] = None if rec["passed"] else "legacy_missing_reason"

history.append(metrics)

with open(metrics_path, 'w') as f:
	json.dump(history, f, indent = 2)
