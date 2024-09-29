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
			answer = round((a + b)/(c * d),4)
			roundto = 0.1
			length = len(str(floor(answer)))
			answer = answer * 10**(10-length)
			roundto = 10**(10-(length-(log10(roundto))))
			remainder = answer%roundto
			if remainder < 0.5*roundto:
				rounded = answer - remainder
			else:
				rounded = answer + (roundto-remainder)
			answer = rounded / 10**(10-length)
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
		number = sqrt(nums[2] * nums[1] - nums[0]**2)		
		roundto = 3
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
			if rounded < 10:
				zeros = ".00"
			elif rounded < 100:
				zeros = ".0"
			else:
				zeros = ""
		elif rounded<1 and rounded*10**(abs(firstsig)+1)%1==0:
			zeros = "00"
		elif rounded<1 and rounded*10**(abs(firstsig)+2)%1==0:
			zeros = "0"
		elif rounded<10 and rounded*10%1==0:
			zeros = "0"
		else:
			zeros = ""
		answer = str(rounded) + zeros
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def squareroot2(n,explanationn):
	import random
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
		number = sqrt(a * b + c * d)	
	
		roundto = 2
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
			if rounded < 10:
				zeros = ".0"
			else:
				zeros = ""
		elif rounded<1 and rounded*10**(abs(firstsig)+1)%1==0:
			zeros = "0"
		else:
			zeros = ""
		answer = str(rounded) + zeros
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
