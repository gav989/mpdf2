#surds.py


def simplifysurdexam(n,explanationn):
#on ks4 h unit 3
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Show that "
			explanation2 = " can be written in the form "
		else:
			explanation1 = ""
			explanation2 = ""
		roots = list(range(2,12))
		multipliers = (2,3,5,6,7,10)
		multipliers2 = (2,3,5,10)
		root = random.choice(roots)
		if root>5:
			multiplier = random.choice(multipliers2)
		else:	
			multiplier = random.choice(multipliers)
		base1 = multiplier * root**2
		base2 = multiplier
		surd = "$\\sqrt{" + str(base1) + "}$"
		answer = str(root) + "$\\sqrt{" + str(multiplier) + "}$"
#write question
		tempquestions.write(explanation1 + surd + explanation2 + answer)
		tempquestions.write("\n")
#write answer
		tempquestions.write("Show steps on board...")

def hsf(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the highest square factor of "
		else:
			explanation = ""
		roots = list(range(2,12))
		multipliers = (2,3,5,6,7,10)
		multipliers2 = (2,3,5,10)
		root = random.choice(roots)
		if root>5:
			multiplier = random.choice(multipliers2)
		else:	
			multiplier = random.choice(multipliers)
		base1 = multiplier * root**2
		base2 = multiplier
		question = str(base1)
		answer = str(root**2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def simplifysurd1(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = list(range(2,12))
		multipliers = (2,3,5,6,7,10)
		multipliers2 = (2,3,5,10)
		root = random.choice(roots)
		if root>5:
			multiplier = random.choice(multipliers2)
		else:	
			multiplier = random.choice(multipliers)
		base1 = multiplier * root**2
		base2 = multiplier
#write question
		tempquestions.write(explanation + "$\\sqrt{" + str(base1) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(root) + "$\\sqrt{" + str(multiplier) + "}$")

def simplifysurd2(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = list(range(2,12))
		multipliers = (2,3,5,6,7,10)
		multipliers2 = (2,3,5,10)
		root = random.choice(roots)
		if root>5:
			multiplier = random.choice(multipliers2)
		else:	
			multiplier = random.choice(multipliers)
		base1 = multiplier * root**2
		base2 = multiplier
		out = random.randrange(2,7)
#write question
		tempquestions.write(explanation + "$" + str(out) + "\\sqrt{" + str(base1) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(out*root) + "$\\sqrt{" + str(multiplier) + "}$")



def simplifysurdmult1(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = (2,3,4,5,6)
		root = random.choice(roots)
		if root==4:
			mults = [2,3,4,5,6]
		else:
			mults = [1,2,3,4,5,6]
		mults.remove(root)
		mult1 = random.choice(mults)
		mults.remove(mult1)
		mult2 = random.choice(mults)
		base1 = root*mult1
		base2 = root*mult2
		base3 = int((base1*base2)/root**2)
		if base3%16==0:
			root = int(root*4)
			base3 = int(base3/16)
		elif base3%9==0:
			root = int(root*3)
			base3 = int(base3/9)
		elif base3%4==0:
			root = int(root * 2)
			base3 = int(base3/4)
#write question
		tempquestions.write(explanation + "$\\sqrt{" + str(base1) + "} \\times \\sqrt{" + str(base2) + "}$")
		tempquestions.write("\n")
#write answer
		if base3==1:
			tempquestions.write(str(root))
		else:
			tempquestions.write(str(root) + "$\\sqrt{" + str(base3) + "}$")

def simplifysurdmult2(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = (2,3,4,5,6)
		root = random.choice(roots)
		if root==4:
			mults = [2,3,4,5,6]
		else:
			mults = [1,2,3,4,5,6]
		mults.remove(root)
		mult1 = random.choice(mults)
		mults.remove(mult1)
		mult2 = random.choice(mults)
		base1 = root*mult1
		base2 = root*mult2
		base3 = int((base1*base2)/root**2)
		if base3%16==0:
			root = int(root*4)
			base3 = int(base3/16)
		elif base3%9==0:
			root = int(root*3)
			base3 = int(base3/9)
		elif base3%4==0:
			root = int(root * 2)
			base3 = int(base3/4)
		out1 = random.randrange(2,7)
		out2 = random.randrange(2,7)
		root = root * out1 * out2
#write question
		tempquestions.write(explanation + "$" + str(out1) + "\\sqrt{" + str(base1) + "} \\times " + str(out2) +"\\sqrt{" + str(base2) + "}$")
		tempquestions.write("\n")
#write answer
		if base3==1:
			tempquestions.write(str(root))
		else:
			tempquestions.write(str(root) + "$\\sqrt{" + str(base3) + "}$")


def simplifysurddiv1(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = list(range(2,6))
		multipliers = (2,3,5)
		root = random.choice(roots)
		multiplier = random.choice(multipliers)
		base1 = multiplier * root**2
		base2 = multiplier
		scale = (2,3,5,6)
		scaler = random.choice(scale)
		base0 = base1 * scaler
#write question
		tempquestions.write(explanation + "$\\sqrt{" + str(base0) + "} \\div \\sqrt{" + str(scaler) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(root) + "$\\sqrt{" + str(multiplier) + "}$")

def simplifysurdadd(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = [2,3,5,6,7]
		root = random.choice(roots)
		ints = [2,3,4,5,6]
		int1 = random.choice(ints)
		ints.remove(int1)
		int2 = random.choice(ints)
		answer = str(int1+int2) + "$\\sqrt{" + str(root) + "}$"
		root1 = root*int1**2
		root2 = root*int2**2
		question = "$\\sqrt{" + str(root1) + "} + \\sqrt{" + str(root2) + "}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def simplifysurdsubtract(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = [2,3,5,6,7]
		root = random.choice(roots)
		ints = [2,3,4,5,6]
		int1 = random.choice(ints)
		ints.remove(int1)
		int2 = random.choice(ints)
		if int2>int1:
			temp = int1
			int1 = int2
			int2 = temp
		if int1-int2==1:
			answer = "$\\sqrt{" + str(root) + "}$"
		else:
			answer = str(int1-int2) + "$\\sqrt{" + str(root) + "}$"
		root1 = root*int1**2
		root2 = root*int2**2
		question = "$\\sqrt{" + str(root1) + "} - \\sqrt{" + str(root2) + "}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def simplifysurddiv2(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		roots = list(range(2,6))
		multipliers = (2,3,5)
		root = random.choice(roots)
		multiplier = random.choice(multipliers)
		base1 = multiplier * root**2
		base2 = multiplier
		scale = (2,3,5,6)
		scaler = random.choice(scale)
		base0 = base1 * scaler
		out1 = random.randrange(2,13)
		out2 = random.randrange(2,13)
		out0 = out1 * out2
#write question
		tempquestions.write(explanation + "$" + str(out0) + "\\sqrt{" + str(base0) + "} \\div " + str(out1) + "\\sqrt{" + str(scaler) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(root*out2) + "$\\sqrt{" + str(multiplier) + "}$")


def surdquadratic1pos(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		roots = (2,3,5,6,7,10)
		order = random.randrange(0,2)
		root = random.choice(roots)
		c1 = 1
		c2 = 1
		if order==0:
			a = random.randrange(1,10)
			b = random.randrange(1,10)
			if a>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if b>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = (root + a*b)*c1*c2
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "($\\sqrt{" + str(root) + "}$" + sign1 + str(a) + ")"
			bracket2 = "($\\sqrt{" + str(root) + "}$" + sign2 + str(b) + ")"
		else:
			a = random.randrange(1,10)
			b = random.randrange(1,10)
			c1 = c1
			c2 = c2
			if c1>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if c2>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = a*b + c1*c2*root
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "(" + str(a) + sign1 + "$\\sqrt{" + str(root) + "}$)"
			bracket2 = "(" + str(b) + sign2 + "$\\sqrt{" + str(root) + "}$)"
#write question
		tempquestions.write(explanation + bracket1 + bracket2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def surdquadratic1(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		roots = (2,3,5,6,7,10)
		order = random.randrange(0,2)
		root = random.choice(roots)
		c1 = 1
		c2 = 1
		if order==0:
			a = random.randrange(1,10)*(-1)**random.randrange(1,3)
			b = random.randrange(1,10)*(-1)**random.randrange(1,3)
			if a>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if b>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = (root + a*b)*c1*c2
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "($\\sqrt{" + str(root) + "}$" + sign1 + str(a) + ")"
			bracket2 = "($\\sqrt{" + str(root) + "}$" + sign2 + str(b) + ")"
		else:
			a = random.randrange(1,10)
			b = random.randrange(1,10)
			c1 = c1 * (-1)**random.randrange(0,2)
			c2 = c2 * (-1)**random.randrange(0,2)
			if c1>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if c2>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = a*b + c1*c2*root
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "(" + str(a) + sign1 + "$\\sqrt{" + str(root) + "}$)"
			bracket2 = "(" + str(b) + sign2 + "$\\sqrt{" + str(root) + "}$)"
#write question
		tempquestions.write(explanation + bracket1 + bracket2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def surdquadratic1squared(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		roots = (2,3,5,6,7,10)
		order = random.randrange(0,2)
		root = random.choice(roots)
		c1 = 1
		c2 = 1
		if order==0:
			a = random.randrange(1,10)*(-1)**random.randrange(1,3)
			b = a
			if a>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if b>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = (root + a*b)*c1*c2
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "($\\sqrt{" + str(root) + "}$" + sign1 + str(a) + ")"
		else:
			a = random.randrange(1,10)
			b = a
			c1 = c1 * (-1)**random.randrange(0,2)
			c2 = c1
			if c1>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if c2>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = a*b + c1*c2*root
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "(" + str(a) + sign1 + "$\\sqrt{" + str(root) + "}$)"
#write question
		tempquestions.write(explanation + bracket1 + "$^{2}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def surdquadratic1squaredpos(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		roots = (2,3,5,6,7,10)
		order = random.randrange(0,2)
		root = random.choice(roots)
		c1 = 1
		c2 = 1
		if order==0:
			a = random.randrange(1,10)
			b = a
			if a>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if b>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = (root + a*b)*c1*c2
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "($\\sqrt{" + str(root) + "}$" + sign1 + str(a) + ")"
		else:
			a = random.randrange(1,10)
			b = a
			c1 = c1
			c2 = c1
			if c1>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if c2>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = a*b + c1*c2*root
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			bracket1 = "(" + str(a) + sign1 + "$\\sqrt{" + str(root) + "}$)"
#write question
		tempquestions.write(explanation + bracket1 + "$^{2}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def surdquadratic2(n,explanationn):
	import random, math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		roots = (2,3,5,6,7,10)
		order = random.randrange(0,2)
		root = random.choice(roots)
		c1 = random.randrange(1,6)
		c2 = random.randrange(1,6)
		if order==0:
			a = random.randrange(1,10)*(-1)**random.randrange(1,3)
			b = random.randrange(1,10)*(-1)**random.randrange(1,3)
			if a>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if b>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = root*c1*c2 + a*b
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			if c1==1:
				c1 = ""
			if c2==1:
				c2 = ""
			bracket1 = "(" + str(c1) + "$\\sqrt{" + str(root) + "}$" + sign1 + str(a) + ")"
			bracket2 = "(" + str(c2) + "$\\sqrt{" + str(root) + "}$" + sign2 + str(b) + ")"
		else:
			a = random.randrange(1,10)
			b = random.randrange(1,10)
			c1 = c1 * (-1)**random.randrange(0,2)
			c2 = c2 * (-1)**random.randrange(0,2)
			if c1>0:
				sign1 = " + "
			else:
				sign1 = " - "
			if c2>0:
				sign2 = " + "
			else:
				sign2 = " - "
			d = a*b + c1*c2*root
			e = a*c2 + b*c1
			if d<0:
				sign3 = "-"
			else:
				sign3 = ""
			if e<0:
				sign4 = " - "
			else:
				sign4 = " + "
			a = abs(a)
			b = abs(b)
			d = str(abs(d))
			e = abs(e)
			c1 = abs(c1)
			c2 = abs(c2)
			if d=="0":
				d=""
				sign3 = ""
				if sign4==" - ":
					sign4 = "-"
				else:
					sign4 = ""
			if e==1:
				answer = sign3 + d + sign4 + "$\\sqrt{" + str(root) + "}$"
			elif e==0:
				answer = sign3 + d
			else:
				answer = sign3 + d + sign4 + str(e) + "$\\sqrt{" + str(root) + "}$"
			if c1==1:
				c1 = ""
			if c2==1:
				c2 = ""
			bracket1 = "(" + str(a) + sign1 + str(c1) + "$\\sqrt{" + str(root) + "}$)"
			bracket2 = "(" + str(b) + sign2 + str(c2) + "$\\sqrt{" + str(root) + "}$)"
#write question
		tempquestions.write(explanation + bracket1 + bracket2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratden1(n,explanationn):
	import random, math
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Rationalise the denominator of "
		else:
			explanation = ""
		surds = [2,3,5,6,7,8]
		dsurd = random.choice(surds)
		numnum = random.randrange(1,10)
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(numnum) + "}{\\sqrt{" + str(dsurd) + "}}$")
		tempquestions.write("\n")
#write answer

		asurd = dsurd
		if asurd%16==0:
			numnum = int(numnum*4)
			asurd = int(asurd/16)
		elif asurd%9==0:
			numnum = int(numnum*3)
			asurd = int(asurd/9)
		elif asurd%4==0:
			numnum = int(numnum * 2)
			asurd = int(asurd/4)
		hcf = gcd(numnum,dsurd)
		numnum = int(numnum / hcf)
		dsurd = int(dsurd / hcf)
		if numnum==1:
			numnum = ""

		if asurd==1:
			if dsurd==1:
				tempquestions.write(str(numnum))
			else:
				tempquestions.write("$\\dfrac{" + str(numnum) + "}{" + str(dsurd) + "}$")
		else:
			if dsurd==1:
				tempquestions.write("$" + str(numnum) + " \\sqrt{" + str(asurd) + "}$")
			else:
				tempquestions.write("$\\dfrac{" + str(numnum) + " \\sqrt{" + str(asurd) + "}}{" + str(dsurd) + "}$")

def ratden2(n,explanationn):
	import random, math
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Rationalise the denominator of "
		else:
			explanation = ""
		surds = [2,3,5,6,7,8]
		nsurd = random.choice(surds)
		surds.remove(nsurd)
		dsurd = random.choice(surds)
		numnum = random.randrange(2,10)
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(numnum) + "\\sqrt{" + str(nsurd) + "}}{\\sqrt{" + str(dsurd) + "}}$")
		tempquestions.write("\n")
#write answer

		asurd = nsurd * dsurd
		if asurd%16==0:
			numnum = int(numnum*4)
			asurd = int(asurd/16)
		elif asurd%9==0:
			numnum = int(numnum*3)
			asurd = int(asurd/9)
		elif asurd%4==0:
			numnum = int(numnum * 2)
			asurd = int(asurd/4)
		hcf = gcd(numnum,dsurd)
		numnum = int(numnum / hcf)
		dsurd = int(dsurd / hcf)
		if numnum==1:
			numnum = ""

		if asurd==1:
			if dsurd==1:
				tempquestions.write(str(numnum))
			else:
				tempquestions.write("$\\dfrac{" + str(numnum) + "}{" + str(dsurd) + "}$")
		else:
			if dsurd==1:
				tempquestions.write("$" + str(numnum) + " \\sqrt{" + str(asurd) + "}$")
			else:
				tempquestions.write("$\\dfrac{" + str(numnum) + " \\sqrt{" + str(asurd) + "}}{" + str(dsurd) + "}$")



def ratdenDOTS(n,explanationn):
	import random, math
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Rationalise the denominator of "
		else:
			explanation = ""
		num = random.randrange(1,6)
		den = random.randrange(1,6)
		surds = [2,3,5,6,7,8,10,12]
		surd = random.choice(surds)
		sign = random.randrange(0,2)
		if surd>den**2:
			order = 0
		else:
			order = 1
		if sign==0:
			signn = " - "
		else:
			signn = " + "
#write question
		if order==0:
			tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{\\sqrt{" + str(surd) + "}" + signn + str(den) + "}$")
		else:
			tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + signn + "\\sqrt{" + str(surd) +"}}$")
		tempquestions.write("\n")
#write answer
		if sign==1:
			signn = " - "
		else:
			signn = " + "
		if order==0:
			d = surd - den**2
		else:
			d = den**2 - surd
		numd = num * den
		if surd==8 or surd==12:
			num = num*2
			surd = int(surd/4)
		hcf1 = gcd(num,numd)
		hcf2 = gcd(num,d)
		hcf = gcd(hcf1,hcf2)
		num = int(num / hcf)
		d = int(d / hcf)
		numd = int(numd/hcf)
		if num==1:
			num = ""
		if order==0:
			if d==1:
				tempquestions.write("$" + str(num) + "\\sqrt{" + str(surd) + "}" + signn + str(numd) + "$")
			else:
				tempquestions.write("$\\dfrac{" + str(num) + "\\sqrt{" + str(surd) + "}" + signn + str(numd) + "}{" + str(d) + "}$")
		else:
			if d==1:
				tempquestions.write("$" + str(numd) + signn + str(num) + "\\sqrt{" + str(surd) + "}$")
			else:
				tempquestions.write("$\\dfrac{" + str(numd) + signn + str(num) + "\\sqrt{" + str(surd) + "}}{" + str(d) + "}$")

def ratden3(n,explanationn):
	import random, math
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Rationalise the denominator of "
		else:
			explanation = ""
		surds = [2,3,5,6,7]
		dsurd = random.choice(surds)
		numnum = random.randrange(1,10)
		if random.randrange(1,3)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(numnum) + sign + "\\sqrt{" + str(dsurd) + "}}{\\sqrt{" + str(dsurd) + "}}$")
		tempquestions.write("\n")
#write answer
		asurd = dsurd
		hcf = gcd(asurd,numnum)
		asurd = int(asurd/hcf)
		numnum = int(numnum/hcf)
		if numnum==1:
			numnum=""
		if asurd==1:
			tempquestions.write("$" + str(numnum) + " \\sqrt{" + str(dsurd) + "}" + sign + str(asurd) + "$")
		else:
			tempquestions.write("$\\dfrac{" + str(numnum) + " \\sqrt{" + str(dsurd) + "}" + sign + str(asurd) + "}{" + str(asurd) + "}$")



def ratdenDOTS2(n,explanationn):
	import random, math
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Rationalise the denominator of "
		else:
			explanation = ""
		nums = list(range(1,10))
		num1 = random.choice(nums)
		nums.remove(num1)
		num2 = random.choice(nums)
		coeff = random.randrange(1,7)
		surds = [2,3,5,6,7,10]
		surd = random.choice(surds)
		toporder = random.randrange(0,2)
		if surd<num2**2:
			bottomorder = 0
		else:
			bottomorder = 1
		signs = [" + "," - "]
		sign1 = random.choice(signs)
		sign2 = random.choice(signs)
		if coeff==1:
			coeff2 = ""
		else:
			coeff2 = coeff
		if toporder==0:
			top = str(num1) + sign1 + str(coeff2) + "\\sqrt{" + str(surd) + "}"
		else:
			top = str(coeff2) + "\\sqrt{" + str(surd) + "}" + sign1 + str(num1)
		if bottomorder==0:
			bottom = str(num2) + sign2 + "\\sqrt{" + str(surd) + "}"
		else:
			bottom = "\\sqrt{" + str(surd) + "}" + sign2 + str(num2)
		question = "$\\dfrac{" + top + "}{" + bottom + "}$"
		if bottomorder==0:
			bottom = num2**2 - surd
		else:
			bottom = surd - num2**2
		if sign1==" - ":
			if toporder==0:
				coeff = 0 - coeff
			else:
				num1 = 0 - num1
		if sign2==" - ":
			coeff2 = 1
		else:
			if bottomorder==0:
				coeff2 = -1
			else:
				coeff2 = 1
				num2 = 0 - num2
		topnum = num1*num2 + coeff*coeff2*surd
		topcoeff = num2*coeff + num1*coeff2
		hcf = gcd(bottom,topnum)
		hcf = abs(gcd(hcf,topcoeff))
		print(hcf)
		topnum = int(topnum/hcf)
		bottom = int(bottom/hcf)
		topcoeff = int(topcoeff/hcf)
		if topcoeff==0:
			top = str(topnum)
		elif topnum==0:
			if topcoeff==1:
				top = "\\sqrt{" + str(surd) + "}"	
			elif topcoeff==-1:
				top = " - \\sqrt{" + str(surd) + "}"	
			else:
				top = str(topcoeff) + "\\sqrt{" + str(surd) + "}"	
		elif topcoeff==-1:
			top = str(topnum) + " - \\sqrt{" + str(surd) + "}"	
		elif topcoeff==1:
			top = str(topnum) + " + \\sqrt{" + str(surd) + "}"	
		elif topcoeff<0:
			top = str(topnum) + " - " + str(abs(topcoeff)) + "\\sqrt{" + str(surd) + "}"	
		else:
			top = str(topnum) + " + " + str(abs(topcoeff)) + "\\sqrt{" + str(surd) + "}"	
		if bottom==1:
			answer = "$" + top + "$"
		else:
			answer = "$\\dfrac{" + top + "}{" + str(bottom) + "}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
