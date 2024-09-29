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
