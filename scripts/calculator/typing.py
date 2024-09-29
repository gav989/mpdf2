#typing.py


def squareroots(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		answer = random.randrange(16,40)
		root = answer**2
#write question
		tempquestions.write(explanation + "$\\sqrt{" + str(root) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def cubes(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		cube = random.randrange(7,15)
		answer = cube**3
#write question
		tempquestions.write(explanation + "$" + str(cube) + "^{3}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def fraction1(n,explanationn):
	import random
	from utilities.rounding import rounddpstring,rounddp
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Work out "
			explanation2 = " giving your answer correct to 1 decimal place."
		else:
			explanation1 = ""
			explanation2 = ""
		answer = 1
		while answer%1==0:
			a = random.randrange(1,10) + random.randrange(1,10)/10
			b = random.randrange(1,10) + random.randrange(1,10)/10
			c = random.randrange(1,10) + random.randrange(1,10)/10
			d = random.randrange(1,10)/10
			answer = rounddp((a + b)/(c * d),1)
		if random.randrange(1,3)==1:
			temp = c
			c = d
			d = temp
		question = "$\\dfrac{" + str(a) + " + " + str(b) + "}{" + str(c) + " \\times " + str(d) + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def squareroot1(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
	from math import log10, floor, sqrt, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Work out "
			explanation2 = " giving your answer correct to 3 significant figures."
		else:
			explanation1 = ""
			explanation2 = ""
		num1 = (random.randrange(1,10)*10 + random.randrange(1,10))/10
		num2 = (random.randrange(1,10)*10 + random.randrange(1,10))/10
		num3 = (random.randrange(1,10)*10 + random.randrange(1,10))/10
		if num1==num2==num3:
			num3 = num3-1
		nums = sorted([num1,num2,num3])
		question = "$\\sqrt{" + str(nums[2]) + " \\times " + str(nums[1]) + " - " + str(nums[0]) + "^{2}}$"
		answer = roundsfstring(sqrt(nums[2] * nums[1] - nums[0]**2),3)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def squareroot2(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
	from math import log10, floor, sqrt, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Work out "
			explanation2 = " giving your answer correct to 2 significant figures."
		else:
			explanation1 = ""
			explanation2 = ""
		a = random.randrange(1,10) + random.randrange(1,10)/10
		b = random.randrange(1,10) + random.randrange(1,10)/10
		c = random.randrange(1,10) + random.randrange(1,10)/10
		d = random.randrange(1,10) + random.randrange(1,10)/10
		question = "$\\sqrt{" + str(a) + "\\times" + str(b) + " + " + str(c) + "\\times" + str(d) + "}$"
		answer = roundsfstring(sqrt(a * b + c * d),2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cuberoot1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the cube root of "
		else:
			explanation = ""
		x = random.randrange(9,100)
		cube = x**3
		question = explanation + str(cube)
		answer = str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
