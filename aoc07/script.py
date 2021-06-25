#!/bin/env python

a = {k:k for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}



with file("input","r") as f:
	l = f.readline()
	while l:
		a[l[36]] += l[5]
		l = f.readline()

res = ""
for y in range(26):
	for x in sorted(a.iterkeys()):
		if a[x] == x:
			res += x
			for m in a:
				a[m] = a[m].replace(x,"")
			break

print a
print res
