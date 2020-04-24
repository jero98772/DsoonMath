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
	else:# difcult == 3:
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
		choise = random.randrange(0,5)
	elif difcult == 3:
		choise = random.randrange(0,13)
	elif difcult == 4:
		choise = random.randrange(0,20)
	
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
	#3
	elif choise== 6:
		typenum = hex(random.randint(-limt,limt))
	elif choise== 7:
		typenum = oct(random.randint(-limt,limt))
	elif  choise== 8:
		typenum = 3.14159265358979323846#pi

	elif choise== 9:
		typenum = 1.41421356237309504#sqrt(2)

	elif choise== 10 :
		typenum =1.73205080756887729352#sqrt(3)

	elif choise== 11:
		typenum =1.61803398874989484820#phi

	elif choise== 12:
		typenum =2.71828182845904523536#e

	elif choise== 13:
		typenum =2.23606797749978969640#sqrt(5)

	elif choise== 14:
		typenum =1.25992104989487316476 #sqrt(2)**3
	#4	
	elif choise== 15:
		typenum = str(random.randint(-limt,limt))+"x**"+str(random.randrange(0,10))
	elif choise== 16:
		typenum = str(random.randint(-limt,limt))+"y**"+str(random.randrange(0,10))
	elif choise== 17:
		typenum = str(random.randint(-limt,limt))+"*z"
	elif choise== 18:
		typenum = str(random.randint(-limt,limt))+"z**"+str(random.randrange(0,10))
	elif choise== 19:
		typenum = str(random.randint(-limt,limt))+"*y"
	return str(typenum) 
def arrays(rand = random.randrange(0,6)):
	if choise== 7:
		typenum = np.random.randint(limt, size=(3,3))

def quantity(levelop= 2,leveDt=1,limt=9999):
	if levelop > 4 :
		levelop = 4
	for level in [levelop,leveDt]:
		if level == 1:
			optionypenums = 4
			rand = random.randrange(2,3)
		elif level == 2:
			rand = random.randrange(2,6)
			optionypenums = 6
		else:# level == 3:
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