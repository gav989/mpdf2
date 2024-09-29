#!/usr/bin/env python3
#multichoice.py


def mc1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "When you see a scatter graph, you should:"
		answers = [
		"Draw a line of best fit",
		"Not draw anything, graphs aren't about drawing",
		"Join up all the points, like a dot to dot, like when you were a child",
		"Draw some weird curve thing"
		]
		answer = answers[0]
		random.shuffle(answers)
		letters = ["A - ","B - ","C - ","D - "]
		aletter = letters[answers.index(answer)]
		question = intro + "\\\\[0.5cm]" + letters[0] + answers[0] + "\\\\[0.3cm]" + letters[1] + answers[1] + "\\\\[0.3cm]" + letters[2] + answers[2] + "\\\\[0.3cm]" + letters[3] + answers[3]
		answer = aletter + answer
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def mc2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "When you are asked to draw a histogram, you should:"
		answers = [
		"Interpret frequency as area of the bar and calculate frequency densities by dividing the frequency (area) by the class widths",
		"Draw a normal bar chart and hope the examiner doesn't notice",
		"Draw a cumulative frequency graph for no reason",
		"Calculate an estimate for the mean and completely ignore the space provided to draw something"
		]
		answer = answers[0]
		random.shuffle(answers)
		letters = ["A - ","B - ","C - ","D - "]
		aletter = letters[answers.index(answer)]
		question = intro + "\\\\[0.5cm]" + letters[0] + answers[0] + "\\\\[0.3cm]" + letters[1] + answers[1] + "\\\\[0.3cm]" + letters[2] + answers[2] + "\\\\[0.3cm]" + letters[3] + answers[3]
		answer = aletter + answer
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
