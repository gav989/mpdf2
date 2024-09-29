#!/usr/bin/env python3
#10.py
def multten(n,explanationn):
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
		a = rounddp(random.randrange(1,1000)/10**random.randrange(0,4),3)
		if a%1==0:
			a = int(a)
		b = 10
		sign = " $\\times$ "
		c = rounddp(a*b,6)
		if random.randrange(1,3)==1:
			d = a
			a = b
			b = d
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(explanation + str(a) + sign + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(c))


def multhundred(n,explanationn):
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
		a = rounddp(random.randrange(1,1000)/10**random.randrange(0,4),3)
		if a%1==0:
			a = int(a)
		b = 100
		sign = " $\\times$ "
		c = rounddp(a*b,6)
		if random.randrange(1,3)==1:
			d = a
			a = b
			b = d
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(explanation + str(a) + sign + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(c))

def multthousand(n,explanationn):
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
		a = rounddp(random.randrange(1,1000)/10**random.randrange(0,4),3)
		if a%1==0:
			a = int(a)
		b = 1000
		sign = " $\\times$ "
		c = rounddp(a*b,6)
		if random.randrange(1,3)==1:
			d = a
			a = b
			b = d
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(explanation + str(a) + sign + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(c))


def divten(n,explanationn):
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
		a = rounddp(random.randrange(1,1000)/10**random.randrange(0,4),3)
		if a%1==0:
			a = int(a)
		b = 10
		sign = " $\\div$ "
		c = rounddp(a/b,6)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(explanation + str(a) + sign + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(c))


def divhundred(n,explanationn):
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
		a = rounddp(random.randrange(1,1000)/10**random.randrange(0,4),3)
		if a%1==0:
			a = int(a)
		b = 100
		sign = " $\\div$ "
		c = rounddp(a/b,6)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(explanation + str(a) + sign + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(c))

def divthousand(n,explanationn):
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
		a = rounddp(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 1000
		sign = " $\\div$ "
		c = rounddp(a/b,6)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(explanation + str(a) + sign + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(c))
