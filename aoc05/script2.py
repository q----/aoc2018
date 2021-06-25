#!/bin/env python

with open("input","r") as f:
	l = f.readline().rstrip()

o = ""
for x in l:
	if len(o) == 0:
		o += x
		continue
	if x.upper() == o[-1:].upper() and x.isupper() == o[-1:].islower():
		o= o[:-1]
		continue
	else:
		o += x
print(o)
print(len(o))
	
