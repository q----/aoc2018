#!/bin/env python
import sys
sys.setrecursionlimit(12341234)

with open("input","r") as f:
	l = f.readline().rstrip().split(" ")

def gogogo(line):
	nodes = []
	total = 0	
	numc = int(line.pop(0))
	numm = int(line.pop(0))
	if not numc:
		for x in range(int(numm)):
			total += int(line.pop(0))
		return total
	for x in range(int(numc)):
		nodes.append(gogogo(line))
	for x in range(int(numm)):
		try:
			total += nodes[int(line.pop(0))-1]
		except:
			pass
	return total

print gogogo(l)
