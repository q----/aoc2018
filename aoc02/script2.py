#!/bin/env python

def diff (st1, st2):
	dif = ""
	for x in range(0,len(st1)):
		if st1[x] == st2[x]:
			 dif += st1[x]
	return dif

with open("input","r") as f:
	l = f.readline()
	while l:
		with open("input","r") as f2:
			l2 = f2.readline()
			while l2:
				if len(diff(l,l2)) + 1 == len(l):
					print diff(l,l2)
				l2 = f2.readline()
		l = f.readline()
