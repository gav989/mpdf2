#pythagoras.py

def pythagoras1(n,explanationn):
	import random
	from math import sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,85"
			bco = "3,50"
			cco = "54,44"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,10" 
			bco = "100,45"
			cco = "38,53"
		a = random.randrange(3,13)
		b = random.randrange(3,13)
		c = "?"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.5]{shape/images/pythag} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}"
		answer = rounddp(sqrt(a**2 + b**2),2)
		question = explanation + image
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagoras2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,85"
			bco = "3,50"
			cco = "54,44"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,10" 
			bco = "100,45"
			cco = "35,53"
		if random.randrange(0,2)==1:
			a = random.randrange(3,13)
			c = a + random.randrange(3,10)
			b = "?"
			answer = sqrt(c**2 - a**2)
		else:
			b = random.randrange(3,13)
			c = b + random.randrange(3,10)
			a = "?"
			answer = sqrt(c**2 - b**2)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.5]{shape/images/pythag} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}"
		question = explanation + image
		answer = rounddp(answer,2)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagoras1bf(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,85"
			bco = "3,50"
			cco = "54,44"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,10" 
			bco = "100,45"
			cco = "38,53"
		a = random.randrange(3,13)
		b = random.randrange(3,13)
		c = "?"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/pythag} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}"
		answer = rounddp(sqrt(a**2 + b**2),2)
		question = explanation + image
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagoras2bf(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,85"
			bco = "3,50"
			cco = "54,44"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,10" 
			bco = "100,45"
			cco = "35,53"
		if random.randrange(0,2)==1:
			a = random.randrange(3,13)
			c = a + random.randrange(3,10)
			b = "?"
			answer = sqrt(c**2 - a**2)
		else:
			b = random.randrange(3,13)
			c = b + random.randrange(3,10)
			a = "?"
			answer = sqrt(c**2 - b**2)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/pythag} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}"
		question = explanation + image
		answer = rounddp(answer,2)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagstarter(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side lengths:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a1 = random.randrange(3,13)
		b1 = random.randrange(3,13)
		answer1 = rounddp(sqrt(a1**2 + b1**2),2)
		a1 = str(a1) + "cm"
		b1 = str(b1) + "cm"
		c1 = "?" 
		if random.randrange(0,2)==1:
			a2 = random.randrange(3,13)
			c2 = a2 + random.randrange(3,10)
			answer2 = rounddp(sqrt(c2**2 - a2**2),2)
			b2 = "?"
			a2 = str(a2) + "cm"
			c2 = str(c2) + "cm"
		else:
			b2 = random.randrange(3,13)
			c2 = b2 + random.randrange(3,10)
			answer2 = rounddp(sqrt(c2**2 - b2**2),2)
			c2 = str(c2) + "cm"
			b2 = str(b2) + "cm"
			a2 = "?"
		if random.randrange(0,2)==0:
			a1,b1,c1,a2,b2,c2 = a2,b2,c2,a1,b1,c1
		image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/pythagstarter2} \\put(-10,50){" + a1 + "} \\put(30,70){" + b1 + "}  \\put(36,50){" + c1 + "}  \\put(90,25){" + a2 + "}  \\put(50,2){" + b2 + "}  \\put(40,27){" + c2 + "}   \\end{overpic}"
		question = explanation + image
		if answer1%1==0:
			answer1 = int(answer1)
		if answer2%1==0:
			answer1 = int(answer2)
		answer = str(answer1) + "cm \\hspace{2cm}" + str(answer2) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def pythagcheck(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "A triangle has sides of length "
			explanation2 = ", is it right-angled?"
		else:
			explanation1 = ""
			explanation2 = ""
		aas = [15,44,88,17,24,51,85,119,52,19,57,104,95,28,84,133,21,140,60,105,120,32,23,96,69,115,160,161,68,136,207,25,75,36,204,175,180,225,27,76,252,135,152,189,228,40,120,29,87,297,145,84,203,280,168,261,31,319,44,93,132,155,217,336,220,279,92,308,341,33,184,165,276,396,231,48,368,240,35,105,336,100,429,200,315,300,385,52,37,156,111,400,185,455,260,259,333,364,108,216,407,468,39,481,195,56,273,168,432,555,280,429,540,41,116,123,205,232,287,504,348,369,60,451,464,616,43,533,129,215,580,301,420,615,124,387,248,473,696,372]
		bs = [112,117,105,144,143,140,132,120,165,180,176,153,168,195,187,156,220,171,221,208,209,255,264,247,260,252,231,240,285,273,224,312,308,323,253,288,299,272,364,357,275,352,345,340,325,399,391,420,416,304,408,437,396,351,425,380,480,360,483,476,475,468,456,377,459,440,525,435,420,544,513,532,493,403,520,575,465,551,612,608,527,621,460,609,572,589,552,675,684,667,680,561,672,528,651,660,644,627,725,713,624,595,760,600,748,783,736,775,665,572,759,700,629,840,837,836,828,825,816,703,805,800,899,780,777,663,924,756,920,912,741,900,851,728,957,884,945,864,697,925]
		cs = [113,125,137,145,145,149,157,169,173,181,185,185,193,197,205,205,221,221,229,233,241,257,265,265,269,277,281,289,293,305,305,313,317,325,325,337,349,353,365,365,373,377,377,389,397,401,409,421,425,425,433,445,445,449,457,461,481,481,485,485,493,493,505,505,509,521,533,533,541,545,545,557,565,565,569,577,593,601,613,617,625,629,629,641,653,661,673,677,685,685,689,689,697,697,701,709,725,725,733,745,745,757,761,769,773,785,785,793,793,797,809,821,829,841,845,845,853,857,865,865,877,881,901,901,905,905,925,925,929,937,941,949,949,953,965,965,977,985,985,997]
		if random.randrange(0,2)==1:
			dec = random.randrange(0,len(aas))
			a = aas[dec]
			b = bs[dec]
			c = cs[dec]
		else:
			a = random.randrange(1,100)*10 + random.randrange(0,10)
			b = random.randrange(1,100)*10 + random.randrange(0,10)
			c = int(sqrt(a**2 + b**2) + random.randrange(19,40)*(-1)**random.randrange(1,3))
		if a**2 + b**2==c**2:
			answer = "yes"
		else:
			answer = "no"
		a = rounddp(a/10,1)
		b = rounddp(b/10,1)
		c = rounddp(c/10,1)
		if a%1==0:
			a = int(a)
		if b%1==0:
			b = int(b)
		if c%1==0:
			c = int(c)
		sides = [str(a),str(b),str(c)]
		random.shuffle(sides)
		question = sides[0] + "cm, " + sides[1] + "cm and " + sides[2] + "cm"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def pythagoras1starter(n,explanationn):
	import random
	from math import sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		rotation = random.randrange(0,2)*180+90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,52"
			bco = "2,30"
			cco = "52,20"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,2" 
			bco = "100,25"
			cco = "38,32"
		a = random.randrange(3,13)
		b = random.randrange(3,13)
		c = "?"
		image = "\\begin{overpic}[angle=" + str(rotation) + ",scale=0.2]{shape/images/pythagstarter} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\end{overpic}"
		answer = rounddp(sqrt(a**2 + b**2),2)
		question = "Find the missing side: " + image
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagoras2starter(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		rotation = random.randrange(0,2)*180 + 90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,52"
			bco = "2,30"
			cco = "52,20"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,2" 
			bco = "100,25"
			cco = "38,32"
		if random.randrange(0,2)==1:
			a = random.randrange(3,13)
			c = a + random.randrange(3,10)
			b = "?"
			answer = sqrt(c**2 - a**2)
		else:
			b = random.randrange(3,13)
			c = b + random.randrange(3,10)
			a = "?"
			answer = sqrt(c**2 - b**2)
		image = "\\begin{overpic}[angle=" + str(rotation) + ",scale=0.2]{shape/images/pythagstarter} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\end{overpic}"
		question = "Find the missing side: " + image
		answer = rounddp(answer,2)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def pythagoras3d(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,10)
		b = random.randrange(2,10)
		c = random.randrange(2,10)
		if random.randrange(0,3)==1:
			length1s = ("AF","EB","DG","HC")
			answera = rounddp(sqrt(a**2 + b**2),2)
		elif random.randrange(0,2)==1:
			length1s = ("BG","FC","AH","ED")
			answera = rounddp(sqrt(a**2 + c**2),2)
		else:
			length1s = ("AC","BD","EG","FH")
			answera = rounddp(sqrt(b**2 + c**2),2)
		length1 = random.choice(length1s)
		length2s = ("BH","FD","AG","EC")
		length2 = random.choice(length2s)
		answerb = rounddp(sqrt(a**2 + b**2 + c**2),2)
		aco = "-10,25"
		bco = "11,3"
		cco = "60,5"
		image = "\\centering\\begin{overpic}[scale=0.5]{shape/images/pythag3d} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}"
		question = image + "\\\\ \\raggedright a) Find length " + length1 + " \\\\ b) Find length " + length2
		answer = "a) " + str(answera) + "cm \\\\ b) " + str(answerb) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
