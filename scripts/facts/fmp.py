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
		tempquestions.write(str(num1) + " is a $\\underline{" + answer +"}$ of " + str(num2))


def listfactors(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "List all the factors of "
		else:
			explanation = ""
		factors = [1]
		nums = [12,14,15,16,18,20,21,22,24,25,27,28,30,32,35,36,40,42,44,45,48,50,54,56,60,64,70,72,80,90,100,120]
		num = random.choice(nums)
		for i in range(2,num):
			if num%i==0:
				factors.append(i)
		answer = ""
		for i in range(0,len(factors)):
			answer = answer + str(factors[i]) + ", "
		answer = answer + str(num)
		question = explanation + str(num)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def listprimes(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn!=0:
			explanation = "List all of the prime numbers "
		else:
			explanation = ""
		dec = random.randrange(1,5)
		if dec==1:
			question = "between 10 and 20"
			answer = "11, 13, 17, 19"
		elif dec==2:
			question = "between 20 and 30"
			answer = "23, 29"
		elif dec==3:
			question = "between 30 and 40"
			answer = "31, 37"
		else:
			question = "between 40 and 50"
			answer = "41, 43, 47"
#write question
		tempquestions.write(explanation + question)

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
		tempquestions.write(str(num) + " is a $\\underline{" + answer +"}$  number")


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



def fmpscwall(n,explanationn):
	import random
	from math import ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
		factorsof = [16,18,20,24,27,28,30,32,35,36,40,45,48,50,56,60,63,64,65,66,70,72,75,80]
		factorsof = random.choice(factorsof)
		factors = []
		for i in range (1,factorsof+1):
			if factorsof%i==0:
				factors.append(i)
		multiplesof = [4,5,6,7,8,9,10,11,12]
		multiplesof = random.choice(multiplesof)
		multiples = []
		for i in range(1,100):
			if i%multiplesof==0:
				multiples.append(i)
		squares = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
		cubes = [1,8,27,64,125]
		fulllist = list(range(1,100))
		nums = []
		nums.append(random.choice(cubes))
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in multiples:
				multiples.remove(nums[i])
			if nums[i] in squares:
				squares.remove(nums[i])
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
			if nums[i] in factors:
				factors.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(factors))
			factors.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in multiples:
				multiples.remove(nums[i])
			if nums[i] in squares:
				squares.remove(nums[i])
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(multiples))
			multiples.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in squares:
				squares.remove(nums[i])
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(squares))
			squares.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in factors:
				factors.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(primes))
			primes.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
		for j in range(0,2):
			nums.append(random.choice(fulllist))
			fulllist.remove(nums[-1])
		answera = []
		answerb = []
		answerc = []
		answerd = []
		answere = []
		primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
		cubes = [1,8,27,64,125]
		for i in range(0,len(nums)):
			if factorsof%nums[i]==0:
				answera.append(str(nums[i]))
			if nums[i]%multiplesof==0:
				answerb.append(str(nums[i]))
			if sqrt(nums[i])==int(sqrt(nums[i])):
				answerc.append(str(nums[i]))
			if nums[i] in cubes:
				answerd.append(str(nums[i]))
			if nums[i] in primes:
				answere.append(str(nums[i]))
			nums[i] = str(nums[i])
		aa = answera
		bb = answerb
		cc = answerc
		dd = answerd
		ee = answere
		answera = aa[0]
		answerb = bb[0]
		answerc = cc[0]
		answerd = dd[0]
		answere = ee[0]
		for i in range(1,len(aa)):
			answera = answera + ", " + aa[i]
		for i in range(1,len(bb)):
			answerb = answerb + ", " + bb[i]
		for i in range(1,len(cc)):
			answerc = answerc + ", " + cc[i]
		if len(dd)>1:
			for i in range(1,len(dd)):
				answerd = answerd + ", " + dd[i]
		for i in range(1,len(ee)):
			answere = answere + ", " + ee[i]
		random.shuffle(nums)
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{| c c c c c |} \\hline " + nums[0] + " & " + nums[1] + " & "  + nums[2] + " & " + nums[3] + " & " + nums[4] + "\\\\ " + nums[5] + " & " + nums[6] + " & "  + nums[7] + " & " + nums[8] + " & " + nums[9] + "\\\\"   + nums[10] + " & " + nums[11] + " & "  + nums[12] + " & " + nums[13] + " & " + nums[14] + "\\\\ \\hline \\end{tabular}"
		nl = "\\\\[0.1cm]"
		intro = "From the box above, write down all of the:"
		questiona = "(a) factors of " + str(factorsof)
		questionb = "(b) multiples of " + str(multiplesof)
		questionc = "(c) square numbers"
		questiond = "(d) cube numbers"
		questione = "(e) prime numbers"
		answera = questiona + " - " + answera
		answerb = questionb + " - " + answerb
		answerc = questionc + " - " + answerc
		answerd = questiond + " - " + answerd
		answere = questione + " - " + answere
		question = "\\begin{center}" + table + "\\end{center}" + intro + nl + questiona + nl + questionb + nl + questionc + nl + questiond + nl + questione
		answer = "\\begin{center}" + table + "\\end{center}" + intro + nl + answera + nl + answerb + nl + answerc + nl + answerd + nl + answere 
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
