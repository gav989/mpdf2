#!/usr/bin/env python3
#simple.py


def simpleprobstarter(n,explanationn):
	import random
	from utilities.fractions import simpfrac
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.2cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		nums = list(range(1,10))
		colours = ["Red","Blue","Green"]
		red = random.choice(nums)
		nums.remove(red)
		blue = random.choice(nums)
		nums.remove(blue)
		green = random.choice(nums)
		colourprobs = [red,blue,green]
		l1 = "In a bag there are " + str(red) + " red balls, " + str(blue) + " blue balls and " + str(green) + " green balls. Danny takes a ball out of the bag at random. Find the probability that Danny's ball is:"
		qa = random.randrange(0,3)
		answera = simpfrac(colourprobs[qa],red+blue+green)
		qa = colours[qa]
		questiona = qa
		questiona = "a) " + qa
		qb = [0,1,2]
		qbb = random.choice(qb)
		qb.remove(qbb)
		questionb = "b) " + colours[qb[0]] + " or " + colours[qb[1]]
		answerb = simpfrac(colourprobs[qb[0]] + colourprobs[qb[1]],red+blue+green)
		qc = qb
		qcc = random.choice(qc)
		qc = [0,1,2]
		qc.remove(qcc)
		questionc = "c) Not " + colours[qcc]
		answerc = simpfrac(colourprobs[qc[0]] + colourprobs[qc[1]],red+blue+green)
		question = l1 + nl + questiona + nl + questionb + nl + questionc
		answer = "a) " + answera + nl + "b) " + answerb + nl + "c) " + answerc
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

