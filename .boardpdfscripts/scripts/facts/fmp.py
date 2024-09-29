#!/usr/bin/env python3
#fmp.py


def fm(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		if random.randrange(0,2)==1:
			answer = "factor"
			num1 = random.randrange(2,13)
			num2 = num1 * random.randrange(2,13)
		else:
			answer = "multiple"
			num2 = random.randrange(2,13)
			num1 = num2 * random.randrange(2,13)
#write question
		tempquestions.write(str(num1) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  of " + str(num2))

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sc(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		if random.randrange(0,3)==1:
			answer = "cube"
			nums = [8,27,125]
			num = random.choice(nums)
		else:
			answer = "square"
			nums = [4,9,16,25,36,49,81,100,121,144,169,196,225]
			num = random.choice(nums)
#write question
		tempquestions.write(str(num) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  number")

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def negsquareroot(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		nums = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		num = random.choice(nums) * -1
		square = num**2
		#write question
		tempquestions.write("The negative square root of " + str(square) + " is .......")

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(num))


def cuberoot(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		nums = [2,3,4,5]
		num = random.choice(nums)
		cube = num**3
		#write question
		tempquestions.write(str(num) + " is the cube root of  .......")

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(cube))
