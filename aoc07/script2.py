#!/bin/env python

workers = 5

a = {k:k for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

def t(a):
	return ord(a) - 4

with file("input","r") as f:
	l = f.readline()
	while l:
		a[l[36]] += l[5]
		l = f.readline()

w = [(".",0) for i in range(workers)]
res = -1
while max([len(a[y]) for y in a]):
	for x in range(workers):
		if w[x][0] != ".":
			w[x] = (w[x][0],w[x][1] -1)
			if w[x][1] == 0:
				for m in a:
					a[m] = a[m].replace(w[x][0],"")
				w[x] = (".",0)
	for x in sorted(a.iterkeys()):
		if a[x] == x:
			if x in [y[0] for y in w]:
				continue
			for m in range(workers):
				if w[m][0] == ".":
					w[m] = (x, t(x))
					break
	res += 1
print res
