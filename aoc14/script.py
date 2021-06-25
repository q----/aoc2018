#!/bin/env python

r = 880751

a = [3,7]
e1 = 0
e2 = 1

while len(a) < r+10:
	for x in str(a[e1] + a[e2]):
		a.append(int(x))
	e1 = (e1 + 1 + a[e1]) % len(a)
	e2 = (e2 + 1 + a[e2]) % len(a)


print a[r:r+10]
