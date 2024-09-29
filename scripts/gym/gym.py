#typing.py


def fexamquestions(n,placeholder=0):
	import random
	for x in range(0, 1):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		question = "\\includegraphics[width=\\linewidth]{gym/images/feq" + str(n) + "}"
		answer = "\\includegraphics[width=\\linewidth]{gym/images/feqa" + str(n) + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def hexamquestions(n,placeholder=0):
	import random
	for x in range(0, 1):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		question = "\\includegraphics[width=\\linewidth]{gym/images/heq" + str(n) + "}"
		answer = "\\includegraphics[width=\\linewidth]{gym/images/heqa" + str(n) + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fexamquestionsbeamer(n,placeholder=0):
	import random
	for x in range(0, 1):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		question = "\\includegraphics[width=\\linewidth,height=0.9\\textheight,keepaspectratio]{gym/images/feq" + str(n) + "}"
		answer = "\\includegraphics[width=\\linewidth]{gym/images/feqa" + str(n) + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def hexamquestionsbeamer(n,placeholder=0):
	import random
	for x in range(0, 1):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		question = "\\includegraphics[width=\\linewidth,height=0.9\\textheight,keepaspectratio]{gym/images/heq" + str(n) + "}"
		answer = "\\includegraphics[width=\\linewidth]{gym/images/heqa" + str(n) + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def foundationformulae(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		questions = [
			"Write down the formula for the area of a circle",
			"Write down the formula for the circumference of a circle",
			"Write down the formula for the area of a triangle",
			"Write down Pythagoras' theorem",
			"Write down the formula for the area of a trapezium"]
		answers = [
			"$A = \\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}\\text{r}^{2}$ ",
			"$C = \\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}\\text{D}$",
			"$\\dfrac{\\text{base} \\times \\text{height}}{2}$",
			"$\\text{a}^{2} + \\text{b}^{2} = \\text{c}^{2}$",
			"$\\dfrac{\\text{a} + \\text{b}}{2} \\times \\text{h}$"]
		cycler = session%len(questions)
		question = questions[cycler]
		answer = answers[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def higherformulae(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		questions = [
			"Write down the quadratic formula",
			"Write down the sine rule",
			"Write down the cosine rule",
			"Write down the trig formula for the area of a triangle",
			"Write down the rearranged cosine rule",
			"Write down the formula triangle for speed",
			"Write down the formula triangle for density",
			"Write down the formula for the area of a circle",
			"Write down the formula for the circumference of a circle",
			"Write down the formula for the area of a triangle",
			"Write down Pythagoras' theorem",
			"Write down the formula for the area of a trapezium"]
		answers = [
			"$x = \\dfrac{-\\text{b} \\pm \\sqrt{\\text{b}^2 - 4\\text{ac}}}{2\\text{a}}$",
			"$\\dfrac{\\text{a}}{\\text{Sin\,A}} = \\dfrac{\\text{b}}{\\text{Sin\,B}} \\left(= \\dfrac{\\text{c}}{\\text{Sin\,C}}\\right)$",
			"$\\text{a}^{2} = \\text{b}^{2} + \\text{c}^{2} - 2\\text{bcCos\,A}$",
			"$\\text{Area} = \\dfrac{1}{2}\\text{abSin\,C}$",
			"$\\text{Cos\,A} = \\dfrac{\\text{b}^{2} + \\text{c}^{2} - \\text{a}^{2}}{2\\text{bc}}$",
			"\\includegraphics[scale=0.4]{gym/images/sdt}",
			"\\includegraphics[scale=0.4]{gym/images/dmv}",
			"$A = \\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}\\text{r}^{2}$",
			"$C = \\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}\\text{D}$",
			"$\\dfrac{\\text{base} \\times \\text{height}}{2}$",
			"$\\text{a}^{2} + \\text{b}^{2} = \\text{c}^{2}$",
			"$\\dfrac{\\text{a} + \\text{b}}{2} \\times \\text{height}$"]
		cycler = session%len(questions)
		question = questions[cycler]
		answer = answers[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def suvat(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		questions = [
			"What does the \"U\" in SUVAT stand for?",
			"What does the \"V\" in SUVAT stand for?",
			"What does the \"A\" in SUVAT stand for?",
			"What does the \"T\" in SUVAT stand for?",
			"What does the \"S\" in SUVAT stand for?"]
		answers = [
			"Initial velocity",
			"Final velocity",
			"Acceleration",
			"Time",
			"Displacement (or distance)"]
		cycler = session%len(questions)
		question = questions[cycler]
		answer = answers[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymmetric(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		questions = [
			"What is the conversion between millimetres and centimetres?",
			"What is the conversion between centimetres and millimetres?",
			"What is the conversion between centimetres and metres?",
			"What is the conversion between metres and centimetres?",
			"What is the conversion between metres and kilometres?",
			"What is the conversion between kilometres and metres?",
#			"What is the conversion between milligrams and grams?",
#			"What is the conversion between grams and milligrams?",
			"What is the conversion between grams and kilograms?",
			"What is the conversion between kilograms and grams?",
#			"What is the conversion between kilograms and tonnes?",
#			"What is the conversion between tonnes and kilograms?",
			"What is the conversion between litres and millilitres?",
			"What is the conversion between millilitres and litres?"]
		answers = [
			"1 cm = 10 mm",
			"1 cm = 10 mm",
			"1 m = 100 cm",
			"1 m = 100 cm",
			"1 km = 1000 m",
			"1 km = 1000 m",
#			"1 g = 1000 mg",
#			"1 g = 1000 mg",
			"1 kg = 1000 g",
			"1 kg = 1000 g",
#			"1 t = 1000 kg",
#			"1 t = 1000 kg",
			"1 l = 1000 ml",
			"1 l = 1000 ml"]
		cycler = session%len(questions)
		question = questions[cycler]
		answer = answers[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def hanglefacts(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 2
		diags = [
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/opposite}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/triangle}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/corresponding}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/alternate}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/cointerior}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/line}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/ct1}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/ct2}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/ct3}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/ct4}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/ct5}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/ct6}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/point}"]
		answers = [
			"Opposite angles are equal",
			"Angles in a triangle sum to 180\\mydeg",
			"Corresponding angles are equal",
			"Alternate angles are equal",
			"Angles on a straight line sum to 180\\mydeg",
			"The angle at the centre is twice the angle at the circumference",
			"The angle in a semi-circle is 90\\mydeg",
			"Angles in the same segment are equal",
			"The angle between a radius and a tangent is 90\\mydeg",
			"Alternate segment theorem",
			"Opposite angles in a cyclic quadrilateral sum to 180\\mydeg",
			"Angles around a point sum to 360\\mydeg"]
		cycler = session%len(diags)
		question = "Explain the angle fact shown in the diagram on the board."
		answer = answers[cycler]
		diag = diags[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		return diag



def hanglefacts2(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 2
		ct13angles = [100,110,130,140,150,160]
		ct13ang = random.choice(ct13angles)
		ct3ang1 = random.randrange(10,50)
		ct3ang2 = ct3ang1
		while ct3ang1==ct3ang2:	
			ct3ang2 = random.randrange(10,50)
		if random.randrange(0,2)==0:
			temp = "ct6"
			op = "opposite1"
			opang = random.randrange(11,18)*10
			opput = "43,30"
			coint = "cointerior"
			cointang = random.randrange(10,17)*10
			cointput = "51,43"
			line = "line"
			lineang = random.randrange(10,17)*10
			lineput = "55,6"
			ct1ang = random.randrange(2,9)*10
			ct1 = "ct1"
			ct1put = "63,73"
			ct2put = "76,59"
			ct12 = "ct12"
			ct6ang = random.randrange(10,17)*10
			ct13 = "ct13"
			ct13ans = int(360 - ct13ang*2)
			ct13put = "51,7"
			if random.randrange(0,2)==0:
				ct3 = "ct3"
				ct3put1 = "71,59"
				ct3put2 = "73,40"
				ct5 = "ct5"
				ct5put = "44,12"
			else:
				ct3 = "ct32"
				ct3put2 = "71,59"
				ct3put1 = "73,40"
				ct5 = "ct52"
				ct5put = "69,67"
			ct6put = "9,67"
		else:
			temp = "ct62"
			op = "opposite2"
			opang = random.randrange(2,9)*10
			opput = "30,22"
			coint = "cointerior2"
			cointang = random.randrange(2,9)*10
			cointput = "46,22"
			line = "line2"
			lineang = random.randrange(2,9)*10
			lineput = "36,6"
			ct1ang = random.randrange(10,17)*10
			ct1 = "ct11"
			ct1put = "40,37"
			ct12 = "ct122"
			ct2put = "40,37"
			ct6ang = random.randrange(2,9)*10
			ct13 = "ct133"
			ct13ans = int((360-ct13ang)/2)
			ct13put = "40,37"
			if random.randrange(0,2)==1:
				ct3 = "ct33"
				ct3put1 = "30,69"
				ct3put2 = "29,25"
				ct5 = "ct53"
				ct5put = "14,69"
			else:
				ct3 = "ct34"
				ct3put2 = "30,69"
				ct3put1 = "29,25"
				ct5 = "ct54"
				ct5put = "68,24"
			ct6put = "16,21"
		ct3ans = ct3ang1
		if ct1ang>95:
			ct1ans = int(ct1ang/2)
		else:
			ct1ans = ct1ang*2
		diags = [
			op,
			"triangle",
			"corresponding",
			"alternate",
			coint,
			line,
			ct1,
			ct12,
			ct13,
			"ct2",
			ct3,
			"ct4",
			ct5,
			temp,
			"point"]
		cycler = session%len(diags)
		angles = [
			opang,
			[random.randrange(2,9)*10,random.randrange(2,9)*10],
			random.randrange(20,80),
			random.randrange(20,80),
			cointang,
			lineang,
			ct1ang,
			ct1ang,
			ct13ang,
			"",
			[ct3ang1,ct3ang2],
			"blank",
			random.randrange(10,50),
			ct6ang,
			[random.randrange(4,8)*10,random.randrange(4,8)*10,random.randrange(10,14)*10]]
		answers = [
			opang,
			180-(angles[1][0] + angles[1][1]),
			angles[2],
			angles[3],
			180-cointang,
			180-lineang,
			ct1ans,
			ct1ans,
			ct13ans,
			90,
			angles[10][0],
			90,
			angles[12],
			180-ct6ang,
			180-(angles[14][0] + angles[14][1] + angles[14][2])]
		puts = [
			"\\put(" + opput + "){" + str(angles[0]) + "\\mydeg}",
			"\\put(60,43){" + str(angles[1][0]) + "\\mydeg} \\put(77,5){" + str(angles[1][1]) + "\\mydeg}",
			"\\put(46,22){" + str(angles[2]) + "\\mydeg}",
			"\\put(46,22){" + str(angles[3]) + "\\mydeg}",
			"\\put(" + cointput + "){" + str(angles[4]) + "\\mydeg}",
			"\\put(" + lineput + "){" + str(angles[5]) + "\\mydeg}",
			"\\put(" + ct1put + "){" + str(angles[6]) + "\\mydeg}",
			"\\put(" + ct2put + "){" + str(angles[7]) + "\\mydeg}",
			"\\put(" + ct13put + "){" + str(angles[8]) + "\\mydeg}",
			"",
			"\\put(" + ct3put1 + "){" + str(angles[10][0]) + "\\mydeg}" + "\\put(" + ct3put2 + "){" + str(angles[10][1]) + "\\mydeg}",
			"",
			"\\put(" + ct5put + "){" + str(angles[12]) + "\\mydeg}",
			"\\put(" + ct6put + "){" + str(angles[13]) + "\\mydeg}",
			"\\put(32,26){" + str(angles[14][0]) + "\\mydeg} \\put(37,40){" + str(angles[14][1]) + "\\mydeg} \\put(43,18){" + str(angles[14][2]) + "\\mydeg}"]
		facts = [
			"opposite angles are equal",
			"angles in a triangle sum to 180\\mydeg",
			"corresponding angles are equal",
			"alternate angles are equal",
			"co-interior angles sum to 180\\mydeg",
			"angles on a straight line sum to 180\\mydeg",
			"the angle at the centre is twice the angle at the circumference",
			"the angle at the centre is twice the angle at the circumference",
			"the angle at the centre is twice the angle at the circumference",
			"the angle in a semi-circle is 90\\mydeg",
			"angles in the same segment are equal",
			"the angle between a radius and a tangent is 90\\mydeg",
			"alternate segment theorem",
			"opposite angles in a cyclic quadrilateral sum to 180\\mydeg",
			"angles around a point sum to 360\\mydeg"]
		question = "Find the missing angle and give a reason for your answer (board)."
		diag = "\\begin{overpic}[scale=" + str(scale) + "]{gym/images/" + diags[cycler] + "} " + puts[cycler] + " \\end{overpic}"
		answer = answers[cycler]
		#diag = diags[cycler]
		answer = str(answer) + "\\mydeg \\hspace{0.05cm} because " + facts[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		return diag




def fanglefacts2(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 2
		scale2 = 0.33
		if random.randrange(0,2)==0:
			op = "opposite1"
			opang = random.randrange(11,18)*10
			opput = "43,30"
			coint = "cointerior"
			cointang = random.randrange(10,17)*10
			cointput = "51,43"
			line = "line"
			lineang = random.randrange(10,17)*10
			lineput = "55,6"
		else:
			temp = "ct62"
			op = "opposite2"
			opang = random.randrange(2,9)*10
			opput = "30,22"
			coint = "cointerior2"
			cointang = random.randrange(2,9)*10
			cointput = "46,22"
			line = "line2"
			lineang = random.randrange(2,9)*10
			lineput = "36,6"
		diags = [
			"poscorrel",
			"negcorrel",
			op,
			"triangle",
			"corresponding",
			"alternate",
			coint,
			line,
			"point"]
		cycler = session%len(diags)
		angles = [
			"",
			"",
			opang,
			[random.randrange(2,9)*10,random.randrange(2,9)*10],
			random.randrange(20,80),
			random.randrange(20,80),
			cointang,
			lineang,
			[random.randrange(4,8)*10,random.randrange(4,8)*10,random.randrange(10,14)*10]]
		answers = [
			"",
			"",
			opang,
			180-(angles[3][0] + angles[3][1]),
			angles[4],
			angles[5],
			180-cointang,
			180-lineang,
			180-(angles[8][0] + angles[8][1] + angles[8][2])]
		puts = [
			"",
			"",
			"\\put(" + opput + "){" + str(angles[2]) + "\\mydeg}",
			"\\put(60,43){" + str(angles[3][0]) + "\\mydeg} \\put(77,5){" + str(angles[3][1]) + "\\mydeg}",
			"\\put(46,22){" + str(angles[4]) + "\\mydeg}",
			"\\put(46,22){" + str(angles[5]) + "\\mydeg}",
			"\\put(" + cointput + "){" + str(angles[6]) + "\\mydeg}",
			"\\put(" + lineput + "){" + str(angles[7]) + "\\mydeg}",
			"\\put(32,26){" + str(angles[8][0]) + "\\mydeg} \\put(37,40){" + str(angles[8][1]) + "\\mydeg} \\put(43,18){" + str(angles[8][2]) + "\\mydeg}"]
		facts = [
			"positive correlation",
			"negative correlation",
			"opposite angles are equal",
			"angles in a triangle sum to 180\\mydeg",
			"corresponding angles are equal",
			"alternate angles are equal",
			"co-interior angles sum to 180\\mydeg",
			"angles on a straight line sum to 180\\mydeg",
			"angles around a point sum to 360\\mydeg"]
		if cycler >= 2:
			question = "Find the missing angle and give a reason for your answer (board)."
			diag = "\\begin{overpic}[scale=" + str(scale) + "]{gym/images/" + diags[cycler] + "} " + puts[cycler] + " \\end{overpic}"
			answer = answers[cycler]
			answer = str(answer) + "\\mydeg \\hspace{0.05cm} because " + facts[cycler]
		else:
			question = "Describe the correlation shown on the graph on the board."
			diag = "\\begin{overpic}[scale=" + str(scale2) + "]{gym/images/" + diags[cycler] + "} \\end{overpic}"
			answer = facts[cycler]
			
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		return diag





def fanglefacts(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 3
		scale2 = 0.33
		diags = [
			"\\includegraphics[scale=" + str(scale2) + "]{gym/images/poscorrel}",
			"\\includegraphics[scale=" + str(scale2) + "]{gym/images/negcorrel}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/point}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/opposite}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/triangle}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/corresponding}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/alternate}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/co-interior}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/line}"]
		answers = [
			"Positive Correlation",
			"Negative Correlation",
			"Angles around a point sum to 360\\mydeg",
			"Opposite angles are equal",
			"Angles in a triangle sum to 180\\mydeg",
			"Corresponding angles are equal",
			"Alternate angles are equal",
			"Co-interior angles sum to 180\\mydeg",
			"Angles on a straight line sum to 180\\mydeg"]
		cycler = session%len(diags)
		if cycler<2:
			question = "Describe the correlation shown on the graph on the board."
		else:
			question = "Explain the angle fact shown in the diagram on the board."
		answer = answers[cycler]
		diag = diags[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		return diag


def shapenames(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 1
		diags = [
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/cone}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/cube}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/cuboid}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/cylinder}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/equilateral}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/hexagon}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/isosceles}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/kite}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/octagon}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/parallelogram}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/pentagon}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/pyramid}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/rectangle}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/rhombus}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/right-angled}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/scalene}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/sphere}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/square}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/trapezium}",
			"\\includegraphics[scale=" + str(scale) + "]{shape/names/triangularprism}"]
		answers = [
			"Cone",
			"Cube",
			"Cuboid",
			"Cylinder",
			"Equilateral Triangle",
			"Hexagon",
			"Isosceles Triangle",
			"Kite",
			"Octagon",
			"Parallelogram",
			"Pentagon",
			"(Square-Based) Pyramid",
			"Rectangle",
			"Rhombus",
			"Right-Angled Triangle",
			"Scalene Triangle",
			"Sphere",
			"Square",
			"Trapezium",
			"Triangular Prism"]
		cycler = session%len(diags)
		question = "Name the shape on the board."
		answer = answers[cycler]
		diag = diags[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		return diag


def exacttrigvalues(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		questions = [
			"Write down the exact value of Sin\,0\\mydeg",
			"Write down the exact value of Sin\,30\\mydeg",
			"Write down the exact value of Sin\,45\\mydeg",
			"Write down the exact value of Sin\,60\\mydeg",
			"Write down the exact value of Sin\,90\\mydeg",
			"Write down the exact value of Cos\,0\\mydeg",
			"Write down the exact value of Cos\,30\\mydeg",
			"Write down the exact value of Cos\,45\\mydeg",
			"Write down the exact value of Cos\,60\\mydeg",
			"Write down the exact value of Cos\,90\\mydeg",
			"Write down the exact value of Tan\,0\\mydeg",
			"Write down the exact value of Tan\,30\\mydeg",
			"Write down the exact value of Tan\,45\\mydeg",
			"Write down the exact value of Tan\,60\\mydeg"]
		answers = [
			"0",
			"$\\dfrac{1}{2}$",
			"$\\dfrac{1}{\\sqrt{2}} \\text{ or } \\dfrac{\\sqrt{2}}{2}$",
			"$\\dfrac{\\sqrt{3}}{2}$",
			"1",
			"1",
			"$\\dfrac{\\sqrt{3}}{2}$",
			"$\\dfrac{1}{\\sqrt{2}} \\text{ or } \\dfrac{\\sqrt{2}}{2}$",
			"$\\dfrac{1}{2}$",
			"0",
			"0",
			"$\\dfrac{1}{\\sqrt{3}}$",
			"1",
			"$\\sqrt{3}$"]
		cycler = session%len(questions)
		question = questions[cycler]
		answer = answers[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def suvattrig(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		questions = [
			"What does the \"U\" in SUVAT stand for?",
			"What does the \"V\" in SUVAT stand for?",
			"What does the \"A\" in SUVAT stand for?",
			"What does the \"T\" in SUVAT stand for?",
			"What does the \"S\" in SUVAT stand for?",
			"Write down the exact value of Sin\,0\\mydeg",
			"Write down the exact value of Sin\,30\\mydeg",
			"Write down the exact value of Sin\,45\\mydeg",
			"Write down the exact value of Sin\,60\\mydeg",
			"Write down the exact value of Sin\,90\\mydeg",
			"Write down the exact value of Cos\,0\\mydeg",
			"Write down the exact value of Cos\,30\\mydeg",
			"Write down the exact value of Cos\,45\\mydeg",
			"Write down the exact value of Cos\,60\\mydeg",
			"Write down the exact value of Cos\,90\\mydeg",
			"Write down the exact value of Tan\,0\\mydeg",
			"Write down the exact value of Tan\,30\\mydeg",
			"Write down the exact value of Tan\,45\\mydeg",
			"Write down the exact value of Tan\,60\\mydeg"]
		answers = [
			"Initial velocity",
			"Final velocity",
			"Acceleration",
			"Time",
			"Displacement (or distance)",
			"0",
			"$\\dfrac{1}{2}$",
			"$\\dfrac{1}{\\sqrt{2}} \\text{ or } \\dfrac{\\sqrt{2}}{2}$",
			"$\\dfrac{\\sqrt{3}}{2}$",
			"1",
			"1",
			"$\\dfrac{\\sqrt{3}}{2}$",
			"$\\dfrac{1}{\\sqrt{2}} \\text{ or } \\dfrac{\\sqrt{2}}{2}$",
			"$\\dfrac{1}{2}$",
			"0",
			"0",
			"$\\dfrac{1}{\\sqrt{3}}$",
			"1",
			"$\\sqrt{3}$"]
		cycler = session%len(questions)
		question = questions[cycler]
		answer = answers[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def hbearingsmem(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		bearings = [
			"000",
			"045",
			"090",
			"135",
			"180",
			"225",
			"270",
			"315"]
		directions = [
			"North",
			"North-East",
			"East",
			"South-East",
			"South",
			"South-West",
			"West",
			"North-West"]
		#cycler = session%len(questions)
		cycler = random.randrange(0,len(bearings))
		if random.randrange(0,2)==1:
			question = "What compass direction is bearing " + bearings[cycler] + "\\mydeg?"
			answer = directions[cycler]
		else:
			question = "On what bearing is compass direction " + directions[cycler] + "?"
			answer = bearings[cycler] + "\\mydeg"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def fbearingsmem(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		bearings = [
			"000",
			"090",
			"180",
			"270"]
		directions = [
			"North",
			"East",
			"South",
			"West"]
		#cycler = session%len(questions)
		cycler = random.randrange(0,len(bearings))
		if random.randrange(0,2)==1:
			question = "What compass direction is bearing " + bearings[cycler] + "\\mydeg?"
			answer = directions[cycler]
		else:
			question = "On what bearing is compass direction " + directions[cycler] + "?"
			answer = bearings[cycler] + "\\mydeg"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def identifygraphs(n,session):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 0.55
		diags = [
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph1}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph2}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph3}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph4}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph5}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph6}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph7}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph8}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph9}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph10}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph11}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph12}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph13}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph14}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph15}",
			"\\includegraphics[scale=" + str(scale) + "]{gym/images/graph16}"]
		answers = [
			"$\\text{y} = \\text{x}$",
			"$\\text{y} = -\\text{x}$",
			"$\\text{y} = \\text{x}^{2}$",
			"$\\text{y} = -\\text{x}^{2}$",
			"$\\text{y} = \\text{x}^{3}$",
			"$\\text{y} = -\\text{x}^{3}$",
			"$\\text{y} = \\dfrac{1}{\\text{x}}$",
			"$\\text{y} = -\\dfrac{1}{\\text{x}}$",
			"$\\text{y} = \\text{Sin\,x}\\mydeg$",
			"$\\text{y} = -\\text{Sin\,x}\\mydeg$",
			"$\\text{y} = \\text{Cos\,x}\\mydeg$",
			"$\\text{y} = -\\text{Cos\,x}\\mydeg$",
			"$\\text{y} = \\text{Tan\,x}\\mydeg$",
			"$\\text{y} = -\\text{Tan\,x}\\mydeg$",
			"$\\text{y} = 2^{\\text{x}}$",
			"$\\text{y} = -2^{\\text{x}}$"]
		cycler = session%len(diags)
		question = "Write down the equation of the graph on the board."
		answer = answers[cycler]
		diag = diags[cycler]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		return diag

def calc1(n,session):
	import random
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		answer = 1
		while answer%1==0:
			a = random.randrange(1,10) + random.randrange(1,10)/10
			b = random.randrange(1,10) + random.randrange(1,10)/10
			c = random.randrange(1,10) + random.randrange(1,10)/10
			d = random.randrange(1,10)/10
			answer = rounddp((a + b)/(c * d),2)
		if random.randrange(1,3)==1:
			temp = c
			c = d
			d = temp
		question = "$\\dfrac{" + str(a) + " + " + str(b) + "}{" + str(c) + " \\times " + str(d) + "}$"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(rounddpstring(answer,2))


def calc2(n,session):
	import random
	from math import sqrt
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(1,10) + random.randrange(1,10)/10
		b = random.randrange(1,10) + random.randrange(1,10)/10
		questions = [
			"$" + str(a) + "^{3} + \\sqrt{" + str(b) + "}$",
			"$\\sqrt{" + str(a) + "} + " + str(b) + "^{3}$",
			"$" + str(a) + "^{2} + \\sqrt[3]{" + str(b) + "}$",
			"$\\sqrt[3]{" + str(a) + "} + " + str(b) + "^{2}$"]
		answers = [
			rounddpstring(a**3 + sqrt(b),2),
			rounddpstring(sqrt(a) + b**3,2),
			rounddpstring(a**2 + b**(1./3),2),
			rounddpstring(a**(1./3) + b**2,2)]
		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def calc3(n,session):
	import random
	from math import sqrt
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(1,10) + random.randrange(1,10)/10
		b = random.randrange(1,11) + random.randrange(1,10)/10
		x = random.randrange(2,6)*2
		y = random.randrange(4,11)
		questions = [
			"$\\sqrt[" + str(x) + "]{" + str(a) + "^{" + str(y) + "} \\times " + str(b) + "}$",
			"$\\sqrt[" + str(x) + "]{" + str(b) + " \\times " + str(a) + "^{" + str(y) + "}}$"]
		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = rounddpstring((a**y * b)**(1./x),2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def calc4(n,session):
	import random
	from math import sqrt
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(1,10) + random.randrange(1,10)/10
		b = random.randrange(1,6) + random.randrange(1,10)/10
		x = random.randrange(2,6)*2
		y = random.randrange(4,9)
		questions = [
			"$(\\sqrt[" + str(x) + "]{" + str(a) + "} + " + str(b) + ")^{" + str(y) + "}$",
			"$(" + str(b) + " + \\sqrt[" + str(x) + "]{" + str(a) + "})^{" + str(y) + "}$"]
		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = rounddpstring((a**(1./x) + b)**y,2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def calc5(n,session): #quad formula
	import random
	from utilities.rounding import rounddp,rounddpstring
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,6)
		b = random.randrange(2,13) * (-1)**random.randrange(1,3)
		c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while c==0:
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while sqrt(b**2 - 4*a*c)%1==0:
			a = random.randrange(2,6)
			b = random.randrange(2,13) * (-1)**random.randrange(1,3)
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
			while c==0:
				c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		answers = [
			rounddpstring((-b + sqrt(b**2 - 4*a*c))/(2*a),2),
			rounddpstring((-b - sqrt(b**2 - 4*a*c))/(2*a),2)]
		if b<0:
			b = "(" + str(b) + ")"
		questions = [
			"$ \\dfrac{- " + str(b) + " + \\sqrt{" + str(b) + "^{2} - 4 \\times "+ str(a) + " \\times " + str(c) + "}}{2 \\times " + str(a) + "}$",
			"$ \\dfrac{- " + str(b) + " - \\sqrt{" + str(b) + "^{2} - 4 \\times "+ str(a) + " \\times " + str(c) + "}}{2 \\times " + str(a) + "}$"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def calc6(n,session): #cosine side
	import random
	from math import cos,radians,sqrt
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		A = random.randrange(10,100)
		b = random.randrange(2,51)
		c = random.randrange(2,51)
		question = "$\\sqrt{" + str(b) + "^{2} + " + str(c) + "^{2} - 2 \\times " + str(b) + " \\times " + str(c) + " \\times \\text{Cos}\," + str(A) + "}$"
		answer = rounddpstring(sqrt(b**2 + c**2 - 2 * b * c * cos(radians(A))),2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def calc7(n,session): #cosine angle
	import random
	from math import cos,radians,sqrt,floor,acos,degrees,ceil
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(4,102)/2
		if a%1==0:
			a = int(a)
		b = random.randrange(4,102)/2
		if b%1==0:
			b = int(b)
		top = floor(a+b) - 1
		bottom = ceil(abs(a-b)) + 1
		c = random.randrange(bottom,top)
		mixer = [a,b,c]
		random.shuffle(mixer)
		a = mixer[0]
		b = mixer[1]
		c = mixer[2]
		question = "$\\text{Cos}^{-1}\\left(\\dfrac{" + str(b) + "^{2} + " + str(c) + "^{2} - " + str(a) + "^{2}}{2 \\times " + str(b) + " \\times " + str(c) + "}\\right)$"
		answer = rounddpstring(degrees(acos((b**2 + c**2 - a**2)/(2*b*c))),2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def calc8(n,session): #sine side
	import random
	from math import sin,radians,sqrt
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		angles = [10,30,50]
		for i in range(0,90):
			dec = random.randrange(0,3)
			angles[dec] = angles[dec] + 1
		a = angles[0]
		a2 = angles[1]
		l1 = random.randrange(4,102)/2
		if l1%1==0:
			l1 = int(l1)
		answer = rounddpstring(l1/sin(radians(a)) * sin(radians(a2)),2)
		question = "$\\dfrac{" + str(l1) + "}{\\text{Sin}\, " + str(a) + "} \\times \\text{Sin}\, " + str(a2) + "$"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def calc9(n,session): #sine angle
	import random
	from math import sin,radians,sqrt,degrees,asin
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(20,70)
		a2 = "?"
		l1 = random.randrange(4,102)/2
		l2 = random.randrange(4,102)/2
		if l1<l2:
			temp = l1
			l1 = l2
			l2 = temp
		if l1%1==0:
			l1 = int(l1)
		if l2%1==0:
			l2 = int(l2)
		question = "$\\text{Sin}^{-1}\\left(\\dfrac{\\text{Sin}\, " + str(a) + "}{" + str(l1) + "} \\times " + str(l2) + "\\right)$"
		answer = rounddpstring(degrees(asin(sin(radians(a))/l1 * l2)),2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def calc10(n,session): #area triangle
	import random
	from math import sin,radians
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
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
		answer = rounddpstring(0.5 * l1 * l2 * sin(radians(a)),2)
		question = "$\\dfrac{1}{2} \\times " + str(l1) + " \\times " + str(l2) + " \\times \\text{Sin}\, " + str(a) + "$"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def calc11(n,session): #mixed number
	import random
	from math import sin,radians
	from math import gcd
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		dens = list(range(2,13))
		den = random.choice(dens)
		nums = []
		for i in range(1,den):
			if gcd(i,den)==1:
				nums.append(i)
		num = random.choice(nums)
		int = random.randrange(1,4)
		multiplier = rounddp(random.randrange(1,10)/10,1)+1
		power = random.randrange(2,6)
		answer = rounddpstring(((int + (num/den))*multiplier)**power,2)
		question = "$(" + str(int) + "\\dfrac{" + str(num) + "}{" + str(den) + "} \\times " + str(multiplier) + ")^{" + str(power) + "}$"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def calc12(n,session): #area circle
	import random
	from math import pi
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		r = rounddp(random.randrange(10,100)/10,1)
		if r%1==0:
			r = int(r)
		question = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}} \\times " + str(r) + "^{2}$"
		answer = rounddpstring(pi * r**2,2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def calc13(n,session): #simple trig
	import random
	from math import sin,radians,cos,tan
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		angle = random.randrange(1,360)
		dec = random.randrange(0,3)
		if dec==0:
			question = "$\\text{Sin\," + str(angle) + "}\\mydeg$"
			answer = rounddpstring(sin(radians(angle)),2)
		elif dec==1:
			question = "$\\text{Cos\," + str(angle) + "}\\mydeg$"
			answer = rounddpstring(cos(radians(angle)),2)
		else:
			angles = list(range(1,360))
			angles.remove(90)
			angles.remove(270)
			angle = random.choice(angles)
			question = "$\\text{Tan\," + str(angle) + "}\\mydeg$"
			answer = rounddpstring(tan(radians(angle)),2)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fracadd(n,explanationn):
	import random
	from math import gcd
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		dens = list(range(2,13))
		den1 = random.choice(dens)
		dens.remove(den1)
		den2 = random.choice(dens)
		nums = []
		for i in range(1,den1):
			if gcd(i,den1)==1:
				nums.append(i)
		num1 = random.choice(nums)
		nums = []
		for i in range(1,den2):
			if gcd(i,den2)==1:
				nums.append(i)
		num2 = random.choice(nums)
		question = "$\\dfrac{" + str(num1) + "}{" + str(den1) + "} + \\dfrac{" + str(num2) + "}{" + str(den2) + "}$"
		numa = num1*den2 + num2*den1
		dena = den1*den2
		hcf = gcd(numa,dena)
		numa = int(numa/hcf)
		dena = int(dena/hcf)
		if numa==dena:
			answer = "1"
		elif numa>dena:
			integer = floor(numa/dena)
			numa = numa-dena*integer
			if numa==0:
				answer = str(integer)
			else:
				answer = "$" + str(integer) + "\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
		else:
			answer = "$\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fracsub(n,explanationn):
	import random
	from math import gcd
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		dens = list(range(2,13))
		den1 = random.choice(dens)
		dens.remove(den1)
		den2 = random.choice(dens)
		nums = []
		for i in range(1,den1):
			if gcd(i,den1)==1:
				nums.append(i)
		num1 = random.choice(nums)
		nums = []
		for i in range(1,den2):
			if gcd(i,den2)==1:
				nums.append(i)
		num2 = random.choice(nums)
		if num1/den1<num2/den2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = den1
			den1 = den2
			den2 = temp
		question = "$\\dfrac{" + str(num1) + "}{" + str(den1) + "} - \\dfrac{" + str(num2) + "}{" + str(den2) + "}$"
		numa = num1*den2 - num2*den1
		dena = den1*den2
		hcf = gcd(numa,dena)
		numa = int(numa/hcf)
		dena = int(dena/hcf)
		if numa==dena:
			answer = "1"
		elif numa>dena:
			integer = floor(numa/dena)
			numa = numa-dena*integer
			if numa==0:
				answer = str(integer)
			else:
				answer = "$" + str(integer) + "\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
		else:
			answer = "$\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def mixnumadd(n,explanationn):
	import random
	from math import gcd
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		dens = list(range(2,13))
		den1 = random.choice(dens)
		dens.remove(den1)
		den2 = random.choice(dens)
		nums = []
		for i in range(1,den1):
			if gcd(i,den1)==1:
				nums.append(i)
		num1 = random.choice(nums)
		nums = []
		for i in range(1,den2):
			if gcd(i,den2)==1:
				nums.append(i)
		num2 = random.choice(nums)
		int1 = random.randrange(0,3)
		if int1==0:
			int2 = random.randrange(1,3)
		else:
			int2 = random.randrange(0,3)
		numa = (num1+int1*den1)*den2 + (num2 + int2*den2)*den1
		dena = den1*den2
		if int1==0:
			int1 = ""
		if int2==0:
			int2 = ""
		question = "$" + str(int1) + "\\dfrac{" + str(num1) + "}{" + str(den1) + "} + " + str(int2) + "\\dfrac{" + str(num2) + "}{" + str(den2) + "}$"
		hcf = gcd(numa,dena)
		numa = int(numa/hcf)
		dena = int(dena/hcf)
		if numa==dena:
			answer = "1"
		elif numa>dena:
			integer = floor(numa/dena)
			numa = numa-dena*integer
			if numa==0:
				answer = str(integer)
			else:
				answer = "$" + str(integer) + "\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
		else:
			answer = "$\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def mixnumsub(n,explanationn):
	import random
	from math import gcd
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		dens = list(range(2,13))
		den1 = random.choice(dens)
		dens.remove(den1)
		den2 = random.choice(dens)
		nums = []
		for i in range(1,den1):
			if gcd(i,den1)==1:
				nums.append(i)
		num1 = random.choice(nums)
		nums = []
		for i in range(1,den2):
			if gcd(i,den2)==1:
				nums.append(i)
		num2 = random.choice(nums)
		int1 = random.randrange(0,3)
		if int1==0:
			int2 = random.randrange(1,3)
		else:
			int2 = random.randrange(0,3)
		if int1+num1/den1<int2+num2/den2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = den1
			den1 = den2
			den2 = temp
			temp = int1
			int1 = int2
			int2 = temp
		numa = (num1+int1*den1)*den2 - (num2 + int2*den2)*den1
		dena = den1*den2
		if int1==0:
			int1 = ""
		if int2==0:
			int2 = ""
		question = "$" + str(int1) + "\\dfrac{" + str(num1) + "}{" + str(den1) + "} - " + str(int2) + "\\dfrac{" + str(num2) + "}{" + str(den2) + "}$"
		hcf = gcd(numa,dena)
		numa = int(numa/hcf)
		dena = int(dena/hcf)
		if numa==dena:
			answer = "1"
		elif numa>dena:
			integer = floor(numa/dena)
			numa = numa-dena*integer
			if numa==0:
				answer = str(integer)
			else:
				answer = "$" + str(integer) + "\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
		else:
			answer = "$\\dfrac{" + str(numa) + "}{" + str(dena) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def compoundinterestgym(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d1 = random.randrange(0,2)
		d1 = 1
		a = random.randrange(1,51)*500
		t2 = " at the start of "
		year = random.randrange(2010,2021)
		d2 = random.randrange(0,2)
		p = random.randrange(2,31)/2
		if p%1==0:
			p = int(p)
		t5 = "\% per year. What is "
		year2 = year + random.randrange(2,10)
		if d1==0:
			t1 = "A population starts at "
			t3 = " and "
			t6 = "the population after "
			if d2==0:
				ans = str(int(rounddp(a * (1-p/100)**(year2 - year),0)))
				t4 = "decreases by "
			else:
				ans = str(int(rounddp(a * (1+p/100)**(year2 - year),0)))
				t4 = "increases by "
		else:
			t1 = "The value of an item starts at \pounds"
			t3 = " and "
			t6 = " its value after "
			if d2==0:
				ans = "\pounds" + str("{0:.2f}".format(a * (1-p/100)**(year2 - year)))
				t4 = "decreases by "
			else:
				ans = "\pounds" + str("{0:.2f}".format(a * (1+p/100)**(year2 - year)))
				t4 = "increases by "
		years = year2 - year
#write question
		tempquestions.write(t1 + str(a) + t3 + t4 + str(p) + t5 + t6 + str(years) + " years?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(ans)


def equationcirclegym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		radius = random.randrange(2,11)
		question = "Write down the equation of the circle with centre (0 , 0) and radius " + str(radius) + "."
		answer = "x$^{2} + $ y$^{2} = $" + str(radius**2)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fdpfive(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]
		q1 = "Write " + percentages[a] + " as a decimal."
		a1 = decimals[a]
		q2 = "Write " + decimals[b] + " as a percentage."
		a2 = percentages[b]
		q3 = "Write " + percentages[c] + " as a fraction in its simplest form."
		a3 = fractions[c]
		q4 = "Write " + fractions[d] + " as a percentage."
		a4 = percentages[d]
		q5 = "Write " + fractions[e] + " as a decimal."
		a5 = decimals[e]
		q6 = "Write " + decimals[f] + " as a fraction in its simplest form."
		a6 = fractions[f]
#write all qs and as
		tempquestions.write(q1)
		tempquestions.write("\n")
		tempquestions.write(a1)
		tempquestions.write("\n")
		tempquestions.write(q2)
		tempquestions.write("\n")
		tempquestions.write(a2)
		tempquestions.write("\n")
		tempquestions.write(q3)
		tempquestions.write("\n")
		tempquestions.write(a3)
		tempquestions.write("\n")
		tempquestions.write(q4)
		tempquestions.write("\n")
		tempquestions.write(a4)
		tempquestions.write("\n")
		tempquestions.write(q5)
		tempquestions.write("\n")
		tempquestions.write(a5)


def fdpsix(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]
		q1 = "Write " + percentages[a] + " as a decimal."
		a1 = decimals[a]
		q2 = "Write " + decimals[b] + " as a percentage."
		a2 = percentages[b]
		q3 = "Write " + percentages[c] + " as a fraction in its simplest form."
		a3 = fractions[c]
		q4 = "Write " + fractions[d] + " as a percentage."
		a4 = percentages[d]
		q5 = "Write " + fractions[e] + " as a decimal."
		a5 = decimals[e]
		q6 = "Write " + decimals[f] + " as a fraction in its simplest form."
		a6 = fractions[f]
#write all qs and as
		tempquestions.write(q1)
		tempquestions.write("\n")
		tempquestions.write(a1)
		tempquestions.write("\n")
		tempquestions.write(q2)
		tempquestions.write("\n")
		tempquestions.write(a2)
		tempquestions.write("\n")
		tempquestions.write(q3)
		tempquestions.write("\n")
		tempquestions.write(a3)
		tempquestions.write("\n")
		tempquestions.write(q4)
		tempquestions.write("\n")
		tempquestions.write(a4)
		tempquestions.write("\n")
		tempquestions.write(q5)
		tempquestions.write("\n")
		tempquestions.write(a5)
		tempquestions.write("\n")
		tempquestions.write(q6)
		tempquestions.write("\n")
		tempquestions.write(a6)

def donothing(n,explanationn):
	import random
	for x in range(0, n):
		print("Doing nothing, as requested")


def fmpscwallgym(n,cycler):
	import random
	from math import ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
		factorsof = [16,18,20,24,27,28,30,32,35,36,40,45,48,50,56,60,63,64,65,66,70,72,75,80]
		factorsof = random.choice(factorsof)
		factors = []
		for i in range (1,factorsof+1):
			if factorsof%i==0:
				factors.append(i)
		multiplesof = [4,5,6,7,8,9,10,11,12]
		multiplesof = random.choice(multiplesof)
		multiples = []
		for i in range(1,100):
			if i%multiplesof==0:
				multiples.append(i)
		squares = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
		cubes = [1,8,27,64,125]
		fulllist = list(range(1,100))
		nums = []
		nums.append(random.choice(cubes))
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in multiples:
				multiples.remove(nums[i])
			if nums[i] in squares:
				squares.remove(nums[i])
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
			if nums[i] in factors:
				factors.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(factors))
			factors.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in multiples:
				multiples.remove(nums[i])
			if nums[i] in squares:
				squares.remove(nums[i])
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(multiples))
			multiples.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in squares:
				squares.remove(nums[i])
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(squares))
			squares.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in primes:
				primes.remove(nums[i])
			if nums[i] in factors:
				factors.remove(nums[i])
		for j in range(0,3):
			nums.append(random.choice(primes))
			primes.remove(nums[-1])
		for i in range(0,len(nums)):
			if nums[i] in fulllist:
				fulllist.remove(nums[i])
		for j in range(0,2):
			nums.append(random.choice(fulllist))
			fulllist.remove(nums[-1])
		answera = []
		answerb = []
		answerc = []
		answerd = []
		answere = []
		primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
		cubes = [1,8,27,64,125]
		for i in range(0,len(nums)):
			if factorsof%nums[i]==0:
				answera.append(str(nums[i]))
			if nums[i]%multiplesof==0:
				answerb.append(str(nums[i]))
			if sqrt(nums[i])==int(sqrt(nums[i])):
				answerc.append(str(nums[i]))
			if nums[i] in cubes:
				answerd.append(str(nums[i]))
			if nums[i] in primes:
				answere.append(str(nums[i]))
			nums[i] = str(nums[i])
		aa = answera
		bb = answerb
		cc = answerc
		dd = answerd
		ee = answere
		answera = aa[0]
		answerb = bb[0]
		answerc = cc[0]
		answerd = dd[0]
		answere = ee[0]
		for i in range(1,len(aa)):
			answera = answera + ", " + aa[i]
		for i in range(1,len(bb)):
			answerb = answerb + ", " + bb[i]
		for i in range(1,len(cc)):
			answerc = answerc + ", " + cc[i]
		if len(dd)>1:
			for i in range(1,len(dd)):
				answerd = answerd + ", " + dd[i]
		for i in range(1,len(ee)):
			answere = answere + ", " + ee[i]
		random.shuffle(nums)
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{| c c c c c |} \\hline " + nums[0] + " & " + nums[1] + " & "  + nums[2] + " & " + nums[3] + " & " + nums[4] + "\\\\ " + nums[5] + " & " + nums[6] + " & "  + nums[7] + " & " + nums[8] + " & " + nums[9] + "\\\\"   + nums[10] + " & " + nums[11] + " & "  + nums[12] + " & " + nums[13] + " & " + nums[14] + "\\\\ \\hline \\end{tabular}"
		questiona = "From the board, write down the factors of " + str(factorsof)
		questionb = "From the board, write down the multiples of " + str(multiplesof)
		questionc = "From the board, write down the square numbers"
		questiond = "From the board, write down the cube numbers"
		questione = "From the board, write down the prime numbers"
		qs = [questiona,questionb,questionc,questiond,questione]
		aas = [answera,answerb,answerc,answerd,answere]
		cycler = cycler%5
		q1 = qs[cycler]
		a1 = aas[cycler]
#write all qs and as
		tempquestions.write(q1)
		tempquestions.write("\n")
		tempquestions.write(a1)
		return table

def coordinatesgym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nums = list(range(-4,5))
		x = random.choice(nums)
		nums.remove(x)
		y = random.choice(nums)
		co = "97.1,97.1"
		co = str(12.0025 * abs(-4 - x)) + " , " + str(12.00625 * abs(-4 - y))
		answer = "(" + str(x) + " , " + str(y) + ")"
		image = "\\begin{overpic}[scale=0.4]{gym/images/coordinategrid2} \\put(" + co + "){\\textbf{x}} \\end{overpic}"
		question = "Write down the co-ordinates of the point marked on the grid below: \\\\ \\begin{center}" + image + "\\end{center}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def cumfreqgym(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "(calc) Complete this table for a cumulative frequency graph:"
		if random.randrange(0,3)==1:
			lowest = random.randrange(1,5)*10
		else:
			lowest = 0
		diffs = [5,10,20,30,40,50]
		diff = random.choice(diffs)
		scorest = [lowest]
		bottoms = []
		xs = []
		scores = []
		scores2 = []
		for i in range(0,5):
			scorest.append(scorest[i]+diff)
			xs.append(scorest[i]+diff)
			bottoms.append(scorest[i])
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
			scores2.append("$" + str(scorest[0]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		inc = random.randrange(3,10)
		for i in range (0,5):
			freqs.append(random.randrange((i+1)*inc+1,(i+2)*inc+1))
		ofreqs = sorted(freqs)
		total = sum(freqs)
		difference = ceil(total/10)*10 - total
		ofreqs[4] = freqs[4] + difference

		dec = random.randrange(0,5)
		if dec==0:
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]
		elif dec==1:
			freqs = [ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1],ofreqs[0]]
		elif dec==2:
			freqs = [ofreqs[0],ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1]]
		elif dec==3:
			freqs = [ofreqs[0],ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2]]
		else:
			if random.randrange(0,2)==1:
				temp = freqs[1]
				freqs[1] = freqs[0]
				freqs[0] = temp
			if random.randrange(0,2)==1:
				temp = freqs[3]
				freqs[3] = freqs[2]
				freqs[2] = temp
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]

		freqslookup = [0,1,2,3,4]
		cumfreqs = [freqs[0],freqs[0]+freqs[1],freqs[0]+freqs[1]+freqs[2],freqs[0]+freqs[1]+freqs[2]+freqs[3],freqs[0]+freqs[1]+freqs[2]+freqs[3]+freqs[4]]
		medgroup = 0
		median = (cumfreqs[4]+1)/2
		while median>cumfreqs[medgroup]:
			medgroup = medgroup + 1
		L = bottoms[medgroup]
		n = cumfreqs[4]
		B = cumfreqs[medgroup-1]
		G = freqs[freqslookup[medgroup]]
		w = xs[medgroup]-bottoms[medgroup]
		median = L + (((n/2)-B)/G) * w
		lqgroup = 0
		lq = (cumfreqs[4]+1)/4
		while lq>cumfreqs[lqgroup]:
			lqgroup = lqgroup + 1
		L = bottoms[lqgroup]
		n = cumfreqs[4]
		B = cumfreqs[lqgroup-1]
		G = freqs[freqslookup[lqgroup]]
		w = xs[lqgroup]-bottoms[lqgroup]
		lq = L + (((n/4)-B)/G) * w
		uqgroup = 0
		uq = 3 * ((cumfreqs[4]+1)/4)
		while uq>cumfreqs[uqgroup]:
			uqgroup = uqgroup + 1
		L = bottoms[uqgroup]
		n = cumfreqs[4]
		B = cumfreqs[uqgroup-1]
		G = freqs[freqslookup[uqgroup]]
		w = xs[uqgroup]-bottoms[uqgroup]
		uq = L + (((3*n/4)-B)/G) * w
		for i in range(0,5):
			freqs[i] = str(freqs[i])
		for i in range(0,5):
			cumfreqs[i] = str(cumfreqs[i])
		for i in range(0,5):
			xs[i] = str(xs[i])
		coordinates = []
		for i in range(0,5):
			coordinates.append("(" + xs[i] + " , " + cumfreqs[i] + ")")
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{3cm} | M{2cm} | M{2.5cm} | M{2.5cm} |} \\hline Score & Frequency & Cumulative Frequency & Co-ordinates \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " & & \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " & & \\\\ \\hline " + scores[2] + " & " + freqs[2] + " & & \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " & & \\\\ \\hline " + scores[4] + " & " + freqs[4] + " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{3cm} | M{2cm} | M{2.5cm} | M{2.5cm} |} \\hline Score & Frequency & Cumulative Frequency & Co-ordinates \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " & " + cumfreqs[0] + " & " + coordinates[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " & " + cumfreqs[1] + " & " + coordinates[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " & " + cumfreqs[2] + " & " + coordinates[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " & " + cumfreqs[3] + " & " + coordinates[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " & " + cumfreqs[4] + " & " + coordinates[4] + " \\\\ \\hline \\end{tabular}"
		for i in range(0,5):
			freqs[i] = str(freqs[i])
		if lq%1==0:
			lq = str(int(lq))
		else:
			lq = str(rounddp(lq,1))
		if median%1==0:
			median = str(int(median))
		else:
			median = str(rounddp(median,1))
		if uq%1==0:
			uq = str(int(uq))
		else:
			uq = str(rounddp(uq,1))
		nl = " \\\\[0.3cm] "
		question = intro + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + "\\begin{center}" + atable + "\\end{center}~"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def histotablegym(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		score1 = random.randrange(0,10)*10
		diffs = [5,10,20,40]
		diff1 = random.choice(diffs)
		if diff1==5:
			freq1 = random.randrange(1,11)
		else:
			freq1 = random.randrange(1,21) * int(diff1/10)
		diff2 = random.choice(diffs)
		if diff2==5:
			freq2 = random.randrange(1,11)
		else:
			freq2 = random.randrange(1,21) * int(diff2/10)
		diff3 = random.choice(diffs)
		if diff3==5:
			freq3 = random.randrange(1,11)
		else:
			freq3 = random.randrange(1,21) * int(diff3/10)
		diff4 = random.choice(diffs)
		if diff4==5:
			freq4 = random.randrange(1,11)
		else:
			freq4 = random.randrange(1,21) * int(diff4/10)
		diff5 = random.choice(diffs)
		if diff5==5:
			freq5 = random.randrange(1,11)
		else:
			freq5 = random.randrange(1,21) * int(diff5/10)
		diffs = [diff1,diff2,diff3,diff4,diff5]
		freqs = [freq1,freq2,freq3,freq4,freq5]
		scores = [score1]
		for i in range(0,len(diffs)):
			scores.append(scores[i] + diffs[i])
		intervals = []
		for i in range(1,len(scores)):
			intervals.append("$" + str(scores[i-1]) + " \\leq (S) < " + str(scores[i]) + "$")
		densities = []	
		for i in range(0,len(diffs)):
			densities.append(rounddp(freqs[i]/diffs[i],1))
		for i in range(0,len(diffs)):
			if densities[i]%1==0:
				densities[i] = int(densities[i])
		for i in range(0,len(diffs)):
			freqs[i] = str(freqs[i])
			densities[i] = str(densities[i])
			diffs[i] = str(diffs[i])
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{3cm} | M{2cm} | M{2.5cm} | M{2.5cm} |} \\hline Score & Frequency & Class Width & Frequency Density \\\\ \\specialrule{1pt}{0pt}{0pt} " + intervals[0] + " & " + freqs[0] + "& & \\\\ \\hline " + intervals[1] + "  & " + freqs[1] + " & & \\\\ \\hline " + intervals[2] + " & " + freqs[2] + " & & \\\\ \\hline " + intervals[3] + "  & " + freqs[3] + " & & \\\\ \\hline " + intervals[4] + " & " + freqs[4] + " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{3cm} | M{2cm} | M{2.5cm} | M{2.5cm} | } \\hline Score & Frequency & Class Width & Frequency Density \\\\ \\specialrule{1pt}{0pt}{0pt} " + intervals[0] + " & " + freqs[0] + " & " + diffs[0] + " & " + densities[0] + " \\\\ \\hline " + intervals[1] + " & " + freqs[1] + " & " + diffs[1] + " & " + densities[1] + " \\\\ \\hline " + intervals[2] + " & " + freqs[2] + " & " + diffs[2] + " & " + densities[2] + " \\\\ \\hline " + intervals[3] + " & " + freqs[3] + " & " + diffs[3] + " & " + densities[3] + " \\\\ \\hline " + intervals[4] + " & " + freqs[4] + " & " + diffs[4] + " & " + densities[4] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = "(calc) Complete this table for a histogram: \\\\ \\begin{center}" + qtable + "\\end{center}"
		answer = "Complete this table for a histogram: \\\\ \\begin{center}" + atable + "\\end{center}"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def meantablegym(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "(calc) Calculate the mean of the data in this table: \\\\"
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			interval = 1
		else:
			interval = random.randrange(2,6)
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*interval
		scores = []
		for i in range(0,6):
			scores.append(scorestart+interval*i)
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		sfreqs = []
		for i in range(0,6):
			sfreqs.append(str(scores[i]*freqs[i]))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]
		multsum = scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5]
		answer = rounddp((scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			scores[i] = str(scores[i])
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{2cm} | M{2cm} | M{3.5cm} |} \\hline Score & Frequency & \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " & \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " & \\\\ \\hline " + scores[2] + " & " + freqs[2] + " & \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " & \\\\ \\hline " + scores[4] + " & " + freqs[4] + " & \\\\ \\hline " + scores[5] + " & " + freqs[5] + " & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{2cm} | M{2cm} | M{3.5cm} |} \\hline Score & Frequency & Score $\\times$ Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " & " + sfreqs[0] + "\\\\ \\hline " + scores[1] + "  & " + freqs[1] + " & " + sfreqs[1] + "\\\\ \\hline " + scores[2] + " & " + freqs[2] + " & " + sfreqs[2] + "\\\\ \\hline " + scores[3] + "  & " + freqs[3] + " & " + sfreqs[3] + "\\\\ \\hline " + scores[4] + " & " + freqs[4] + " & " + sfreqs[4] + "\\\\ \\hline " + scores[5] + " & " + freqs[5] + " & " + sfreqs[5] + "\\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\begin{center}" + table + "\\end{center}"
		answer = "\\begin{center}" + atable + "\\\\[0.3cm]" + str(multsum) + " $\\div$ " + str(freqsum) + " = " + str(answer) + "\\end{center}"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def meantablegroupedgym(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "(calc) Calculate an estimate for the mean of the data in this table: \\\\ "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*10
		if random.randrange(0,2)==1:
			diffs = [5,10,15,20,25,30,40,50]
		else:
			diffs = [50,100,150,200,250,300,350,400,450,500]
		scorest = [scorestart]
		for i in range(0,5):
			scorest.append(scorest[i]+random.choice(diffs))
		midpoints = []
		for i in range(0,5):
			a = scorest[i]
			b = scorest[i + 1]
			if (a+b)/2%1==0:
				midpoints.append(int((a+b)/2))
			else:
				midpoints.append(rounddp((a+b)/2,1))
		scores = []
		for i in range(0,5):
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqpoints = []
		for i in range (0,5):
			freqpoints.append(rounddp(midpoints[i]*freqs[i],1))
			if freqpoints[i]%1==0:
				freqpoints[i] = str(int(freqpoints[i]))
			else:
				freqpoints[i] = str(freqpoints[i])
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]
		freqpointsum = midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4]
		answer = rounddp((midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]),2)
		for i in range (0,5):
			if midpoints[i]%1==0:
				midpoints[i] = str(int(midpoints[i]))
			else:
				midpoints[i] = str(midpoints[i])
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]
		if answer%1==0:
			answer = int(answer)
		for i in range(0,5):
			freqs[i] = str(freqs[i])
			midpoints[i] = str(midpoints[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{3.5cm} | M{2cm} |  M{2.5cm} | M{2.5cm} |} \\hline Score & Frequency & & \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " & & \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " & & \\\\ \\hline " + scores[2] + " & " + freqs[2] + " & & \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " & & \\\\ \\hline " + scores[4] + " & " + freqs[4] + " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{3.5cm} | M{2cm} |  M{2.5cm} | M{2.5cm} |} \\hline Score & Frequency & Midpoint & Frequency $\\times$ Midpoint \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " & " + midpoints[0] + " & " + freqpoints[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " & " + midpoints[1] + " & " + freqpoints[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " & " + midpoints[2] + " & " + freqpoints[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " & " + midpoints[3] + " & " + freqpoints[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " & " + midpoints[4] + " & " + freqpoints[4] + " \\\\ \\hline \\end{tabular}"
		#first column used to be 3cm, increased to 3.5 for year 9 live lesson, but may need to be reverted for gym
		nl = " \\\\[0.3cm] "
		question = explanation + "\\begin{center}" + table + "\\end{center} Explain why it is not possible to use the information from this table to calculate the exact value of the mean score."
		answer = "\\begin{center}" + atable + "\\\\[0.3cm]" + str(freqpointsum) + " $\\div$ " + str(freqsum) + " = " + str(answer) + "\\end{center} Exact scores are not recorded."
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflecty2gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			y = random.randrange(-6,7)
			xs = list(range(-8,9))
			ys = []
			if y>=0:
				for i in range(y,9):
					ys.append(i)
			else:
				for i in range(-8,y+1):
					ys.append(i)
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		Ax = ax
		Bx = bx
		Cx = cx
		Ay = y + y - ay
		By = y + y - by
		Cy = y + y - cy
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if y==0:
			end = "line \\mbox{y = 0} (or x-axis)"
		else:
			end = "line \\mbox{y = $" + str(y) + "$}"

		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.7]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"


		answer = "Reflection in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflectx2gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			x = random.randrange(-6,7)
			ys = list(range(-8,9))
			xs = []
			if x>=0:
				for i in range(x,9):
					xs.append(i)
			else:
				for i in range(-8,x+1):
					xs.append(i)
			ay = random.choice(ys)
			by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			cy = random.choice(ys)
			ax = random.choice(xs)
			if ay==by:
				xs.remove(ax)
				bx = random.choice(xs)
				xs.append(ax)
			else:
				bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			if ay==cy:
				while ax in xs:
					xs.remove(ax)
				cx = random.choice(xs)
			elif by==cy:
				while bx in xs:
					xs.remove(bx)
				cx = random.choice(xs)
			else:
				cx = random.choice(xs)
		Ay = ay
		By = by
		Cy = cy
		Ax = x + x - ax
		Bx = x + x - bx
		Cx = x + x - cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if x==0:
			end = "line \\mbox{x = 0} (or y-axis)"
		else:
			end = "line \\mbox{x = $" + str(x) + "$}"

		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"

		answer = "Reflection in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectyx2gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = x}"
			ys = []
			if ax==8:
				ay = 8
			else:
				for i in range(ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==8:
				by = 8
			else:
				for i in range(bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==8:
				cy = 8
			else:
				for i in range(cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = ay
		Bx = by
		Cx = cy
		Ay = ax
		By = bx
		Cy = cx
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectynegx2gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==-8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==-8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = $-$x}"
	
			ys = []
			if ax==-8:
				ay = 8
			else:
				for i in range(-ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==-8:
				by = 8
			else:
				for i in range(-bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==-8:
				cy = 8
			else:
				for i in range(-cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = -ay
		Bx = -by
		Cx = -cy
		Ay = -ax
		By = -bx
		Cy = -cx
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describerotate902gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = ydist
		nydist = -xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = ydist
		nydist = -xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = ydist
		nydist = -xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describerotate1802gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		if direction==0:
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2:
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "180\\mydeg"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -xdist
		nydist = -ydist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -xdist
		nydist = -ydist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -xdist
		nydist = -ydist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describerotate90ac2gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg anti-clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -ydist
		nydist = xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -ydist
		nydist = xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -ydist
		nydist = xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describetranslate2gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

		xtop = random.randrange(7,10)
		ytop = random.randrange(7,10)
		xbottom = xtop - 15
		ybottom = ytop - 15
		xs = list(range(xbottom,xtop))
		ys = list(range(ybottom,ytop))
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		xs = sorted([ax,bx,cx])
		ys = sorted([ay,by,cy])
		xmax = 8 - xs[2]
		xmin = -8 - xs[0]
		ymax = 8 - ys[2]
		ymin = -8 - ys[0]
		xs = list(range(xmin,xmax+1))
		ys = list(range(ymin,ymax+1))
		vx = random.choice(xs)
		if vx==0:
			if 0 in ys:
				ys.remove(0)
		vy = random.choice(ys)
		Ax = ax + vx
		Bx = bx + vx
		Cx = cx + vx
		Ay = ay + vy
		By = by + vy
		Cy = cy + vy
		vector = "\\Large{$\\left(\\begin{smallmatrix}" + str(vx) + "\\\\" + str(vy) + "\\end{smallmatrix}\\right)$}"
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
#create question
		answer = "Translation by " + vector
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describeenlargepos2gym(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)


			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def describeenlargeposfrac2gym(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		sf = "$\\dfrac{1}{" + str(sf) + "}$"
		aax = (ax+8)*0.4203125 + 0.135
		aay = (ay+8)*0.42 + 0.18
		bbx = (bx+8)*0.4203125 + 0.135
		bby = (by+8)*0.42 + 0.18
		ccx = (cx+8)*0.4203125 + 0.135
		ccy = (cy+8)*0.42 + 0.18
		AAx = (Ax+8)*0.4203125 + 0.135
		AAy = (Ay+8)*0.42 + 0.18
		BBx = (Bx+8)*0.4203125 + 0.135
		BBy = (By+8)*0.42 + 0.18
		CCx = (Cx+8)*0.4203125 + 0.135
		CCy = (Cy+8)*0.42 + 0.18
		ax = AAx
		bx = BBx
		cx = CCx
		ay = AAy
		by = BBy
		cy = CCy
		Ay = aay
		By = bby
		Cy = ccy
		Ax = aax
		Bx = bbx
		Cx = ccx
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describeenlargeneg2gym(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = list(range(-4,5))
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(1,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$" + str(0 - sf) + "$"
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describeenlargenegfrac2gym(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-4,-3,-2,2,3,4,1,-1]
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$-\\dfrac{1}{" + str(sf) + "}$"
		aax = (ax+8)*0.4203125 + 0.135
		aay = (ay+8)*0.42 + 0.18
		bbx = (bx+8)*0.4203125 + 0.135
		bby = (by+8)*0.42 + 0.18
		ccx = (cx+8)*0.4203125 + 0.135
		ccy = (cy+8)*0.42 + 0.18
		AAx = (Ax+8)*0.4203125 + 0.135
		AAy = (Ay+8)*0.42 + 0.18
		BBx = (Bx+8)*0.4203125 + 0.135
		BBy = (By+8)*0.42 + 0.18
		CCx = (Cx+8)*0.4203125 + 0.135
		CCy = (Cy+8)*0.42 + 0.18
		ax = AAx
		bx = BBx
		cx = CCx
		ay = AAy
		by = BBy
		cy = CCy
		Ay = aay
		By = bby
		Cy = ccy
		Ax = aax
		Bx = bbx
		Cx = ccx
		
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)






def gymreflect(n,explanationn):
	import random
	from fractions import Fraction
	from utilities.transformations import choosetriangle,choosetrianglediag,drawtriangle,reflectorvertical,reflectorhorizontal,reflectordiagonal
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		chooser = random.randrange(0,3)
		if chooser==0: #vertical reflect in y = n
			reflectline = random.randrange(-4,5)
			height = min(8-reflectline,abs(-8-reflectline))
			xmin = -8
			xmax = 8
			if random.randrange(0,2)==1:
				ymin = reflectline - height
				ymax = reflectline
			else:
				ymax = reflectline + height
				ymin = reflectline
			qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
			atriangle = reflectorvertical(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],reflectline)
			intro = "Reflect the triangle in the line y = " + str(reflectline) + "."
		elif chooser==1: #horizontal reflect
			reflectline = random.randrange(-4,5)
			height = min(8-reflectline,abs(-8-reflectline))
			ymin = -8
			ymax = 8
			if random.randrange(0,2)==1:
				xmin = reflectline - height
				xmax = reflectline
			else:
				xmax = reflectline + height
				xmin = reflectline
			qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
			atriangle = reflectorhorizontal(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],reflectline)
			intro = "Reflect the triangle in the line x = " + str(reflectline) + "."
		else: #diagonal
			reflectline = (-1)**random.randrange(1,3)
			qtriangle = list(choosetrianglediag(reflectline))
			atriangle = reflectordiagonal(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],reflectline)
			if reflectline==-1:
				sign = "-"
			else:
				sign = ""
			intro = "Reflect the triangle in the line y = " + sign + "x."
			
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])

		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymrotate(n,explanationn):
	import random
	from fractions import Fraction
	from utilities.transformations import choosetriangle,drawtriangle,rotator
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		squarelength = random.randrange(3,8)*2
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		centre = [int((squareleft + squareright)/2),int((squaretop + squarebottom)/2)]
		if random.randrange(0,2)==1:
			ymax = squaretop
			ymin = centre[1]
		else:
			ymax = centre[1]
			ymin = squarebottom
		if random.randrange(0,2)==1:
			xmax = squareright
			xmin = centre[0]
		else:
			xmax = centre[0]
			xmin = squareleft
		angles = [90,-90,180]
		angle = random.choice(angles)
		
		
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = rotator(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],angle,centre[0],centre[1])
		if angle==90:
			direction = "clockwise"
		elif angle==180:
			direction = ""
		else:
			angle = 90
			direction = "anti-clockwise"
		intro = "Rotate the triangle " + str(angle) + "\\mydeg \\hspace{0.1cm}" + direction + " about centre (" + str(centre[0]) + " , " + str(centre[1]) + ")."

		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5],centre[0],centre[1])
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def gymtranslate(n,explanationn):
	import random
	from utilities.transformations import choosetriangle,drawtriangle,translator
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		xmax = 8 - 8 * random.randrange(0,2)
		xmin = xmax - 8	
		ymax = 8 - 8 * random.randrange(0,2)
		ymin = ymax - 8	
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		trileft = min(qtriangle[0],qtriangle[2],qtriangle[4])
		triright = max(qtriangle[0],qtriangle[2],qtriangle[4])
		tritop = max(qtriangle[1],qtriangle[3],qtriangle[5])
		tribottom = min(qtriangle[1],qtriangle[3],qtriangle[5])
		vxmin = -8 - xmin
		vxmax = 8 - xmax
		vymin = -8 - ymin
		vymax = 8 - ymax
		vx = random.randrange(vxmin,vxmax+1)
		vylist = list(range(vymin,vymax+1))
		if abs(vx) < abs(triright - trileft):
			for i in range(0,abs(tritop - tribottom)):
				if i in vylist:
					vylist.remove(i)
				if -i in vylist:
					vylist.remove(-i)
		if vx in vylist:
			vylist.remove(vx)
		vy = random.choice(vylist)
		atriangle = translator(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],vx,vy)
		vector = "\\Large{$\\left(\\begin{smallmatrix}" + str(vx) + "\\\\" + str(vy) + "\\end{smallmatrix}\\right)$}"
		intro = "Translate the triangle by vector " + vector + "."

		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymenlargepos(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(2,5)
		#identify square in which enlargement will take place
		squarelength = sf * random.randrange(2,floor(15/sf)+1)
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side the centre will be
		centredist = sf * random.randrange(0,squarelength/sf +1)
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find centre
		if corner==0:
			centrex = squareleft
			centrey = squarebottom + centredist
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop
		elif corner==2:
			centrex = squareright
			centrey = squaretop - centredist
		else:
			centrex = squareright - centredist
			centrey = squarebottom
		#find corner coords of small square, make into x/y min/max
		smallsquare = enlarger(squareleft,squarebottom,squareleft,squaretop,squareright,squarebottom,centrex,centrey,1/sf,squareright,squaretop)
		xmin = smallsquare[0]
		xmax = smallsquare[4]
		ymin = smallsquare[1]
		ymax = smallsquare[3]
		#adjust one of them so centre doesn't touch triangle
		if corner==0:
			xmin += 1
		elif corner==1:
			ymax -= 1
		elif corner==2:
			xmax -= 1
		else:
			ymin += 1
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		intro = "Enlarge the triangle by scale factor " + str(sf) + " at centre (" + str(centrex) + " , " + str(centrey) + ")."

		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5],centrex,centrey)
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymenlargeneg(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(1,5)
		#identify square in which enlargement will take place
		squarelength = (sf+1) * random.randrange(2,floor(14/(sf+1))+1)   #might be wrong
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side (inset by small square side length) the centre will be
		smallsquarelength = squarelength/(sf+1)
		medsquarelength = smallsquarelength * sf
		numberofcentres = squarelength - medsquarelength
		centredistgap = (squarelength - 2*smallsquarelength) / (numberofcentres-1)
		centredists = [squarelength - smallsquarelength]
#		q = smallsquarelength
#		while q not in centredists:
#			centredists.append(q)
#			q += centredistgap
#		centredists = sorted(centredists)
		
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find 'top' of med square ('top' rotates dependong on chosen corner)
		medtopgap = random.randrange(0,squarelength-medsquarelength + 1)
		smallbottomgap = medtopgap * sf
		medtopsmallbottomdist = squarelength - medtopgap - smallbottomgap
		centredist = squarelength - medtopgap - (sf/(sf+1))*medtopsmallbottomdist
		#find centre
		if corner==0:
			centrex = squareleft + smallsquarelength
			centrey = squarebottom + centredist
			xmin = centrex
			xmax = xmin + medsquarelength
			ymax = squaretop - medtopgap
			ymin = ymax - medsquarelength
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop - smallsquarelength
			ymax = centrey
			ymin = ymax - medsquarelength
			xmin = squareleft + smallsquarelength
			xmax = squareright - medtopgap
		elif corner==2:
			centrex = squareright - smallsquarelength
			centrey = squaretop - centredist
			xmax = centrex
			xmin = xmax - medsquarelength
			ymin = squarebottom + medtopgap
			ymax = ymin + medsquarelength
		else:
			centrex = squareright - centredist
			centrey = squarebottom + smallsquarelength
			ymin = centrey
			ymax = centrey + medsquarelength
			xmin = squareleft + medtopgap
			xmax = xmin + medsquarelength
		#that was med triangle square, frac enlarge to find small square
		sf *= -1
		smallsquare = enlarger(xmin,ymin,xmin,ymax,xmax,ymin,centrex,centrey,1/sf,xmax,ymax)
		#remember it all flipped roun
		xmin = int(smallsquare[4])
		xmax = int(smallsquare[0])
		ymin = int(smallsquare[3])
		ymax = int(smallsquare[1])


		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		intro = "Enlarge the triangle by scale factor " + str(sf) + " at centre (" + str(int(centrex)) + " , " + str(int(centrey)) + ")."

		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5],centrex,centrey)
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def gymenlargeposfrac(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(2,5)
		#identify square in which enlargement will take place
		squarelength = sf * random.randrange(2,floor(15/sf)+1)
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side the centre will be
		centredist = sf * random.randrange(0,squarelength/sf +1)
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find centre
		if corner==0:
			centrex = squareleft
			centrey = squarebottom + centredist
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop
		elif corner==2:
			centrex = squareright
			centrey = squaretop - centredist
		else:
			centrex = squareright - centredist
			centrey = squarebottom
		#find corner coords of small square, make into x/y min/max
		smallsquare = enlarger(squareleft,squarebottom,squareleft,squaretop,squareright,squarebottom,centrex,centrey,1/sf,squareright,squaretop)
		xmin = smallsquare[0]
		xmax = smallsquare[4]
		ymin = smallsquare[1]
		ymax = smallsquare[3]
		#adjust one of them so centre doesn't touch triangle
		if corner==0:
			xmin += 1
		elif corner==1:
			ymax -= 1
		elif corner==2:
			xmax -= 1
		else:
			ymin += 1
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		qtriangle,atriangle = atriangle,qtriangle
		intro = "Enlarge the triangle by scale factor $\\dfrac{1}{ " + str(sf) + "}$ at centre (" + str(centrex) + " , " + str(centrey) + ")."

		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5],centrex,centrey)
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymenlargenegfrac(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(1,5)
		#identify square in which enlargement will take place
		squarelength = (sf+1) * random.randrange(2,floor(14/(sf+1))+1)   #might be wrong
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side (inset by small square side length) the centre will be
		smallsquarelength = squarelength/(sf+1)
		medsquarelength = smallsquarelength * sf
		numberofcentres = squarelength - medsquarelength
		centredistgap = (squarelength - 2*smallsquarelength) / (numberofcentres-1)
		centredists = [squarelength - smallsquarelength]
#		q = smallsquarelength
#		while q not in centredists:
#			centredists.append(q)
#			q += centredistgap
#		centredists = sorted(centredists)
		
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find 'top' of med square ('top' rotates dependong on chosen corner)
		medtopgap = random.randrange(0,squarelength-medsquarelength + 1)
		smallbottomgap = medtopgap * sf
		medtopsmallbottomdist = squarelength - medtopgap - smallbottomgap
		centredist = squarelength - medtopgap - (sf/(sf+1))*medtopsmallbottomdist
		#find centre
		if corner==0:
			centrex = squareleft + smallsquarelength
			centrey = squarebottom + centredist
			xmin = centrex
			xmax = xmin + medsquarelength
			ymax = squaretop - medtopgap
			ymin = ymax - medsquarelength
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop - smallsquarelength
			ymax = centrey
			ymin = ymax - medsquarelength
			xmin = squareleft + smallsquarelength
			xmax = squareright - medtopgap
		elif corner==2:
			centrex = squareright - smallsquarelength
			centrey = squaretop - centredist
			xmax = centrex
			xmin = xmax - medsquarelength
			ymin = squarebottom + medtopgap
			ymax = ymin + medsquarelength
		else:
			centrex = squareright - centredist
			centrey = squarebottom + smallsquarelength
			ymin = centrey
			ymax = centrey + medsquarelength
			xmin = squareleft + medtopgap
			xmax = xmin + medsquarelength
		#that was med triangle square, frac enlarge to find small square
		sf *= -1
		smallsquare = enlarger(xmin,ymin,xmin,ymax,xmax,ymin,centrex,centrey,1/sf,xmax,ymax)
		#remember it all flipped roun
		xmin = int(smallsquare[4])
		xmax = int(smallsquare[0])
		ymin = int(smallsquare[3])
		ymax = int(smallsquare[1])


		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		qtriangle,atriangle = atriangle,qtriangle
		intro = "Enlarge the triangle by scale factor $-\\dfrac{1}{ " + str(abs(sf)) + "}$ at centre (" + str(int(centrex)) + " , " + str(int(centrey)) + ")."
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5],centrex,centrey)
		answer = str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



#######copy paste all transformations and make into describes



def gymreflectdescribe(n,explanationn):
	import random
	from fractions import Fraction
	from utilities.transformations import choosetriangle,choosetrianglediag,drawtriangle,reflectorvertical,reflectorhorizontal,reflectordiagonal
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		chooser = random.randrange(0,3)
		if chooser==0: #vertical reflect in y = n
			reflectline = random.randrange(-4,5)
			height = min(8-reflectline,abs(-8-reflectline))
			xmin = -8
			xmax = 8
			if random.randrange(0,2)==1:
				ymin = reflectline - height
				ymax = reflectline
			else:
				ymax = reflectline + height
				ymin = reflectline
			qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
			atriangle = reflectorvertical(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],reflectline)
			intro = "Reflected in the line y = " + str(reflectline) + "."
		elif chooser==1: #horizontal reflect
			reflectline = random.randrange(-4,5)
			height = min(8-reflectline,abs(-8-reflectline))
			ymin = -8
			ymax = 8
			if random.randrange(0,2)==1:
				xmin = reflectline - height
				xmax = reflectline
			else:
				xmax = reflectline + height
				xmin = reflectline
			qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
			atriangle = reflectorhorizontal(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],reflectline)
			intro = "Reflected in the line x = " + str(reflectline) + "."
		else: #diagonal
			reflectline = (-1)**random.randrange(1,3)
			qtriangle = list(choosetrianglediag(reflectline))
			atriangle = reflectordiagonal(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],reflectline)
			if reflectline==-1:
				sign = "-"
			else:
				sign = ""
			intro = "Reflected in the line y = " + sign + "x."
		answer = intro	
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])

		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymrotatedescribe(n,explanationn):
	import random
	from fractions import Fraction
	from utilities.transformations import choosetriangle,drawtriangle,rotator
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		squarelength = random.randrange(3,8)*2
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		centre = [int((squareleft + squareright)/2),int((squaretop + squarebottom)/2)]
		if random.randrange(0,2)==1:
			ymax = squaretop
			ymin = centre[1]
		else:
			ymax = centre[1]
			ymin = squarebottom
		if random.randrange(0,2)==1:
			xmax = squareright
			xmin = centre[0]
		else:
			xmax = centre[0]
			xmin = squareleft
		angles = [90,-90,180]
		angle = random.choice(angles)
		
		
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = rotator(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],angle,centre[0],centre[1])
		if angle==90:
			direction = "clockwise"
		elif angle==180:
			direction = ""
		else:
			angle = 90
			direction = "anti-clockwise"
		intro = "Rotated " + str(angle) + "\\mydeg \\hspace{0.1cm}" + direction + " about centre (" + str(centre[0]) + " , " + str(centre[1]) + ")."
		answer = intro
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def gymtranslatedescribe(n,explanationn):
	import random
	from utilities.transformations import choosetriangle,drawtriangle,translator
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		xmax = 8 - 8 * random.randrange(0,2)
		xmin = xmax - 8	
		ymax = 8 - 8 * random.randrange(0,2)
		ymin = ymax - 8	
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		trileft = min(qtriangle[0],qtriangle[2],qtriangle[4])
		triright = max(qtriangle[0],qtriangle[2],qtriangle[4])
		tritop = max(qtriangle[1],qtriangle[3],qtriangle[5])
		tribottom = min(qtriangle[1],qtriangle[3],qtriangle[5])
		vxmin = -8 - xmin
		vxmax = 8 - xmax
		vymin = -8 - ymin
		vymax = 8 - ymax
		vx = random.randrange(vxmin,vxmax+1)
		vylist = list(range(vymin,vymax+1))
		if abs(vx) < abs(triright - trileft):
			for i in range(0,abs(tritop - tribottom)):
				if i in vylist:
					vylist.remove(i)
				if -i in vylist:
					vylist.remove(-i)
		if vx in vylist:
			vylist.remove(vx)
		vy = random.choice(vylist)
		atriangle = translator(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],vx,vy)
		vector = "\\Large{$\\left(\\begin{smallmatrix}" + str(vx) + "\\\\" + str(vy) + "\\end{smallmatrix}\\right)$}"
		intro = "Translated by vector " + vector + "."
		answer = intro
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymenlargeposdescribe(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(2,5)
		#identify square in which enlargement will take place
		squarelength = sf * random.randrange(2,floor(15/sf)+1)
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side the centre will be
		centredist = sf * random.randrange(0,squarelength/sf +1)
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find centre
		if corner==0:
			centrex = squareleft
			centrey = squarebottom + centredist
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop
		elif corner==2:
			centrex = squareright
			centrey = squaretop - centredist
		else:
			centrex = squareright - centredist
			centrey = squarebottom
		#find corner coords of small square, make into x/y min/max
		smallsquare = enlarger(squareleft,squarebottom,squareleft,squaretop,squareright,squarebottom,centrex,centrey,1/sf,squareright,squaretop)
		xmin = smallsquare[0]
		xmax = smallsquare[4]
		ymin = smallsquare[1]
		ymax = smallsquare[3]
		#adjust one of them so centre doesn't touch triangle
		if corner==0:
			xmin += 1
		elif corner==1:
			ymax -= 1
		elif corner==2:
			xmax -= 1
		else:
			ymin += 1
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		intro = "Enlarged by scale factor " + str(sf) + " at centre (" + str(centrex) + " , " + str(centrey) + ")."
		answer = intro
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def gymenlargenegdescribe(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(1,5)
		#identify square in which enlargement will take place
		squarelength = (sf+1) * random.randrange(2,floor(14/(sf+1))+1)   #might be wrong
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side (inset by small square side length) the centre will be
		smallsquarelength = squarelength/(sf+1)
		medsquarelength = smallsquarelength * sf
		numberofcentres = squarelength - medsquarelength
		centredistgap = (squarelength - 2*smallsquarelength) / (numberofcentres-1)
		centredists = [squarelength - smallsquarelength]
#		q = smallsquarelength
#		while q not in centredists:
#			centredists.append(q)
#			q += centredistgap
#		centredists = sorted(centredists)
		
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find 'top' of med square ('top' rotates dependong on chosen corner)
		medtopgap = random.randrange(0,squarelength-medsquarelength + 1)
		smallbottomgap = medtopgap * sf
		medtopsmallbottomdist = squarelength - medtopgap - smallbottomgap
		centredist = squarelength - medtopgap - (sf/(sf+1))*medtopsmallbottomdist
		#find centre
		if corner==0:
			centrex = squareleft + smallsquarelength
			centrey = squarebottom + centredist
			xmin = centrex
			xmax = xmin + medsquarelength
			ymax = squaretop - medtopgap
			ymin = ymax - medsquarelength
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop - smallsquarelength
			ymax = centrey
			ymin = ymax - medsquarelength
			xmin = squareleft + smallsquarelength
			xmax = squareright - medtopgap
		elif corner==2:
			centrex = squareright - smallsquarelength
			centrey = squaretop - centredist
			xmax = centrex
			xmin = xmax - medsquarelength
			ymin = squarebottom + medtopgap
			ymax = ymin + medsquarelength
		else:
			centrex = squareright - centredist
			centrey = squarebottom + smallsquarelength
			ymin = centrey
			ymax = centrey + medsquarelength
			xmin = squareleft + medtopgap
			xmax = xmin + medsquarelength
		#that was med triangle square, frac enlarge to find small square
		sf *= -1
		smallsquare = enlarger(xmin,ymin,xmin,ymax,xmax,ymin,centrex,centrey,1/sf,xmax,ymax)
		#remember it all flipped roun
		xmin = int(smallsquare[4])
		xmax = int(smallsquare[0])
		ymin = int(smallsquare[3])
		ymax = int(smallsquare[1])


		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		intro = "Enlarged by scale factor " + str(sf) + " at centre (" + str(int(centrex)) + " , " + str(int(centrey)) + ")."
		answer = intro
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def gymenlargeposfracdescribe(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(2,5)
		#identify square in which enlargement will take place
		squarelength = sf * random.randrange(2,floor(15/sf)+1)
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side the centre will be
		centredist = sf * random.randrange(0,squarelength/sf +1)
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find centre
		if corner==0:
			centrex = squareleft
			centrey = squarebottom + centredist
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop
		elif corner==2:
			centrex = squareright
			centrey = squaretop - centredist
		else:
			centrex = squareright - centredist
			centrey = squarebottom
		#find corner coords of small square, make into x/y min/max
		smallsquare = enlarger(squareleft,squarebottom,squareleft,squaretop,squareright,squarebottom,centrex,centrey,1/sf,squareright,squaretop)
		xmin = smallsquare[0]
		xmax = smallsquare[4]
		ymin = smallsquare[1]
		ymax = smallsquare[3]
		#adjust one of them so centre doesn't touch triangle
		if corner==0:
			xmin += 1
		elif corner==1:
			ymax -= 1
		elif corner==2:
			xmax -= 1
		else:
			ymin += 1
		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		qtriangle,atriangle = atriangle,qtriangle
		intro = "Enlarged by scale factor $\\dfrac{1}{ " + str(sf) + "}$ at centre (" + str(centrex) + " , " + str(centrey) + ")."
		answer = intro
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def gymenlargenegfracdescribe(n,explanationn):
	import random
	from math import floor
	from utilities.transformations import choosetriangle,drawtriangle,enlarger
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sf = random.randrange(1,5)
		#identify square in which enlargement will take place
		squarelength = (sf+1) * random.randrange(2,floor(14/(sf+1))+1)   #might be wrong
		squaretop = 8 - random.randrange(0,16-squarelength)
		squarebottom = squaretop - squarelength
		squareright = 8 - random.randrange(0,16-squarelength)
		squareleft = squareright - squarelength
		#the distance into the square along one side (inset by small square side length) the centre will be
		smallsquarelength = squarelength/(sf+1)
		medsquarelength = smallsquarelength * sf
		numberofcentres = squarelength - medsquarelength
		centredistgap = (squarelength - 2*smallsquarelength) / (numberofcentres-1)
		centredists = [squarelength - smallsquarelength]
#		q = smallsquarelength
#		while q not in centredists:
#			centredists.append(q)
#			q += centredistgap
#		centredists = sorted(centredists)
		
		#choose which corner to count in from, clockwise, bottom left = 0
		corner = random.randrange(0,4)
		#find 'top' of med square ('top' rotates dependong on chosen corner)
		medtopgap = random.randrange(0,squarelength-medsquarelength + 1)
		smallbottomgap = medtopgap * sf
		medtopsmallbottomdist = squarelength - medtopgap - smallbottomgap
		centredist = squarelength - medtopgap - (sf/(sf+1))*medtopsmallbottomdist
		#find centre
		if corner==0:
			centrex = squareleft + smallsquarelength
			centrey = squarebottom + centredist
			xmin = centrex
			xmax = xmin + medsquarelength
			ymax = squaretop - medtopgap
			ymin = ymax - medsquarelength
		elif corner==1:
			centrex = squareleft + centredist
			centrey = squaretop - smallsquarelength
			ymax = centrey
			ymin = ymax - medsquarelength
			xmin = squareleft + smallsquarelength
			xmax = squareright - medtopgap
		elif corner==2:
			centrex = squareright - smallsquarelength
			centrey = squaretop - centredist
			xmax = centrex
			xmin = xmax - medsquarelength
			ymin = squarebottom + medtopgap
			ymax = ymin + medsquarelength
		else:
			centrex = squareright - centredist
			centrey = squarebottom + smallsquarelength
			ymin = centrey
			ymax = centrey + medsquarelength
			xmin = squareleft + medtopgap
			xmax = xmin + medsquarelength
		#that was med triangle square, frac enlarge to find small square
		sf *= -1
		smallsquare = enlarger(xmin,ymin,xmin,ymax,xmax,ymin,centrex,centrey,1/sf,xmax,ymax)
		#remember it all flipped roun
		xmin = int(smallsquare[4])
		xmax = int(smallsquare[0])
		ymin = int(smallsquare[3])
		ymax = int(smallsquare[1])


		qtriangle = list(choosetriangle(xmin,xmax,ymin,ymax))
		atriangle = enlarger(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],centrex,centrey,sf)
		qtriangle,atriangle = atriangle,qtriangle
		intro = "Enlarged by scale factor $-\\dfrac{1}{ " + str(abs(sf)) + "}$ at centre (" + str(int(centrex)) + " , " + str(int(centrey)) + ")."
		answer = intro
		#below could be static
		finalqtriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5])
		question = intro + "\\\\ \\centering" +  str(finalqtriangle)
		atriangle = drawtriangle(qtriangle[0],qtriangle[1],qtriangle[2],qtriangle[3],qtriangle[4],qtriangle[5],atriangle[0],atriangle[1],atriangle[2],atriangle[3],atriangle[4],atriangle[5])
		intro = "Describe the single transformation that maps the light triangle onto the dark triangle."
		question = intro + "\\\\ \\centering" + str(atriangle)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
