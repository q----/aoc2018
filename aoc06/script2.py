#!/bin/env python

a = []

with open("input","r") as f:
	l = f.readline()
	while l:
		a.append(l.rstrip().split(", "))
		l = f.readline()

def di (x,y):
	return abs(int(x[0])-int(y[0])) + abs(int(x[1])-int(y[1]))

m,n = max([int(x[0]) for x in a]),max([int(x[1]) for x in a])

k = 0
for x in range(m+1):
	for y in range(n+1):
		if sum([di(g,(x,y)) for g in a]) < 10000:
			k += 1

print k
print m
print n
