# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from DsoonMath import quantity ,answertime,answer, p,error 
import time
limit = 99
level = 0
for i in range(5):
	expresion = quantity(levelop= 0,leveDt=1,limit=limit)
	print(i,expresion)		
	#time.sleep(60*0.4)
	#p("time")
	p(error(input(), answer(expresion)))
	p(answer(expresion))
print()
