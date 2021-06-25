#!/bin/env python

def Rep (st, c):
	d = {}
	for x in st:
		try:
			d[x]+=1
		except:
			d[x]=1
	for k in d:
		if d[k] == c:
			return True
	return False


t = 0
th = 0

with open("input","r") as f:
	l = f.readline()
	while l:
		t  += 1 if Rep(l,2) else 0
		th += 1 if Rep(l,3) else 0

		l = f.readline()

print (t*th)
