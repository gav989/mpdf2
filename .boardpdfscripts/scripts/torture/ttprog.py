#!/usr/bin/env python3
#ttprog.py

def timestablesnormal(n,a):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		b = random.randrange(2,13)
		dec = random.randrange(0,2)
#write question
		if dec==1:
			tempquestions.write(str(a) + " $\\times$ " + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		else:
			tempquestions.write(str(b) + " $\\times$ " + str(a) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		if dec==1:
			tempquestions.write(str(a) + " $\\times$ " + str(b) + " = $\\underline{" + str(a*b) +"}$")
		else:
			tempquestions.write(str(b) + " $\\times$ " + str(a) + " = $\\underline{" + str(a*b) +"}$")


def timestablesdivide(n,b):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,13)
#write question
		tempquestions.write(str(a*b) + " $\\div$ " + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b) + " $\\div$ " + str(b) + " = $\\underline{" + str(a) +"}$")


def timestableshard(n,a,choice):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		b = random.randrange(2,13)
#write question
		if choice==1:
			dec = random.randrange(0,2)
			if dec==1:
				tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm}$ $\\times$ " + str(a) + " = " + str(a*b))
			else:
				tempquestions.write(str(a) + "$\\times$ " + "$\\rule[-1.5mm]{1cm}{0.15mm}$ = " + str(a*b))
			tempquestions.write("\n")
			if dec==1:
				tempquestions.write("\\underline{" + str(b) + "} $\\times$ " + str(a) + " = " + str(a*b))
			else:
				tempquestions.write(str(b) + "$\\times$ " + "$\\underline{" + str(b) + "}$ = " + str(a*b))
		elif choice==2:
			tempquestions.write(str(a*b) + " $\\div$ " + "$\\rule[-1.5mm]{1cm}{0.15mm}$ = " + str(a))
			tempquestions.write("\n")
			tempquestions.write(str(a*b) + " $\\div$ " + "$\\underline{" + str(b) + "}$ = " + str(a))
		else:
			tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm}$ $\\div$ " + str(b) + " = " + str(a))
			tempquestions.write("\n")
			tempquestions.write("\\underline{" + str(a*b) + "} $\\div$ " + str(b) + " = " + str(a))
