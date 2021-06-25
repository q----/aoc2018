#!/bin/env python
a = []

with open("input","r") as f:
	l = f.readline()
	while l:
		a.append(l.rstrip())
		l = f.readline()

def s(a,x,y):
	try:
		if x < 0 or y < 0:
			return 0
		if a[x][y] == "|":
			return 1
		elif a[x][y] == "#":
			return 2
		else:
			return 0
	except:
		return 0

def g(a):
	b = ["" for x in range(len(a))]
	for x in range(len(a)):
		for y in range(len(a[x])):
			q = {".":0,"|":1,"#":2}[a[x][y]]
			t = -1 if q == 1 else 0
			l = -1 if q == 2 else 0
			for n in (-1,0,1):
				for m in (-1,0,1):
					if s(a,x+n,y+m) == 1:
						t += 1
					elif s(a,x+n,y+m) == 2:
						l += 1
			if q == 0:
				if t >= 3:
					b[x] += "|"
				else:
					b[x] += "."
			elif q == 1:
				if l >= 3:
					b[x] += "#"
				else:
					b[x] += "|"
			else:
				if l >= 1 and t >= 1:
					b[x] += "#"
				else:
					b[x] += "."
	return b

def sc(a):
	l,t = 0,0
	for s in a:
		for y in s:
			if y == "|":
				t += 1
			elif y == "#":
				l += 1
	return t*l

def prin(a):
	for x in a:
		print x
	print ""

prin(a)
x = 0
#for x in range(1000000000):
while x < 1000000000:
	x += 1
	a = g(a)
	print x, sc(a)
