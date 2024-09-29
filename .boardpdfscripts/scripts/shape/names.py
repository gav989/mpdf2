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
		question = "What is the name of this shape? \\\\[0.3cm]\\hfill\\includegraphics[scale=1]{shape/names/" + image + "}\\hfill"
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
		question = "What is the name of this shape? \\\\[0.3cm]\\hfill\\includegraphics[scale=1]{shape/names/" + image + "}\\hfill"
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
		question = "What is the name of this shape? \\\\[0.3cm]\\hfill\\includegraphics[scale=1]{shape/names/" + image + "}\\hfill"
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
		question = "What is the name of this shape? \\\\[0.3cm]\\hfill\\includegraphics[scale=1]{shape/names/" + image + "}\\hfill"
		if shape=="triangularprism":
			shape = "triangular prism"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(shape)