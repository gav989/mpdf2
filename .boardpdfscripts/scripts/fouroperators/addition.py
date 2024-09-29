#!/usr/bin/env python3
#addition.py
def singledigitaddition(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10)
		b = random.randrange(1,10)
#write question
		tempquestions.write(explanation + str(a) + " + " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a+b))


def twodigitaddition(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(10,100)
		b = random.randrange(10,100)
#write question
		tempquestions.write(explanation + str(a) + " + " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a+b))


def threedigitaddition(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(100,1000)
		b = random.randrange(100,1000)
#write question
		tempquestions.write(explanation + str(a) + " + " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a+b))


def fulladdition(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
#write question
		tempquestions.write(explanation + str(a) + " + " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a+b))

def decimaladdition(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		digits = random.randrange(1,3)
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,4)
		b = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		b = b / 10**random.randrange(1,4)
#write question
		tempquestions.write(explanation + str(a) + " + " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(round(a+b,3)))
