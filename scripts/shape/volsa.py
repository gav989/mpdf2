#volsa.py

def volumecuboid(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume of a cuboid measuring  "
		else:
			explanation = ""
		a = random.randrange(1,13)
		b = random.randrange(2,13)
		c = random.randrange(2,13)
		volume = a * b * c
#write question
		tempquestions.write(explanation + str(a) + "cm by " + str(b) + "cm by " + str(c) + "cm")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(volume) + "cm$^3$")
			


def sacuboid(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the surface area of a cuboid measuring  "
		else:
			explanation = ""
		a = random.randrange(1,13)
		b = random.randrange(2,13)
		c = random.randrange(2,13)
		sa = (a * b + a * c + b * c) * 2
#write question
		tempquestions.write(explanation + str(a) + "cm by " + str(b) + "cm by " + str(c) + "cm")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(sa) + "cm$^2$")


def volsacuboid(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		a = random.randrange(1,13)
		b = random.randrange(2,13)
		c = random.randrange(2,13)
		sa = (a * b + a * c + b * c) * 2
		vol = a * b * c
		l1 = "A cuboid measures " + str(a) + "cm by " + str(b) + "cm by " + str(c) + "cm."
		l2 = "a) Find the volume of the cuboid"
		l3 = "b) Find the surface area of the cuboid"
		question = l1 + nl + l2 + nl + l3
		answer = "a) " + str(vol) + "cm$^3$" + nl + "b) " + str(sa) + "cm$^2$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def volumelprism(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		a = random.randrange(8,16)
		b = random.randrange(8,16)
		c = random.randrange(2,6)
		e = b - c
		if random.randrange(0,2)==1:
			temp = c
			c = e
			e = temp
		d = random.randrange(2,6)
		f = a - d
		if random.randrange(0,2)==1:
			temp = d
			d = f
			f = temp
		g = random.randrange(2,9)
		volume = (a*b - e*d) * g
		a = str(a) + "cm"
		b = str(b) + "cm"
		c = str(c) + "cm"
		d = str(d) + "cm"
		e = str(e) + "cm"
		f = str(f) + "cm"
		g = str(g) + "cm"
		dec = random.randrange(0,3)
		if dec==1:
			a = ""
		elif dec==2:
			d = ""
		else:
			f = ""
		dec = random.randrange(0,3)
		if dec==1:
			b = ""
		elif dec==2:
			c = ""
		else:
			e = ""
		dec = random.randrange(0,4)
		aco = "-22,50"
		bco = "35,6"
		cco = "7,78"
		dco = "50,64"
		eco = "63,45"
		fco = "98,22"
		gco = "90,3"
		image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/lprism} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\put(" + dco + "){" + str(d) + "} \\put(" + eco + "){" + str(e) + "}  \\put(" + fco + "){" + str(f) + "} \\put(" + gco + "){" + str(g) + "} \\end{overpic}"	
		answer = str(volume) + "cm$^{3}$"
#write question
		tempquestions.write(image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def volsatriprism1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(2,10)
		d = random.randrange(2,10)
		if b>a:
			a,b = b,a
		c = rounddp(sqrt(a**2 + b**2),5)
		vol = rounddp(a*b*d*0.5,2)
		if vol%1==0:
			vol = int(vol)
		sa = rounddp(a*b + d*b + a*d + c*d,2)
		if sa%1==0:
			sa = int(sa)
		a = str(a) + "cm"
		b = str(b) + "cm"
		d = str(d) + "cm"
		vol = str(vol) + "cm$^{3}$"
		sa = str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.1]{shape/images/triangularprism1} \\put(-25,35){" + a + "} \\put(19,2){" + b + "}  \\put(60,8){" + d + "}   \\end{overpic}"	
		question = image
		answer = "Volume = " + vol + "\\\\ Surface Area = " + sa
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def volsatriprism2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		a = random.randrange(2,7)
		if random.randrange(0,2)==1:
			aco = "-25,35"
		else:
			aco = "19,2"
		c = a + random.randrange(2,7)
		d = random.randrange(2,10)
		b = rounddp(sqrt(c**2 - a**2),5)
		vol = rounddp(a*b*d*0.5,2)
		if vol%1==0:
			vol = int(vol)
		sa = rounddp(a*b + d*b + a*d + c*d,2)
		if sa%1==0:
			sa = int(sa)
		a = str(a) + "cm"
		c = str(c) + "cm"
		d = str(d) + "cm"
		vol = str(vol) + "cm$^{3}$"
		sa = str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.1]{shape/images/triangularprism1} \\put(" + aco + "){" + a + "} \\put(29,41){" + c + "}  \\put(60,8){" + d + "}   \\end{overpic}"	
		question = image
		answer = "Volume = " + vol + "\\\\ Surface Area = " + sa
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def volsatriprism3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(2,10)
		d = random.randrange(2,10)
		if b>a:
			a,b = b,a
		c = rounddp(sqrt(a**2 + b**2),5)
		vol = rounddp(a*b*d,2)
		if vol%1==0:
			vol = int(vol)
		sa = rounddp(a*b*2 + d*b*2 + c*d*2,2)
		if sa%1==0:
			sa = int(sa)
		b = b * 2
		a = str(a) + "cm"
		b = str(b) + "cm"
		d = str(d) + "cm"
		vol = str(vol) + "cm$^{3}$"
		sa = str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.4]{shape/images/triangularprism2} \\put(21.2,15){" + a + "} \\put(19,2){" + b + "}  \\put(60,8){" + d + "}   \\end{overpic}"	
		question = image
		answer = "Volume = " + vol + "\\\\ Surface Area = " + sa
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def volsatriprism4(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		dec = random.randrange(0,2)
		a = random.randrange(2,7)
		if random.randrange(0,2)==1:
			aco = "-25,35"
		else:
			aco = "19,2"
		c = a + random.randrange(2,7)
		d = random.randrange(2,10)
		b = rounddp(sqrt(c**2 - a**2),5)
		if dec==1:
			a,b = b,a
		vol = rounddp(a*b*d,2)
		if vol%1==0:
			vol = int(vol)
		sa = rounddp(a*b*2 + d*b*2 + c*d*2,2)
		if sa%1==0:
			sa = int(sa)
		b = b * 2
		a = str(a) + "cm"
		b = str(b) + "cm"
		c = str(c) + "cm"
		d = str(d) + "cm"
		if dec==1:
			a = ""
		else:
			b = ""
		vol = str(vol) + "cm$^{3}$"
		sa = str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.4]{shape/images/triangularprism2} \\put(21.2,15){" + a + "} \\put(19,2){" + b + "}  \\put(39,29){" + c + "}    \\put(60,8){" + d + "}   \\end{overpic}"	
		question = image
		answer = "Volume = " + vol + "\\\\ Surface Area = " + sa
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def volsasphere(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		r = rounddp(random.randrange(3,31)/2,1)
		if r%1==0:
			r = int(r)
		answer = rounddp((4/3) * pi * r**3,2)
		answer2 = rounddp(4 * pi * r**2,2)
		answer = "Volume = " + str(answer) + "cm$^{3}$ \\\\ Surface Area = " + str(answer2) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.7]{shape/images/sphere} \\put(49,52){" + str(r) + "cm} \\end{overpic}"	
		question = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def volsacone1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		r = random.randrange(3,10)
		l = random.randrange(2,10) + r
		h = rounddp(sqrt(l**2 - r**2),5)
		vol = rounddp((1/3) * pi * r**2 * h,2)
		sa = rounddp(pi * r * l + pi * r**2,2)
		answer = "Volume = " + str(vol) + "cm$^{3}$ \\\\ Surface Area = " + str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.7]{shape/images/cone1} \\put(52,7){" + str(r) + "cm} \\put(80,52){" + str(l) + "cm} \\end{overpic}"	
		question = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def volsacone2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		r = random.randrange(3,10)
		h = random.randrange(3,10)
		l = rounddp(sqrt(h**2 + r**2),5)
		vol = rounddp((1/3) * pi * r**2 * h,2)
		sa = rounddp(pi * r * l + pi * r**2,2)
		answer = "Volume = " + str(vol) + "cm$^{3}$ \\\\ Surface Area = " + str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.7]{shape/images/cone2} \\put(52,7){" + str(r) + "cm} \\put(52,40){" + str(h) + "cm} \\end{overpic}"	
		question = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def volsacone3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""
		h = random.randrange(3,10)
		l = random.randrange(2,10) + h
		r = rounddp(sqrt(l**2 - h**2),5)
		vol = rounddp((1/3) * pi * r**2 * h,2)
		sa = rounddp(pi * r * l + pi * r**2,2)
		answer = "Volume = " + str(vol) + "cm$^{3}$ \\\\ Surface Area = " + str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=1.7]{shape/images/cone3} \\put(52,40){" + str(h) + "cm} \\put(80,52){" + str(l) + "cm} \\end{overpic}"	
		question = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def volsacylinder1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""

		r = random.randrange(3,10)
		h = 2 * r + random.randrange(3,10)
		d = r * 2
		vol = rounddp(pi * r**2 * h,2)
		sa = rounddp(pi * d * h + 2 * pi * r**2,2)
		answer = "Volume = " + str(vol) + "cm$^{3}$ \\\\ Surface Area = " + str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=4]{shape/images/cylinder1} \\put(40,3){" + str(h) + "cm} \\put(83,20){" + str(d) + "cm} \\end{overpic}"	
		question = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def volsacylinder2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the volume and surface area:\\\\[0.1cm] "
		else:
			explanation = ""

		r = random.randrange(3,10)
		h = 2 * r + random.randrange(3,10)
		d = r * 2
		vol = rounddp(pi * r**2 * h,2)
		sa = rounddp(pi * d * h + 2 * pi * r**2,2)
		answer = "Volume = " + str(vol) + "cm$^{3}$ \\\\ Surface Area = " + str(sa) + "cm$^{2}$"
		image = "\\centering\\begin{overpic}[scale=4]{shape/images/cylinder2} \\put(40,3){" + str(h) + "cm} \\put(83,20){" + str(r) + "cm} \\end{overpic}"	
		question = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

