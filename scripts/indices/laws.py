#!/usr/bin/env python3
#laws.py



def multindpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)
		ind2 = random.randrange(2,10)
		ind3 = ind1 + ind2
#write question
		tempquestions.write(explanation + str(base) + "$^{" + str(ind1) + "} \\times " + str(base) + "^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")

def multind(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind3 = ind1 + ind2
#write question
		tempquestions.write(explanation + str(base) + "$^{" + str(ind1) + "} \\times " + str(base) + "^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")

def multindneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		if ind1<0:
			ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		else:
			ind2 = random.randrange(2,10)*(-1)
		ind3 = ind1 + ind2
#write question
		tempquestions.write(explanation + str(base) + "$^{" + str(ind1) + "} \\times " + str(base) + "^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")


def divindpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)
		ind2 = random.randrange(2,10)
		ind3 = ind1 - ind2
#write question
		if random.randrange(0,2)==1:
			tempquestions.write(explanation + str(base) + "$^{" + str(ind1) + "} \\div " + str(base) + "^{" + str(ind2) + "}$")
		else:
			tempquestions.write(explanation + "$\\dfrac{" + str(base) + "^{" + str(ind1) + "}}{" + str(base) + "^{" + str(ind2) + "}}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")


def divind(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind3 = ind1 - ind2
#write question
		if random.randrange(0,2)==1:
			tempquestions.write(explanation + str(base) + "$^{" + str(ind1) + "} \\div " + str(base) + "^{" + str(ind2) + "}$")
		else:
			tempquestions.write(explanation + "$\\dfrac{" + str(base) + "^{" + str(ind1) + "}}{" + str(base) + "^{" + str(ind2) + "}}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")

def divindneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		if ind1<0:
			ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		else:
			ind2 = random.randrange(2,10)*(-1)
		ind3 = ind1 - ind2
#write question
		if random.randrange(0,2)==1:
			tempquestions.write(explanation + str(base) + "$^{" + str(ind1) + "} \\div " + str(base) + "^{" + str(ind2) + "}$")
		else:
			tempquestions.write(explanation + "$\\dfrac{" + str(base) + "^{" + str(ind1) + "}}{" + str(base) + "^{" + str(ind2) + "}}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")

def indindpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)
		ind2 = random.randrange(2,10)
		ind3 = ind1 * ind2
#write question
		tempquestions.write(explanation + "$(" + str(base) + "^{" + str(ind1) + "})^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")


def indind(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind3 = ind1 * ind2
#write question
		tempquestions.write(explanation + "$(" + str(base) + "^{" + str(ind1) + "})^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")

def indindneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		base = random.randrange(2,10)
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		if ind1<0:
			ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		else:
			ind2 = random.randrange(2,10)*(-1)
		ind3 = ind1 * ind2
#write question
		tempquestions.write(explanation + "$(" + str(base) + "^{" + str(ind1) + "})^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(base) + "^{" + str(ind3) + "}$")
