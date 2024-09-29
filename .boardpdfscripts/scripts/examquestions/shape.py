#!/usr/bin/env python3
#shape.py

def circlesquare(n,explanationn):
#in ks4 higher unit 2
	import random
	from math import sqrt,floor,log10,pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		diameters = (3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
		diameter = random.choice(diameters)
		side = sqrt(2 * (diameter/2)**2)
		answer = "(a) Before rounding: " + str(side)
		roundto = 0.01
		length = len(str(floor(side)))
		side = side * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = side%roundto
		if remainder < 0.5*roundto:
			rounded = side - remainder
		else:
			rounded = side + (roundto-remainder)
		rounded = rounded / 10**(10-length)
		area = round(pi * (diameter/2)**2 - rounded**2,2)
		answer = answer + nl + "(b) " + str(area) + "cm$^{2}$"
		if rounded%1==0:
			zeros = ".00"
			rounded = int(rounded)
		elif (rounded*10)%1==0:
			zeros = "0"
		else:
			zeros = ""
		side = str(rounded) + zeros	
		intro = "The diagram shows a company logo." + nl + "It is a square inside a circle of diameter " + str(diameter) + "cm." + nl + "The vertices of the square lie on the circumference of the circle."
		image = "\\hfill\\includegraphics[scale=0.5]{examquestions/images/squarecircle}\\hfill"
		questiona = "(a) Show that the square has sides of length " + str(side) + "cm, correct to 2 decimal places."
		questionb = "(b) Calculate the area of the shaded region of the logo."
		question = intro + nl + image + nl + questiona + nl + questionb
		
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def toy(n,explanationn):
#in ks4 higher unit 2
	import random
	from math import sqrt,floor,log10,pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		r = random.randrange(3,11)
		hyp = random.randrange(3,11) + r
		h = round(sqrt(hyp**2 - r**2),1)
		if h%1==0:
			h = int(h)
		volume = round((1/3)*pi*r**2*h + (2/3)*pi*r**3,2)
		intro = "A child's toy is made by joining a cone to a hemisphere.\\\\The hemisphere and cone each have radius " + str(r) + "cm.\\\\The slant height of the cone is " + str(hyp) + "cm."
		image = "\\hfill\\begin{overpic}[scale=0.45]{examquestions/images/toy} \\put(65,70){" + str(hyp) + "cm} \\put(48,37){" + str(r) + "cm} \\end{overpic}\\hfill"


		questiona = "(a) Show that the total height, \\textit{H}, of the toy is " + str(h + r)+ "cm."
		questionb = "(b) Calculate the total volume of the toy."
		answer = "(b) " + str(volume) + "cm$^{3}$"
		question = intro + nl + image + nl + questiona + nl + questionb
		
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def circletable(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		radii = (2,3,4,5,6,8,9)
		radius = random.choice(radii)*10
		coeff = radius**2
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		intro =  "A circular table top has radius " + str(radius) + "cm."
		questiona = "(a) Calculate the area of the table top in cm$^{2}$, giving your answer as a multiple of " + pi + "."
		thickness = random.randrange(5,30)*.5
		if thickness %1==0:
			thickness = int(thickness)
		volume = str(int(coeff * thickness)) + pi
		questionb = "(b) The volume of the table is " + volume + "cm$^{3}$. \\\\ Calculate the thickness of the table top."
		question = intro + nl + questiona + nl + questionb
		answer = "(a) " + str(coeff) + pi + "cm$^{2}$" + nl + "(b) " + str(thickness) + "cm"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def pythaggrid(n,explanationn):
#in ks4 higher unit 3
	import random
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		a = random.randrange(0,10)
		b = random.randrange(0,10)
		nums = [3,4,5,6,7,8,9]
		n1 = random.choice(nums)
		nums.remove(n1)
		n2 = random.choice(nums) * (-1)**random.randrange(1,3)
		c = a + n1
		d = b + n2
		e = c + abs(n2)
		if n2<0:
			f = d + n1
		else:
			f = d - n1
		p = abs(e-a)
		q = abs(f-b)
		if random.randrange(1,3)==2:
			coordinates = ["(" + str(a) + " , " + str(b) + ")","(" + str(c) + " , " + str(d) + ")","(" + str(e) + " , " + str(f) + ")"]
		else:
			coordinates = ["(" + str(b) + " , " + str(a) + ")","(" + str(d) + " , " + str(c) + ")","(" + str(f) + " , " + str(e) + ")"]
		random.shuffle(coordinates)
		question = "A triangle ABC has vertices at A " + coordinates[0] + ", B " + coordinates[1] + " and C " + coordinates[2] + ". Use Pythagoras to calculate the length of the longest side of the triangle."
		answer = round(sqrt(p**2+q**2),2)
		if answer%1==0:
			answer = str(int(answer))
		else:
			answer = str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def icosagon(n,explanationn):
#in ks4 intermediate unit 4
	import random
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		c = random.randrange(2,7)
		b = c + random.randrange(2,7)
		a = b + c
		answer = str(a**2 + c**2 + 2*a*c - 2*b*c) + "m$^{2}$"
		a = str(a) + "m"
		b = str(b) + "m"
		c = str(c) + "m"
		intro = "The diagram shows the plan of a cat's playpen. The plan has four lines of symmetry.\\\\"
		questiona = "\\\\Work out the area of the plan."
		image = "\\hfill\\begin{overpic}[scale=0.8]{examquestions/images/icosagon} \\put(4,46){" + a + "} \\put(48,78){" + b + "} \\put(75.5,88){" + c + "} \\put(92,72.5){" + c + "} \\end{overpic}\\hfill"
		question = intro + image + questiona
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def frustum1(n,explanationn):
#in ks4 higher unit 5 old
	import random
	from math import sqrt,pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		h1 = random.randrange(1,6)*2
		r1 = random.randrange(1,6)*2
		sf = random.randrange(3,8)/2
		h2 = int(h1 * sf)
		r2 = int(r1 * sf)
		answer = str(round((1/3)*pi*r2**2*(h1+h2) - (1/3)*pi*r1**2*h1,2)) + "m$^{3}$"
		r1 = str(r1) + "m"
		r2 = str(r2) + "m"
		h1 = str(h1) + "m"
		h2 = str(h2) + "m"
		intro = "Find the volume of the frustum.\\\\"
		image = "\\hfill\\begin{overpic}[scale=0.8]{examquestions/images/frustum} \\put(53,61){" + r1 + "} \\put(63,18){" + r2 + "} \\put(40,70){" + h1 + "} \\put(40,38){" + h2 + "} \\end{overpic}\\hfill"
		question = intro + image
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def tripara(n,explanationn):
#in ks4 higher unit 5 old
	import random
	from math import sqrt,pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = random.randrange(2,6)
		if scale==2:
			scaletext = "twice"
		elif scale==3:
			scaletext = "three times"
		elif scale==4:
			scaletext = "four times"
		elif scale==5:
			scaletext = "five times"
		a = random.randrange(2,7)*2
		b = random.randrange(2,7)*2
		triarea = a*b/2
		paraarea = triarea*scale
		bases = []
		check = 4
		while check<paraarea/check+1:
			if paraarea%check==0:
				bases.append(check)
			check = check + 1
		c = random.choice(bases)
		h = int(paraarea/c)
		nl = " \\\\[0.3cm] "
		a = str(a) + "cm"
		b = str(b) + "cm"
		c = str(c) + "cm"
		intro = "The area of the parallelogram is " + scaletext + " the area of the triangle."
		questiona = "Show that the perpendicular height $h$ of the parallelogram is " + str(h) + "cm."
		image = "\\hfill\\begin{overpic}[scale=0.8]{examquestions/images/tripara} \\put(3,17){" + a + "} \\put(18,4){" + b + "} \\put(57,4){" + c + "} \\put(62,16){$h$} \\end{overpic}\\hfill"
		question = intro + nl + image + nl + questiona
		answer = "test"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

