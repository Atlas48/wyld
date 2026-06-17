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
	new = w, floor(w * 5 / 7 + 0.5)
else:
	new = floor(h * 7 / 5 + 0.5), h

print("%dx%d"%new)
