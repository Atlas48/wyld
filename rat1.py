#!/usr/bin/env python3
#!/usr/bin/env python3
from sys import stderr, argv
from math import floor

try:
	w = float(argv[1])
	h = float(argv[2])
except (IndexError, ValueError):
	print("Requries a height and a width argument.")
	sys.exit(1)

if w * 5 <= h * 7:
	new = w, (w*5)//7
else:
	new = (h*7)//5, h

print("%dx%d"%new)
