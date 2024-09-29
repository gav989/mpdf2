#!/usr/bin/env python3
#formulae.py


def formulae11t3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"Write down the quadratic formula",
			"Write down the sine rule",
			"Write down the cosine rule",
			"Write down the formula for the area of a circle",
			"Write down the trig formula for the area of a triangle",
			"Write down the formula for the circumference of a circle",
			"Write down the formula for the area of a triangle",
			"Write down the formula for the area of a trapezium",
			"Write down the rearranged cosine rule"]

		answers = [
			"$x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$",
			"$\\dfrac{a}{SinA} = \\dfrac{b}{SinB} = \\dfrac{c}{SinC}$",
			"$a^{2} = b^{2} + c^{2} - 2bcCosA$",
			"$A = \\mathlarger{\\mathlarger{\\mathlarger{\\pi}}} \\times r \\times r$",
			"$Area = \\dfrac{1}{2}abSinC$",
			"$C = \\mathlarger{\\mathlarger{\\mathlarger{\\pi}}} \\times D$",
			"$\\dfrac{base \\times height}{2}$",
			"$\\dfrac{a + b}{2} \\times height$",
			"$CosA = \\dfrac{b^{2} + c^{2} - a^{2}}{2bc}$"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
