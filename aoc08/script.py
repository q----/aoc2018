#!/bin/env python

class Tree(object):
	def __init__(self, metadata=None, children=None):
		self.metadata = []
		self.children = []
		if metadata is not None:
			for m in metadata:
				self.add_metadata(m)
		if children is not None:
			for c in children:
				self.add_child(c)

	def add_child(self, node):
		assert isinstance(node, Tree)
		self.children.append(node)
	def add_metadata(self, m):
		self.metadata.append(m)


with open("input","r") as f:
	l = f.readline().rstrip().split(" ")

def gogogo(line):
	total = 0
	numc = line.pop(0)
	numm = line.pop(0)
	for x in range(int(numc)):
		total += int(gogogo(line))
	for x in range(int(numm)):
		total += int(line.pop(0))
	return total

print gogogo(l)
