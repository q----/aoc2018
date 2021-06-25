#!/bin/env python

d = {}
a = {}

def g(l):
	o = {}
	for x in l:
		try:
			o[x] = d[l[x-2] + l[x-1] + l[x] + l[x+1] + l[x+2]]
		except Exception:
			o[x] = '.'
	return o

with open("input","r") as f:
	l = f.readline()
	q = l.split(" ")[2].rstrip() + ''.join(['.' for x in range(300)])
	a = {x:q[x] for x in range(300)}
	for x in range(-10,0):
		a[x] = "."
	l = f.readline()
	l = f.readline()
	while l:
		d[l.split(" => ")[0]] = l.split(" => ")[1].rstrip()
		l = f.readline()

p = 0

for x in range(20):
	a= g(a)
	st = ""
	t = 0
	for s in a:
		if a[s] == "#":
			t += s
	print x,t,t-p
	p = t
