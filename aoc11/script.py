#!/bin/env python

sn = 2568

def p (x,y):
	return ((x+10)*y + sn) * (x+10)/100%10 -5

max = 0
m,n,g = 0,0,0
for s in range(1,20):
	for x in range(1,302-s):
		for y in range(1,302-s):
			t = 0
			for l in range(s):
				for q in range(s):
					t += p(x+l,y+q)
			if max <= t:
				max = t
				m = x
				n = y
				g = s

print m
print n
print g
