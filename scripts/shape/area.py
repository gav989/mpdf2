#area.py

def arearectangle(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area:\\\\"
		else:
			explanation = ""
		a = random.randrange(4,13)
		b = random.randrange(4,13)
		area = a * b
		a = str(a) + "cm"
		b =  str(b) + "cm"
		image = "\\centering\\begin{overpic}[scale=0.7]{shape/images/rectangle} \\put(45,2){" + a + "} \\put(12,30){" + b + "} \\end{overpic}"	
		answer = str(area) + "cm$^{2}$"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
			
def areatriangle(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area:\\\\"
		else:
			explanation = ""
		a = random.randrange(4,13)
		b = random.randrange(4,13)
		area = rounddp(a * b/2,1)
		if area%1==0:
			area = int(area)
		a = str(a) + "cm"
		b =  str(b) + "cm"
		dec = random.randrange(0,3)
		if dec==1:
			image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/triangle1} \\put(45,1){" + a + "} \\put(45,40){" + b + "} \\end{overpic}"	
		elif dec==2:
			image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/triangle2} \\put(19,1){" + a + "} \\put(88,45){" + b + "} \\end{overpic}"	
		else:
			image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/triangle3} \\put(29,1){" + a + "} \\put(78,45){" + b + "} \\end{overpic}"	
			
		answer = str(area) + "cm$^{2}$"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def areaparallelogram(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and perimeter:\\\\"
		else:
			explanation = ""
		a = random.randrange(4,13)
		b = random.randrange(4,9)
		c = b + random.randrange(1,5)
		peri = a + a + c + c
		area = a * b
		a = str(a) + "cm"
		b =  str(b) + "cm"
		c =  str(c) + "cm"
		image = "\\centering\\begin{overpic}[scale=0.7]{shape/images/parallelogram} \\put(39,7){" + a + "} \\put(62,30){" + b + "}\\put(1,30){" + c + "} \\end{overpic}"	
		answer = "A = " + str(area) + "cm$^{2}$, P = " + str(peri) + "cm"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def areatrapezium(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area:\\\\"
		else:
			explanation = ""
		a = random.randrange(4,8)
		b = a + random.randrange(1,5)
		h = random.randrange(4,13)
		area = rounddp((a + b) * .5 * h,1)
		if area%1==0:
			area = int(area)
		a = str(a) + "cm"
		b =  str(b) + "cm"
		h =  str(h) + "cm"
		if random.randrange(0,2)==1:
			image = "\\centering\\begin{overpic}[scale=0.7]{shape/images/trapezium1} \\put(45,50){" + a + "} \\put(45,6){" + b + "}\\put(29,29){" + h + "} \\end{overpic}"	
		else:
			image = "\\centering\\begin{overpic}[scale=0.3]{shape/images/trapezium2} \\put(-13,30){" + b + "} \\put(90,30){" + a + "}\\put(40,0){" + h + "} \\end{overpic}"	
		answer = str(area) + "cm$^{2}$"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def arealshape(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area:\\\\"
		else:
			explanation = ""

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
		area = a*b - e*d
		a = str(a) + "cm"
		b = str(b) + "cm"
		c = str(c) + "cm"
		d = str(d) + "cm"
		e = str(e) + "cm"
		f = str(f) + "cm"
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
		if dec==1:
			rotation = 0
			aco = "-14,50"
			bco = "40,1"
			cco = "15,92"
			dco = "43,64"
			eco = "55,41"
			fco = "91,20"
		elif dec==2:
			rotation = 90
			aco = "40,1"
			bco = "91,50"
			cco = "-14,23"
			dco = "25,43"
			eco = "37,68"
			fco = "64,91"
		elif dec==3:
			rotation = 180
			aco = "90,48"
			bco = "42,92"
			cco = "65,1"
			dco = "34,29"
			eco = "27,53"
			fco = "-14,75"
		else:
			rotation = 270
			aco = "42,91"
			bco = "-14,50"
			cco = "91,70"
			dco = "60,50"
			eco = "40,29"
			fco = "15,2"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/l} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\put(" + dco + "){" + str(d) + "} \\put(" + eco + "){" + str(e) + "}  \\put(" + fco + "){" + str(f) + "} \\end{overpic}"	


		answer = str(area) + "cm$^{2}$"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def areaperilshape(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and perimeter:\\\\"
		else:
			explanation = ""
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
		area = a*b - e*d
		peri = a + a + b + b
		a = str(a) + "cm"
		b = str(b) + "cm"
		c = str(c) + "cm"
		d = str(d) + "cm"
		e = str(e) + "cm"
		f = str(f) + "cm"
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
		if dec==1:
			rotation = 0
			aco = "-14,50"
			bco = "40,1"
			cco = "15,92"
			dco = "43,64"
			eco = "55,41"
			fco = "91,20"
		elif dec==2:
			rotation = 90
			aco = "40,1"
			bco = "91,50"
			cco = "-14,23"
			dco = "25,43"
			eco = "37,68"
			fco = "64,91"
		elif dec==3:
			rotation = 180
			aco = "90,48"
			bco = "42,92"
			cco = "65,1"
			dco = "34,29"
			eco = "27,53"
			fco = "-14,75"
		else:
			rotation = 270
			aco = "42,91"
			bco = "-14,50"
			cco = "91,70"
			dco = "60,50"
			eco = "40,29"
			fco = "15,2"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/l} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\put(" + dco + "){" + str(d) + "} \\put(" + eco + "){" + str(e) + "}  \\put(" + fco + "){" + str(f) + "} \\end{overpic}"	


		answer = "A = " + str(area) + "cm$^{2}$ and Perimeter = " + str(peri) + "cm"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

