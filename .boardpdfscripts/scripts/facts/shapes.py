#!/usr/bin/env python3
#fmp.py


def triangles(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"What is the name of a triangle with no equal sides?",
			"What is the name of a triangle with two equal sides?",
			"What is the name of a triangle with three equal sides?"]

		answers = [
			"Scalene",
			"Isosceles",
			"Equilateral"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def polygons(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"What is the name of a shape with 5 sides?",
			"What is the name of a shape with 6 sides?",
			"What is the name of a shape with 8 sides?"]

		answers = [
			"Pentagon",
			"Hexagon",
			"Octagon"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadrilaterals(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"Which quadrilateral has four equal sides and four right angles?",
			"Which quadrilateral has four equal sides and two lines of symmetry?",
			"Which quadrilateral has two pairs of equal angles, two pairs of parallel lines and no lines of symmetry?",
			"Which quadrilateral has four right angles and two lines of symmetry?",
			"Which quadrilateral has two pairs of equal adjacent sides and no reflex angles?",
			"Which quadrilateral has only one pair of parallel sides?"]

		answers = [
			"Square",
			"Rhombus",
			"Parallelogram",
			"Rectangle",
			"Kite",
			"Trapezium"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadrilateralsymmetry(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"How many lines of symmetry does a square have?",
			"How many lines of symmetry does a rectangle have?",
			"How many lines of symmetry does a rhombus have?",
			"How many lines of symmetry does a parallelogram have?",
			"How many lines of symmetry does a kite have?",
			"How many lines of symmetry does a trapezium have?"]

		answers = [
			"4",
			"2",
			"2",
			"0",
			"1",
			"Sometimes 1"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circleformulae(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"What is the formula for finding the area of a circle?",
			"What is the formula for finding the circumference of a circle?"]

		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"


		answers = [
			pi + "$\\times r \\times r$",
			pi + "$\\times D$"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def metricconversions(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"What is the conversion between millimetres and centimetres?",
			"What is the conversion between centimetres and millimetres?",
			"What is the conversion between centimetres and metres?",
			"What is the conversion between metres and centimetres?",
			"What is the conversion between metres and kilometres?",
			"What is the conversion between kilometres and metres?",
			"What is the conversion between milligrams and grams?",
			"What is the conversion between grams and milligrams?",
			"What is the conversion between grams and kilograms?",
			"What is the conversion between kilograms and grams?",
			"What is the conversion between kilograms and tonnes?",
			"What is the conversion between tonnes and kilograms?",
			"What is the conversion between litres and millilitres?",
			"What is the conversion between millilitres and litres?"]

		answers = [
			"1 cm = 10 mm",
			"1 cm = 10 mm",
			"1 m = 100 cm",
			"1 m = 100 cm",
			"1 km = 1000 m",
			"1 km = 1000 m",
			"1 g = 1000 mg",
			"1 g = 1000 mg",
			"1 kg = 1000 g",
			"1 kg = 1000 g",
			"1 t = 1000 kg",
			"1 t = 1000 kg",
			"1 l = 1000 ml",
			"1 l = 1000 ml"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def metricunits(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"Which metric unit would you use to measure the length of a football pitch?",
			"Which metric unit would you use to measure the length of a car?",
			"Which metric unit would you use to measure the length of a ferry?",
			"Which metric unit would you use to measure the length of this room?",
			"Which metric unit would you use to measure the length of a pen?",
			"Which metric unit would you use to measure the length of a pencil?",
			"Which metric unit would you use to measure the length of your foot?",
			"Which metric unit would you use to measure the diameter of a cake?",
			"Which metric unit would you use to measure the distance from here to London?",
			"Which metric unit would you use to measure the distance from here to Brazil?",
			"Which metric unit would you use to measure the distance from here to the moon?",
			"Which metric unit would you use to measure the distance from the moon to the sun?",
			"Which metric unit would you use to measure the mass of an apple?",
			"Which metric unit would you use to measure the mass of a mug?",
			"Which metric unit would you use to measure the mass of a phone?",
			"Which metric unit would you use to measure the mass of a calculator?",
			"Which metric unit would you use to measure the mass of a human?",
			"Which metric unit would you use to measure the mass of a wheelbarrow?",
			"Which metric unit would you use to measure the mass of a dog?",
			"Which metric unit would you use to measure the mass of a teacher?",
			"Which metric unit would you use to measure the mass of a building?",
			"Which metric unit would you use to measure the mass of a boat?",
			"Which metric unit would you use to measure the mass of a van?",
			"Which metric unit would you use to measure the mass of a car?",
			"Which metric unit would you use to measure the capacity of a mug?",
			"Which metric unit would you use to measure the capacity of a can of drink?",
			"Which metric unit would you use to measure the capacity of a water bottle?",
			"Which metric unit would you use to measure the capacity of a cup?",
			"Which metric unit would you use to measure the capacity of a bath?",
			"Which metric unit would you use to measure the capacity of the petrol tank of a car?",
			"Which metric unit would you use to measure the capacity of a swiming pool?",
			"Which metric unit would you use to measure the capacity of a pond?"]

		answers = [
			"Metres",
			"Metres",
			"Metres",
			"Metres",
			"Centimetres",
			"Centimetres",
			"Centimetres",
			"Centimetres",
			"Kilometres",
			"Kilometres",
			"Kilometres",
			"Kilometres",
			"Grams",
			"Grams",
			"Grams",
			"Grams",
			"Kilograms",
			"Kilograms",
			"Kilograms",
			"Kilograms",
			"Tonnes",
			"Tonnes",
			"Tonnes",
			"Tonnes",
			"Millilitres",
			"Millilitres",
			"Millilitres",
			"Millilitres",
			"Litres",
			"Litres",
			"Litres",
			"Litres"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def threedshapes(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""

		questions = [
			"What mathematical shape is a Pringles tube?",
			"What mathematical shape is a ball?",
			"What mathematical shape is a Toblerone?",
			"What mathematical shape is a cereal box?",
			"What mathematical shape is an ice cream cone?",
			"What mathematical shape is a dice?"]

		answers = [
			"Cylinder",
			"Sphere",
			"Triangular Prism",
			"Cuboid",
			"Cone",
			"Cube"]

		dec = random.randrange(0,len(questions))
		question = questions[dec]
		answer = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def exteriorangle1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		words = ["five","six","eight","nine","ten","twelve","twenty"]
		answers = [72,60,45,40,36,30,18]
		dec = random.randrange(0,7)
		question = "Find the size of an exterior angle of a regular polygon with " + words[dec] + " sides."
		answer = str(answers[dec]) + "\\mydeg"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def exteriorangle2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		words = ["five","six","eight","nine","ten","twelve"]
		answers = [72,60,45,40,36,30]
		dec = random.randrange(0,6)
		question = "The exterior angle of a regular polygon is " + str(answers[dec]) + "\\mydeg" + ", how many sides does the polygon have?"
		answer = words[dec]
		
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

