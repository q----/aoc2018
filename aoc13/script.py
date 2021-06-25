#!/bin/env python
class cart:
	def __init__(self,pos,dire):
		self.pos = pos
		self.dire = dire
		self.inte = -1
		self.turn = 0
	def move(self,a):
		self.pos = (self.pos[0] + self.dire[0], self.pos[1] + self.dire[1])
		self.turn += 1
		if a[self.pos[1]][self.pos[0]] == "\\":
			self.dire = (self.dire[1],self.dire[0])
		elif a[self.pos[1]][self.pos[0]] == "/":
			self.dire = (-self.dire[1],-self.dire[0])
		elif a[self.pos[1]][self.pos[0]] == "+":
			if self.inte == -1:
				self.dire = (self.dire[1],-self.dire[0])
				self.inte = 0
			elif self.inte == 0:
				self.inte = 1
			elif self.inte == 1:
				self.dire = (-self.dire[1],self.dire[0])
				self.inte = -1

def gc(cars,a):
	mint = min([c.turn for c in cars])
	miny = min([c.pos[1] for c in cars])
	minx = min([c.pos[0] for c in cars])
	ca = cart((10000,10000),(1,0))
	f = 1
	for c in cars:
		if c.turn == mint and c.pos == (minx,miny):
			ca = c
			break
		if c.turn == mint and c.pos[1] == miny:
			ca = c
			f = 0
			continue
		if f and c.turn == mint:
			if c.pos[1] < ca.pos[1]:
				ca = c
			elif c.pos[1] == ca.pos[1]:
				if c.pos[0] < ca.pos[0]:
					ca = c
	ca.move(a)

def coll(cars):
	for c in cars:
		for d in cars:
			if c.pos == d.pos and c.dire != d.dire:
				print c.pos
				return False
	return True

def d (c):
	if c == "^":
		return (0,-1)
	if c == ">":
		return (1,0)
	if c == "<":
		return (-1,0)
	if c == "v":
		return (0,1)
	return None


t = []
with open("input","r") as f:
	l = f.readline()
	while l:
		t.append(l)
		l = f.readline()

cars = []
for l in range(len(t)):
	for c in range(len(t[l])):
		if t[l][c] in "><v^":
			cars.append(cart((c,l),d(t[l][c])))
			print c,l,d(t[l][c])
	t[l] = t[l].replace(">","-").replace("<","-").replace("^","|").replace("v","|")



while coll(cars):
	gc(cars,t)
