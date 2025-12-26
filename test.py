import json
from datetime import datetime

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

with open("metrics.json", 'w') as f:
	json.dump(metrics, f, indent = 2)
