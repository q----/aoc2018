#!/bin/env python
reg = [0 for x in range(6)]
reg[0] = 1
ip = 0
i = []
def addi (reg, a, b, c):
	reg[c] = reg[a] + b
	return 1

def seti (reg, a, b, c):
	reg[c] = a
	return 1

def mulr (reg, a, b, c):
	reg[c] = reg[a] * reg[b]
	return 1

def eqrr (reg,a,b,c):
	reg[c] = int(reg[a] == reg[b])
	return 1

def addr (reg,a,b,c):
	reg[c] = reg[a] + reg[b]
	return 1

def gtrr (reg,a,b,c):
	reg[c] = int(reg[a] > reg[b])
	return 1

def muli (reg,a,b,c):
	reg[c] = reg[a] * b
	return 1

def setr (reg,a,b,c):
	reg[c] = reg[a]
	return 1


with open("input","r") as f:
	l = f.readline()
	ip = int(l[4])
	l = f.readline()
	while l:
		i.append(l.rstrip().split(" "))
		l = f.readline()

while True:
	try:
		exec(i[reg[ip]][0] + "(reg," + i[reg[ip]][1] + "," + i[reg[ip]][2] + "," + i[reg[ip]][3] + ")")
		reg[ip] += 1
	except IndexError:
		print reg[0]
		break
