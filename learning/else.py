#!/usr/bin/env python3

#A small example to show off the functionality of an 'else'
#statement following a loop
print("loop success example:")
for i in range(0, 10):
	print(i)
else:
	print("done")
print("loop fail example")
for i in range(0, 10):
	print(i)
	if (i == 5):
		break
else:
	print("done")
