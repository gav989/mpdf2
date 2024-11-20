#!/usr/bin/env python3
#negativenumbers.py
import random
from math import floor,gcd
from utilities.rounding import rounddp

def negcountup(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		start = random.randrange(1,16) * (-1)**random.randrange(1,4)
		count = random.randrange(1,16)
		answer = str(start + count)
		question = "Start on " + str(start) + " and count up " + str(count)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def negcountdown(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		start = random.randrange(1,16) * (-1)**random.randrange(1,4)
		count = random.randrange(1,16)
		answer = str(start - count)
		question = "Start on " + str(start) + " and count down " + str(count)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def negadd(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		answer = str(a + b)
		question = explanation + "$" + str(a) + " + " + str(b) + "$"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def negsubtract(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,16)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,4)
		if dec==1:
			a = random.randrange(1,16)
			b = random.randrange(-15,0)
		elif dec==2:
			a = random.randrange(-15,0)
			b = random.randrange(-15,0)
		else:
			b = random.randrange(1,16)
			a = random.randrange(-15,0)
		answer = str(a - b)
		question = explanation + "$" + str(a) + " - " + str(b) + "$"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)



def negmultiply(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		answer = str(a * b)
		question = explanation + "$" + str(a) + " \\times " + str(b) + "$"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)



def negdivide(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		a = str(answer * b)
		question = explanation + "$" + str(a) + " \\div " + str(b) + "$"
		answer = str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)



def negaddbig(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(40,200)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,3)
		if dec==1:
			a = random.randrange(40,200)
			b = random.randrange(-200,-40)
		elif dec==2:
			b = random.randrange(40,200)
			a = random.randrange(-200,-40)
		else:
			a = random.randrange(-200,-40)
			b = random.randrange(-200,-40)
		answer = str(a + b)
		question = explanation + "$" + str(a) + " + " + str(b) + "$"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)



def negsubtractbig(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(40,200)*(-1)**random.randrange(1,3)
		dec = random.randrange(0,4)
		if dec==1:
			a = random.randrange(40,200)
			b = random.randrange(-200,-40)
		elif dec==2:
			a = random.randrange(-200,-40)
			b = random.randrange(-200,-40)
		else:
			b = random.randrange(40,200)
			a = random.randrange(-200,-40)
		answer = str(a - b)
		question = explanation + "$" + str(a) + " - " + str(b) + "$"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def negsquaring(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		num = random.randrange(1,16)*(-1)
		answer = str(num * num)
		question = "($" + str(num) + ")^{2}$"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




