#quadratics.py

def quadprep1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		a = random.randrange(1,13)
		b = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "a + b = " + str(a + b) + " and ab = " + str(a*b) )
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + " and " + str(b))

def quadprep2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		a = random.randrange(1,13)*(-1)**random.randrange(1,3)
		b = random.randrange(1,13)*(-1)**random.randrange(1,3)
#write question
		tempquestions.write(explanation + "a + b = " + str(a + b) + " and ab = " + str(a*b) )
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + " and " + str(b))


def expandquadraticspos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(1,13))
		d = 1
		e = random.choice(mylist)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")


def expandquadratics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")

def expandquadratics2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		tempquestions.write(explanation + "$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")

def expandquadraticsdots1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = e*-1
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")


def expandquadraticssquared1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = e
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")^2$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")


def factorisequadratics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )

def factorisequadratics2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )

def factorisequadraticsdots1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = e*-1
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )



def solvequadratics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = 1 
		else:
			sign1 = -1
		if g<0:
			sign2 = 1
		else:
			sign2 = -1
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(sign1*e) + "$ and $x = " + str(sign2*g) + "$")

def solvequadratics2(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = ""
		else:
			sign1 = "-"
		if g<0:
			sign2 = ""
		else:
			sign2 = "-"
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		int1 = ""
		int2 = ""
		if e%d==0:
			x1 = str(int(e/d))
		else:
			x1 = Fraction(e,d)
			if x1>1:
				int1 = int(floor(x1))
				x1 = x1 - int1
			x1 = "\\dfrac{" + str(x1.numerator) + "}{" + str(x1.denominator) + "}"
		if g%f==0:
			x2 = str(int(g/f))
		else:
			x2 = Fraction(g,f)
			if x2>1:
				int2 = int(floor(x2))
				x2 = x2 - int2
			x2 = "\\dfrac{" + str(x2.numerator) + "}{" + str(x2.denominator) + "}"
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + sign1 + str(int1) + x1 + "$ and $x = " + sign2 + str(int2) + x2 + "$")

def quadraticformula(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		a = random.randrange(1,6)
		b = random.randrange(1,13) * (-1)**random.randrange(1,3)
		c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while c==0:
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while sqrt(b**2 - 4*a*c)%1==0:
			a = random.randrange(1,6)
			b = random.randrange(1,13) * (-1)**random.randrange(1,3)
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
			while c==0:
				c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		x1 = round((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
		x2 = round((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
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
		if b==1:
			b = ""
		if a==1:
			a = ""
#write question
		tempquestions.write(explanation + "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("x = " + str(x1) + " and " + str(x2))


def completesquare(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write in the form $(x + a)^2 + b$: "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,7) * 2 * (-1)**random.randrange(1,3)
		c = list(range(-8,20))
		c.remove(0)
		c = random.choice(c) 
		adjuster = int(c - (b/2)**2)
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
		if b==1:
			b = ""
		if a==1:
			a = ""
		if adjuster<0:
			sign3 = " - "
			adjuster = abs(adjuster)
		else:
			sign3 = " + "
#write question
		tempquestions.write(explanation + "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(int(b/2)) + ")^2" + sign3 + str(adjuster) + "$")


def completesquaresolve(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve by completing the square and state the minimum point of"
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,7) * 2 * (-1)**random.randrange(1,3)
		cs = list(range(floor((b/2)**2)-8,floor((b/2)**2)))
		c = random.choice(cs) 
		while c==0:
			c = random.choice(cs) 
		adjuster = int(c - (b/2)**2)
		x1 = round((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
		x2 = round((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		minim = "(" + str(int(-b/2)) + " , " + str(adjuster) + ")"
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
		if b==1:
			b = ""
		if a==1:
			a = ""
		if adjuster<0:
			sign3 = " - "
			adjuster = abs(adjuster)
		else:
			sign3 = " + "
#write question
		tempquestions.write(explanation + "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("x = " + str(x1) + " and " + str(x2) + ", min = " + minim)
