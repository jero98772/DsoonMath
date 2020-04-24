# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from DsoonMath import quantity ,answertime,answer, p
import time
limit = 999
level = 0
for i in range(5):
	expresion = quantity(levelop= 1,leveDt=0,limt=limit)
	print(i,expresion)		
	time.sleep(60*0.5)
	p(answer(limit,expresion))
print()




