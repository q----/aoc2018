#!/bin/env python

with open("input","r") as f:
	l = f.readline().rstrip()

i = 0

while i < len(l)-1:
	if l[i].upper() == l[i+1].upper() and l[i].isupper() == l[i+1].islower():
		l = l[:i] + l[i+2:]
		i = 0
		continue
	i += 1

print(l)
print(len(l))
