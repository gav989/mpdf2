#simultaneous.py

def simeqlin1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5]
		choice = random.randrange(0,20)
		same = random.randrange(1,8)
		x = random.randrange(1,10) * (-1)**random.randrange(1,3)
		y = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if random.randrange(1,3)==1:
			a = choices1[choice]
			b = same * (-1)**random.randrange(1,3)
			c = a * x + b * y
			d = choices2[choice]
			e = same * (-1)**random.randrange(1,3)
			f = d * x + e * y
		else:
			a = same
			b = choices1[choice] * (-1)**random.randrange(1,3)
			c = a * x + b * y
			d = same
			e = choices2[choice] * (-1)**random.randrange(1,3)
			f = d * x + e * y
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "	
		if e<0:
			sign2 = " - "
			e = abs(e)
		else:
			sign2 = " + "	
		if a==1:
			a = ""
		if b==1:
			b = ""
		if d==1:
			d = ""
		if e==1:
			e = ""
		equation1 = str(a) + "x" + sign1 + str(b) + "y = " + str(c)
		equation2 = str(d) + "x" + sign2 + str(e) + "y = " + str(f)
#write question
		tempquestions.write(explanation + "$\\begin{array}{ll} " + equation1 + " \\\\ " + equation2 + " \\end{array}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + ", y = " + str(y) + "$")


def simeqlin2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5]
		choice = random.randrange(0,20)
		fac1 = random.randrange(1,5)
		fac2 = fac1 * random.randrange(2,6)
		if random.randrange(0,2)==1:
			temp = fac1
			fac1 = fac2
			fac2 = temp
		x = random.randrange(1,10) * (-1)**random.randrange(1,3)
		y = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if random.randrange(1,3)==1:
			a = choices1[choice]
			b = fac1 * (-1)**random.randrange(1,3)
			c = a * x + b * y
			d = choices2[choice]
			e = fac2 * (-1)**random.randrange(1,3)
			f = d * x + e * y
		else:
			a = fac1
			b = choices1[choice] * (-1)**random.randrange(1,3)
			c = a * x + b * y
			d = fac2
			e = choices2[choice] * (-1)**random.randrange(1,3)
			f = d * x + e * y
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "	
		if e<0:
			sign2 = " - "
			e = abs(e)
		else:
			sign2 = " + "	
		if a==1:
			a = ""
		if b==1:
			b = ""
		if d==1:
			d = ""
		if e==1:
			e = ""
		equation1 = str(a) + "x" + sign1 + str(b) + "y = " + str(c)
		equation2 = str(d) + "x" + sign2 + str(e) + "y = " + str(f)
#write question
		tempquestions.write(explanation + "$\\begin{array}{ll} " + equation1 + " \\\\ " + equation2 + " \\end{array}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + ", y = " + str(y) + "$")


def simeqlin3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5]
		templist=list(range(0,20))
		choice1 = random.choice(templist)
		templist.remove(choice1)
		choice2 = random.choice(templist)
		x = random.randrange(1,10) * (-1)**random.randrange(1,3)
		y = random.randrange(1,10) * (-1)**random.randrange(1,3)
		a = choices1[choice1]
		b = choices1[choice2] * (-1)**random.randrange(1,3)
		c = a * x + b * y
		d = choices2[choice1]
		e = choices2[choice2] * (-1)**random.randrange(1,3)
		f = d * x + e * y
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "	
		if e<0:
			sign2 = " - "
			e = abs(e)
		else:
			sign2 = " + "	
		if a==1:
			a = ""
		if b==1:
			b = ""
		if d==1:
			d = ""
		if e==1:
			e = ""
		equation1 = str(a) + "x" + sign1 + str(b) + "y = " + str(c)
		equation2 = str(d) + "x" + sign2 + str(e) + "y = " + str(f)
#write question
		tempquestions.write(explanation + "$\\begin{array}{ll} " + equation1 + " \\\\ " + equation2 + " \\end{array}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + ", y = " + str(y) + "$")




def simeqquad1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		num1 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		num2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		co1 = 1
		co2 = 1
		x1 = (num1 * (-1))/co1
		x2 = (num2 * (-1))/co2
		a = co1 * co2
		b = num1 * co2 + num2 * co1
		c = num1 * num2
		m = random.randrange(1,5)
		cc = random.randrange(0,9)*(-1)**random.randrange(1,3)
		y1 = m * x1 + cc
		y2 = m * x2 + cc
		b = b + m
		c = c + cc
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if cc<0:
			sign3 = " - "
			cc = abs(cc)
		else:
			sign3 = " + "
		if a==1:
			a = ""
		if b==1:
			b = ""
		if m==1:
			m = ""
		x1 = int(x1)
		x2 = int(x2)
		y1 = int(y1)
		y2 = int(y2)
		if b==0:
			equation1 = "y = " + str(a) + "x^{2}" + sign2 + str(c)
		else:
			equation1 = "y = " + str(a) + "x^{2}" + sign1 + str(b) + "x" + sign2 + str(c)
		if cc==0:
			equation2 = "y = " + str(m) + "x"
		else:
			equation2 = "y = " + str(m) + "x" + sign3 + str(cc)
#write question
		tempquestions.write(explanation + "$\\begin{array}{ll} " + equation1 + " \\\\ " + equation2 + " \\end{array}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("(" + str(x1) + " , " + str(y1) + ") and (" + str(x2) + " , " + str(y2) + ")")


def simeqquad2(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		num1 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		num2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		co1 = random.randrange(1,5)
		if co1==1:
			co2 = random.randrange(2,7)
		else:
			co2 = random.randrange(1,4)
		a = co1 * co2
		b = num1 * co2 + num2 * co1
		c = num1 * num2
		m = random.randrange(1,5)
		cc = random.randrange(0,9)*(-1)**random.randrange(1,3)
		b = b + m
		c = c + cc
		if num1%co1==0:
			x1 = int((num1 * -1)/co1)
			if (m * x1 + cc)%1==0:
				y1 = m * x1 + cc
			else:
				y1 = Fraction(m * x1 + cc,1)
				y1int = floor(y1.numerator/y1.denominator)
				y1 = y1 - y1int
				if y1int==0:
					y1int = ""
				y1 = str(y1int) + "$\\dfrac{" + str(y1.numerator) + "}{" + str(y1.denominator) + "}$"
		else:
			x1 = Fraction(num1 * -1,co1)
			if (m * x1 + cc)%1==0:
				y1 = m * x1 + cc
			else:
				y1 = Fraction(m * x1 + cc,1)
				y1int = floor(y1.numerator/y1.denominator)
				y1 = y1 - y1int
				if y1int==0:
					y1int = ""
				y1 = str(y1int) + "$\\dfrac{" + str(y1.numerator) + "}{" + str(y1.denominator) + "}$"
			x1int = floor(x1.numerator/x1.denominator)
			x1 = x1 - x1int
			if x1int==0:
				x1int = ""
			x1 = str(x1int) + "$\\dfrac{" + str(x1.numerator) + "}{" + str(x1.denominator) + "}$"
		if num2%co2==0:
			x2 = int((num2 * -1)/co2)
			if (m * x2 + cc)%1==0:
				y2 = m * x2 + cc
			else:
				y2 = Fraction(m * x2 + cc,1)
				y2int = floor(y2.numerator/y2.denominator)
				y2 = y2 - y2int
				if y2int==0:
					y2int = ""
				y2 = str(y2int) + "$\\dfrac{" + str(y2.numerator) + "}{" + str(y2.denominator) + "}$"
		else:
			x2 = Fraction(num2 * -1,co2)
			if (m * x2 + cc)%1==0:
				y2 = m * x2 + cc
			else:
				y2 = Fraction(m * x2 + cc,1)
				y2int = floor(y2.numerator/y2.denominator)
				y2 = y2 - y2int
				if y2int==0:
					y2int = ""
				y2 = str(y2int) + "$\\dfrac{" + str(y2.numerator) + "}{" + str(y2.denominator) + "}$"
			x2int = floor(x2.numerator/x2.denominator)
			x2 = x2 - x2int
			if x2int==0:
				x2int = ""
			x2 = str(x2int) + "$\\dfrac{" + str(x2.numerator) + "}{" + str(x2.denominator) + "}$"
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if cc<0:
			sign3 = " - "
			cc = abs(cc)
		else:
			sign3 = " + "
		if a==1:
			a = ""
		if b==1:
			b = ""
		if m==1:
			m = ""
		if b==0:
			equation1 = "y = " + str(a) + "x^{2}" + sign2 + str(c)
		else:
			equation1 = "y = " + str(a) + "x^{2}" + sign1 + str(b) + "x" + sign2 + str(c)
		if cc==0:
			equation2 = "y = " + str(m) + "x"
		else:
			equation2 = "y = " + str(m) + "x" + sign3 + str(cc)
#write question
		tempquestions.write(explanation + "$\\begin{array}{ll} " + equation1 + " \\\\ " + equation2 + " \\end{array}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("(" + str(x1) + " , " + str(y1) + ") and (" + str(x2) + " , " + str(y2) + ")")

