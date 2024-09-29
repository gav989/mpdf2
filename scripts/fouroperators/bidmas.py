#!/usr/bin/env python3
#bidmas.py


def bidmas1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(5,50)
		b = random.randrange(2,10)
		c = random.randrange(2,10)
		if random.randrange(0,2)==1:
			sign2 = "\\div"
			b = c* random.randrange(2,10)
			temp = int(b/c)
		else:
			sign2 = "\\times"
			temp = b*c
		if random.randrange(0,2)==1:
			sign1 = "+"
			temp = a + temp
		else:
			sign1 = "-"
			temp = a - temp
		question = str(a) + sign1 + str(b) + sign2 + str(c)
		answer = temp
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(2,10)
		c = random.randrange(2,10)
		d = random.randrange(2,10)
		if random.randrange(0,2)==1:
			sign1 = "+"
			temp = a + b
		else:
			sign1 = "-"
			temp = a-b
		if sign1=="+":
			sign2 = "-"
			temp = temp - c
		elif random.randrange(0,2)==1:
			sign2 = "+"
			temp = temp + c
		else:
			sign2 = "-"
			temp = temp - c
		sign3 = "+"
		temp = temp + d
		question = str(a) + sign1 + str(b) + sign2 + str(c) + sign3 + str(d)
		answer = temp
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(5,50)
		b = random.randrange(2,10)
		c = random.randrange(2,10)
		d = random.randrange(2,10)
		if random.randrange(0,2)==1:
			sign2 = "\\div"
			b = c* random.randrange(2,10)
			temp = int(b/c)
		else:
			sign2 = "\\times"
			temp = b*c
		if random.randrange(0,2)==1:
			sign1 = "+"
			temp = a + temp
		else:
			sign1 = "-"
			temp = a - temp
		if random.randrange(0,2)==1:
			sign3 = "+"
			temp = temp + d
		else:
			sign3 = "-"
			temp = temp - d
		question = str(a) + sign1 + str(b) + sign2 + str(c) + sign3 + str(d)
		answer = temp
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(2,10)
		c = random.randrange(2,10)
		d = random.randrange(2,10)
		if random.randrange(0,2)==1:
			sign1 = "\\times"
			temp = a*b
		else:
			sign1 = "\\div"
			a = b * random.randrange(2,10)
			temp = int(a/b)
		if random.randrange(0,2)==1:
			sign3 = "\\times"
			temp2 = c*d
		else:
			sign3 = "\\div"
			c = d * random.randrange(2,10)
			temp2 = int(c/d)
		if random.randrange(0,2)==1:
			sign2 = "+"
			temp = temp + temp2
		else:
			sign2 = "-"
			temp = temp - temp2
		
		
		question = str(a) + sign1 + str(b) + sign2 + str(c) + sign3 + str(d)
		answer = temp
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = random.randrange(2,10)
		a = temp * answer
		c = random.randrange(2,10)*(-1)**random.randrange(1,3)
		bs = list(range(2,10))
		bs.remove(temp)
		b = random.choice(bs)
		c = abs(b - temp)
		if b>temp:
			sign = "-"
		else:
			sign = "+"
		question = "\\dfrac{" + str(a) + "}{" + str(b) + sign + str(c) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas6(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		c = random.randrange(2,10)
		answer = random.randrange(2,10)
		temp = answer * c
		if random.randrange(0,2)==1:
			sign = "-"
			b = random.randrange(3,13)
			a = temp + b
		else:
			sign = "+"
			b = random.randrange(2,temp)
			a = temp - b
		question = "\\dfrac{" + str(a) + sign + str(b) + "}{" + str(c) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas7(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = random.randrange(2,10)
		a = temp * answer
		c = random.randrange(2,10)*(-1)**random.randrange(1,3)
		bs = list(range(2,10))
		bs.remove(temp)
		b = random.choice(bs)
		c = abs(b - temp)
		if b>temp:
			sign = "-"
		else:
			sign = "+"
		temp = a
		if random.randrange(0,2)==1:
			sign1 = "-"
			y = random.randrange(3,13)
			x = temp + y
		else:
			sign1 = "+"
			y = random.randrange(2,temp)
			x = temp - y
		question = "\\dfrac{" + str(x) + sign1 + str(y) + "}{" + str(b) + sign + str(c) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas8(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(2,10)
		c = random.randrange(2,10)
		if random.randrange(0,2)==1:
			sign = "+"
			if random.randrange(0,2)==1:
				question = str(a) + "^{2}" + sign + str(b) + "\\times" + str(c)
			else:
				question = str(b) + "\\times" + str(c) + sign + str(a) + "^{2}"
			answer = a**2 + b * c
		else:
			sign = "-"
			if a**2>b*c:
				question = str(a) + "^{2}" + sign + str(b) + "\\times" + str(c)
			else:
				question = str(b) + "\\times" + str(c) + sign + str(a) + "^{2}"
			answer = abs(a**2 - b * c)
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas9(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		c = random.randrange(2,10)
		answer = random.randrange(2,10)
		temp = answer * c
		aas = list(range(2,10))
		aas.remove(c)
		a = random.choice(aas)
		if a**2>temp:
			sign = "-"
			b = a**2 - temp
			question = "\\dfrac{" + str(a) + "^{2}" + sign + str(b) + "}{" + str(c) + "}"
		else:
			sign = "+"
			b = temp - a**2
			if random.randrange(0,2)==1:
				question = "\\dfrac{" + str(a) + "^{2}" + sign + str(b) + "}{" + str(c) + "}"
			else:
				question = "\\dfrac{" + str(b) + sign + str(a) + "^{2}}{" + str(c) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas10(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		c = random.randrange(2,10)
		answer = temp * c
		aas = list(range(2,10))
		aas.remove(temp)
		a = random.choice(aas)
		b = abs(temp - a)
		if a<temp:
			brac = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac = "(" + str(a) + " - " + str(b) + ")"
		dec = random.randrange(0,3)
		if dec==1:
			question = brac + " \\times " + str(c)
		elif dec==2:
			question = str(c) + " \\times " + brac
		else:
			question = str(a) + brac

#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas11(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = list(range(2,10))
		num1 = random.choice(nums)
		nums.remove(num1)
		num2 = random.choice(nums)
		answer = num1*num2

		aas = list(range(2,10))
		aas.remove(num1)
		a = random.choice(aas)
		b = abs(num1-a)
		if a<num1:
			brac1 = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac1 = "(" + str(a) + " - " + str(b) + ")"
		
		cs = list(range(2,10))
		cs.remove(num2)
		c = random.choice(cs)
		d = abs(num2-c)
		if c<num2:
			brac2 = "(" + str(c) + " + " + str(d) + ")"
		else:
			brac2 = "(" + str(c) + " - " + str(d) + ")"
		
		question = brac1 + " \\times " + brac2
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas12(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = temp**2
		aas = list(range(2,10))
		aas.remove(temp)
		a = random.choice(aas)
		b = abs(temp - a)
		if a<temp:
			brac = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac = "(" + str(a) + " - " + str(b) + ")"
		question = brac + "^{2}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas13(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = temp**2
		aas = list(range(2,10))
		aas.remove(temp)
		a = random.choice(aas)
		b = abs(temp - a)
		c = random.randrange(2,10)
		if a<temp:
			brac = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac = "(" + str(a) + " - " + str(b) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,2)==1:
				question = brac + "^{2} + " + str(c)
			else:
				question = str(c) + " + " + brac + "^{2}"
			answer = answer + c
		else:
			if random.randrange(0,2)==1:
				question = brac + "^{2} - " + str(c)
				answer = answer - c
			else:
				c = c + answer
				question = str(c) + " - " + brac + "^{2}"
				answer = c - answer
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas14(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			a = random.randrange(2,10)
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				brac = a + b
				bracstring = "(" + str(a) + " + " + str(b) + ")"
			else:
				if a<b:
					a,b = b,a
				brac = a - b
				bracstring = "(" + str(a) + " - " + str(b) + ")"
		else:
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				brac = a + b
				bracstring = "(" + str(a) + " + " + str(b) + ")"
			else:
				a = b**2 + random.randrange(2,10)
				brac = a - b
				bracstring = "(" + str(a) + " - " + str(b) + ")"
		temp = random.randrange(2,10)
		c = temp + brac
		if random.randrange(0,2)==1:
			d = random.randrange(2,10)
			answer = (c-brac)*d
			if random.randrange(0,2)==1:
				question = "(" + str(c) + " - " + bracstring + ") \\times " + str(d)
			else:
				question = str(d) + "\\times (" + str(c) + " - " + bracstring + ")"
		else:
			
			d = (c-brac) * random.randrange(2,10)
			answer = int(d/(c-brac))
			question = str(d) + "\\div (" + str(c) + " - " + bracstring + ")"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def bidmas15(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		nums = list(range(2,10))
		temp1 = random.choice(nums)
		nums.remove(temp1)
		answer = temp1**2
		temp2 = random.choice(nums)
		a = temp1 * temp2
		nums.remove(temp2)
		swap = random.randrange(0,2)
		if swap==1:
			temp2,a = a,temp2
		nums = list(range(2,10))
		if temp2 in nums:
			nums.remove(temp2)
		b = random.choice(nums)
		c = abs(b-temp2)
		if b>temp2:
			sign = " - "
		else:
			sign = " + "
		if swap==1:
			question = "((" + str(b) + sign + str(c) + ") \\div" + str(a) + ")^{2}"
		else:
			question = "(" + str(a) + "\\div (" + str(b)  + sign + str(c) + "))^{2}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas16(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		brac = random.randrange(2,10)
		nums = list(range(2,10))
		nums.remove(brac)
		c = random.choice(nums)
		d = abs(brac-c)
		if c>brac:
			sign2 = " - "
		else:
			sign2 = " + "
		b = random.randrange(2,10)
		temp = b * brac
		brac = "(" + str(c) + sign2 + str(d) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				question = str(a) + " + "  + str(b) + "\\times (" + str(c) + sign2 + str(d) + ")"
				answer = a + temp
			else:
				a = temp + random.randrange(2,10)
				question = str(a) + " - "  + str(b) + "\\times (" + str(c) + sign2 + str(d) + ")"
				answer = a - temp
		else:
			a = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = "(" + str(c) + sign2 + str(d) + ") \\times" + str(b) + " + " + str(a)
				answer = temp + a
			else:
				question = "(" + str(c) + sign2 + str(d) + ") \\times" + str(b) + " - " + str(a)
				answer = temp - a
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas17(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(0,3)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas18(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(0,3)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		if random.randrange(0,2)==1:
			d = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = question + " + " + str(d)
				answer = answer + d
			else:
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				answer = answer + d
				question = str(d) + " + " + question
			else:
				d = answer + random.randrange(2,10)
				answer = d - answer
				question = str(d) + " - " + question
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas19(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			a = random.randrange(2,10)
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				brac = a**2 + b
				bracstring = "(" + str(a) + "^{2} + " + str(b) + ")"
			else:
				brac = a**2 - b
				bracstring = "(" + str(a) + "^{2} - " + str(b) + ")"
		else:
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				brac = a + b**2
				bracstring = "(" + str(a) + " + " + str(b) + "^{2})"
			else:
				a = b**2 + random.randrange(2,10)
				brac = a - b**2
				bracstring = "(" + str(a) + " - " + str(b) + "^{2})"
		temp = random.randrange(2,10)
		c = temp + brac
		if random.randrange(0,2)==1:
			d = random.randrange(2,10)
			answer = (c-brac)*d
			if random.randrange(0,2)==1:
				question = "(" + str(c) + " - " + bracstring + ") \\times " + str(d)
			else:
				question = str(d) + "\\times (" + str(c) + " - " + bracstring + ")"
		else:
			
			d = (c-brac) * random.randrange(2,10)
			answer = int(d/(c-brac))
			question = str(d) + "\\div (" + str(c) + " - " + bracstring + ")"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def bidmas20(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(0,2)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def bidmas21(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(0,2)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = question + " + " + str(d)
				answer = answer + d
			else:
				d = random.randrange(1,answer)
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = str(d) + " + " + question
				answer = answer + d
			else:
				d = answer + random.randrange(1,answer)
				answer = d - answer
				question = str(d) + " - " + question
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def bidmas22(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		c = random.randrange(2,10)
		temp = random.randrange(2,10)
		bs = list(range(2,10))
		bs.remove(temp)
		a = random.choice(bs)
		b = abs(temp-a)
		if a<temp:
			sign = " + "
		else:
			sign = " - "
		bracstring = "(" + str(a) + sign + str(b) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,2)==1:
				answer = temp * c
				question = bracstring + " \\times " + str(c)
			else:
				answer = random.randrange(2,10)
				temp = answer * c
				bs = list(range(2,10))
				if temp in bs:
					bs.remove(temp)
				a = random.choice(bs)
				b = abs(temp - a)
				if a<temp:
					sign = " + "
				else:
					sign = " - "
				bracstring = "(" + str(a) + sign + str(b) + ")"
				question = bracstring + " \\div " + str(c)
		else:
			answer = temp * c
			question = str(c) + " \\times " + bracstring
				
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas23(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		c = random.randrange(2,10)
		temp = random.randrange(2,10)
		bs = list(range(2,10))
		bs.remove(temp)
		a = random.choice(bs)
		b = abs(temp-a)
		if a<temp:
			sign = " + "
		else:
			sign = " - "
		bracstring = "(" + str(a) + sign + str(b) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,2)==1:
				answer = temp * c
				question = bracstring + " \\times " + str(c)
			else:
				answer = random.randrange(2,10)
				temp = answer * c
				bs = list(range(2,10))
				if temp in bs:
					bs.remove(temp)
				a = random.choice(bs)
				b = abs(temp - a)
				if a<temp:
					sign = " + "
				else:
					sign = " - "
				bracstring = "(" + str(a) + sign + str(b) + ")"
				question = bracstring + " \\div " + str(c)
		else:
			answer = temp * c
			question = str(c) + " \\times " + bracstring
		ds = list(range(2,10))
		if answer in ds:
			ds.remove(answer)
		d = random.choice(ds)
		if d**2>answer:
			question = str(d) + "^{2} - " + question
			answer = d**2 - answer
		else:
			answer = d**2 + answer
			if random.randrange(0,2)==1:
				question = str(d) + "^{2} + " + question
			else:
				question = question + " + " + str(d) + "^{2}"

#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmas24(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		temp = random.randrange(2,min(a**2,10))
		answer = a**2 - temp
		bs = list(range(2,10))
		bs.remove(temp)
		b = random.choice(bs)
		c = abs(temp-b)
		if b<temp:
			bracstring = "(" + str(b) + " + " + str(c) + ")"
		else:
			bracstring = "(" + str(b) + " - " + str(c) + ")"
		question = str(a) + "^{2} - " + bracstring
		
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmas25(n,explanationn):
	import random
	from math import ceil,sqrt,floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			temp1 = random.randrange(2,10)
			a = random.randrange(ceil(sqrt(temp1))+1,10)
			temp2 = a**2 - temp1
			nums = list(range(max(2,temp2 - 9),temp2+10))
			nums.remove(temp2)
			b = random.choice(nums)
			c = abs(temp2 - b)
			if b<temp2:
				bracstring = "(" + str(b) + " + " + str(c) + ")"
			else:
				bracstring = "(" + str(b) + " - " + str(c) + ")"
			bracstring = "(" + str(a) + "^{2} - " + bracstring + ")"
			d = random.randrange(2,10)
			answer = temp1 * d
			if random.randrange(0,2)==1:
				question = str(d) + " \\times " + bracstring
			else:
				question = bracstring + " \\times " + str(d)
		else:
			d = random.randrange(2,10)
			a = random.randrange(ceil(sqrt(2*d)+1),11)
			brac = random.randrange(2,floor(a**2/d))
			answer = brac
			brac = brac * d
			temp2 = a**2 - brac
			nums = list(range(max(2,temp2 - 9),temp2+10))
			nums.remove(temp2)
			b = random.choice(nums)
			c = abs(temp2 - b)
			if b<temp2:
				bracstring = "(" + str(b) + " + " + str(c) + ")"
			else:
				bracstring = "(" + str(b) + " - " + str(c) + ")"
			question = "(" + str(a) + "^{2} - " + bracstring + ") \\div " + str(d)
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs1(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = temp**2
		aas = list(range(2,10))
		aas.remove(temp)
		a = random.choice(aas)
		b = abs(temp - a)
		if a<temp:
			brac = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac = "(" + str(a) + " - " + str(b) + ")"
		question = brac + "^{2}"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs2(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = temp**2
		aas = list(range(2,10))
		aas.remove(temp)
		a = random.choice(aas)
		b = abs(temp - a)
		c = random.randrange(2,10)
		if a<temp:
			brac = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac = "(" + str(a) + " - " + str(b) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(1,2)==1:
				question = brac + "^{2} + " + str(c)
			else:
				question = str(c) + " + " + brac + "^{2}"
			answer = answer + c
		else:
			if random.randrange(1,2)==1:
				question = brac + "^{2} - " + str(c)
				answer = answer - c
			else:
				question = str(c) + " - " + brac + "^{2}"
				answer = c - answer
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs3(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		temp = random.randrange(2,10)
		answer = temp**2
		aas = list(range(2,10))
		aas.remove(temp)
		a = random.choice(aas)
		b = abs(temp - a)
		c = random.randrange(2,10)
		if a<temp:
			brac = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac = "(" + str(a) + " - " + str(b) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,1)==1:
				question = brac + "^{2} + " + str(c)
			else:
				question = str(c) + " + " + brac + "^{2}"
			answer = answer + c
		else:
			if random.randrange(0,1)==1:
				question = brac + "^{2} - " + str(c)
				answer = answer - c
			else:
				c = c + answer
				question = str(c) + " - " + brac + "^{2}"
				answer = c - answer
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs4(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			a = random.randrange(2,10)
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				brac = a + b
				bracstring = "(" + str(a) + " + " + str(b) + ")"
			else:
				if a<b:
					a,b = b,a
				brac = a - b
				bracstring = "(" + str(a) + " - " + str(b) + ")"
		else:
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				brac = a + b
				bracstring = "(" + str(a) + " + " + str(b) + ")"
			else:
				a = b**2 + random.randrange(2,10)
				brac = a - b
				bracstring = "(" + str(a) + " - " + str(b) + ")"
		temp = random.randrange(2,10)
		c = temp + brac
		if random.randrange(0,2)==1:
			d = random.randrange(2,10)
			answer = (c-brac)*d
			if random.randrange(0,1)==1:
				question = "(" + str(c) + " - " + bracstring + ") \\times " + str(d)
			else:
				question = str(d) + "\\times (" + str(c) + " - " + bracstring + ")"
		else:
			
			d = (c-brac) * random.randrange(2,10)
			answer = int(d/(c-brac))
			question = str(d) + "\\div (" + str(c) + " - " + bracstring + ")"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs5(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			a = random.randrange(2,10)
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				brac = a + b
				bracstring = "(" + str(a) + " + " + str(b) + ")"
			else:
				if a<b:
					a,b = b,a
				brac = a - b
				bracstring = "(" + str(a) + " - " + str(b) + ")"
		else:
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				brac = a + b
				bracstring = "(" + str(a) + " + " + str(b) + ")"
			else:
				a = b**2 + random.randrange(2,10)
				brac = a - b
				bracstring = "(" + str(a) + " - " + str(b) + ")"
		temp = random.randrange(2,10)
		c = temp + brac
		if random.randrange(1,2)==1:
			d = random.randrange(2,10)
			answer = (c-brac)*d
			if random.randrange(1,2)==1:
				question = "(" + str(c) + " - " + bracstring + ") \\times " + str(d)
			else:
				question = str(d) + "\\times (" + str(c) + " - " + bracstring + ")"
		else:
			
			d = (c-brac) * random.randrange(2,10)
			answer = int(d/(c-brac))
			question = str(d) + "\\div (" + str(c) + " - " + bracstring + ")"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs6(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		nums = list(range(2,10))
		temp1 = random.choice(nums)
		nums.remove(temp1)
		answer = temp1**2
		temp2 = random.choice(nums)
		a = temp1 * temp2
		nums.remove(temp2)
		swap = 1 
		if swap==1:
			temp2,a = a,temp2
		nums = list(range(2,10))
		if temp2 in nums:
			nums.remove(temp2)
		b = random.choice(nums)
		c = abs(b-temp2)
		if b>temp2:
			sign = " - "
		else:
			sign = " + "
		if swap==1:
			question = "((" + str(b) + sign + str(c) + ") \\div" + str(a) + ")^{2}"
		else:
			question = "(" + str(a) + "\\div (" + str(b)  + sign + str(c) + "))^{2}"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs7(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		nums = list(range(2,10))
		temp1 = random.choice(nums)
		nums.remove(temp1)
		answer = temp1**2
		temp2 = random.choice(nums)
		a = temp1 * temp2
		nums.remove(temp2)
		swap = 7 
		if swap==1:
			temp2,a = a,temp2
		nums = list(range(2,10))
		if temp2 in nums:
			nums.remove(temp2)
		b = random.choice(nums)
		c = abs(b-temp2)
		if b>temp2:
			sign = " - "
		else:
			sign = " + "
		if swap==1:
			question = "((" + str(b) + sign + str(c) + ") \\div" + str(a) + ")^{2}"
		else:
			question = "(" + str(a) + "\\div (" + str(b)  + sign + str(c) + "))^{2}"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs8(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		brac = random.randrange(2,10)
		nums = list(range(2,10))
		nums.remove(brac)
		c = random.choice(nums)
		d = abs(brac-c)
		if c>brac:
			sign2 = " - "
		else:
			sign2 = " + "
		b = random.randrange(2,10)
		temp = b * brac
		brac = "(" + str(c) + sign2 + str(d) + ")"
		if random.randrange(1,2)==1:
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				question = str(a) + " + "  + str(b) + "\\times (" + str(c) + sign2 + str(d) + ")"
				answer = a + temp
			else:
				a = temp + random.randrange(2,10)
				question = str(a) + " - "  + str(b) + "\\times (" + str(c) + sign2 + str(d) + ")"
				answer = a - temp
		else:
			a = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = "(" + str(c) + sign2 + str(d) + ") \\times" + str(b) + " + " + str(a)
				answer = temp + a
			else:
				question = "(" + str(c) + sign2 + str(d) + ") \\times" + str(b) + " - " + str(a)
				answer = temp - a
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs9(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		brac = random.randrange(2,10)
		nums = list(range(2,10))
		nums.remove(brac)
		c = random.choice(nums)
		d = abs(brac-c)
		if c>brac:
			sign2 = " - "
		else:
			sign2 = " + "
		b = random.randrange(2,10)
		temp = b * brac
		brac = "(" + str(c) + sign2 + str(d) + ")"
		if random.randrange(0,1)==1:
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				question = str(a) + " + "  + str(b) + "\\times (" + str(c) + sign2 + str(d) + ")"
				answer = a + temp
			else:
				a = temp + random.randrange(2,10)
				question = str(a) + " - "  + str(b) + "\\times (" + str(c) + sign2 + str(d) + ")"
				answer = a - temp
		else:
			a = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = "(" + str(c) + sign2 + str(d) + ") \\times" + str(b) + " + " + str(a)
				answer = temp + a
			else:
				question = "(" + str(c) + sign2 + str(d) + ") \\times" + str(b) + " - " + str(a)
				answer = temp - a
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs10(n,explanationn):
	import random,re
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(1,3)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(1,2)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs11(n,explanationn):
	import random,re
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(2,4)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(0,1)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs12(n,explanationn):
	import random,re
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(1,3)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(1,2)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		if random.randrange(1,2)==1:
			d = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = question + " + " + str(d)
				answer = answer + d
			else:
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				answer = answer + d
				question = str(d) + " + " + question
			else:
				d = answer + random.randrange(2,10)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def bidmasbracs13(n,explanationn):
	import random,re
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(1,3)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(1,2)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		if random.randrange(0,1)==1:
			d = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = question + " + " + str(d)
				answer = answer + d
			else:
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				answer = answer + d
				question = str(d) + " + " + question
			else:
				d = answer + random.randrange(2,10)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs14(n,explanationn):
#merge with 13
	import random,re
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(2,4)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(0,1)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		if random.randrange(1,2)==1:
			d = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = question + " + " + str(d)
				answer = answer + d
			else:
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				answer = answer + d
				question = str(d) + " + " + question
			else:
				d = answer + random.randrange(2,10)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs15(n,explanationn):
	import random,re
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		b = random.randrange(2,10)
		dec = random.randrange(2,4)
		if dec==1:
			c = random.randrange(2,10)
			temp = c * random.randrange(floor(b**2/c)+1,floor(b**2/c)+5)
			a = temp - b**2
			answer = int((a+b**2)/c)
			if random.randrange(0,2)==1:
				question = "(" + str(a) + " + " + str(b) + "^{2}) \\div" + str(c)
			else:
				question = "(" + str(b) + "^{2} + " + str(a) + ") \\div" + str(c)
		elif dec==2:
			a = b**2 + random.randrange(2,10)
			c = random.randrange(2,10)
			answer = int(c * (a - b**2))
			if random.randrange(0,1)==1:
				question = "(" + str(a) + " - " + str(b) + "^{2}) \\times " + str(c)
			else:
				question = str(c) + "\\times (" + str(a) + " - " + str(b) + "^{2})"
		else:
			a = b**2 + random.randrange(2,10)
			c = (a - b**2) * random.randrange(2,10)
			answer = int(c/(a-b**2))
			question = str(c) + " \\div (" + str(a) + " - " + str(b) + "^{2})"
		if random.randrange(0,1)==1:
			d = random.randrange(2,10)
			if random.randrange(0,2)==1:
				question = question + " + " + str(d)
				answer = answer + d
			else:
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				answer = answer + d
				question = str(d) + " + " + question
			else:
				d = answer + random.randrange(2,10)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs16(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			a = random.randrange(2,10)
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				brac = a**2 + b
				bracstring = "(" + str(a) + "^{2} + " + str(b) + ")"
			else:
				brac = a**2 - b
				bracstring = "(" + str(a) + "^{2} - " + str(b) + ")"
		else:
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				brac = a + b**2
				bracstring = "(" + str(a) + " + " + str(b) + "^{2})"
			else:
				a = b**2 + random.randrange(2,10)
				brac = a - b**2
				bracstring = "(" + str(a) + " - " + str(b) + "^{2})"
		temp = random.randrange(2,10)
		c = temp + brac
		if random.randrange(1,2)==1:
			d = random.randrange(2,10)
			answer = (c-brac)*d
			if random.randrange(1,2)==1:
				question = "(" + str(c) + " - " + bracstring + ") \\times " + str(d)
			else:
				question = str(d) + "\\times (" + str(c) + " - " + bracstring + ")"
		else:
			
			d = (c-brac) * random.randrange(2,10)
			answer = int(d/(c-brac))
			question = str(d) + "\\div (" + str(c) + " - " + bracstring + ")"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs17(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			a = random.randrange(2,10)
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				brac = a**2 + b
				bracstring = "(" + str(a) + "^{2} + " + str(b) + ")"
			else:
				brac = a**2 - b
				bracstring = "(" + str(a) + "^{2} - " + str(b) + ")"
		else:
			b = random.randrange(2,10)
			if random.randrange(0,2)==1:
				a = random.randrange(2,10)
				brac = a + b**2
				bracstring = "(" + str(a) + " + " + str(b) + "^{2})"
			else:
				a = b**2 + random.randrange(2,10)
				brac = a - b**2
				bracstring = "(" + str(a) + " - " + str(b) + "^{2})"
		temp = random.randrange(2,10)
		c = temp + brac
		if random.randrange(0,2)==1:
			d = random.randrange(2,10)
			answer = (c-brac)*d
			if random.randrange(0,1)==1:
				question = "(" + str(c) + " - " + bracstring + ") \\times " + str(d)
			else:
				question = str(d) + "\\times (" + str(c) + " - " + bracstring + ")"
		else:
			
			d = (c-brac) * random.randrange(2,10)
			answer = int(d/(c-brac))
			question = str(d) + "\\div (" + str(c) + " - " + bracstring + ")"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs18(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets:  "
		else:
			explanation = ""
		nums = list(range(2,10))
		num1 = random.choice(nums)
		nums.remove(num1)
		num2 = random.choice(nums)
		answer = num1*num2

		aas = list(range(2,10))
		aas.remove(num1)
		a = random.choice(aas)
		b = abs(num1-a)
		if a<num1:
			brac1 = "(" + str(a) + " + " + str(b) + ")"
		else:
			brac1 = "(" + str(a) + " - " + str(b) + ")"
		
		cs = list(range(2,10))
		cs.remove(num2)
		c = random.choice(cs)
		d = abs(num2-c)
		if c<num2:
			brac2 = "(" + str(c) + " + " + str(d) + ")"
		else:
			brac2 = "(" + str(c) + " - " + str(d) + ")"
		
		question = brac1 + " \\times " + brac2
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs19(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(1,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(1,2)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def bidmasbracs20(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(0,1)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs21(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(1,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(1,2)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		if random.randrange(1,2)==1:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = question + " + " + str(d)
				answer = answer + d
			else:
				d = random.randrange(1,answer)
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = str(d) + " + " + question
				answer = answer + d
			else:
				d = answer + random.randrange(1,answer)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs22(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(0,1)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
		if random.randrange(0,1)==1:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = question + " + " + str(d)
				answer = answer + d
			else:
				d = random.randrange(1,answer)
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = str(d) + " + " + question
				answer = answer + d
			else:
				d = answer + random.randrange(1,answer)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs23(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			sign1 = " \\times "
			a = random.randrange(2,10)
			if a<6:
				temps = [2,3,4,5,10]
			else:
				temps = [2,5,10]
			temp = random.choice(temps)
			answer = a**2 * temp
			bs = list(range(2,11))
			bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			if random.randrange(0,2)==1:
				question = "(" + str(b) + sign2 + str(c) + ")" + sign1 + str(a) + "^{2}"
				bracpos = 1
			else:
				question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
				bracpos = 2
		else:
			sign1 = " \\div "
			aas = [4,6,8,9,10]
			a = random.choice(aas)
			temps = []
			for i in range(2,a):
				if a**2%i==0:
					temps.append(i)
					temps.append(int(a**2/i))
			temp = random.choice(temps)
			answer = int(a**2 / temp)
			bs = list(range(2,11))
			if temp in bs:
				bs.remove(temp)
			b = random.choice(bs)
			c = abs(b-temp)
			if b<temp:
				sign2 = " + "
			else:
				sign2 = " - "
			question = str(a) + "^{2}" + sign1 + "(" + str(b) + sign2 + str(c) + ")"
			bracpos = 2
		if bracpos==2:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = question + " + " + str(d)
				answer = answer + d
			else:
				d = random.randrange(1,answer)
				question = question + " - " + str(d)
				answer = answer - d
		else:
			if random.randrange(0,2)==1:
				d = random.randrange(2,10)
				question = str(d) + " + " + question
				answer = answer + d
			else:
				d = answer + random.randrange(1,answer)
				answer = d - answer
				question = str(d) + " - " + question
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs24(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		c = random.randrange(2,10)
		temp = random.randrange(2,10)
		bs = list(range(2,10))
		bs.remove(temp)
		a = random.choice(bs)
		b = abs(temp-a)
		if a<temp:
			sign = " + "
		else:
			sign = " - "
		bracstring = "(" + str(a) + sign + str(b) + ")"
		if random.randrange(1,2)==1:
			if random.randrange(0,2)==1:
				answer = temp * c
				question = bracstring + " \\times " + str(c)
			else:
				answer = random.randrange(2,10)
				temp = answer * c
				bs = list(range(2,10))
				if temp in bs:
					bs.remove(temp)
				a = random.choice(bs)
				b = abs(temp - a)
				if a<temp:
					sign = " + "
				else:
					sign = " - "
				bracstring = "(" + str(a) + sign + str(b) + ")"
				question = bracstring + " \\div " + str(c)
		else:
			answer = temp * c
			question = str(c) + " \\times " + bracstring
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
				
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs25(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		c = random.randrange(2,10)
		temp = random.randrange(2,10)
		bs = list(range(2,10))
		bs.remove(temp)
		a = random.choice(bs)
		b = abs(temp-a)
		if a<temp:
			sign = " + "
		else:
			sign = " - "
		bracstring = "(" + str(a) + sign + str(b) + ")"
		if random.randrange(0,1)==1:
			if random.randrange(0,1)==1:
				answer = temp * c
				question = bracstring + " \\times " + str(c)
			else:
				answer = random.randrange(2,10)
				temp = answer * c
				bs = list(range(2,10))
				if temp in bs:
					bs.remove(temp)
				a = random.choice(bs)
				b = abs(temp - a)
				if a<temp:
					sign = " + "
				else:
					sign = " - "
				bracstring = "(" + str(a) + sign + str(b) + ")"
				question = bracstring + " \\div " + str(c)
		else:
			answer = temp * c
			question = str(c) + " \\times " + bracstring
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
				
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs26(n,explanationn):
#this one not split because it's too complicated
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		c = random.randrange(2,10)
		temp = random.randrange(2,10)
		bs = list(range(2,10))
		bs.remove(temp)
		a = random.choice(bs)
		b = abs(temp-a)
		if a<temp:
			sign = " + "
		else:
			sign = " - "
		bracstring = "(" + str(a) + sign + str(b) + ")"
		if random.randrange(0,2)==1:
			if random.randrange(0,2)==1:
				answer = temp * c
				question = bracstring + " \\times " + str(c)
			else:
				answer = random.randrange(2,10)
				temp = answer * c
				bs = list(range(2,10))
				if temp in bs:
					bs.remove(temp)
				a = random.choice(bs)
				b = abs(temp - a)
				if a<temp:
					sign = " + "
				else:
					sign = " - "
				bracstring = "(" + str(a) + sign + str(b) + ")"
				question = bracstring + " \\div " + str(c)
		else:
			answer = temp * c
			question = str(c) + " \\times " + bracstring
		ds = list(range(2,10))
		if answer in ds:
			ds.remove(answer)
		d = random.choice(ds)
		if d**2>answer:
			question = str(d) + "^{2} - " + question
			answer = d**2 - answer
		else:
			answer = d**2 + answer
			if random.randrange(0,2)==1:
				question = str(d) + "^{2} + " + question
			else:
				question = question + " + " + str(d) + "^{2}"
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"

#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs27(n,explanationn):
	import random,re
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		a = random.randrange(2,10)
		temp = random.randrange(2,min(a**2,10))
		answer = a**2 - temp
		bs = list(range(2,10))
		bs.remove(temp)
		b = random.choice(bs)
		c = abs(temp-b)
		if b<temp:
			bracstring = "(" + str(b) + " + " + str(c) + ")"
		else:
			bracstring = "(" + str(b) + " - " + str(c) + ")"
		question = str(a) + "^{2} - " + bracstring
		
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def bidmasbracs28(n,explanationn):
	import random,re
	from math import ceil,sqrt,floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			temp1 = random.randrange(2,10)
			a = random.randrange(ceil(sqrt(temp1))+1,10)
			temp2 = a**2 - temp1
			nums = list(range(max(2,temp2 - 9),temp2+10))
			nums.remove(temp2)
			b = random.choice(nums)
			c = abs(temp2 - b)
			if b<temp2:
				bracstring = "(" + str(b) + " + " + str(c) + ")"
			else:
				bracstring = "(" + str(b) + " - " + str(c) + ")"
			bracstring = "(" + str(a) + "^{2} - " + bracstring + ")"
			d = random.randrange(2,10)
			answer = temp1 * d
			if random.randrange(0,1)==1:
				question = str(d) + " \\times " + bracstring
			else:
				question = bracstring + " \\times " + str(d)
		else:
			d = random.randrange(2,10)
			a = random.randrange(ceil(sqrt(2*d)+1),11)
			brac = random.randrange(2,floor(a**2/d))
			answer = brac
			brac = brac * d
			temp2 = a**2 - brac
			nums = list(range(max(2,temp2 - 9),temp2+10))
			nums.remove(temp2)
			b = random.choice(nums)
			c = abs(temp2 - b)
			if b<temp2:
				bracstring = "(" + str(b) + " + " + str(c) + ")"
			else:
				bracstring = "(" + str(b) + " - " + str(c) + ")"
			question = "(" + str(a) + "^{2} - " + bracstring + ") \\div " + str(d)
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def bidmasbracs29(n,explanationn):
	import random,re
	from math import ceil,sqrt,floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Add brackets "
		else:
			explanation = ""
		if random.randrange(1,2)==1:
			temp1 = random.randrange(2,10)
			a = random.randrange(ceil(sqrt(temp1))+1,10)
			temp2 = a**2 - temp1
			nums = list(range(max(2,temp2 - 9),temp2+10))
			nums.remove(temp2)
			b = random.choice(nums)
			c = abs(temp2 - b)
			if b<temp2:
				bracstring = "(" + str(b) + " + " + str(c) + ")"
			else:
				bracstring = "(" + str(b) + " - " + str(c) + ")"
			bracstring = "(" + str(a) + "^{2} - " + bracstring + ")"
			d = random.randrange(2,10)
			answer = temp1 * d
			if random.randrange(1,2)==1:
				question = str(d) + " \\times " + bracstring
			else:
				question = bracstring + " \\times " + str(d)
		else:
			d = random.randrange(2,10)
			a = random.randrange(ceil(sqrt(2*d)+1),11)
			brac = random.randrange(2,floor(a**2/d))
			answer = brac
			brac = brac * d
			temp2 = a**2 - brac
			nums = list(range(max(2,temp2 - 9),temp2+10))
			nums.remove(temp2)
			b = random.choice(nums)
			c = abs(temp2 - b)
			if b<temp2:
				bracstring = "(" + str(b) + " + " + str(c) + ")"
			else:
				bracstring = "(" + str(b) + " - " + str(c) + ")"
			question = "(" + str(a) + "^{2} - " + bracstring + ") \\div " + str(d)
		answer = "$" + question + " = " + str(answer) + "$"
		question = "\\mbox{" + re.sub('\(|\)','',answer) + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
