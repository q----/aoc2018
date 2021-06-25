#!/bin/env python

def addr (reg,a,b,c):
	reg[c] = reg[a] + reg[b]

def addi (reg,a,b,c):
	reg[c] = reg[a] + b

def mulr (reg,a,b,c):
	reg[c] = reg[a] * reg[b]

def muli (reg,a,b,c):
	reg[c] = reg[a] * b

def banr (reg,a,b,c):
	reg[c] = reg[a] & reg[b]

def bani (reg,a,b,c):
	reg[c] = reg[a] & b

def borr (reg,a,b,c):
	reg[c] = reg[a] | reg[b]

def bori (reg,a,b,c):
	reg[c] = reg[a] | b

def setr (reg,a,b,c):
	reg[c] = reg[a]

def seti (reg,a,b,c):
	reg[c] = a

def gtir (reg,a,b,c):
	reg[c] = int(a > reg[b])

def gtri (reg,a,b,c):
	reg[c] = int(reg[a] > b)

def gtrr (reg,a,b,c):
	reg[c] = int(reg[a] > reg[b])

def eqir (reg,a,b,c):
	reg[c] = int(a == reg[b])

def eqri (reg,a,b,c):
	reg[c] = int(reg[a] == b)

def eqrr (reg,a,b,c):
	reg[c] = int(reg[a] == reg[b])

def ex (dic,reg,o,a,b,c):
	cmd = dic[o] + "(reg," + a + "," + b + "," + c + ")"
	exec(cmd)


opr = list(("addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"))

d = {x:list(opr) for x in range(16)}
t = 0
with open("inp1","r") as f:
	l = f.readline()
	while l:
		orireg = list((int(l[9]),int(l[12]),int(l[15]),int(l[18])))
		l = f.readline()
		arg = l.rstrip().split(" ")
		l = f.readline()
		finreg = list((int(l[9]),int(l[12]),int(l[15]),int(l[18])))
		l = f.readline()
		l = f.readline()
		m = 0
		for x in opr:
			tmp = list(orireg)
			exec(x + "(tmp," + arg[1] + "," + arg[2] + "," + arg[3] + ")")
			if x in d[int(arg[0])] and len([i for i in range(len(finreg)) if finreg[i] == tmp[i]]) != 4:
				d[int(arg[0])].remove(x)

while max([len(d[x]) for x in d]) > 1:
	for m in d:
		if len(d[m]) == 1:
			for n in d:
				if len(d[n]) > 1:
					try:
						d[n].remove(d[m][0])
					except:
						pass

for x in d:
	d[x] = d[x][0]

reg = [0,0,0,0]
with open("inp2","r") as f:
	l = f.readline()
	while l:
		args = l.rstrip().split(" ")
		ex(d,reg,int(args[0]),args[1],args[2],args[3])
		l = f.readline()

print reg
