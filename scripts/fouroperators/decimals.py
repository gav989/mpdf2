#!/usr/bin/env python3
#decimals.py

def decmultmental1(n,explanationn):
	import random
	from utilities.sf import sftonum
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = [1,2,3,4,5,6,7,8,9,11,12]
		a = random.choice(nums)
		b = random.choice(nums)
		inda = random.randrange(1,5)
		indb = random.randrange(1,6-inda)
		c = a * b
		indc = inda + indb
		if c%10==0:
			c = int(c/10)
			indc = indc + 1
		a = sftonum(str(a),inda)
		b = sftonum(str(b),indb)
		c = sftonum(str(c),indc)
		question = a + " $\\times$ " + b
		answer = c
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def decmultmental2(n,explanationn):
	import random
	from utilities.sf import sftonum
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = [1,2,3,4,5,6,7,8,9,11,12]
		a = random.choice(nums)
		b = random.choice(nums)
		inda = random.randrange(1,5)
		indb = random.randrange(1,6-inda)
		inda = inda * -1
		indb = indb * -1
		c = a * b
		indc = inda + indb
		if c%10==0:
			c = int(c/10)
			indc = indc + 1
		a = sftonum(str(a),inda)
		b = sftonum(str(b),indb)
		c = sftonum(str(c),indc)
		question = a + " $\\times$ " + b
		answer = c
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def decmultmental3(n,explanationn):
	import random
	from utilities.sf import sftonum
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = [1,2,3,4,5,6,7,8,9,11,12]
		a = random.choice(nums)
		b = random.choice(nums)
		inda = random.randrange(1,5)
		indb = random.randrange(1,6-inda)
		inda = inda * -1
		if random.randrange(0,2)==1:
			inda,indb = indb,inda
		c = a * b
		indc = inda + indb
		if c%10==0:
			c = int(c/10)
			indc = indc + 1
		a = sftonum(str(a),inda)
		b = sftonum(str(b),indb)
		c = sftonum(str(c),indc)
		question = a + " $\\times$ " + b
		answer = c
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def decdivmental1(n,explanationn):
	import random
	from utilities.sf import sftonum
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = [1,2,3,4,5,6,7,8,9,11,12]
		a = random.choice(nums)
		b = random.choice(nums)
		inda = random.randrange(1,5)
		indb = random.randrange(1,6-inda)
		c = a * b
		indc = inda + indb
		if c%10==0:
			c = int(c/10)
			indc = indc + 1
		a = sftonum(str(a),inda)
		b = sftonum(str(b),indb)
		c = sftonum(str(c),indc)
		question = c + " $\\div$ " + b
		answer = a
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def decdivmental2(n,explanationn):
	import random
	from utilities.sf import sftonum
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = [1,2,3,4,5,6,7,8,9,11,12]
		a = random.choice(nums)
		b = random.choice(nums)
		inda = random.randrange(1,5)
		indb = random.randrange(1,6-inda)
		inda = inda * -1
		indb = indb * -1
		c = a * b
		indc = inda + indb
		if c%10==0:
			c = int(c/10)
			indc = indc + 1
		a = sftonum(str(a),inda)
		b = sftonum(str(b),indb)
		c = sftonum(str(c),indc)
		question = c + " $\\div$ " + b
		answer = a
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def decdivmental3(n,explanationn):
	import random
	from utilities.sf import sftonum
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = [1,2,3,4,5,6,7,8,9,11,12]
		a = random.choice(nums)
		b = random.choice(nums)
		inda = random.randrange(1,5)
		indb = random.randrange(1,6-inda)
		inda = inda * -1
		if random.randrange(0,2)==1:
			inda,indb = indb,inda
		c = a * b
		indc = inda + indb
		if c%10==0:
			c = int(c/10)
			indc = indc + 1
		a = sftonum(str(a),inda)
		b = sftonum(str(b),indb)
		c = sftonum(str(c),indc)
		question = c + " $\\div$ " + b
		answer = a
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
