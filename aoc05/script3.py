#!/bin/env python

with open("input","r") as f:
	l = f.readline().rstrip()

min = 50000
minl = ""
o = ""
for m in "abcdefghijklmnopqrstuvwxyz":
	for x in l:
		if len(o) == 0:
			o += x
			continue
		if x.lower() == m:
			continue
		if x.upper() == o[-1:].upper() and x.isupper() == o[-1:].islower():
			o= o[:-1]
			continue
		else:
			o += x
	if len(o) < min:
		min = len(o)
		minl = m
	o=""

print(min)
print(minl)
	
