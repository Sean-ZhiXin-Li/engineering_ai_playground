param =float( input())
a = 12
b = 123
c = 135
if param > 1:
	print(param - 1)
else:
	data = (abs(param - 1))
	with open('Output.txt', 'w') as f:
		f.write(f"{data}\n")
if a + b == c:
	print("Hello Engineering World!!!")
else:
	print("Well, you need to check your numbers, ensure you can into a real engineering world")

