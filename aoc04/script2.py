#!/bin/env python

d = {}
g = 0
s = -1

with open("good_input","r") as f:
	l = f.readline()
	while l:
		if l[19] == 'G':
			g = int(l.split("#")[1].split(" ")[0])
		elif l[19] == 'f':
			s = int(l[15:17])
		else:
			if g not in d:
				d[g] = {}
			for m in range(s,int(l[15:17])):
				if m not in d[g]:
					d[g][m] = 0
				d[g][m] += 1
		l = f.readline()	

for n in d:
	for z in d[n]:
		if d[n][z] > d[g][m]:
			(g,m) = (n,z)

print(m * g)	

