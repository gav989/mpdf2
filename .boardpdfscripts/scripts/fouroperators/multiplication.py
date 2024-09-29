#!/usr/bin/env python3
#questiontemplate.py

def timestables(n,explanationn):
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
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def threebyonemultiplication(n,explanationn):
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
		b = random.randrange(111,1000)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))


def twobyonemultiplication(n,explanationn):
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
		b = random.randrange(11,100)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def twobytwomultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,100)
		b = random.randrange(11,100)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def twobythreemultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(101,1000)
		b = random.randrange(11,100)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def decimalmultiplication0(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,3)
		b = random.randrange(2,10)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
		answer = round(a*b,6)
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def decimalmultiplication1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,3)
		b = random.randrange(11,100)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
		answer = round(a*b,6)
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def decimalmultiplication2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,3)
		b = random.randrange(1,10) + 10 * random.randrange(1,10)
		b = b / 10**random.randrange(1,3)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
		answer = round(a*b,6)
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
