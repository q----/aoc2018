#!/bin/env python

pnum = 416 
lsc = 7161700

s = [0 for x in range(pnum)]
m = 1
c = [0]
i = 0

while m < lsc:
	if m % 10000 == 0:
		print(m)
	if m%23 == 0:
		i = (i-7)%len(c)
		s[m%pnum] += m + c.pop(i)
	else:
		i = (i+2)%len(c)
		c.insert(i,m)
	m += 1

print max(s)
