#!/usr/bin/env python3
#addition.py
def singledigitsubtraction(n,explanationn):
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
		if a<b:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " - " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a-b))


def twodigitsubtraction(n,explanationn):
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
		if a<b:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " - " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a-b))


def threedigitsubtraction(n,explanationn):
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
		if a<b:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " - " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a-b))


def fullsubtraction(n,explanationn):
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
		if a<b:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " - " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a-b))



def decimalsubtraction(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
		a = a / 10**random.randrange(1,2)
		b = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		b = b / 10**random.randrange(1,2)
		if a<b:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " - " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounddp(a-b,3)))





