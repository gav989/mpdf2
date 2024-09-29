#similarity.py

def findsf1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		num1 = random.randrange(4,13)
		sf = random.randrange(2,6)
		num2 = num1 * sf
		question = str(num1) + " $\\times \\rule[-1.5mm]{1cm}{0.15mm}$ = " + str(num2)
		answer = str(sf)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
			

def findsf2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		question = str(num1) + " $\\times \\rule[-1.5mm]{1cm}{0.15mm}$ = " + str(num2)
		answer = str(sf)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def usesf1(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		question = str(num1) + " $\\times$ " + sf
		answer = str(num2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def usesf2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		question = str(num2) + " $\\div$ " + sf
		answer = str(num1)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def simtri1int(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		nums = list(range(3,25))
		num1 = random.choice(nums)
		nums.remove(num1)
		num3 = random.choice(nums)
		sf = random.randrange(2,5)
		num2 = num1 * sf
		num4 = num3 * sf
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		if random.randrange(0,2)==0:
			answer = str(num2)
			num2 = "?"
		else:
			answer = str(num4)
			num4 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri1} \\put(15,3){" + str(num1) + "cm" + "} \\put(34,25){" + str(num3) + "cm" + "} \\put(62,3){" + str(num2) + "cm" + "} \\put(85,25){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")



def simtri1(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		array[lookup].remove(num1)
		num3 = random.choice(array[lookup])
		num4 = int(num3/den)*(num + (den*integer))
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		if random.randrange(0,2)==0:
			answer = str(num2)
			num2 = "?"
		else:
			answer = str(num4)
			num4 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri1} \\put(15,3){" + str(num1) + "cm" + "} \\put(34,25){" + str(num3) + "cm" + "} \\put(62,3){" + str(num2) + "cm" + "} \\put(85,25){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")



def simtri2int(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		nums = list(range(3,25))
		num1 = random.choice(nums)
		nums.remove(num1)
		num3 = random.choice(nums)
		sf = random.randrange(2,5)
		num2 = num1 * sf
		num4 = num3 * sf
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		if random.randrange(0,2)==0:
			answer = str(num1)
			num1 = "?"
		else:
			answer = str(num3)
			num3 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri1} \\put(15,3){" + str(num1) + "cm" + "} \\put(34,25){" + str(num3) + "cm" + "} \\put(62,3){" + str(num2) + "cm" + "} \\put(85,25){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")



def simtri2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		array[lookup].remove(num1)
		num3 = random.choice(array[lookup])
		num4 = int(num3/den)*(num + (den*integer))
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		if random.randrange(0,2)==0:
			answer = str(num1)
			num1 = "?"
		else:
			answer = str(num3)
			num3 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri1} \\put(15,3){" + str(num1) + "cm" + "} \\put(34,25){" + str(num3) + "cm" + "} \\put(62,3){" + str(num2) + "cm" + "} \\put(85,25){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")



def simtri3(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		array[lookup].remove(num1)
		num3 = random.choice(array[lookup])
		num4 = int(num3/den)*(num + (den*integer))
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		if random.randrange(0,2)==0:
			answer = str(num2)
			num2 = "?"
		else:
			answer = str(num4)
			num4 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri3} \\put(15,12){" + str(num1) + "cm" + "} \\put(50,10){" + str(num3) + "cm" + "} \\put(67,26){" + str(num2) + "cm" + "} \\put(23,28){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")


def simtri4(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		array[lookup].remove(num1)
		num3 = random.choice(array[lookup])
		num4 = int(num3/den)*(num + (den*integer))
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		if random.randrange(0,2)==0:
			answer = str(num1)
			num1 = "?"
		else:
			answer = str(num3)
			num3 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri3} \\put(15,12){" + str(num1) + "cm" + "} \\put(50,10){" + str(num3) + "cm" + "} \\put(67,26){" + str(num2) + "cm" + "} \\put(23,28){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")



def simtri5(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing side length:\\\\"
		else:
			explanation = ""
		halfs = [4,6,8,10,12,14,16,18,20,22,24,26,28,30]
		thirds = [6,9,12,15,18,21,24,27,30]
		quarters = [8,12,16,20,24,28,32]
		fifths = [10,15,20,25,30]
		den = random.randrange(2,6)
		if den<4:
			num = random.randrange(1,den)
		else:
			num = 1
		integer = random.randrange(1,4)
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		sf = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		array = [halfs,thirds,quarters,fifths]
		lookup = den - 2
		num1 = random.choice(array[lookup])
		num2 = int(num1/den)*(num + (den*integer))
		array[lookup].remove(num1)
		num3 = random.choice(array[lookup])
		num4 = int(num3/den)*(num + (den*integer))
		if num1 > num2:
			temp = num1
			num1 = num2
			num2 = temp
			temp = num3
			num3 = num4
			num4 = temp
		answer = str(num4-num3)
		num4 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri2} \\put(48,15){" + str(num1) + "cm" + "} \\put(65,22){" + str(num2) + "cm" + "} \\put(18,17){" + str(num3) + "cm" + "} \\put(41,35){" + str(num4) + "cm" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")


def simtriarea(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing area:\\\\"
		else:
			explanation = ""
		sf = random.randrange(2,6)
		length1 = random.randrange(2,11)
		length2 = length1 * sf
		area1 = random.randrange(2,11) + length1
		area2 = area1 * sf * sf
		if random.randrange(0,2)==1:
			answer = area1
			area1 = "?"
		else:
			answer = area2
			area2 = "?"
		image = "\\centering\\begin{overpic}[scale=0.6]{shape/images/simtri1} \\put(3,23){" + str(length1) + "cm" + "} \\put(48,27){" + str(length2) + "cm" + "} \\put(8,3){A = " + str(area1) + "cm$^{2}$" + "} \\put(55,3){A = " + str(area2) + "cm$^{2}$" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + "cm$^{2}$")


def simvolume(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing volume:\\\\"
		else:
			explanation = ""
		sf = random.randrange(2,6)
		length1 = random.randrange(2,11)
		length2 = length1 * sf
		vol1 = random.randrange(2,11) + length1
		vol2 = vol1 * sf * sf * sf
		if random.randrange(0,2)==1:
			answer = vol1
			vol1 = "?"
		else:
			answer = vol2
			vol2 = "?"
		if random.randrange(0,2)==1:
			image = "\\centering\\begin{overpic}[scale=0.84]{shape/images/simcone} \\put(21,15){" + str(length1) + "cm" + "} \\put(72,16.5){" + str(length2) + "cm" + "} \\put(8,0){V = " + str(vol1) + "cm$^{3}$" + "} \\put(55,0){V = " + str(vol2) + "cm$^{3}$" + "} \\end{overpic}"
		else:
			image = "\\centering\\begin{overpic}[scale=0.84]{shape/images/simcylinder} \\put(21,15){" + str(length1) + "cm" + "} \\put(72,16.5){" + str(length2) + "cm" + "} \\put(8,0){V = " + str(vol1) + "cm$^{3}$" + "} \\put(55,0){V = " + str(vol2) + "cm$^{3}$" + "} \\end{overpic}"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + "cm$^{3}$")
