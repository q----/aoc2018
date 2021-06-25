#!/bin/env python

a = []

with open("input","r") as f:
	l = f.readline()
	while l:
		a.append(l.rstrip().split(", "))
		l = f.readline()

def di (x,y):
	return abs(int(x[0])-int(y[0])) + abs(int(x[1])-int(y[1]))

def mi (x):
	flag = False
	b = None
	for m in a:
		if not b:
			b = m
			continue
		if di(x,b) > di(m,x):
			b = m
			flag = False
		elif di(x,b) == di(m,x):
			flag = True
	return (0,0) if flag else b


m,n = 0,0
for x in a:
	if x[0] > m:
		m =int( x[0])
	if x[1] > n:
		n =int( x[1])

d={}

for x in a:
	d[x[0]] = 0
d[0] = 0


for x in range(-490,m+490):
	for y in range(-490,n+490):
		d[mi((x,y))[0]]+=1

d = {(x,d[x]) for x in d if d[x] < 10000}
print d

d[0] = 0
m = 0
for x in d:
	if d[x] > d[m]:
		m = x

print (d[m])
