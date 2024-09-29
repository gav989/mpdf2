#fracneg.py

def fracindices1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
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
		question = "$" + str(base) + "^{\\frac{" + str(num) + "}{" + str(den) + "}}$"
#write question
		tempquestions.write(explanation + "\\large " + question + "\\normalsize")
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
			explanation = "Evaluate "
		else:
			explanation = ""
		den = random.randrange(2,4)
		selection=(2,3,4,5,10)
		bottom = random.choice(selection)
		base = bottom**den
		if bottom in (2,10):
			nums = [2,3,4,5,6]
			nums.remove(den)
			num = random.choice(nums)
		elif den==3:
			num = 2
		else:
			num = 3
		bottom = bottom**num
		question = "$" + str(base) + "^{\\frac{" + str(num) + "}{" + str(den) + "}}$"
#write question
		tempquestions.write(explanation + "\\large" + question + "\\normalsize")
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
			explanation = "Evaluate "
		else:
			explanation = ""
		base = random.randrange(2,16)
		if base<6 or base==10:
			index = random.randrange(1,4)
		else:
			index = random.randrange(1,3)
#write question
		tempquestions.write(explanation + "\\large$" + str(base) + "^{-" + str(index) + "}$\\normalsize")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{1}{" + str(base**index) + "}$")



def negfrac(n,explanationn):
#OLD DONT USE
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
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

		if pos==1:
			question = "$" + str(base) + "^{\\frac{" + str(num) + "}{" + str(den) + "}}$"
		else:
			question = "$" + str(base) + "^{-\\frac{" + str(num) + "}{" + str(den) + "}}$"

#write question
		tempquestions.write(explanation + "\\large " + question + "\\normalsize")

		tempquestions.write("\n")
#write answer
		if pos==1:
			tempquestions.write(str(bottom))
		else:
			tempquestions.write("$\\dfrac{1}{" + str(bottom) + "}$")


def negfrac1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
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
		question = "$" + str(base) + "^{-\\frac{" + str(num) + "}{" + str(den) + "}}$"

#write question
		tempquestions.write(explanation + "\\large " + question + "\\normalsize")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{1}{" + str(bottom) + "}$")



def negfrac2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
		else:
			explanation = ""
		den = random.randrange(2,4)
		selection=(2,3,4,5,10)
		bottom = random.choice(selection)
		base = bottom**den
		if bottom in (2,10):
			nums = [2,3,4,5,6]
			nums.remove(den)
			num = random.choice(nums)
		elif den==3:
			num = 2
		else:
			num = 3
		bottom = bottom**num
		question = "$" + str(base) + "^{-\\frac{" + str(num) + "}{" + str(den) + "}}$"

#write question
		tempquestions.write(explanation + "\\large " + question + "\\normalsize")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{1}{" + str(bottom) + "}$")


def fraction1pos(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
		else:
			explanation = ""
		power = random.randrange(2,4)
		nums = [1]
		if power==3:
			dens = list(range(2,6))
			den = random.choice(dens)
			for i in range(2,den):
				if gcd(den,i)==1:
					nums.append(i)
		else:
			dens = list(range(2,16))
			den = random.choice(dens)
			for i in range(2,den):
				if gcd(den,i)==1:
					nums.append(i)
		num = random.choice(nums)
		question = "$\\left(\\dfrac{" + str(num) + "}{" + str(den) + "}\\right)^{" + str(power) + "}$"
		answer = "$\\dfrac{" + str(num**power) + "}{" + str(den**power) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fraction1neg(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
		else:
			explanation = ""
		power = random.randrange(1,4)
		nums = [1]
		if power==3:
			dens = list(range(2,6))
			den = random.choice(dens)
			for i in range(2,den):
				if gcd(den,i)==1:
					nums.append(i)
		else:
			dens = list(range(2,16))
			den = random.choice(dens)
			for i in range(2,den):
				if gcd(den,i)==1:
					nums.append(i)
		num = random.choice(nums)
		power = 0 - power
		question = "$\\left(\\dfrac{" + str(num) + "}{" + str(den) + "}\\right)^{" + str(power) + "}$"
		temp = num
		num = den**abs(power)
		den = temp**abs(power)
		if num%den==0:
			answer = str(int(num/den))
		else:
			integer = floor(num/den)
			num = num - den*integer
			answer = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fraction2pos(n,explanationn):
	import random
	from math import floor
	from math import gcd
	from utilities.rounding import roundnearest
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
		else:
			explanation = ""
		squares = []
		cubes = []
		for i in range(1,6):
			squares.append(i**2)
		for i in range(1,6):
			cubes.append(i**3)
		pden = random.randrange(2,4)
		if random.randrange(0,9)==1:
			if random.randrange(0,2)==1:
				base = 2
			else:
				base = 10
			temp = list(range(2,7))
			pden = random.choice(temp)
			temp.remove(pden)
			pnum = random.choice(temp)
			num = 1
			den = base**pden
		elif pden==2:
			pnum = 2 + (-1)**random.randrange(1,3)
			num = random.choice(squares)
			squares.remove(num)
			if num!=1:
				squares.remove(1)
			den = random.choice(squares)
		else:
			pnum = random.randrange(1,3)
			num = random.choice(cubes)
			cubes.remove(num)
			if num!=1:
				cubes.remove(1)
			den = random.choice(cubes)
		question = "$\\left(\\dfrac{" + str(num) + "}{" + str(den) + "}\\right)^{\\dfrac{" + str(pnum) + "}{" + str(pden) + "}}$"
		num = int(roundnearest(num**(pnum/pden),1))
		den = int(roundnearest(den**(pnum/pden),1))
		if num%den==0:
			answer = str(int(num/den))
		elif num>den:
			integer = floor(num/den)
			num = num - den*integer
			answer = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		else:
			answer = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fraction2neg(n,explanationn):
	import random
	from math import floor
	from math import gcd
	from utilities.rounding import roundnearest
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
		else:
			explanation = ""
		squares = []
		cubes = []
		for i in range(1,6):
			squares.append(i**2)
		for i in range(1,6):
			cubes.append(i**3)
		pden = random.randrange(2,4)
		if random.randrange(0,9)==1:
			if random.randrange(0,2)==1:
				base = 2
			else:
				base = 10
			temp = list(range(2,7))
			pden = random.choice(temp)
			temp.remove(pden)
			pnum = random.choice(temp)
			num = 1
			den = base**pden
		elif pden==2:
			pnum = 2 + (-1)**random.randrange(1,3)
			num = random.choice(squares)
			squares.remove(num)
			if num!=1:
				squares.remove(1)
			den = random.choice(squares)
		else:
			pnum = random.randrange(1,3)
			num = random.choice(cubes)
			cubes.remove(num)
			if num!=1:
				cubes.remove(1)
			den = random.choice(cubes)
		question = "$\\left(\\dfrac{" + str(num) + "}{" + str(den) + "}\\right)^{-\\dfrac{" + str(pnum) + "}{" + str(pden) + "}}$"
		temp = int(roundnearest(num**(pnum/pden),1))
		num = int(roundnearest(den**(pnum/pden),1))
		den = temp
		if num%den==0:
			answer = str(int(num/den))
		elif num>den:
			integer = floor(num/den)
			num = num - den*integer
			answer = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		else:
			answer = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def zero(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Evaluate "
		else:
			explanation = ""
		question = str(random.randrange(1,16)) + "$^{0}$"
		answer = str(1)
#write question
		tempquestions.write(explanation + "\\large" + question + "\\normalsize")

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def writeaspower1(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		bases = [2,3,4,5,10]
		base = random.choice(bases)
		if base==2:
			index = random.randrange(2,6)
		else:
			index = random.randrange(2,4)
		question = str(base**index)
		answer = str(base) + "^{" + str(index) + "}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")



def writeaspower2(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		bases = [2,3,4,5,10]
		base = random.choice(bases)
		if base==2:
			index = random.randrange(2,6)
		else:
			index = random.randrange(2,4)
		index2 = random.randrange(2,10)
		question = str(base**index) + "^{" + str(index2) + "}"
		answer = str(base) + "^{" + str(index*index2) + "}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")



def writeaspower3(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		bases = [2,3,4,5,10]
		base = random.choice(bases)
		if base==2:
			index = random.randrange(2,6)
		else:
			index = random.randrange(2,4)
		question = "\\dfrac{1}{" + str(base**index) + "}"
		answer = str(base) + "^{-" + str(index) + "}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")




def writeaspower4(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		bases = [2,3,4,5,10]
		base = random.choice(bases)
		if base==2:
			index = random.randrange(2,6)
		else:
			index = random.randrange(2,4)
		index2 = random.randrange(2,10)
		question = "\\dfrac{1}{" + str(base**index) + "^{" + str(index2) + "}}"
		answer = str(base) + "^{-" + str(index*index2) + "}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")



def writeaspower5(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		bases = [2,3,5,6,7,10]
		base = random.choice(bases)
		answer = str(base) + "^{\\frac{1}{2}}"
		question = "\\sqrt{" + str(base) + "}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")




def writeaspower6(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		power = random.randrange(2,4)
		if power==3:
			bases = [2,3,4,5]
			roots = [2,4,5,7,8]
		else:
			bases = list(range(2,10))
			roots = [3,5,7,9]
		root = random.choice(roots)
		base = random.choice(bases)
		if root==2:
			question = "\\sqrt{" + str(base**power) + "}"
		else:
			question = "\\sqrt[" + str(root) + "]{" + str(base**power) + "}"
		answer = str(base) + "^{\\frac{" + str(power) + "}{" + str(root) + "}}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")



def writeaspower7(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		bases = [2,3,5,6,7,10]
		base = random.choice(bases)
		answer = str(base) + "^{-\\frac{1}{2}}"
		question = "\\dfrac{1}{\\sqrt{" + str(base) + "}}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")



def writeaspower8(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		power = random.randrange(2,4)
		if power==3:
			bases = [2,3,4,5]
			roots = [2,4,5,7,8]
		else:
			bases = list(range(2,10))
			roots = [3,5,7,9]
		root = random.choice(roots)
		base = random.choice(bases)
		if root==2:
			question = "\\sqrt{" + str(base**power) + "}"
		else:
			question = "\\sqrt[" + str(root) + "]{" + str(base**power) + "}"
		question = "\\dfrac{1}{" + question + "}"
		answer = str(base) + "^{-\\frac{" + str(power) + "}{" + str(root) + "}}"
		question = "$" + question + "$ as a power of " + str(base)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\large$" + answer + "$\\normalsize")



def writeaspowermult(n,explanationn):
	import random
	from math import floor,gcd
	from fractions import Fraction
	from utilities.fractions import simpfrac
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of k when you write "
		else:
			explanation = ""
		check = 0
		while check==0:
			questions = []
			bases = [2,3,4,5,10]
			base = random.choice(bases)

			indexes = []

			choices = list(range(1,9))
			choice1 = random.choice(choices)
			choices.remove(choice1)
			choice2 = random.choice(choices)
			choices = [choice1,choice2]
		#1
			if 1 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				question = str(base**index)
				answer = str(base) + "^{" + str(index) + "}"
				questions.append(question)
				indexes.append(index)
		#2
			if 2 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				index2 = random.randrange(2,10)
				question = str(base**index) + "^{" + str(index2) + "}"
				answer = str(base) + "^{" + str(index*index2) + "}"
				questions.append(question)
				indexes.append(index*index2)
		#3
			if 3 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				question = "\\dfrac{1}{" + str(base**index) + "}"
				answer = str(base) + "^{-" + str(index) + "}"
				questions.append(question)
				indexes.append(0 - index)
		#4
			if 4 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				index2 = random.randrange(2,10)
				question = "\\dfrac{1}{" + str(base**index) + "^{" + str(index2) + "}}"
				answer = str(base) + "^{-" + str(index*index2) + "}"
				questions.append(question)
				indexes.append(0 - index*index2)
		#5
			if 5 in choices:
		#		bases = [2,3,5,6,7,10]
				answer = str(base) + "^{\\frac{1}{2}}"
				question = "\\sqrt{" + str(base) + "}"
				questions.append(question)
				indexes.append(Fraction(1,2))
		#6
			if 6 in choices:
				power = random.randrange(2,4)
				if power==3:
					roots = [2,4,5,7,8]
				else:
					roots = [3,5,7,9]
				root = random.choice(roots)
				if root==2:
					question = "\\sqrt{" + str(base**power) + "}"
				else:
					question = "\\sqrt[" + str(root) + "]{" + str(base**power) + "}"
				answer = str(base) + "^{\\frac{" + str(power) + "}{" + str(root) + "}}"
				questions.append(question)
				indexes.append(Fraction(power,root))
		#7
			if 7 in choices:
				answer = str(base) + "^{-\\frac{1}{2}}"
				question = "\\dfrac{1}{\\sqrt{" + str(base) + "}}"
				questions.append(question)
				indexes.append(Fraction(-1,2))
		#8
			if 8 in choices:
				power = random.randrange(2,4)
				if power==3:
					roots = [2,4,5,7,8]
				else:
					roots = [3,5,7,9]
				root = random.choice(roots)
				if root==2:
					question = "\\sqrt{" + str(base**power) + "}"
				else:
					question = "\\sqrt[" + str(root) + "]{" + str(base**power) + "}"
				question = "\\dfrac{1}{" + question + "}"
				answer = str(base) + "^{-\\frac{" + str(power) + "}{" + str(root) + "}}"
				questions.append(question)
				indexes.append(Fraction(0 - power,root))
#collate
			question = "\\mbox{$" + questions[0] + " \\times " + questions[1] + "$} in the form " + str(base) + "$^{k}$"
			answer = Fraction(indexes[0]+indexes[1])
			print(answer)
			check = answer
			if answer<0:
				sign = "-"
				answer = 0 - answer
			else:
				sign = ""
			answer = simpfrac(answer.numerator,answer.denominator)
#answer for just k
			answer = "$" + sign + answer + "$"
#normal answer
#			answer = "\\large" + str(base) + "\\normalsize$^{" + sign + answer + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def writeaspowerdiv(n,explanationn):
	import random
	from math import floor,gcd
	from fractions import Fraction
	from utilities.fractions import simpfrac
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of k when you write "
		else:
			explanation = ""
		check = 0
		while check==0:
			questions = []
			bases = [2,3,4,5,10]
			base = random.choice(bases)

			indexes = []

			choices = [1,2,5,6]
			choice1 = random.choice(choices)
			choices.remove(choice1)
			choice2 = random.choice(choices)
			choices = [choice1,choice2]
		#1
			if 1 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				question = str(base**index)
				answer = str(base) + "^{" + str(index) + "}"
				questions.append(question)
				indexes.append(index)
		#2
			if 2 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				index2 = random.randrange(2,10)
				question = str(base**index) + "^{" + str(index2) + "}"
				answer = str(base) + "^{" + str(index*index2) + "}"
				questions.append(question)
				indexes.append(index*index2)
		#3
			if 3 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				question = "\\dfrac{1}{" + str(base**index) + "}"
				answer = str(base) + "^{-" + str(index) + "}"
				questions.append(question)
				indexes.append(0 - index)
		#4
			if 4 in choices:
				if base==2:
					index = random.randrange(2,6)
				else:
					index = random.randrange(2,4)
				index2 = random.randrange(2,10)
				question = "\\dfrac{1}{" + str(base**index) + "^{" + str(index2) + "}}"
				answer = str(base) + "^{-" + str(index*index2) + "}"
				questions.append(question)
				indexes.append(0 - index*index2)
		#5
			if 5 in choices:
		#		bases = [2,3,5,6,7,10]
				answer = str(base) + "^{\\frac{1}{2}}"
				question = "\\sqrt{" + str(base) + "}"
				questions.append(question)
				indexes.append(Fraction(1,2))
		#6
			if 6 in choices:
				power = random.randrange(2,4)
				if power==3:
					roots = [2,4,5,7,8]
				else:
					roots = [3,5,7,9]
				root = random.choice(roots)
				if root==2:
					question = "\\sqrt{" + str(base**power) + "}"
				else:
					question = "\\sqrt[" + str(root) + "]{" + str(base**power) + "}"
				answer = str(base) + "^{\\frac{" + str(power) + "}{" + str(root) + "}}"
				questions.append(question)
				indexes.append(Fraction(power,root))
		#7
			if 7 in choices:
				answer = str(base) + "^{-\\frac{1}{2}}"
				question = "\\dfrac{1}{\\sqrt{" + str(base) + "}}"
				questions.append(question)
				indexes.append(Fraction(-1,2))
		#8
			if 8 in choices:
				power = random.randrange(2,4)
				if power==3:
					roots = [2,4,5,7,8]
				else:
					roots = [3,5,7,9]
				root = random.choice(roots)
				if root==2:
					question = "\\sqrt{" + str(base**power) + "}"
				else:
					question = "\\sqrt[" + str(root) + "]{" + str(base**power) + "}"
				question = "\\dfrac{1}{" + question + "}"
				answer = str(base) + "^{-\\frac{" + str(power) + "}{" + str(root) + "}}"
				questions.append(question)
				indexes.append(Fraction(0 - power,root))
#collate
			question = "$\\dfrac{" + questions[0] + "}{" + questions[1] + "}$ in the form " + str(base) + "$^{k}$"
			answer = Fraction(indexes[0]-indexes[1])
			print(answer)
			check = answer
			if answer<0:
				sign = "-"
				answer = 0 - answer
			else:
				sign = ""
			answer = simpfrac(answer.numerator,answer.denominator)
#answer for just k
			answer = "$" + sign + answer + "$"
#normal answer
#			answer = "\\large" + str(base) + "\\normalsize$^{" + sign + answer + "}$"
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
