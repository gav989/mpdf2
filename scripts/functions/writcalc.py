#!/usr/bin/env python3
#writcalc.py


def singledigitaddition(n,explanationn):
	import random
	questions = []
	answers = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10)
		b = random.randrange(1,10)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		questions.append(question)
		answers.append(answer)
	listofquestionsandanswers = [questions,answers]
	return(listofquestionsandanswers)
	

def twodigitaddition(n,explanationn):
	import random
	questions = []
	answers = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(10,100)
		b = random.randrange(10,100)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		questions.append(question)
		answers.append(answer)
	listofquestionsandanswers = [questions,answers]
	return(listofquestionsandanswers)


def threedigitaddition(n,explanationn):
	import random
	questions = []
	answers = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(100,1000)
		b = random.randrange(100,1000)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		questions.append(question)
		answers.append(answer)
	listofquestionsandanswers = [questions,answers]
	return(listofquestionsandanswers)

def threedigitaddition(n,explanationn):
	import random
	questions = []
	answers = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(100,1000)
		b = random.randrange(100,1000)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		questions.append(question)
		answers.append(answer)
	listofquestionsandanswers = [questions,answers]
	return(listofquestionsandanswers)



def fulladdition(n,explanationn):
	import random
	questions = []
	answers = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		questions.append(question)
		answers.append(answer)
	listofquestionsandanswers = [questions,answers]
	return(listofquestionsandanswers)


def decimaladdition(n,explanationn):
	import random
	from utilities.rounding import rounddp
	questions = []
	answers = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		digits = random.randrange(1,3)
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,2)
		b = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		b = b / 10**random.randrange(1,2)
		question = explanation + str(a) + " + " + str(b)
		answer = str(rounddp(a+b,3))
##################################
		questions.append(question)
		answers.append(answer)
	listofquestionsandanswers = [questions,answers]
	return(listofquestionsandanswers)






