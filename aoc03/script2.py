#!/bin/env python

def tuplize (str):
        a = int(str.split(" ")[0].split("#")[1])
        b = int(str.split(" ")[2].split(",")[0])
        c = int(str.split(",")[1].split(":")[0])
        (d,e) = str.split(" ")[3].split("x")
        return (a,b,c,int(d),int(e))

def overlap (str1, str2):
	a = tuplize(str1)
	b = tuplize(str2)
	if a[0] == b[0]:
		return True
	if a[1] <= b[1]:
		if b[1] - a[1] < a[3]:
			if a[2] <= b[2]:
				if b[2] - a[2] < a[4]:
					return False
			else:
				if a[2] - b[2] < b[4]:
					return False
	else:
		return overlap(str2,str1)
	return True

with open("input","r") as f:
	l = f.readline()
	while l:
		with open("input","r") as f2:
			l2 = f2.readline()
			while(overlap(l,l2)):
				l2 = f2.readline()
				if not l2:
					print(tuplize(l)[0])
					break
		l = f.readline()

