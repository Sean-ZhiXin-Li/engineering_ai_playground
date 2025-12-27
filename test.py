import json
from datetime import datetime
import os

passed = False
param =float( input())
a = 12
b = 123
c = 135
if param > 1:
	print(param - 1)
	passed = True
else:
	data = (abs(param - 1))
	with open('Output.txt', 'w') as f:
		f.write(f"{data}\n")
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
	"bad": [1, 2, 3]
}

metrics_path = "metrics.json"

if os.path.exists(metrics_path):
	with open(metrics_path, 'r') as f:
		history = json.load(f)
else:
	history = []

if not isinstance(history, list):
	history = []

history.append(metrics)

with open(metrics_path, 'w') as f:
	json.dump(history, f, indent = 2)


