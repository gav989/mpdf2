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



def timestablesnormal2(n,a):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		b = random.randrange(2,10)
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


def timestablesdivide2(n,b):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,10)
#write question
		tempquestions.write(str(a*b) + " $\\div$ " + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b) + " $\\div$ " + str(b) + " = $\\underline{" + str(a) +"}$")


def timestableshard2(n,a,choice):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		b = random.randrange(2,10)
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

def timestablesdoubling(n):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = 2
		bs = [2,4,6,8,10,12,14,16,18,20,24,28,32,36,3,9,15,21,27]
		b = random.choice(bs)
#write question
		tempquestions.write(str(b) + " $\\times$ " + str(a) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b) + " $\\times$ " + str(a) + " = $\\underline{" + str(a*b) +"}$")


def timestableshalving(n):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = 2
		bs = [4,8,12,16,20,24,28,32,36,40,48,56,64,72,6,18,30,42,54,10,50,60,70,80,90]
		b = random.choice(bs)
#write question
		tempquestions.write(str(b) + " $\\div$ " + str(a) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(b) + " $\\div$ " + str(a) + " = $\\underline{" + str(int(b/a)) +"}$")
