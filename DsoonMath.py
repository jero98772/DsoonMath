# -*- coding: utf-8 -*-
#!/usr/bin/env python 

#import math
#math lib is for add trigonometric funtions and log functions 
import random
from pseudorandom import prandom
from datetime import datetime
import time
#p() is fast debug print i use for see error in a big log of errors 
def p(*args):
	for i in args:
		print("\n",i,"\n")
def	basicoperators(rand = random.randrange(0,4)):

	choise = rand
	if choise== 0:
		operator="+"
	elif choise== 1:
		operator="-"
	elif choise== 2:
		operator="*"
	elif choise== 3:
		operator="/"
	elif choise== 4:
		operator="%"
	return str(operator)
# reason why return the operator as string because will go through the function eval or be print with a number
def avasedoperators(rand = random.randrange(1,4)):
	choise = rand
	lim =15
	if choise== 0:
		operator = ""
	elif choise== 1:
		operator= "**(1/2)"
	elif choise== 2:
		operator= "**(2)"
	elif choise== 3:
		operator= "**("+str(random.randrange(-lim,lim))+"/"+str(random.randrange(-lim,lim))+")"
	if choise== 4:
		operator= "**("+str(random.randrange(-lim,lim))+")"
	return str(operator)
def operators(rand = random.randrange(0,1),difcult  = random.randrange(1,4)):
	operator = "+"
	choise = rand


	if difcult == 1 or  difcult == 0 :
		operatorB = 1
		operatorA = 1
		choise = 0

	elif difcult == 2:
		operatorB = 5
		operatorA = 1
		choise = 0

	elif difcult == 3:
		operatorB = 5
		operatorA = 3
		choise = 1

	else:# difcult == 3:
		operatorB = 5
		operatorA = 5
		choise = 1
	if choise == 0:
		operator = basicoperators(random.randrange(0,operatorB))
	elif choise == 1:
		operator = avasedoperators(random.randrange(0,operatorA))+basicoperators(random.randrange(0,operatorB))
	return str(operator)
def typenum(rand= random.randrange(0,10),difcult  = random.randrange(1,3),limit = 9999):
	typenum = 0
	choise = rand
	if difcult == 0:
		choise = 0
	elif difcult == 1:
		choise = random.randrange(0,3)
	elif difcult == 2:
		choise = random.randrange(0,6)
	elif difcult == 3:
		choise = random.randrange(0,14)
	elif difcult == 4:
		choise = random.randrange(0,20)
	
	#level
	#1
	if choise == 0:
		typenum = random.randint(-limit,limit)
	elif choise == 1:
		typenum = round(random.random(),3)
	elif choise == 2:
		typenum = round(random.randint(-limit,limit)*0.01,2)
	#2
	elif choise== 3:
		typenum = bin(random.randint(-limit,limit))
	elif choise== 4:
		typenum = str(random.randint(-limit,limit))+"*x"
	elif choise== 5:
		typenum = complex(random.randint(-limit,limit))
	#3
	elif choise== 6:
		typenum = hex(random.randint(-limit,limit))
	elif choise== 7:
		typenum = oct(random.randint(-limit,limit))
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
		typenum = str(random.randint(-limit,limit))+"x**"+str(random.randrange(0,10))
	elif choise== 16:
		typenum = str(random.randint(-limit,limit))+"y**"+str(random.randrange(0,10))
	elif choise== 17:
		typenum = str(random.randint(-limit,limit))+"*z"
	elif choise== 18:
		typenum = str(random.randint(-limit,limit))+"z**"+str(random.randrange(0,10))
	elif choise== 19:
		typenum = str(random.randint(-limit,limit))+"*y"
	return str(typenum) 
"""
import numpy as np
def arrays(rand = random.randrange(0,6)):
	if choise== 7:
		typenum = np.random.randint(limit, size=(3,3))
#disabled for now for future parts of the project
"""
def quantity(levelop= 2,leveDt=1,limit=9999):
	if levelop > 4 :
		levelop = 4

	for level in [levelop,leveDt]:
		if level == 0:
			optionypenums = 0
			rand = 2
		elif level == 1:
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
			operation += typenum(selctnum,difcult = leveDt,limit=limit)
		else:
			operation += operators(optionypenums,levelop)
			operation += typenum(selctnum,difcult = leveDt,limit=limit)

	return operation
#unknowns = lambda a, b, c: ((-b + ((b * b) - (4 * a * c))**1/2) / (2 * a), (-b - (((b * b) - (4 * a * c)))**(1/2)) / (2 * a))#is cuadraticformula is called for find unknowns in a fromula
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
def answer(  expresion = quantity()):
	try:
		answer = str(eval(expresion))
	except :
		answer = "coming soon"
#coming soon can solove ecuation of frist grade and second grade this is the impresión

	return answer