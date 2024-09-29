#!/usr/bin/env python3
#shape.py

def circlesquare(n,explanationn):
#in ks4 higher unit 2
	import random
	from math import sqrt,floor,log10,pi
	from utilities.rounding import rounddp,rounddpstring
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
		side = rounddp(sqrt(2 * (diameter/2)**2),5)
		squarea = 2 * (diameter/2)**2
		circlea = pi * (diameter/2)**2
		shadea = rounddp(circlea-squarea,2)
		if shadea%1==0:
			shadea = int(shadea)
		answer = "(a) Before rounding: " + str(side) + "..." + nl + "(b) " + str(shadea) + "cm$^{2}$"
		side = rounddpstring(side,2)
		intro = "The diagram shows a company logo.\\\\It is a square inside a circle of diameter " + str(diameter) + "cm.\\\\The vertices of the square lie on the circumference of the circle."
		image = "\\centering\\includegraphics[scale=0.5]{examquestions/images/squarecircle}"
		questiona = "(a) Show that the square has sides of length " + str(side) + "cm, correct to 2 decimal places."
		questionb = "(b) Calculate the area of the shaded region of the logo."
		question = intro + nl + image + nl + "\\raggedright" + questiona + nl + questionb
		
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def toy(n,explanationn):
#in ks4 higher unit 2
	import random
	from utilities.rounding import rounddp
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
		h = rounddp(sqrt(hyp**2 - r**2),1)
		if h%1==0:
			h = int(h)
		volume = rounddp((1/3)*pi*r**2*h + (2/3)*pi*r**3,2)
		intro = "A cat's toy is made by joining a cone to a hemisphere." + nl + "The hemisphere and cone each have radius " + str(r) + "cm." + nl + "The slant height of the cone is " + str(hyp) + "cm."
		image = "\\begin{overpic}[scale=0.45]{examquestions/images/toy} \\put(65,70){" + str(hyp) + "cm} \\put(48,37){" + str(r) + "cm} \\end{overpic}"
		questiona = "(a) Show that the total height, \\textit{H}, of the toy is " + str(h + r)+ "cm."
		questionb = "(b) Calculate the total volume of the toy."
		answer = "(b) " + str(volume) + "cm$^{3}$"
		question = "\\begin{minipage}{0.45\\textwidth}" + intro + nl + questiona + nl + questionb + "\\end{minipage} \\hfill \\begin{minipage}{0.45\\textwidth}" + image + " \\end{minipage}"

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
	from utilities.rounding import rounddp
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
		answer = rounddp(sqrt(p**2+q**2),2)
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
		questiona = "\\\\ \\raggedright Work out the area of the plan."
		image = "\\begin{overpic}[scale=0.65]{examquestions/images/icosagon} \\put(4,46){" + a + "} \\put(48,78){" + b + "} \\put(75.5,88){" + c + "} \\put(92,72.5){" + c + "} \\end{overpic}"
		question = intro + "\\centering" + image + questiona
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def frustum1(n,explanationn):
#in ks4 higher unit 5 old
	import random
	from utilities.rounding import rounddp
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
		answer = str(rounddp((1/3)*pi*r2**2*(h1+h2) - (1/3)*pi*r1**2*h1,2)) + "m$^{3}$"
		r1 = str(r1) + "m"
		r2 = str(r2) + "m"
		h1 = str(h1) + "m"
		h2 = str(h2) + "m"
		image = "\\begin{overpic}[scale=0.77]{examquestions/images/frustum} \\put(53,61){" + r1 + "} \\put(63,18){" + r2 + "} \\put(40,70){" + h1 + "} \\put(40,38){" + h2 + "} \\end{overpic}"
#write question
		tempquestions.write("\\centering" + image)

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
		answer = "$(\\dfrac{" + str(a) + "\\times" + str(b) + "}{2} \\times" + str(scale) + ")\\div" + str(c) + "$"
		nl = " \\\\[0.3cm] "
		a = str(a) + "cm"
		b = str(b) + "cm"
		c = str(c) + "cm"
		intro = "The area of the parallelogram is " + scaletext + " the area of the triangle."
		questiona = "\\raggedright Show that the perpendicular height $h$ of the parallelogram is " + str(h) + "cm."
		image = "\\centering\\begin{overpic}[scale=0.8]{examquestions/images/tripara} \\put(3,17){" + a + "} \\put(18,4){" + b + "} \\put(58,4){" + c + "} \\put(62,16){$h$} \\end{overpic}"
		question = intro + nl + image + nl + questiona
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def surdarea(n,explanationn):
#in ks4 higher unit 5 old
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		

		roots = (2,3,4,5,6)
		root = random.choice(roots)
		mults = [2,3,4,5,6]
		mults.remove(root)
		mult1 = random.choice(mults)
		mults.remove(mult1)
		mult2 = random.choice(mults)
		base1 = root*mult1
		base2 = root*mult2
		if base2>base1:
			temp = base1
			base1 = base2
			base2 = temp
		base3 = int((base1*base2)/root**2)
		if base3%16==0:
			root = int(root*4)
			base3 = int(base3/16)
		elif base3%9==0:
			root = int(root*3)
			base3 = int(base3/9)
		elif base3%4==0:
			root = int(root * 2)
			base3 = int(base3/4)
		intro = "The diagram shows a shape made from two squares and two right-angled triangles.\\\\The area of the smaller square is " + str(base2) + "cm$^{2}$ and the area of the larger square is " + str(base1) + "cm$^{2}$."
		image = "\\centering\\begin{overpic}[scale=0.4]{examquestions/images/surdarea} \\put(56,66){" + str(base1) + "cm$^{2}$} \\put(6,15){" + str(base2) + "cm$^{2}$} \\end{overpic}"
		questiona = "Work out the area of the complete shape.\\\\Give your answer in the form $a + b\\sqrt{c}$, where c is as small as possible."
		question = intro + "\\\\" + image + "\\\\" + "\\raggedright " + questiona
		answer = str(base1 + base2) + " + " + str(root) + "$\\sqrt{" + str(base3) + "}$"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def pencils1(n,explanationn):
#in ks4 higher unit 5 old
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		d = random.randrange(4,21)
		r = rounddp(d/2,1)
		if r%1==0:
			r = int(r)
		dec = random.randrange(0,4)
		if dec==1:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils1}"
			answer = pi*d + 4*d
			quantity = "Four"
		elif dec==2:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils2}"
			answer = pi*d + 2*d
			quantity = "Two"
		elif dec==3:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils3}"
			answer = pi*d + 6*d
			quantity = "Six"
		else:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils4}"
			answer = pi*d + 4*d
			quantity = "Three"
		intro = quantity + " pencils are held together with a band." + nl + "The figure below shows the bottom end of the pencils and the band."
		if random.randrange(0,2)==1:
			line2 = "Each of the pencils has a diameter of " + str(d) + "mm."
		else:
			line2 = "Each of the pencils has a radius of " + str(r) + "mm."
		question = "Find the length of the band in this position."
		questiona = "Work out the area of the complete shape.\\\\Give your answer in the form $a + b\\sqrt{c}$, where c is as small as possible."
		question = intro + nl + image + "\\end{center}" + line2 + nl + question
		answer = rounddp(answer,2)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "mm"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def pencils2(n,explanationn):
#in ks4 higher unit 5 old
	import random
	from math import pi,sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		d = random.randrange(4,21)
		r = rounddp(d/2,1)
		if r%1==0:
			r = int(r)
		dec = random.randrange(0,4)
		if dec==1:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils5}"
			answer = pi*d + 2*d + sqrt(2*d**2)
			quantity = "Three"
		elif dec==2:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils6}"
			answer = pi*d + 2*(2*d + sqrt(2*d**2))
			quantity = "Six"
		elif dec==3:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils7}"
			answer = pi*d + 3*d
			quantity = "Three"
		else:
			image = "\\begin{center}\\includegraphics[scale=0.4]{examquestions/images/pencils8}"
			answer = pi*d + 6*d
			quantity = "Six"
		intro = quantity + " pencils are held together with a band." + nl + "The figure below shows the bottom end of the pencils and the band."
		if random.randrange(0,2)==1:
			line2 = "Each of the pencils has a diameter of " + str(d) + "mm."
		else:
			line2 = "Each of the pencils has a radius of " + str(r) + "mm."
		question = "Find the length of the band in this position."
		questiona = "Work out the area of the complete shape.\\\\Give your answer in the form $a + b\\sqrt{c}$, where c is as small as possible."
		question = intro + nl + image + "\\end{center}" + line2 + nl + question
		answer = rounddp(answer,2)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "mm"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def densitylift(n,explanationn):
#in higher unit 5
	import random
	from utilities.rounding import rounddp,roundnearest
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.01cm] "
		l = random.randrange(1,21)/10
		if l%1==0:
			l = int(l)
		w = random.randrange(1,21)/10
		if w%1==0:
			w = int(w)
		d = random.randrange(1,21)/10
		if d%1==0:
			d = int(d)
		density = random.randrange(1,5) + random.randrange(1,10)/10
		mass = rounddp(1000 * l * w * d * density,2)
		if mass%1==0:
			mass = int(mass)
		maxi = roundnearest(mass,100)
		if mass>maxi:
			answer = "No because " + str(mass) + " $>$ " + str(maxi)
		else:
			answer = "Yes because " + str(mass) + " $\\leq$ " + str(maxi)
		line1 = "A scientist needs to lift a piece of catassium."
		line2 = "It is a cuboid with dimensions " + str(l) + "m by " + str(w) + "m by " + str(d) + "m."
		line3 = "Catassium has a density of " + str(density) + "g/cm$^{3}$."
		line4 = "The scientist's lifting gear can lift a maximum load of " + str(maxi) + "kg."
		line5 = "Can the lifting gear be used to lift the catassium? Justify Your Decision."
		question = line1 + nl + line2 + nl + line3 + nl + line4 + nl + line5
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def polygonanglesequation(n,explanationn):
#in higher unit 8
	import random
	from utilities.rounding import rounddp,roundnearest
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sides = [4,5,6,8,9,10,12,15,18,20,24,30,36,40,45,60,72,90,120]
		side = random.choice(sides)
		phrase = {4:"equal to",5:"1.5 times",6:"twice",8:"three times",9:"3.5 times",10:"four times",12:"five times",15:"eleven times",18:"eight times",20:"nine times",24:"eleven times",30:"fourteen times",36:"seventeen times",40:"nineteen times",45:"21.5 times",60:"twentty-nine times",72:"thirty-five times",90:"forty-four times",120:"fifty-nine times"}
		question = "An interior angle of a regular polygon is " + phrase[side] + " its exterior angle. Work out the number of sides of the polygon."
		answer = str(side)
#write question		
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fractionperimeter(n,explanationn):
#in ks3 unit 4 extension
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the perimeter:\\\\"
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		i1 = random.randrange(1,4)
		i2 = random.randrange(0,3)
		f3 = (f1 + f2)*2
		i3 = f3.numerator//f3.denominator
		f3 = f3 - i3
		i3 = i3 + (i2 + i1)*2
		i3 = str(i3) + " "
		if i2==0:
			i2 = ""
		frac1 = "$" + str(i1) + "\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "}$"
		frac2 = "$" + str(i2) + "\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$"
		if f3.numerator==0:
			answer = i3
		else:
			answer = "$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$"
		image = "\\begin{overpic}[scale=0.65]{examquestions/images/rectangle} \\put(40,43){" + frac1 + "cm} \\put(86,30){" + frac2 + "cm} \\end{overpic}"
		question = explanation + "\\centering" + image 
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tiles(n,explanationn):
	import random
	from math import gcd,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		tile = random.randrange(2,10)*10
		lengths = list(range(3,13))
		h = random.choice(lengths)
		lengths.remove(h)
		w = random.choice(lengths)
		if h>1:
			temp = w
			w = h
			h = temp
		totaltiles = w*h
		w = w*tile
		h = h*tile
		hcf = gcd(w,h)
		w = rounddp(w/100,1)
		h = rounddp(h/100,1)
		pack = random.randrange(4,7)*2
		cost = random.randrange(4,11)
		packs = ceil(totaltiles/pack)
		totalcost = "\\pounds" + str(packs*cost)
		if w%1==0:
			w = int(w)
		if h%1==0:
			h = int(h)
		w = str(w) + "m"
		h = str(h) + "m"
		words = ["floor","wall","patio"]
		wall = random.choice(words)
		image = "\\begin{overpic}[scale=0.45]{examquestions/images/rectangle} \\put(86,28){" + w + "} \\put(40,55){" + h + "} \\end{overpic}"
		l1 = "Pawl wants to cover his rectangular " + wall + " with square tiles."
		l2 = "(b) Find the largest possible size of tile he could use to fill his " + wall + " without having to cut any tiles down."
		l3 = "The tiles Pawl has chosen have sides of length " + str(tile) + "cm. Tile come in packs of " + str(pack) + " and each pack costs \\pounds" + str(cost) + "."
		l4 = "(a) Work out how much it costs Pawl to tile his " + wall + "."
		nl = " \\\\[0.3cm] "
		question = l1 + nl + "\\begin{center}" + image + "\\end{center}" + l3 + nl + l4 + nl + l2
		answer = "(a) " + totalcost + nl + "(b) " + str(hcf) + "cm"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tilesstarter(n,explanationn):
	import random
	from math import gcd,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		tile = random.randrange(2,10)*10
		lengths = list(range(3,13))
		h = random.choice(lengths)
		lengths.remove(h)
		w = random.choice(lengths)
		if h>1:
			temp = w
			w = h
			h = temp
		totaltiles = w*h
		w = w*tile
		h = h*tile
		w = rounddp(w/100,1)
		h = rounddp(h/100,1)
		if w%1==0:
			w = int(w)
		if h%1==0:
			h = int(h)
		w = str(w) + "m"
		h = str(h) + "m"
		words = ["floor","wall","patio"]
		wall = random.choice(words)
		image = "\\begin{overpic}[scale=0.3]{examquestions/images/rectangle} \\put(86,28){" + w + "} \\put(40,55){" + h + "} \\end{overpic}"
		l1 = "Pawl wants to cover his " + wall + " with square tiles."

		l3 = "The tiles have sides of length " + str(tile) + "cm. How many tiles will he need?"
		nl = " \\\\[0.1cm] "
		question = l1 + nl + "\\begin{center}" + image + "\\end{center}" + l3
		answer = str(totaltiles)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagrectangle(n,explanationn):
	import random
	from math import sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(3,13)
		b = random.randrange(3,13)
		if b>a:
			temp = a
			a = b
			b = temp
		answer = rounddp(sqrt(a**2 + b**2),2)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
		wco = "43,54" 
		hco = "89,28" 
		image = "\\centering\\begin{overpic}[scale=0.53]{shape/images/rectangleloci} \\put(" + wco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(b) + "cm} \\end{overpic}"
		if random.randrange(0,2)==1:
			question = "Find distance AC"
		else:
			question = "Find distance BD"
		question = question + "\\\\" + image
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

