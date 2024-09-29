#!/usr/bin/env python3
#estimation.py

def estimation1(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the value of "

		else:
			explanation = ""


		a = random.randrange(3,10) + random.randrange(0,10)/10 + random.randrange(1,9)/100
		a = round(a,2)
		b = random.randrange(9,35) + random.randrange(1,10)/10
		b = round(b,1)
		dec = random.randrange(1,6)
		if dec==1:
			c = 5 + (random.randrange(0,5)/10 + random.randrange(1,10)/100)*(-1)**random.randrange(1,3)
			cc = 5
		elif dec==2:
			c = 4 + (random.randrange(0,5)/10 + random.randrange(1,10)/100)*(-1)**random.randrange(1,3)
			cc = 4
		elif dec==3:
			c = 2 + (random.randrange(0,5)/10 + random.randrange(1,10)/100)*(-1)**random.randrange(1,3)
			cc = 2
		elif dec==4:
			c = 10 + (random.randrange(0,5) + random.randrange(0,10)/10)
			cc = 10
		elif dec==5:
			c = 20 + (random.randrange(0,5) + random.randrange(0,10)/10)
			cc = 20
		number = a
			


		roundto = 1
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		rounded = rounded / 10**(10-firstsig)
		if rounded%1==0:
			rounded = int(rounded)

		aa = rounded
		number = b

		roundto = 1
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		rounded = rounded / 10**(10-firstsig)
		if rounded%1==0:
			rounded = int(rounded)
		bb = rounded

		question = explanation + "$\\dfrac{" + str(a) + " \\times "+ str(b) + "}{" + str(c) + "}$"
		answer = (aa*bb)/cc
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def estimation2(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the value of "

		else:
			explanation = ""
		num1 = random.randrange(1,11)*100
		num2 = int(num1/10)
		factors = []
		for i in range(1,10):
			if num2%i==0:
				factors.append(i)
		num2 = random.choice(factors) * 10
		answer = int(num1/num2)
		if random.randrange(0,2)==1:
			num1 = num1 + random.randrange(1,50)
		else:
			num1 = num1 - random.randrange(1,51)
		if num2==10:
			num2 = random.randrange(11,15)
		else:
			if random.randrange(0,2)==1:
				num2 = num2 + random.randrange(1,5)
			else:
				num2 = num2 - random.randrange(1,6)
		question = str(num1) + " $\div$ " + str(num2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
