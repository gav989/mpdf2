#!/usr/bin/env python3
#questiontemplate.py

def divisiontables(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,13)
		b = random.randrange(2,13)
#write question
		tempquestions.write(explanation + str(a*b) + " $\\div$ " + str(a))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b))

def divisiontablesten(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,13) * 10
		b = random.randrange(2,13)
#write question
		tempquestions.write(explanation + str(a*b) + " $\\div$ " + str(a))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b))

def singledigitdivision(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(13,10**(random.randrange(2,3)))
#write question
		tempquestions.write(explanation + str(a*b) + " $\\div$ " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b))

def twodigitdivision(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,40)
		if random.randrange(0,2)==1:
			b = random.randrange(1,7) + random.randrange(0,7)*10 + random.randrange(1,7)*100
		else:
			b = random.randrange(1,7) + random.randrange(1,7)*10
#write question
		tempquestions.write(explanation + str(a*b) + " $\\div$ " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b))

def twodigitdivisioneasy(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,20)
		if random.randrange(0,2)==1:
			b = random.randrange(1,7) + random.randrange(0,7)*10 + random.randrange(1,7)*100
		else:
			b = random.randrange(1,7) + random.randrange(1,7)*10
#write question
		tempquestions.write(explanation + str(a*b) + " $\\div$ " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b))


def twodigittables(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write out the first five numbers in the "
			explanation2 = " times table"
		else:
			explanation1 = ""
			explanation2 = ""
		n = random.randrange(1,9) + random.randrange(1,9)*10
#write question
		tempquestions.write(explanation1 + str(n) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(n) + ", " + str(n*2) + ", " + str(n*3) + ", " + str(n*4) + ", " + str(n*5))

def decimaldivision1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(1,10**random.randrange(1,3)) * 10 + random.randrange(1,10)
		c = a*b
		while c%10==0:
			c = c/10
		c = c/10**random.randrange(1,4)
		b = c/a		
#write question
		tempquestions.write(explanation + str(c) + " $\\div$ " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(round(b,6)))

def decimaldivision2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		divisor = (2,4,5,6,8)
		a = random.choice(divisor)
		if a==6:
			c = 3 * ((random.randrange(20,300)*2)-1)
		elif a==5:
			c = 5 * random.randrange(20,200) - random.randrange(1,5)
		else:
			c = (random.randrange(100,1000)*2)-1
		b = c/a		
#write question
		tempquestions.write(explanation + str(c) + " $\\div$ " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(round(b,6)))
