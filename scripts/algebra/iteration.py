#iteration.py

def iterationquad1(n,explanationn):
	import random
	from math import floor,sqrt,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		x2 = 314159
#this while loop is because sometimes (e.g. a=4 b=3 c=-2) the derivative closer to 1 doesnt work out. this cycles until it does work out. no idea why this happens but this works.
		while x2==314159:
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
			root1 = rounddp((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
			root2 = rounddp((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
			if abs(root1)<abs(root2):
				root = root1
			else:
				root = root2
			upper = ceil(root)
			lower = floor(root)
			try:
				der1 = (0-b)/(2 * sqrt(a) * sqrt(0 - c - b*root))
			except Exception:
				der1 = 1000
			der2 = (0 - 2*a*root)/b
			if der1>1 and der2>1:
				if der1<der2:
					der = der1
				else:
					der = der2
			elif der1>1:
				der = der2
			elif der2>1:
				der = der1
			else:
				if der1>der2:
					der = der1
				else:
					der = der2
			x0 = 0
			if der==der1:
				d = 0-c
				e = 0-b
				f = a
				x1 = sqrt((d + e*x0)/f)
	#			x2 = sqrt((d + e*x1)/f)
				try:
					x2 = sqrt((d + e*x1)/f)
				except Exception:
					x2 = 314159
	#			x3 = sqrt((d + e*x2)/f)
				if x2==314159:
					x3 = 2
				else:
					x3 = sqrt((d + e*x2)/f)
				if f<0:
					d = 0-d
					e = 0-e
					f = 0-f
				if e<0:
					e = abs(e)
					if e==1:
						e = ""
					rearranged = "$x = \\sqrt{\\dfrac{" + str(d) + " - " + str(e) + "x}{" + str(f) + "}}$"
					rearrangedit = "$x_{n+1} = \\sqrt{\\dfrac{" + str(d) + " - " + str(e) + "x_{n}}{" + str(f) + "}}$"
				else:
					if d>0:
						signre = " + "
					else:
						signre = " - "
					if e==1:
						e = ""
					elif e==-1:
						e = "-"
					rearranged = "$x = \\sqrt{\\dfrac{" + str(e) + "x" + signre + str(abs(d)) + "}{" + str(f) + "}}$"
					rearrangedit = "$x_{n+1} = \\sqrt{\\dfrac{" + str(e) + "x_{n}" + signre + str(abs(d)) + "}{" + str(f) + "}}$"
			else:
				d = 0-c
				e = 0-a
				f = b
				x1 = (d + e*x0**2)/f
				x2 = (d + e*x1**2)/f
				x3 = (d + e*x2**2)/f
				if f<0:
					d = 0-d
					e = 0-e
					f = 0-f
				if e>0 and d<0:
					if e==1:
						e = ""
					elif e==-1:
						e = "-"
					rearranged = "$x = \\dfrac{" + str(e) + "x^{2} - " + str(abs(d)) + "}{" + str(f) + "}$"
					rearrangedit = "$x_{n+1} = \\dfrac{" + str(e) + "x_{n}\\hspace{0pt}^{2} - " + str(abs(d)) + "}{" + str(f) + "}$"
				elif e<0 and d>0:
					e = abs(e)
					if e==1:
						e = ""
					rearranged = "$x = \\dfrac{" + str(d) + " - " + str(e) + "x^{2}}{" + str(f) + "}$"
					rearrangedit = "$x_{n+1} = \\dfrac{" + str(d) + " - " + str(e) + "x_{n}\\hspace{0pt}^{2}}{" + str(f) + "}$"
				else:
					if d<0:
						signre = " - "
					else:
						signre = " + "
					if e==1:
						e = ""
					elif e==-1:
						e = "-"
					rearranged = "$x = \\dfrac{" + str(e) + "x^{2}" + signre + str(abs(d)) + "}{" + str(f) + "}$"
					rearrangedit = "$x_{n+1} = \\dfrac{" + str(e) + "x_{n}\\hspace{0pt}^{2}" + signre + str(abs(d)) + "}{" + str(f) + "}$"
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
		if x1%1==0:
			x1 = int(x1)
		else:
			x1 = rounddp(x1,5)
		if x2%1==0:
			x2 = int(x2)
		else:
			x2 = rounddp(x2,5)
		if x3%1==0:
			x3 = int(x3)
		else:
			x3 = rounddp(x3,5)
		equation = "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + " = 0$"
		questiona = "(a) Show that the equation " + equation + " has a solution between " + str(lower) + " and " + str(upper) + "."
		questionb = "(b) Show that the equation " + equation  + " can be rearranged to give " + rearranged + "."
		if random.randrange(0,2)==0:
			end = "an approximate solution to " + equation
		else:
			end = "$x_{1}, x_{2}$ and $x_{3}$"
		questionc = "(c) Starting with $x_{0}$ = " + str(x0) + ", use the iteration formula " + rearrangedit + " three times to find " + end + "."
		question = "original " + equation + " rearranged " + rearranged
		question = questiona + nl + questionb + nl + questionc
		answer = "$x_{1}$ = " + str(x1) + nl + "$x_{2}$ = " + str(x2) + nl + "$x_{3}$ = " + str(x3)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def iterationquad1lite(n,explanationn):
	import random
	from math import floor,sqrt,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		x2 = 314159
#this while loop is because sometimes (e.g. a=4 b=3 c=-2) the derivative closer to 1 doesnt work out. this cycles until it does work out. no idea why this happens but this works.
		while x2==314159:
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
			root1 = rounddp((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
			root2 = rounddp((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
			if abs(root1)<abs(root2):
				root = root1
			else:
				root = root2
			upper = ceil(root)
			lower = floor(root)
			try:
				der1 = (0-b)/(2 * sqrt(a) * sqrt(0 - c - b*root))
			except Exception:
				der1 = 1000
			der2 = (0 - 2*a*root)/b
			if der1>1 and der2>1:
				if der1<der2:
					der = der1
				else:
					der = der2
			elif der1>1:
				der = der2
			elif der2>1:
				der = der1
			else:
				if der1>der2:
					der = der1
				else:
					der = der2
			x0 = 0
			if der==der1:
				d = 0-c
				e = 0-b
				f = a
				x1 = sqrt((d + e*x0)/f)
	#			x2 = sqrt((d + e*x1)/f)
				try:
					x2 = sqrt((d + e*x1)/f)
				except Exception:
					x2 = 314159
	#			x3 = sqrt((d + e*x2)/f)
				if x2==314159:
					x3 = 2
				else:
					x3 = sqrt((d + e*x2)/f)
				if f<0:
					d = 0-d
					e = 0-e
					f = 0-f
				if e<0:
					e = abs(e)
					if e==1:
						e = ""
					rearrangedit = "$x_{n+1} = \\sqrt{\\dfrac{" + str(d) + " - " + str(e) + "x_{n}}{" + str(f) + "}}$"
				else:
					if d>0:
						signre = " + "
					else:
						signre = " - "
					if e==1:
						e = ""
					elif e==-1:
						e = "-"
					rearrangedit = "$x_{n+1} = \\sqrt{\\dfrac{" + str(e) + "x_{n}" + signre + str(abs(d)) + "}{" + str(f) + "}}$"
			else:
				d = 0-c
				e = 0-a
				f = b
				x1 = (d + e*x0**2)/f
				x2 = (d + e*x1**2)/f
				x3 = (d + e*x2**2)/f
				if f<0:
					d = 0-d
					e = 0-e
					f = 0-f
				if e>0 and d<0:
					if e==1:
						e = ""
					elif e==-1:
						e = "-"
					rearrangedit = "$x_{n+1} = \\dfrac{" + str(e) + "x_{n}\\hspace{0pt}^{2} - " + str(abs(d)) + "}{" + str(f) + "}$"
				elif e<0 and d>0:
					e = abs(e)
					if e==1:
						e = ""
					rearrangedit = "$x_{n+1} = \\dfrac{" + str(d) + " - " + str(e) + "x_{n}\\hspace{0pt}^{2}}{" + str(f) + "}$"
				else:
					if d<0:
						signre = " - "
					else:
						signre = " + "
					if e==1:
						e = ""
					elif e==-1:
						e = "-"
					rearrangedit = "$x_{n+1} = \\dfrac{" + str(e) + "x_{n}\\hspace{0pt}^{2}" + signre + str(abs(d)) + "}{" + str(f) + "}$"
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
		if x1%1==0:
			x1 = int(x1)
		else:
			x1 = rounddp(x1,5)
		if x2%1==0:
			x2 = int(x2)
		else:
			x2 = rounddp(x2,5)
		if x3%1==0:
			x3 = int(x3)
		else:
			x3 = rounddp(x3,5)
		question = "Starting with $x_{0}$ = " + str(x0) + ", use the iteration formula " + rearrangedit + " three times to find $x_{1}, x_{2}$ and $x_{3}$."
		answer = "$x_{1}$ = " + str(x1) + ", $x_{2}$ = " + str(x2) + ", $x_{3}$ = " + str(x3)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
