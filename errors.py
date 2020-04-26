from DsoonMath import quantity ,answertime,answer,p
#is for learn with errors
def partexpresion(expresion):
#i use to separe signs ["+","-","*","/","%","**","(1/2)","**(2)"]
	i = 0
	nums = []
	numspos = []
	signspos = []
	signs = []
	expresion = list(expresion)
	knownsigns = ["+","-","*","/","%","**","(1/2)","**(2)"]
	numbersb10 = [str(b10) for b10 in range(10)]
	for parts in expresion:
		for sign,numberb10 in zip(knownsigns,numbersb10):
			if sign == parts:
				signs.append(sign)
				signspos.append(i)
				
			elif numberb10 == parts:
				nums.append(numberb10)
				numspos.append(i)

		i += 1
	p("numpos"+str(numspos),"num"+str(nums),"signspos"+str(signspos),"signs"+str(signs),expresion)
	#return 
def error(expresion, answer):
	#try:
		answer = eval(answer)
		expresion = eval(expresion)
		S_answer = str(eval(str(answer)))
		S_expresion = str(eval(str(expresion)))
		#partexpresion(str(expresion))
		if S_expresion !=  S_answer:
			signerrorP = answer*1
			signerrorM = answer*-1

			if expresion == signerrorM or signerrorP == expresion:
				teori = """
	you have a error in sign 
	signs sumation
	+ (+) + = +
	- (+) - = -
	- (+) + =  if - > that + num = - or if + > that - num = + 
	+ (+) - =  if - > that + num = - or  if + > that - num = +
	signs multiplication
	+ (*) + = +
	- (*) - = + 
	- (*) + = -
	+ (*) - = - 
	"""
				return teori
			#elif
		else:
			teori = "dont have corrections"
			return teori
	#except:
		#teori = "you are test not developed levels if you need solution can test lower levels"
		#return teori
def help():
	mesage="""
			fabs = is asbsolute value is a equivalent math operator |x|
			log1p(x) =  natural logarithm of 1+x
			hypot = sqrt(x*x + y*y)
			cos = cos() funtion
			sin = sin() funtion
			tan = tan() funtion
			"""

	