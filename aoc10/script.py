#!/bin/env python

import sys

a = []

def parse(l):
	a = int(l.split("<")[1].split(",")[0].rstrip())
	b = int(l.split(",")[1].split(">")[0].rstrip())
	c = int(l.split("<")[2].split(",")[0].rstrip())
	d = int(l.split(",")[2].split(">")[0].rstrip())
	return (a,b,c,d)

def tr(a,t):
	b = []
	for x in a:
		b.append((x[0] + t * x[2], x[1] + t * x[3]))
	return b

def ra(a):
	return (min([x[0] for x in a]),max([x[0] for x in a]),min([x[1] for x in a]),max([x[1] for x in a]))

def prin(a):
	r = ra(a)
	for y in range(ra(a)[2],ra(a)[3]+1):
		for x in range(ra(a)[0],ra(a)[1]+1):
			if (x,y) in a:
				sys.stdout.write("#")
			else:
				sys.stdout.write(" ")
		sys.stdout.write("\n")


def negative(a):
	for x in a:
		if min(x) < 0:
			
			return True
	return False


with open("input2","r") as f:
	l = f.readline()
	while l:
		a.append(parse(l))
		l = f.readline()

t = 0
ts = []
while t < 100000:
	if not negative(tr(a,t)):
		ts.append(t)
	t += 1

prin(tr(a,sum(ts)/len(ts)))
print(sum(ts)/len(ts))
