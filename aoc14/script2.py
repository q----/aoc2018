#!/bin/env python

r = 633601

a = [3,7]
e1 = 0
e2 = 1

while a[-6:] != [6,3,3,6,0,1] and a[-7:-1] != [6,3,3,6,0,1]:
	for x in str(a[e1] + a[e2]):
		a.append(int(x))
	e1 = (e1 + 1 + a[e1]) % len(a)
	e2 = (e2 + 1 + a[e2]) % len(a)


print a[-7:]
print len(a) - 7
