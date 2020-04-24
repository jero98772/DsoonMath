# -*- coding: utf-8 -*-
from math import *
import random
import numpy as np
from pseudorandom import prandom
from datetime import datetime
import time
def p(*args):
	for i in args:
		print("\n",i,"\n")
def	basicoperators(rand = random.randrange(0,4)):
	choise = rand
	if choise== 4:
		operator="%"
	elif choise== 3:
		operator="/"
	elif choise== 2:
		operator="*"
	elif choise== 1:
		operator="-"
	elif choise== 0:
		operator="+"
	return str(operator)
def avasedoperators(rand = random.randrange(1,4)):
	choise = rand
	lim =15
	if choise== 0:
		operator = ""
	elif choise== 1:
		operator="**(1/2)"
	elif choise== 2:
		operator="**("+str(random.randrange(-lim,lim))+")"
	elif choise== 3:
		operator="**("+str(random.randrange(-lim,lim))+"/"+str(random.randrange(-lim,lim))+")"
	if choise== 4:
		operator="**(2)"
	return str(operator)
def operators(rand = random.randrange(0,1),difcult  = random.randrange(1,3)):
	operator = "+"
	choise = rand
	if difcult == 1:
		operatorB = 1
		operatorA = 4
		choise = 0
	elif difcult == 2:
		operatorB = 4
		operatorA = 4
	elif difcult == 3:
		operatorB = 4
		operatorA = 4
	if choise == 0:
		operator = basicoperators(random.randrange(0,operatorB))
	elif choise == 1:
		operator = avasedoperators(random.randrange(0,operatorA))+basicoperators(random.randrange(0,operatorB))
	return str(operator)
def typenum(rand= random.randrange(0,10),difcult  = random.randrange(1,3),limt = 9999):
	typenum = 0
	choise = rand
	if difcult == 1:
		choise = random.randrange(0,2)
	elif difcult == 2:
		choise = random.randrange(0,7)
	elif difcult == 3:
		choise = random.randrange(0,10)
	#level
	#1
	if choise == 0:
		typenum = random.randint(-limt,limt)
	elif choise == 1:
		typenum = round(random.random(),3)
	elif choise == 2:
		typenum = round(random.randint(-limt,limt)*0.01,2)
	#2
	elif choise== 3:
		typenum = bin(random.randint(-limt,limt))
	elif choise== 4:
		typenum = str(random.randint(-limt,limt))+"*x"
	elif choise== 5:
		typenum = complex(random.randint(-limt,limt))
	elif choise== 6:
		typenum = hex(random.randint(-limt,limt))
	elif choise== 7:
		typenum = oct(random.randint(-limt,limt))
	#3	
	elif choise== 8:
		typenum = str(random.randint(-limt,limt))+"y"
	elif choise== 9:
		typenum = str(random.randint(-limt,limt))+"x"+avasedoperators()+basicoperators()
	elif choise== 10:
		typenum = str(random.randint(-limt,limt))+"x"+avasedoperators()+basicoperators()
	return str(typenum) 
def arrays(rand = random.randrange(0,6)):
	if choise== 7:
		typenum = np.random.randint(limt, size=(3,3))

def quantity(levelop= 2,leveDt=1,limt=9999):
	for level in [levelop,leveDt]:
		if level == 1:
			optionypenums = 4
			rand = random.randrange(2,3)
		elif level == 2:
			rand = random.randrange(2,6)
			optionypenums = 6
		elif level == 3:
			rand = random.randrange(2,8)
			optionypenums =10

	operation = ""
	now = int(datetime.now().strftime('%S'))
	psdop = prandom(valorInicial=now,multiplicador=now+2,mod = 6,veces=4)
	listop = psdop.vector()

	psdtynum = prandom(valorInicial=now,multiplicador=now+7,mod = 7,veces=7)
	listpsdtnum = psdtynum.vector()

	for i,selctnum,optionypenums in zip(range(rand),listpsdtnum,listop):
		if i == 0:
			operation += typenum(selctnum,level,limt)
		else:
			operation += operators(optionypenums,level)
			operation += typenum(selctnum,level,limt)

	return operation
#unknowns = lambda a, b, c: ((-b + ((b * b) - (4 * a * c))**1/2) / (2 * a), (-b - (((b * b) - (4 * a * c)))**(1/2)) / (2 * a))
def answertime( limit , expresion ,Vtime):
	for x in range(limit):
		if Vtime == False:
			Vtime = limit*len(str(limit))	
		else:
			try:
				Vtime = Vtime
				
			except :
				Vtime = limit*len(str(limit))
			if not Vtime:
				Vtime = limit*len(str(limit))
	answer = str(eval(expresion))
	time.sleep(Vtime)
	return answer
def answer( limit , expresion = quantity()):
	for i in "qwertyuiopñlkjhgfdsazxcvbnm":
		if i in str(expresion):
			answer = "proximamente la solucion"
	else:
		answer = str(eval(expresion))
	return answer