#!/usr/bin/env python3
#negatives.py
def negadd(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,16)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,3)
		if dec==1:
			a = random.randrange(1,16)
			b = random.randrange(-15,0)
		elif dec==2:
			b = random.randrange(1,16)
			a = random.randrange(-15,0)
		else:
			a = random.randrange(-15,0)
			b = random.randrange(-15,0)
		answer = a + b
#write question
		tempquestions.write(explanation + str(a) + " + " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def negsubtract(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,16)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,3)
		if dec==1:
			a = random.randrange(1,16)
			b = random.randrange(-15,0)
		elif dec==2:
			b = random.randrange(1,16)
			a = random.randrange(-15,0)
		else:
			a = random.randrange(-15,0)
			b = random.randrange(-15,0)
		answer = a - b
#write question
		tempquestions.write(explanation + str(a) + " - " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def negmultiply(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,16)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,3)
		if dec==1:
			a = random.randrange(1,13)
			b = random.randrange(-12,0)
		elif dec==2:
			b = random.randrange(1,13)
			a = random.randrange(-12,0)
		else:
			a = random.randrange(-12,0)
			b = random.randrange(-12,0)
		answer = a * b
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def negdivide(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,16)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,3)
		if dec==1:
			answer = random.randrange(1,13)
			b = random.randrange(-12,0)
		elif dec==2:
			b = random.randrange(1,13)
			answer = random.randrange(-12,0)
		else:
			answer = random.randrange(-12,0)
			b = random.randrange(-12,0)
		a = answer * b
#write question
		tempquestions.write(explanation + str(a) + " $\\div$ " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

