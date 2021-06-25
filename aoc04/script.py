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
				d[g] = 0
			d[g] += int(l[15:17])-s
		l = f.readline()	


for x in d:
	if d[x] > d[g]:
		g = x

a = [0 for x in range(60)]

with open("good_input","r") as f:
        l = f.readline()
        while l:
                if l[19] == 'G':
                        g2 = int(l.split("#")[1].split(" ")[0])
                elif l[19] == 'f' and g2 == g:
                        s = int(l[15:17])
                else:
			if g2 == g:
				for m in range(s,int(l[15:17])):
					a[m] += 1
                l = f.readline()

max = 0
for n in range(len(a)):
	if a[max] < a[n]:
		max = n

print(max * g)	

