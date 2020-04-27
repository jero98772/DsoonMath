# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from DsoonMath import quantity ,answertime,answer, p, error,simplyfie
import time
import random


def varius():
	limit = 999
	level = 5
	liste =[]
	i = 0
	lm = 21
	expresion = 0
	for j in range(lm):
		expresion = quantity(levelop= level+4 ,leveDt=level ,limit=limit*100)
		liste.append(str(j)+" level :expert-9")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level+3 ,leveDt=level ,limit=limit*100)
		liste.append(str(j)+" level :expert-8")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level+2 ,leveDt=level ,limit=limit*100)
		liste.append(str(j)+" level :expert-7")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level+1 ,leveDt=level ,limit=limit*100)
		liste.append(str(j)+" level :expert-6")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level ,leveDt=level ,limit=limit*100)
		liste.append(str(j)+" level :expert-5")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level -1,leveDt=level-1 ,limit=limit*10)
		liste.append(str(j)+" level :hard-4")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level -2,leveDt=level-2 ,limit=limit)
		liste.append(str(j)+" level :medium-3")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= level -3,leveDt=level-3,limit=limit)
		liste.append(str(j)+" level : easy-2")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= 0,leveDt=0,limit=int(limit*10))
		liste.append(str(j)+" level : easy-1.3")
		liste.append(expresion)		
	for j in range(lm):
		expresion = quantity(levelop= 0,leveDt=0,limit=int(limit))
		liste.append(str(j)+" level : easy-1.2")
		liste.append(expresion)
	for j in range(lm):
		expresion = quantity(levelop= 0,leveDt=0,limit=int(limit/10))
		liste.append(str(j)+" level : baby-1.1")
		liste.append(expresion)

	i2= 0
	level = 5
	mitad = (len(liste)//2)+1


	for k in liste:
		a = i
		if i  % 2 == 1 :
			a = answer(k)
		if i2 ==lm and level > 0 :
			i2 = 0
			level -=1
		elif i ==mitad:#+(mitad): 
			break
		liste.append(" question "+str(i)+" answer "+str(a))
		i+= 1
		i2 += 1 

	for i in liste:
		p(i)
	return varius
def spcecifie(levelop= 0 ,leveDt= 1,limit= 999):
	limit = 999
	liste =[]
	i = 0
	lm = 21
	expresion = 0
	for j in range(lm):
		expresion = quantity(levelop= levelop ,leveDt= leveDt,limit= limit)
		liste.append(str(j)+" level :")
		liste.append(expresion)
	for i in liste:
		p(i)
	return liste
def inputprogram():
	
	limit = 99
	level = 5
	for i in range(10):
		expresion = quantity(levelop= 5,leveDt=3,limit=limit)
		print(i,expresion)		

		p(error(input(), answer(expresion)))
		p(answer(expresion))
	print()
def timeprogram():
	
	limit = 99
	level = 5
	for i in range(5):
		expresion = quantity(levelop= 0,leveDt=1,limit=limit)
		print(i,expresion)		
		time.sleep(60*0.4)
		p(answer(expresion))
	print()
def spcecifieexcerises():

	limit = 999
	level = 1
	for i in range(5):
		expresion = simplyfie(level=level,limit=limit)
		print(i,expresion)		
		p(answer(expresion))
def sets():
	x = {type(1.0)}
	aSets = { type(1),type(1.0),type(1j),type(0b011010101)}
	print(x.union(aSets))
	print(x | aSets)

def test():
	
	limit = 99
	for i in range(10):
		expresion = quantity(levelop= 3 ,leveDt=0 ,limit=limit)
		print(i,")",expresion)		

	print()
def mix():
	limit =9* (10*random.randrange(0,10))
	expresion = quantity(levelop= random.randrange(0,9) ,leveDt=random.randrange(0,4) ,limit=limit)
	print(expresion)
	return expresion
