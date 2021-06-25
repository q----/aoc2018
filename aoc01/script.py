#!/bin/env python

import os

flag = False
s = {0}
t = 0

while not flag:
	with open('input','r') as f:
		l = f.readline()
		while l and not flag:
			t += int(l)
			if t in s:
				print t
				flag = True
			s.add(t)
			l = f.readline()
