#trig.py

def sinside1(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		h = random.randrange(7,51)
		angle = random.randrange(15,81)
		o = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				sco = "60,5"
				oco = "10,40"
				hco = "54,46"
			elif rotation==270:
				sco = "4,29"
				oco = "40,85"
				hco = "45,39"
			elif rotation==180:
				sco = "29,87"
				oco = "83,50"
				hco = "26,44"
			else:
				sco = "82,62" 
				oco = "50,9"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				sco = "19,68"
				oco = "44,3"
				hco = "54,46"
			elif rotation==270:
				sco = "69,72"
				oco = "-6,50"
				hco = "45,39"
			elif rotation==180:
				sco = "67,24"
				oco = "50,90"
				hco = "26,44"
			else:
				sco = "18,20" 
				oco = "100,45"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		o = rounddp(sin(radians(angle))*h,2)
		question = explanation + image
		answer = o
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sinside2(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		o = random.randrange(7,51)
		angle = random.randrange(15,81)
		h = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				sco = "60,5"
				oco = "-9,40"
				hco = "54,46"
			elif rotation==270:
				sco = "4,29"
				oco = "40,85"
				hco = "45,39"
			elif rotation==180:
				sco = "29,87"
				oco = "83,50"
				hco = "40,44"
			else:
				sco = "82,62" 
				oco = "50,9"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				sco = "19,68"
				oco = "40,3"
				hco = "54,46"
			elif rotation==270:
				sco = "69,72"
				oco = "-25,50"
				hco = "45,39"
			elif rotation==180:
				sco = "67,24"
				oco = "40,90"
				hco = "40,44"
			else:
				sco = "18,20" 
				oco = "100,45"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		h = rounddp(o/sin(radians(angle)),2)
		question = explanation + image
		answer = h
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cosside1(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		h = random.randrange(7,51)
		angle = random.randrange(15,81)
		a = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				cco = "60,5"
				aco = "43,3"
				hco = "54,46"
			elif rotation==270:
				cco = "4,29"
				aco = "-6,50"
				hco = "45,39"
			elif rotation==180:
				cco = "29,87"
				aco = "54,90"
				hco = "26,44"
			else:
				cco = "82,62" 
				aco = "100,45"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				cco = "19,68"
				aco = "10,45"
				hco = "54,46"
			elif rotation==270:
				cco = "69,72"
				aco = "40,85"
				hco = "45,39"
			elif rotation==180:
				cco = "67,24"
				aco = "83,50"
				hco = "26,44"
			else:
				cco = "18,20" 
				aco = "50,9"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		a = rounddp(cos(radians(angle))*h,2)
		question = explanation + image
		answer = a
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cosside2(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		a = random.randrange(7,51)
		angle = random.randrange(15,81)
		h = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				cco = "60,5"
				aco = "28,3"
				hco = "54,46"
			elif rotation==270:
				cco = "4,29"
				aco = "-25,50"
				hco = "45,39"
			elif rotation==180:
				cco = "29,87"
				aco = "48,90"
				hco = "40,44"
			else:
				cco = "82,62" 
				aco = "100,45"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				cco = "19,68"
				aco = "-9,40"
				hco = "54,46"
			elif rotation==270:
				cco = "69,72"
				aco = "40,85"
				hco = "45,39"
			elif rotation==180:
				cco = "67,24"
				aco = "83,50"
				hco = "40,44"
			else:
				cco = "18,20" 
				aco = "50,9"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		h = rounddp(a/cos(radians(angle)),2)
		question = explanation + image
		answer = h
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tanside2(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		o = random.randrange(7,51)
		angle = random.randrange(15,81)
		a = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				tco = "60,5"
				aco = "43,3"
				oco = "-10,45"
			elif rotation==270:
				tco = "4,29"
				aco = "-6,50"
				oco = "40,85"
			elif rotation==180:
				tco = "29,87"
				aco = "54,90"
				oco = "83,50"
			else:
				tco = "82,62" 
				aco = "100,45"
				oco = "50,9"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "} \\put(" + oco + "){" + str(o) + "cm} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				tco = "19,68"
				aco = "10,45"
				oco = "43,3"
			elif rotation==270:
				tco = "69,72"
				aco = "40,85"
				oco = "-24,50"
			elif rotation==180:
				tco = "67,24"
				aco = "83,50"
				oco = "48,90"
			else:
				tco = "18,20" 
				aco = "50,9"
				oco = "100,45"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "} \\put(" + oco + "){" + str(o) + "cm} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		a = rounddp(o/tan(radians(angle)),2)
		question = explanation + image
		answer = a
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tanside1(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		a = random.randrange(7,51)
		angle = random.randrange(15,81)
		o = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				tco = "60,5"
				aco = "28,3"
				oco = "-10,45"
			elif rotation==270:
				tco = "4,29"
				aco = "-24,50"
				oco = "40,85"
			elif rotation==180:
				tco = "29,87"
				aco = "49,90"
				oco = "83,50"
			else:
				tco = "82,62" 
				aco = "100,45"
				oco = "50,9"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "cm} \\put(" + oco + "){" + str(o) + "} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				tco = "19,68"
				aco = "-7,45"
				oco = "43,3"
			elif rotation==270:
				tco = "69,72"
				aco = "40,85"
				oco = "-6,50"
			elif rotation==180:
				tco = "67,24"
				aco = "83,50"
				oco = "48,90"
			else:
				tco = "18,20" 
				aco = "50,9"
				oco = "100,45"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "cm} \\put(" + oco + "){" + str(o) + "} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		o = rounddp(tan(radians(angle))*a,2)
		question = explanation + image
		answer = o
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sinangle(n,explanationn):
	import random
	from math import radians,degrees,asin,acos,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		o = random.randrange(3,35)
		h = o + random.randrange(3,35)
		angle = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				sco = "62,5"
				oco = "-8,40"
				hco = "54,46"
			elif rotation==270:
				sco = "7,30"
				oco = "40,85"
				hco = "45,39"
			elif rotation==180:
				sco = "31,86"
				oco = "83,50"
				hco = "26,44"
			else:
				sco = "87,63" 
				oco = "50,9"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "} \\end{overpic}"
		else:
			if rotation==0:
				sco = "22,70"
				oco = "44,3"
				hco = "54,46"
			elif rotation==270:
				sco = "71,72"
				oco = "-23,50"
				hco = "45,39"
			elif rotation==180:
				sco = "72,22"
				oco = "42,90"
				hco = "26,44"
			else:
				sco = "21,21" 
				oco = "100,45"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "} \\end{overpic}"
		s = rounddp(degrees(asin(o/h)),2)
		question = explanation + image
		answer = s
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def cosangle(n,explanationn):
	import random
	from math import radians,degrees,asin,acos,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		a = random.randrange(3,35)
		h = a + random.randrange(3,35)
		angle = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				cco = "62,5"
				aco = "28,3"
				hco = "54,46"
			elif rotation==270:
				cco = "7,30"
				aco = "-23,50"
				hco = "45,39"
			elif rotation==180:
				cco = "31,86"
				aco = "48,90"
				hco = "26,44"
			else:
				cco = "87,63" 
				aco = "100,45"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "} \\end{overpic}"
		else:
			if rotation==0:
				cco = "22,70"
				aco = "-8,40"
				hco = "54,46"
			elif rotation==270:
				cco = "71,72"
				aco = "40,85"
				hco = "45,39"
			elif rotation==180:
				cco = "72,22"
				aco = "83,50"
				hco = "26,44"
			else:
				cco = "21,21" 
				aco = "50,9"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "} \\end{overpic}"
		c = rounddp(degrees(acos(a/h)),2)
		question = explanation + image
		answer = c
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tanangle(n,explanationn):
	import random
	from math import radians,degrees,asin,acos,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		o = random.randrange(3,44)
		a = random.randrange(3,44)
		angle = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				tco = "62,5"
				oco = "-8,40"
				aco = "28,3"
			elif rotation==270:
				tco = "7,30"
				oco = "40,85"
				aco = "-23,50"
			elif rotation==180:
				tco = "31,86"
				oco = "83,50"
				aco = "48,89"
			else:
				tco = "87,63" 
				oco = "50,9"
				aco = "100,44"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "cm} \\put(" + aco + "){" + str(a) + "cm} \\put(" + tco + "){" + str(angle) + "} \\end{overpic}"
		else:
			if rotation==0:
				tco = "22,70"
				oco = "44,3"
				aco = "-8,46"
			elif rotation==270:
				tco = "71,72"
				oco = "-23,50"
				aco = "40,85"
			elif rotation==180:
				tco = "72,22"
				oco = "42,90"
				aco = "83,50"
			else:
				tco = "21,21" 
				oco = "100,45"
				aco = "45,8"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "cm} \\put(" + aco + "){" + str(a) + "cm} \\put(" + tco + "){" + str(angle) + "} \\end{overpic}"
		t = rounddp(degrees(atan(o/a)),2)
		question = explanation + image
		answer = t
		if answer%1==0:
			answer = int(answer)
		answer = str(answer) + "\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def exactvaluessin(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the exact value of "
		else:
			explanation = ""
		angles = [0,30,45,60,90]
		sins = {0:"0",30:"\\dfrac{1}{2}",45:"\\dfrac{1}{\\sqrt{2}}",60:"\\dfrac{\\sqrt{3}}{2}",90:"1"}
		x = random.choice(angles)
		question = explanation + "Sin\," + str(x) + "\\mydeg"
		answer = "$" + sins[x] + "$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def exactvaluescos(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the exact value of "
		else:
			explanation = ""
		angles = [0,30,45,60,90]
		coss = {90:"0",60:"\\dfrac{1}{2}",45:"\\dfrac{1}{\\sqrt{2}}",30:"\\dfrac{\\sqrt{3}}{2}",0:"1"}
		x = random.choice(angles)
		question = explanation + "Cos\," + str(x) + "\\mydeg"
		answer = "$" + coss[x] + "$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def exactvaluestan(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the exact value of "
		else:
			explanation = ""
		angles = [0,30,45,60]
		tans = {0:"0",30:"\\dfrac{1}{\\sqrt{3}}",45:"1",60:"\\sqrt{3}"}
		x = random.choice(angles)
		question = explanation + "Tan\," + str(x) + "\\mydeg"
		answer = "$" + tans[x] + "$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sinside1nc(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		h = random.randrange(7,51)
		angles = [30,45,60]
		angle = random.choice(angles)
		o = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				sco = "60,5"
				oco = "10,40"
				hco = "54,46"
			elif rotation==270:
				sco = "4,29"
				oco = "40,85"
				hco = "45,39"
			elif rotation==180:
				sco = "29,87"
				oco = "83,50"
				hco = "26,44"
			else:
				sco = "82,62" 
				oco = "50,9"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				sco = "19,68"
				oco = "44,3"
				hco = "54,46"
			elif rotation==270:
				sco = "69,72"
				oco = "-6,50"
				hco = "45,39"
			elif rotation==180:
				sco = "67,24"
				oco = "50,90"
				hco = "26,44"
			else:
				sco = "18,20" 
				oco = "100,45"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		if angle==30:
			if h%2==0:
				o = int(h/2)
			else:
				o = rounddp(h/2,1)
		elif angle==45:
			o = "$\\dfrac{" + str(h) + "}{\\sqrt{2}}$"
		else:
			if h%2==0:
				o = str(int(h/2)) + "$\\sqrt{3}$"
			else:
				o = "$\\dfrac{" + str(h) + "\\sqrt{3}}{2}$"
		question = explanation + image
		answer = o
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sinside2nc(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		o = random.randrange(7,51)
		angles = [30,45,60]
		angle = random.choice(angles)
		h = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				sco = "60,5"
				oco = "-9,40"
				hco = "54,46"
			elif rotation==270:
				sco = "4,29"
				oco = "40,85"
				hco = "45,39"
			elif rotation==180:
				sco = "29,87"
				oco = "83,50"
				hco = "40,44"
			else:
				sco = "82,62" 
				oco = "50,9"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				sco = "19,68"
				oco = "40,3"
				hco = "54,46"
			elif rotation==270:
				sco = "69,72"
				oco = "-25,50"
				hco = "45,39"
			elif rotation==180:
				sco = "67,24"
				oco = "40,90"
				hco = "40,44"
			else:
				sco = "18,20" 
				oco = "100,45"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + sco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		h = rounddp(o/sin(radians(angle)),2)
		if angle==30:
			h = o * 2
		elif angle==45:
			h = str(o) + "$\\sqrt{2}$"
		else:
			h = "$\\dfrac{" + str(o*2) + "}{\\sqrt{3}}$"
		question = explanation + image
		answer = h
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cosside1nc(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		h = random.randrange(7,51)
		angles = [30,45,60]
		angle = random.choice(angles)
		a = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				cco = "60,5"
				aco = "43,3"
				hco = "54,46"
			elif rotation==270:
				cco = "4,29"
				aco = "-6,50"
				hco = "45,39"
			elif rotation==180:
				cco = "29,87"
				aco = "54,90"
				hco = "26,44"
			else:
				cco = "82,62" 
				aco = "100,45"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				cco = "19,68"
				aco = "10,45"
				hco = "54,46"
			elif rotation==270:
				cco = "69,72"
				aco = "40,85"
				hco = "45,39"
			elif rotation==180:
				cco = "67,24"
				aco = "83,50"
				hco = "26,44"
			else:
				cco = "18,20" 
				aco = "50,9"
				hco = "32,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		if angle==60:
			if h%2==0:
				a = int(h/2)
			else:
				a = rounddp(h/2,1)
		elif angle==45:
			a = "$\\dfrac{" + str(h) + "}{\\sqrt{2}}$"
		else:
			if h%2==0:
				a = str(int(h/2)) + "$\\sqrt{3}$"
			else:
				a = "$\\dfrac{" + str(h) + "\\sqrt{3}}{2}$"
		question = explanation + image
		answer = a
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cosside2nc(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		a = random.randrange(7,51)
		angles = [30,45,60]
		angle = random.choice(angles)
		h = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				cco = "60,5"
				aco = "28,3"
				hco = "54,46"
			elif rotation==270:
				cco = "4,29"
				aco = "-25,50"
				hco = "45,39"
			elif rotation==180:
				cco = "29,87"
				aco = "48,90"
				hco = "40,44"
			else:
				cco = "82,62" 
				aco = "100,45"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				cco = "19,68"
				aco = "-9,40"
				hco = "54,46"
			elif rotation==270:
				cco = "69,72"
				aco = "40,85"
				hco = "45,39"
			elif rotation==180:
				cco = "67,24"
				aco = "83,50"
				hco = "40,44"
			else:
				cco = "18,20" 
				aco = "50,9"
				hco = "45,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "} \\put(" + cco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		if angle==60:
			h = a * 2
		elif angle==45:
			h = str(a) + "$\\sqrt{2}$"
		else:
			h = "$\\dfrac{" + str(a*2) + "}{\\sqrt{3}}$"
		question = explanation + image
		answer = h
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def tanside2nc(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		o = random.randrange(7,51)
		angles = [30,45,60]
		angle = random.choice(angles)
		a = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				tco = "60,5"
				aco = "43,3"
				oco = "-10,45"
			elif rotation==270:
				tco = "4,29"
				aco = "-6,50"
				oco = "40,85"
			elif rotation==180:
				tco = "29,87"
				aco = "54,90"
				oco = "83,50"
			else:
				tco = "82,62" 
				aco = "100,45"
				oco = "50,9"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "} \\put(" + oco + "){" + str(o) + "cm} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				tco = "19,68"
				aco = "10,45"
				oco = "43,3"
			elif rotation==270:
				tco = "69,72"
				aco = "40,85"
				oco = "-24,50"
			elif rotation==180:
				tco = "67,24"
				aco = "83,50"
				oco = "48,90"
			else:
				tco = "18,20" 
				aco = "50,9"
				oco = "100,45"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "} \\put(" + oco + "){" + str(o) + "cm} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		a = rounddp(o/tan(radians(angle)),2)
		if angle==30:
			a = str(o) + "$\\sqrt{3}$"
		elif angle==45:
			a = o
		else:
			a = "$\\dfrac{" + str(o) + "}{\\sqrt{3}}$"
		question = explanation + image
		answer = a
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tanside1nc(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		a = random.randrange(7,51)
		angles = [30,45,60]
		angle = random.choice(angles)
		o = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				tco = "60,5"
				aco = "28,3"
				oco = "-10,45"
			elif rotation==270:
				tco = "4,29"
				aco = "-24,50"
				oco = "40,85"
			elif rotation==180:
				tco = "29,87"
				aco = "49,90"
				oco = "83,50"
			else:
				tco = "82,62" 
				aco = "100,45"
				oco = "50,9"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "cm} \\put(" + oco + "){" + str(o) + "} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		else:
			if rotation==0:
				tco = "19,68"
				aco = "-7,45"
				oco = "43,3"
			elif rotation==270:
				tco = "69,72"
				aco = "40,85"
				oco = "-6,50"
			elif rotation==180:
				tco = "67,24"
				aco = "83,50"
				oco = "48,90"
			else:
				tco = "18,20" 
				aco = "50,9"
				oco = "100,45"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "cm} \\put(" + oco + "){" + str(o) + "} \\put(" + tco + "){" + str(angle) + "\\mydeg} \\end{overpic}"
		o = rounddp(tan(radians(angle))*a,2)
		if angle==60:
			o = str(a) + "$\\sqrt{3}$"
		elif angle==45:
			o = a
		else:
			o = "$\\dfrac{" + str(a) + "}{\\sqrt{3}}$"
		question = explanation + image
		answer = o
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def sinanglenc(n,explanationn):
	import random
	from math import radians,degrees,asin,acos,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		angles = [30,45,60]
		angle = random.choice(angles)
		if random.randrange(0,2)==0:
			h = random.randrange(7,51)
			if angle==30:
				if h%2==0:
					o = int(h/2)
				else:
					o = rounddp(h/2,1)
			elif angle==45:
				o = "$\\dfrac{" + str(h) + "}{\\sqrt{2}}$"
			else:
				if h%2==0:
					o = str(int(h/2)) + "$\\sqrt{3}$"
				else:
					o = "$\\dfrac{" + str(h) + "\\sqrt{3}}{2}$"
		else:
			o = random.randrange(7,51)
			if angle==30:
				h = o * 2
			elif angle==45:
				h = str(o) + "$\\sqrt{2}$"
			else:
				h = "$\\dfrac{" + str(o*2) + "}{\\sqrt{3}}$"
		answer = str(angle) + "\\mydeg"
		angle = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				sco = "62,5"
				oco = "-8,40"
				hco = "54,46"
			elif rotation==270:
				sco = "7,30"
				oco = "40,85"
				hco = "45,39"
			elif rotation==180:
				sco = "31,86"
				oco = "83,50"
				hco = "26,44"
			else:
				sco = "87,63" 
				oco = "50,9"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "} \\end{overpic}"
		else:
			if rotation==0:
				sco = "22,70"
				oco = "44,3"
				hco = "54,46"
			elif rotation==270:
				sco = "71,72"
				oco = "-23,50"
				hco = "45,39"
			elif rotation==180:
				sco = "72,22"
				oco = "42,90"
				hco = "26,44"
			else:
				sco = "21,21" 
				oco = "100,45"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + sco + "){" + str(angle) + "} \\end{overpic}"
		question = explanation + image
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def cosanglenc(n,explanationn):
	import random
	from math import radians,degrees,asin,acos,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		a = random.randrange(3,35)
		h = a + random.randrange(3,35)
		angles = [30,45,60]
		angle = random.choice(angles)
		if random.randrange(0,2)==0:
			h = random.randrange(7,51)
			if angle==60:
				if h%2==0:
					a = int(h/2)
				else:
					a = rounddp(h/2,1)
			elif angle==45:
				o = "$\\dfrac{" + str(h) + "}{\\sqrt{2}}$"
			else:
				if h%2==0:
					a = str(int(h/2)) + "$\\sqrt{3}$"
				else:
					a = "$\\dfrac{" + str(h) + "\\sqrt{3}}{2}$"
		else:
			a = random.randrange(7,51)
			if angle==60:
				h = a * 2
			elif angle==45:
				h = str(a) + "$\\sqrt{2}$"
			else:
				h = "$\\dfrac{" + str(a*2) + "}{\\sqrt{3}}$"
		answer = str(angle) + "\\mydeg"
		angle = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				cco = "62,5"
				aco = "28,3"
				hco = "54,46"
			elif rotation==270:
				cco = "7,30"
				aco = "-23,50"
				hco = "45,39"
			elif rotation==180:
				cco = "31,86"
				aco = "48,90"
				hco = "26,44"
			else:
				cco = "87,63" 
				aco = "100,45"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "} \\end{overpic}"
		else:
			if rotation==0:
				cco = "22,70"
				aco = "-8,40"
				hco = "54,46"
			elif rotation==270:
				cco = "71,72"
				aco = "40,85"
				hco = "45,39"
			elif rotation==180:
				cco = "72,22"
				aco = "83,50"
				hco = "26,44"
			else:
				cco = "21,21" 
				aco = "50,9"
				hco = "31,53"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + aco + "){" + str(a) + "cm} \\put(" + hco + "){" + str(h) + "cm} \\put(" + cco + "){" + str(angle) + "} \\end{overpic}"
		question = explanation + image
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def tananglenc(n,explanationn):
	import random
	from math import radians,degrees,asin,acos,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		angles = [30,45,60]
		angle = random.choice(angles)
		if random.randrange(0,2)==0:
			o = random.randrange(7,51)
			if angle==30:
				a = str(o) + "$\\sqrt{3}$"
			elif angle==45:
				a = o
			else:
				a = "$\\dfrac{" + str(o) + "}{\\sqrt{3}}$"
		else:
			a = random.randrange(7,51)
			if angle==60:
				o = str(a) + "$\\sqrt{3}$"
			elif angle==45:
				o = a
			else:
				o = "$\\dfrac{" + str(a) + "}{\\sqrt{3}}$"
		answer = str(angle) + "\\mydeg"
		angle = "?"
		rotation = random.randrange(0,4)*90
		if random.randrange(0,2)==1:
			if rotation==0:
				tco = "62,5"
				oco = "-8,40"
				aco = "28,3"
			elif rotation==270:
				tco = "7,30"
				oco = "40,85"
				aco = "-23,50"
			elif rotation==180:
				tco = "31,86"
				oco = "83,50"
				aco = "48,89"
			else:
				tco = "87,63" 
				oco = "50,9"
				aco = "100,44"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig1} \\put(" + oco + "){" + str(o) + "cm} \\put(" + aco + "){" + str(a) + "cm} \\put(" + tco + "){" + str(angle) + "} \\end{overpic}"
		else:
			if rotation==0:
				tco = "22,70"
				oco = "44,3"
				aco = "-8,46"
			elif rotation==270:
				tco = "71,72"
				oco = "-23,50"
				aco = "40,85"
			elif rotation==180:
				tco = "72,22"
				oco = "42,90"
				aco = "83,50"
			else:
				tco = "21,21" 
				oco = "100,45"
				aco = "45,8"
			image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trig2} \\put(" + oco + "){" + str(o) + "cm} \\put(" + aco + "){" + str(a) + "cm} \\put(" + tco + "){" + str(angle) + "} \\end{overpic}"
		question = explanation + image
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def trigareatriangle(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sin,radians
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l1 = random.randrange(4,102)/2
		l2 = random.randrange(4,102)/2
		if l1%1==0:
			l1 = int(l1)
		else:
			l1 = rounddp(l1,1)
		if l2%1==0:
			l2 = int(l2)
		else:
			l2 = rounddp(l2,1)
		area = rounddp(0.5 * l1 * l2 * sin(radians(a)),2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "48,50"
			l1co = "0,40"
			l2co = "78,40"
		elif rotation==270:
			aco = "55,38"
			l1co = "34,75"
			l2co = "35,13"
		elif rotation==180:
			aco = "34,40"
			l1co = "-9,50"
			l2co = "70,50"
		else:
			aco = "32,54" 
			l1co = "37,20"
			l2co = "40,83"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trigareatriangle} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\end{overpic}"
		question = explanation + image
		answer = str(area) + "cm$^{2}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def cosineruleside(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,cos,radians,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l1 = random.randrange(4,102)/2
		l2 = random.randrange(4,102)/2
		l3 = "?"
		answer = rounddp(sqrt(l1**2 + l2**2 - 2 * l1 * l2 * cos(radians(a))),2)
		if l1%1==0:
			l1 = int(l1)
		else:
			l1 = rounddp(l1,1)
		if l2%1==0:
			l2 = int(l2)
		else:
			l2 = rounddp(l2,1)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "48,50"
			l1co = "0,40"
			l2co = "78,40"
			l3co = "50,8"
		elif rotation==270:
			aco = "55,38"
			l1co = "34,75"
			l2co = "35,13"
			l3co = "-1,47"
		elif rotation==180:
			aco = "34,40"
			l1co = "-9,50"
			l2co = "70,50"
			l3co = "47,85"
		else:
			aco = "32,54" 
			l1co = "37,20"
			l2co = "40,83"
			l3co = "95,50"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trigareatriangle} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\put(" + l3co + "){" + str(l3) + "} \\end{overpic}"
		question = explanation + image
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cosineruleangle(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,cos,radians,sqrt,floor,acos,degrees,ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = "?"
		l1 = random.randrange(4,102)/2
		l2 = random.randrange(4,102)/2
		top = floor(l1+l2) - 1
		bottom = ceil(abs(l1-l2)) + 1
		l3 = random.randrange(bottom,top)
		mixer = [l1,l2,l3]
		random.shuffle(mixer)
		l1 = mixer[0]
		l2 = mixer[1]
		l3 = mixer[2]
		answer = rounddp(degrees(acos((l1**2 + l2**2 - l3**2)/(2*l1*l2))),2)
		if l1%1==0:
			l1 = int(l1)
		else:
			l1 = rounddp(l1,1)
		if l2%1==0:
			l2 = int(l2)
		else:
			l2 = rounddp(l2,1)
		if l3%1==0:
			l3 = int(l3)
		else:
			l3 = rounddp(l3,1)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "52,50"
			l1co = "0,40"
			l2co = "78,40"
			l3co = "45,8"
		elif rotation==270:
			aco = "55,38"
			l1co = "34,75"
			l2co = "35,13"
			l3co = "-20,47"
		elif rotation==180:
			aco = "38,40"
			l1co = "-9,50"
			l2co = "70,50"
			l3co = "42,85"
		else:
			aco = "32,54" 
			l1co = "37,20"
			l2co = "40,83"
			l3co = "95,50"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trigareatriangle} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\put(" + l3co + "){" + str(l3) + "cm} \\end{overpic}"
		question = explanation + image
		answer = str(answer) + "\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sineruleside(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sin,radians,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		angles = [10,30,50]
		for i in range(0,90):
			dec = random.randrange(0,3)
			angles[dec] = angles[dec] + 1
		a = angles[0]
		a2 = angles[1]
		l1 = random.randrange(4,102)/2
		l2 = "?"
		answer = rounddp(l1/sin(radians(a)) * sin(radians(a2)),2)
		if random.randrange(0,2)==0:
			temp = a
			a = a2
			a2 = temp
			temp = l1
			l1 = l2
			l2 = temp
			if l2%1==0:
				l2 = int(l2)
			else:
				l2 = rounddp(l2,1)
		else:
			if l1%1==0:
				l1 = int(l1)
			else:
				l1 = rounddp(l1,1)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "67,10"
			a2co = "14,10"
			l1co = "0,40"
			l2co = "78,40"
		elif rotation==270:
			aco = "8,18"
			a2co = "8,72"
			l1co = "34,75"
			l2co = "35,13"
		elif rotation==180:
			aco = "68,80"
			a2co = "14,80"
			l1co = "-9,50"
			l2co = "70,50"
		else:
			aco = "73,73" 
			a2co = "75,23"
			l1co = "37,20"
			l2co = "40,83"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/sinerule} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\put(" + a2co + "){" + str(a2) + "\\mydeg} \\end{overpic}"
		question = explanation + image
		answer = str(answer) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sineruleangle(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sin,radians,sqrt,degrees,asin
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(20,70)
		a2 = "?"
		l1 = random.randrange(4,102)/2
		l2 = random.randrange(4,102)/2
		if l1<l2:
			temp = l1
			l1 = l2
			l2 = temp
		answer = rounddp(degrees(asin(sin(radians(a))/l1 * l2)),2)
		if random.randrange(0,2)==0:
			temp = a
			a = a2
			a2 = temp
			temp = l1
			l1 = l2
			l2 = temp
		if l2%1==0:
			l2 = int(l2)
		else:
			l2 = rounddp(l2,1)
		if l1%1==0:
			l1 = int(l1)
		else:
			l1 = rounddp(l1,1)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "67,10"
			a2co = "14,10"
			l1co = "0,40"
			l2co = "78,40"
		elif rotation==270:
			aco = "8,18"
			a2co = "8,72"
			l1co = "34,75"
			l2co = "35,13"
		elif rotation==180:
			aco = "68,80"
			a2co = "14,80"
			l1co = "-9,50"
			l2co = "70,50"
		else:
			aco = "73,73" 
			a2co = "75,23"
			l1co = "37,20"
			l2co = "40,83"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/sinerule} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\put(" + a2co + "){" + str(a2) + "\\mydeg} \\end{overpic}"
		question = explanation + image
		answer = str(answer) + "\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sineruleambiguous(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sin,radians,sqrt,degrees,asin,floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(15,40)
		a2 = "?"
		l1 = random.randrange(20,102)/2
		maxl2 = int(floor(l1/sin(radians(a)))-1)
		l2 = random.randrange(int(l1)+2,maxl2)
		answer = rounddp(180 - degrees(asin(sin(radians(a))/l1 * l2)),2)
		if l2%1==0:
			l2 = int(l2)
		else:
			l2 = rounddp(l2,1)
		if l1%1==0:
			l1 = int(l1)
		else:
			l1 = rounddp(l1,1)
		rotation = random.randrange(0,4)*90
		rotation = 0
		if rotation==0:
			aco = "17,4"
			a2co = "58,23"
			l1co = "76,20"
			l2co = "45,4"
		elif rotation==270:
			aco = "8,18"
			a2co = "8,72"
			l1co = "34,75"
			l2co = "35,13"
		elif rotation==180:
			aco = "68,80"
			a2co = "14,80"
			l1co = "-9,50"
			l2co = "70,50"
		else:
			aco = "73,73" 
			a2co = "75,23"
			l1co = "37,20"
			l2co = "40,83"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.6]{shape/images/sineruleambiguous} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\put(" + a2co + "){" + str(a2) + "\\mydeg} \\end{overpic}"
		question = explanation + image
		answer = str(answer) + "\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def trigareatriangle2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,cos,radians,sqrt,floor,acos,degrees,ceil,sin
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = "?"
		l1 = random.randrange(4,102)/2
		l2 = random.randrange(4,102)/2
		top = floor(l1+l2) - 1
		bottom = ceil(abs(l1-l2)) + 1
		l3 = random.randrange(bottom,top)
		mixer = [l1,l2,l3]
		random.shuffle(mixer)
		l1 = mixer[0]
		l2 = mixer[1]
		l3 = mixer[2]
		answer = degrees(acos((l1**2 + l2**2 - l3**2)/(2*l1*l2)))
		if l1%1==0:
			l1 = int(l1)
		else:
			l1 = rounddp(l1,1)
		if l2%1==0:
			l2 = int(l2)
		else:
			l2 = rounddp(l2,1)
		if l3%1==0:
			l3 = int(l3)
		else:
			l3 = rounddp(l3,1)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "52,50"
			l1co = "0,40"
			l2co = "78,40"
			l3co = "45,8"
		elif rotation==270:
			aco = "55,38"
			l1co = "34,75"
			l2co = "35,13"
			l3co = "-20,47"
		elif rotation==180:
			aco = "38,40"
			l1co = "-9,50"
			l2co = "70,50"
			l3co = "42,85"
		else:
			aco = "32,54" 
			l1co = "37,20"
			l2co = "40,83"
			l3co = "95,50"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/trigareatriangle2} \\put(" + l1co + "){" + str(l1) + "cm} \\put(" + l2co + "){" + str(l2) + "cm} \\put(" + l3co + "){" + str(l3) + "cm} \\end{overpic}"
		question = explanation + image
		answer = rounddp(0.5 * l1 * l2 * sin(radians(answer)),2)
		answer = str(answer) + "cm$^{2}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
