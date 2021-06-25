#!/bin/env python

a = [[0] * 1000 for i in range(1000)]

def tuplize (str):
	a = int(str.split(" ")[0].split("#")[1])
	b = int(str.split(" ")[2].split(",")[0])
	c = int(str.split(",")[1].split(":")[0])
	(d,e) = str.split(" ")[3].split("x")
	return (a,b,c,int(d),int(e))

with open("input","r") as f:
	l = f.readline().rstrip()
	while l:
		t = tuplize(l)
		for i in range(t[3]):
			for j in range(t[4]):
				 a[t[1]+i][t[2]+j] += 1
		l = f.readline().rstrip()
		
count=0
for i in range(1000):
	for j in range(1000):
		if a[i][j] >= 2:
			count += 1

print (count)
