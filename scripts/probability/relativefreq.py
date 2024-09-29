#!/usr/bin/env python3
#relativefreq.py


def rf1(n,explanationn):
	import random
	from math import gcd
	from utilities.fractions import simpfrac
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		mults = [1,2,4,6,8,10]
		mult = random.choice(mults)
		n1 = 50*mult
		freqs = [1,5,10,15]
		for i in range(0,19):
			temp = random.randrange(0,4)
			freqs[temp] = freqs[temp] + 1
		for i in range(0,4):
			freqs[i] = freqs[i] * mult
		random.shuffle(freqs)
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c | c | c |} \\hline Colour & R & Y & B & G \\\\ \\hline Frequency & " + str(freqs[0]) + " & " + str(freqs[1]) + " & " + str(freqs[2]) + " & " + str(freqs[3]) + " \\\\ \\hline \\end{tabular}"
		
		l1 = "A spinner can land on red, yellow, blue or green. It is spun " + str(n1) + " times:"
		qa = random.randrange(0,4)
		colours = ["Red","Yellow","Blue","Green"]
		l2 = "a) Find the relative frequency of the spinner landing on " + colours[qa]
		answera = str(rounddp(freqs[qa]/n1,4)) + " or " + simpfrac(freqs[qa],n1)
		n2 = 100 * random.randrange(4,11) * 2
		l3 = "b) Joel spins the same spinner " + str(n2) + " times. How many times would you expect the spinner to land on " + colours[qa] + "?"
		answerb = int(n2 * freqs[qa] / n1)
		question = l1 + nl + table + nl + l2 + nl + l3
		answer = "a) " + answera + nl + "b) " + str(answerb)
		
		

#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
