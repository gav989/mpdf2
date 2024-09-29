#!/usr/bin/env python3
#primefactors.py
def factortrees1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " as a product of prime factors"
		else:
			explanation1 = ""
			explanation2 = ""
		if random.randrange(1,3)==1:
			a = random.randrange(2,13)
			b = random.randrange(2,13)
		else:
			a = random.randrange(1,11)
			b = 10**random.randrange(1,3)
		number = a * b
		two = 0
		three = 0
		five = 0
		seven = 0
		eleven = 0
		factorisation = "$"
		while two==0:
			if number%2==0:
				number = number / 2
				factorisation = factorisation + "2 \\times "
			else:
				two = 1
		while three==0:
			if number%3==0:
				number = number / 3
				factorisation = factorisation + "3 \\times "
			else:
				three = 1
		while five==0:
			if number%5==0:
				number = number / 5
				factorisation = factorisation + "5 \\times "
			else:
				five = 1
		while seven==0:
			if number%7==0:
				number = number / 7
				factorisation = factorisation + "7 \\times "
			else:
				seven = 1
		while eleven==0:
			if number%11==0:
				number = number / 11
				factorisation = factorisation + "11 \\times "
			else:
				eleven = 1
		factorisation = factorisation[:-7]
		factorisation = factorisation + "$"
#write question
		tempquestions.write(explanation1 + str(a*b) + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(factorisation)


def factortrees2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " as a product of prime factors"
		else:
			explanation1 = ""
			explanation2 = ""
		a = random.randrange(2,13)
		b = random.randrange(2,13)
		if random.randrange(1,3)==1:
			c = random.randrange(1,13)
		else:
			c = 10**random.randrange(1,3)
		number = a * b * c
		two = 0
		three = 0
		five = 0
		seven = 0
		eleven = 0
		factorisation = "$"
		while two==0:
			if number%2==0:
				number = number / 2
				factorisation = factorisation + "2 \\times "
			else:
				two = 1
		while three==0:
			if number%3==0:
				number = number / 3
				factorisation = factorisation + "3 \\times "
			else:
				three = 1
		while five==0:
			if number%5==0:
				number = number / 5
				factorisation = factorisation + "5 \\times "
			else:
				five = 1
		while seven==0:
			if number%7==0:
				number = number / 7
				factorisation = factorisation + "7 \\times "
			else:
				seven = 1
		while eleven==0:
			if number%11==0:
				number = number / 11
				factorisation = factorisation + "11 \\times "
			else:
				eleven = 1
		factorisation = factorisation[:-7]
		factorisation = factorisation + "$"
#write question
		tempquestions.write(explanation1 + str(a*b*c) + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(factorisation)



def hcf(n,explanationn):
	import random
	from math import floor
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the Highest Common Factor of:  "
		else:
			explanation = ""
		hcfchoice = (2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25,27,28,30,32,35,36,40,42,44,45,48)
		hcf = random.choice(hcfchoice)
		choices = [2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25,27,28,30,32,35,36,40,42,44,45,48,49,50,54,55,56,60,63,64,66,70,72,75]
		length = len(choices)
		for i in range(0,length-1):
			item = choices[length-1-i]
			if item>floor(150/hcf)+1:
				choices.remove(item)
		a = random.choice(choices)
		length = len(choices)
		for i in range(0,length):
			item = choices[length-1-i]
			if item%a==0 or a%item==0:
				choices.remove(item)
		b = random.choice(choices)
		a = a*hcf
		b = b*hcf
		hcf = gcd(a,b)
#write question
		tempquestions.write(explanation + str(a) + " and " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(hcf))



def lcm(n,explanationn):
	import random
	from math import floor
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the Lowest Common Multiple of:  "
		else:
			explanation = ""
		hcfchoice = (2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25,27,28,30,32,35,36,40,42,44,45,48)
		hcf = random.choice(hcfchoice)
		choices = [2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25,27,28,30,32,35,36,40,42,44,45,48,49,50,54,55,56,60,63,64,66,70,72,75]
		length = len(choices)
		for i in range(0,length-1):
			item = choices[length-1-i]
			if item>floor(150/hcf)+1:
				choices.remove(item)
		a = random.choice(choices)
		length = len(choices)
		for i in range(0,length):
			item = choices[length-1-i]
			if item%a==0 or a%item==0:
				choices.remove(item)
		b = random.choice(choices)
		a = a*hcf
		b = b*hcf
		hcf = gcd(a,b)
		lcm = int(a * b / hcf)
#write question
		tempquestions.write(explanation + str(a) + " and " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(lcm))


def hcflcm(n,explanationn):
	import random
	from math import floor
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the Highest Common Factor and Lowest Common Multiple of:  "
		else:
			explanation = ""
		hcfchoice = (2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25,27,28,30,32,35,36,40,42,44,45,48)
		hcf = random.choice(hcfchoice)
		choices = [2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25,27,28,30,32,35,36,40,42,44,45,48,49,50,54,55,56,60,63,64,66,70,72,75]
		length = len(choices)
		for i in range(0,length-1):
			item = choices[length-1-i]
			if item>floor(150/hcf)+1:
				choices.remove(item)
		a = random.choice(choices)
		length = len(choices)
		for i in range(0,length):
			item = choices[length-1-i]
			if item%a==0 or a%item==0:
				choices.remove(item)
		b = random.choice(choices)
		a = a*hcf
		b = b*hcf
		hcf = gcd(a,b)
		lcm = int(a * b / hcf)
#write question
		tempquestions.write(explanation + str(a) + " and " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write("HCF = " + str(hcf) + " and LCM = " + str(lcm))



def trains(n,explanationn):
	import random
	from math import floor
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""



		hcfchoice = (2,3,4,5,6,7,8,9,10,11,12)
		hcf = random.choice(hcfchoice)
		choices = [2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20]
		length = len(choices)
		for i in range(0,length-1):
			item = choices[length-1-i]
			if item>floor(40/hcf)+1:
				choices.remove(item)
		a = random.choice(choices)
		length = len(choices)
		for i in range(0,length):
			item = choices[length-1-i]
			if item%a==0 or a%item==0:
				choices.remove(item)
		b = random.choice(choices)



		interval1 = a*hcf
		interval2 = b*hcf
		hcf = gcd(interval1,interval2)
		lcm = int(interval1 * interval2 / hcf)
		hour = random.randrange(8,20)
		mins = random.randrange(0,6)*10
		if hour<10:
			h = "0" + str(hour)
		else:
			h = str(hour)
		if mins==0:
			m = "00"
		else:
			m = str(mins)
		starttime = h + ":" + m
		temphours = floor(lcm/60)
		lcm = lcm - 60*temphours
		hour = hour + temphours
		mins = mins + lcm
		if mins>59:
			mins = mins - 60
			hour = hour + 1
		if hour<10:
			h = "0" + str(hour)
		else:
			h = str(hour)
		if mins==0:
			m = "00"
		elif mins<10:
			mins = "0" + str(mins)
		else:
			m = str(mins)
		endtime = h + ":" + m
#write question
		tempquestions.write(explanation + "At a train station, northbound trains stop every " + str(interval1)  + " minutes and southbound trains stop every " + str(interval2) + " minutes.\\\\[0.3cm] Two trains stopped together at " + starttime + ".\\\\[0.3cm] Work out the next time when two trains will stop together at this station.")

		tempquestions.write("\n")
#write answer
		tempquestions.write(endtime)
