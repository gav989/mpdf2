#fracneg.py

def fracindices1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		den = random.randrange(2,4)
		if den==2:
			selection=list(range(2,16))
		else:
			selection=(2,3,4,5,10)
		bottom = random.choice(selection)
		base = bottom**den
		num = 1
#write question
		tempquestions.write(explanation + "$" + str(base) + "^{\\frac{" + str(num) + "}{" + str(den) + "}}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(bottom))

def fracindices2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		den = random.randrange(2,4)
		if den==2:
			selection=list(range(2,16))
		else:
			selection=(2,3,4,5,10)
		bottom = random.choice(selection)
		base = bottom**den
		if den==3:
			num = random.randrange(1,3)
		elif den==2 and bottom in (2,3,4,5,10):
			num = 2 + (-1)**random.randrange(1,3)
		else:
			num = 1
		bottom = bottom**num
#write question
		tempquestions.write(explanation + "$" + str(base) + "^{\\frac{" + str(num) + "}{" + str(den) + "}}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(bottom))


def negindices(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		base = random.randrange(2,16)
		if base<6 or base==10:
			index = random.randrange(1,4)
		else:
			index = random.randrange(1,3)
#write question
		tempquestions.write(explanation + "$" + str(base) + "^{-" + str(index) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\frac{1}{" + str(base**index) + "}$")

def negfrac(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		pos = random.randrange(0,2)
		den = random.randrange(2,4)
		if den==2:
			selection=list(range(2,16))
		else:
			selection=(2,3,4,5,10)
		bottom = random.choice(selection)
		base = bottom**den
		if den==3:
			num = random.randrange(1,3)
		elif den==2 and bottom in (2,3,4,5,10):
			num = 2 + (-1)**random.randrange(1,3)
		else:
			num = 1
		bottom = bottom**num
#write question
		if pos==1:
			tempquestions.write(explanation + "$" + str(base) + "^{\\frac{" + str(num) + "}{" + str(den) + "}}$")
		else:
			tempquestions.write(explanation + "$" + str(base) + "^{-\\frac{" + str(num) + "}{" + str(den) + "}}$")
		tempquestions.write("\n")
#write answer
		if pos==1:
			tempquestions.write(str(bottom))
		else:
			tempquestions.write("$\\frac{1}{" + str(bottom) + "}$")
