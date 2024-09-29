#names.py

def quadrilaterals(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		quads = ["square","rectangle","kite","rhombus","parallelogram","trapezium"]
		quad = random.choice(quads)
		image = quad
		question = "What is the name of this shape? \\\\[0.3cm]\\centering\\includegraphics[scale=1]{shape/names/" + image + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(quad)


def polygons(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		polygons = ["pentagon","hexagon","octagon"]
		polygon = random.choice(polygons)
		image = polygon
		question = "What is the name of this shape? \\\\[0.3cm]\\centering\\includegraphics[scale=1]{shape/names/" + image + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(polygon)


def triangles(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		triangles = ["equilateral","isosceles","scalene","right-angled"]
		triangle = random.choice(triangles)
		image = triangle
		question = "What is the name of this shape? \\\\[0.3cm]\\centering\\includegraphics[scale=1]{shape/names/" + image + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(triangle + " triangle")

def threed(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		shapes = ["cone","pyramid","sphere","cylinder","triangularprism","cube","cuboid"]
		shape = random.choice(shapes)
		image = shape
		question = "What is the name of this shape? \\\\[0.3cm]\\centering\\includegraphics[scale=1]{shape/names/" + image + "}"
		if shape=="triangularprism":
			shape = "triangular prism"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(shape)



def quadrilateralsstarter(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		quads = ["square","rectangle","kite","rhombus","parallelogram","trapezium"]
		quad = random.choice(quads)
		image = quad
		question = "\\centering\\includegraphics[scale=0.35]{shape/names/" + image + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(quad)


def polygonsstarter(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		polygons = ["pentagon","hexagon","octagon"]
		polygon = random.choice(polygons)
		image = polygon
		question = "\\centering\\includegraphics[scale=0.3]{shape/names/" + image + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(polygon)


def trianglesstarter(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		triangles = ["equilateral","isosceles","scalene","right-angled"]
		triangle = random.choice(triangles)
		image = triangle
		question = "\\centering\\includegraphics[scale=0.35]{shape/names/" + image + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(triangle + " triangle")

def threedstarter(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		shapes = ["cone","pyramid","sphere","cylinder","triangularprism","cube","cuboid"]
		shape = random.choice(shapes)
		image = shape
		question = "\\centering\\includegraphics[scale=0.35]{shape/names/" + image + "}"
		if shape=="triangularprism":
			shape = "triangular prism"
		if shape=="pyramid":
			shape = "(square based) pyramid"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(shape)

def symmetrystarter(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		shapes = ["symmetry1","symmetry2","symmetry3","symmetry4","symmetry5","symmetry6","symmetry7","symmetry8","symmetry9","symmetry10","symmetry11","symmetry12"]
		lines = [4,3,4,5,5,2,0,1,2,0,1,0]
		rotates = [4,3,4,5,5,2,2,0,2,3,0,4]
		choice = random.randrange(0,len(shapes))
		shape = shapes[choice]
		line = str(lines[choice])
		rotate = str(rotates[choice])

		image = "\\centering\\includegraphics[scale=0.45]{shape/images/" + shape + "}"
		questiona = "\\raggedright a) How many lines of symmetry does this shape have?"
		questionb = "b) What order of rotational symmetry does this shape have?"
		nl = "\\\\[0.1cm]"
		question = image + nl + questiona + nl + questionb
		answer = "a) " + line + nl + "b) " + rotate
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circlepartsstarter(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		rot = random.randrange(0,4)*90
		image2 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts2}"
		image3 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts3}"
		image4 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts4}"
		image5 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts5}"
		image6 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts6}"
		image7 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts7}"
		image8 = "\\centering\\includegraphics[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts8}"
		images = [image2,image3,image4,image5,image6,image7,image8]
		labels = ["A","B","C","D","E","F","G"]
		if rot==0:
			coords = ["11,81","64,91","89,72","57,24","75,47","17,10","84,4"]
		elif rot==90:
			coords = ["12,10","2,65","20,89","68,56","48,75","82,17","89,84"]
		elif rot==180:
			coords = ["82,12","29,1","4,20","37,68","18,49","76,82","9,89"]
		else:
			coords = ["81,82","91,29","72,4","24,37","46,17.5","11,77","4,9"]
		answers = ["Radius","Diameter","Circumference","Sector","Segment","Chord","Tangent"]
		order = list(range(0,7))
		random.shuffle(order)
		if rot>100:
			for i in range(0,len(images)):
				images[i] = "\\put(0,100){" + images[i] + "}"
		else:
			for i in range(0,len(images)):
				images[i] = "\\put(0,0){" + images[i] + "}"
		image = "\\centering\\begin{overpic}[scale=0.92,angle = " + str(rot) + "]{shape/names/circleparts1} "
		for i in range(0,4):
			image = image + images[order[i]]
			image = image + "\\put(" + coords[order[i]] + "){" + labels[i] + "}"
		image = image + " \\end{overpic}"
		question = image
		nl = "\\\\[0.3cm]"
		answer = "A = " + answers[order[0]] + nl + "B = " + answers[order[1]] + nl + "C = " + answers[order[2]] + nl + "D = " + answers[order[3]]
#write question
		tempquestions.write("Identify the parts of this circle:\\\\" + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def edgesverticesfaces(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		shapes = ["pyramid","triangularprism","cube","cuboid"]
		edges = ["8","9","12","12"]
		vertices = ["5","6","8","8"]
		faces = ["5","5","6","6"]
		choice = random.randrange(0,len(shapes))
		shape = shapes[choice]
		edges = edges[choice]
		vertices = vertices[choice]
		faces = faces[choice]
		image = "\\centering\\includegraphics[scale=0.5]{shape/names/" + shape + "}"
		if shape=="triangularprism":
			shape = "triangular prism"
		if shape=="pyramid":
			shape = "square based pyramid"
		l1 = "\\raggedright A " + shape + " has:"
		l2 = "$\\rule[-1.5mm]{1cm}{0.15mm}$ edges"
		l3 = "$\\rule[-1.5mm]{1cm}{0.15mm}$ vertices"
		l4 = "$\\rule[-1.5mm]{1cm}{0.15mm}$ faces"
		nl = "\\\\[0.05cm]"
		question = image + nl + l1 + nl + l2 + nl + l3 + nl + l4
		l2 = "$\\underline{" + edges + "}$ edges"
		l3 = "$\\underline{" + vertices + "}$ vertices"
		l4 = "$\\underline{" + faces + "}$ faces"

		answer = image + nl + l1 + nl + l2 + nl + l3 + nl + l4
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
