# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from DsoonMath import quantity ,answertime,answer, p
from errors import error
import time
limit = 999
level = 4
liste =[]
i = 0
lm = 21
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
	liste.append(str(j)+" level : easy-2")
	liste.append(expresion)
	expresion = quantity(levelop= level -3,leveDt=level-3,limit=limit)
for j in range(lm):
	liste.append(str(j)+" level : baby-1")
	liste.append(expresion)
	expresion = quantity(levelop= 1,leveDt=0,limit=int(limit/10))
i2= 0
level = 5
mitad = (len(liste)/2)
for k in liste:
	a = i
	if i  % 2 == 1 :
		a = answer(k)
	if i2 ==lm and level > 0 :
		i2 = 0
		level -=1
	elif i ==mitad+(mitad): 
		break
	liste.append(" question "+str(i)+" answer "+str(a))
	i+= 1
	i2 += 1 
for i in liste:
	p(i)





