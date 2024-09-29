#!/usr/bin/env python3
#estimation.py

def estimation1(n,explanationn):
	import random
	from math import log10, floor, ceil
	from utilities.rounding import rounddp,roundsf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the value of "

		else:
			explanation = ""
		a = random.randrange(3,10) + random.randrange(0,10)/10 + random.randrange(1,9)/100
		a = rounddp(a,2)
		b = random.randrange(9,35) + random.randrange(1,10)/10
		b = rounddp(b,1)
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
		c = rounddp(c,3)
		aa = roundsf(a,1)
		bb = roundsf(b,1)
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
		num1 = random.randrange(2,11)*100
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

def estimation3(n,explanationn):
	import random
	from utilities.rounding import roundnearest
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the value of "
		else:
			explanation = ""
		num1 = random.randrange(1,10)*100 + random.randrange(1,100)
		num2 = random.randrange(1,10)*100 + random.randrange(1,100)
		question = str(num1) + " $\\times$ " + str(num2)
		num1 = roundnearest(num1,100)
		num2 = roundnearest(num2,100)
		answer = int(num1 * num2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\num{" + str(answer) + "}")



def estimation4(n,explanationn):
	import random
	from utilities.rounding import roundsf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the value of "
		else:
			explanation = ""
		bs = [10,10,10,10,10,10,10,20,10,10,10,10,10,10,20,10,20,10,10,10,10,10,10,20,10,20,10,20,10,20,10,20,20]
		cs = [10,20,10,20,30,10,20,20,10,20,50,10,60,20,30,40,20,10,70,20,10,20,40,20,80,40,40,20,60,30,80,40,50]
		answers = [2,1,3,1.5,1,4,2,1,5,2.5,1,6,1,3,1,1.5,1.5,7,1,3.5,8,40,2,2,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
		dec = random.randrange(0,len(bs))
		b = bs[dec]
		c = cs[dec]
		answer = answers[dec]
		a = int(b * c * answer)
		if b==10:
			b = b + random.randrange(1,5)
		else:
			if random.randrange(0,2)==1:
				b = b + random.randrange(1,5)
			else:
				b = b - random.randrange(1,6)
		if c==10:
			c = c + random.randrange(1,5)
		else:
			if random.randrange(0,2)==1:
				c = c + random.randrange(1,5)
			else:
				c = c - random.randrange(1,6)
		if random.randrange(0,2)==1:
			a = a + random.randrange(1,50)
		else:
			a = a - random.randrange(1,51)
		if random.randrange(0,2)==1:
			temp = b
			b = c
			c = temp
		question = "$\\dfrac{" + str(a) + "}{" + str(b) + " \\times " + str(c) + "}$"
		answer = str(answer)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
