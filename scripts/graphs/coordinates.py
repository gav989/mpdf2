#!/usr/bin/env python3
#coordinates.py
def midpoint(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the midpoint of "
		else:
			explanation = ""
		x1 = random.randrange(-10,11)
		y1 = random.randrange(-10,11)
		x2 = x1 + random.randrange(1,11)*(-1)**random.randrange(1,3)
		y2 = y1 + random.randrange(1,11)*(-1)**random.randrange(1,3)
		x = (x1 + x2)/2
		y = (y1 + y2)/2
		if x%1==0:
			x = int(x)
		if y%1==0:
			y = int(y)
#write question
		tempquestions.write(explanation + "$(" + str(x1) + " , " + str(y1) + ")$ and $(" + str(x2) + " , " + str(y2) + ")$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(x) + " , " + str(y) + ")$")

def distance(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the distance between "
		else:
			explanation = ""
		x1 = random.randrange(-10,11)
		y1 = random.randrange(-10,11)
		x2 = x1 + random.randrange(1,11)*(-1)**random.randrange(1,3)
		y2 = y1 + random.randrange(1,11)*(-1)**random.randrange(1,3)
		distance = rounddp(sqrt((x1-x2)**2 + (y1-y2)**2),2)
		if distance%1==0:
			distance = int(distance)
#write question
		tempquestions.write(explanation + "$(" + str(x1) + " , " + str(y1) + ")$ and $(" + str(x2) + " , " + str(y2) + ")$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(distance))


def distance8(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the distance between "
		else:
			explanation = ""
		xs = list(range(-8,9))
		ys = list(range(-8,9))
		x1 = random.choice(xs)
		xs.remove(x1)
		x2 = random.choice(xs)
		y1 = random.choice(ys)
		ys.remove(y1)
		y2 = random.choice(ys)

		distance = rounddp(sqrt((x1-x2)**2 + (y1-y2)**2),2)
		if distance%1==0:
			distance = int(distance)
#write question
		tempquestions.write(explanation + "$(" + str(x1) + " , " + str(y1) + ")$ and $(" + str(x2) + " , " + str(y2) + ")$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(distance))