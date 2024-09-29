#!/usr/bin/env python3
#linear.py

def writegradient(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,6) * (-1)**random.randrange(1,3)
		intercepts = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
		intercepts.remove(gradient)
		intercept = random.choice(intercepts)
		if intercept<0:
			sign = " - "
			intercept = abs(intercept)
		elif intercept==0:
			sign = ""
			intercept = ""
		else:
			sign = " + "
			intercept = abs(intercept)
		answer = gradient
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		equation = "y = " + str(gradient) + "x" + sign + str(intercept)
#write question
		tempquestions.write("Write down the gradient of the line " + equation)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def writeintercept(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,6) * (-1)**random.randrange(1,3)
		intercepts = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
		intercepts.remove(gradient)
		intercept = random.choice(intercepts)
		answer = intercept
		if intercept<0:
			sign = " - "
			intercept = abs(intercept)
		elif intercept==0:
			sign = ""
			intercept = ""
		else:
			sign = " + "
			intercept = abs(intercept)
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		equation = "y = " + str(gradient) + "x" + sign + str(intercept)
#write question
		tempquestions.write("Write down where the line " + equation + " crosses the y-axis")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def writeequation(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,6) * (-1)**random.randrange(1,3)
		intercepts = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
		intercepts.remove(gradient)
		intercept = random.choice(intercepts)
		answer = intercept
		if intercept<0:
			sign = " - "
			intercept = abs(intercept)
		elif intercept==0:
			sign = ""
			intercept = ""
		else:
			sign = " + "
			intercept = abs(intercept)
		question = "Write down the equation of the line that has a gradient of " + str(gradient) + " and crosses the y-axis at " + str(answer)
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		equation = "y = " + str(gradient) + "x" + sign + str(intercept)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)


def plotlinpos(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		m = random.randrange(1,4)
		c = random.randrange(-5,6)
		xs = [1,2,3]
		ys = []
		for i in range(0,3):
			ys.append(m*xs[i] + c)
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " \\\\ \\hline y & & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + "\\\\ \\hline \\end{tabular}"
		xmin = -2
		xmax = 4
		if c<0:
			ymin = c-1
		else:
			ymin = -1
		if ys[2]>0:
			ymax = ys[2]+1
		else:
			ymax = 1
		graph = "\\begin{gnuplot}[terminal=pdf] set nokey; set grid; set border 0; set xtics axis 1; set ytics axis 1; set size ratio 2; set size 1,1; set zeroaxis linewidth 2 linetype 1; set yrange [" + str(ymin) + ":" + str(ymax) + "]; set xrange [" + str(xmin) + ":" + str(xmax) + "]; plot " + str(m) + "*x+" + str(c) + " \end{gnuplot}"
		if c>0:
			sign = " + "
		elif c<0:
			sign = " - "
			c = abs(c)
		else:
			sign = ""
			c = ""
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		else:
			m = abs(m)
		equation = "y = " + str(m) + "x" + sign + str(c)
		question =  equation + "\\hfill" + qtable + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		answer = "\\begin{minipage}{0.2\\textwidth}" + equation + nl + atable + "\\end{minipage} \\hfill \\begin{minipage}{0.7\\textwidth}" + graph + " \\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def plotlinneg(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		m = random.randrange(-3,0)
		c = random.randrange(0,10)
		xs = [1,2,3]
		ys = []
		for i in range(0,3):
			ys.append(m*xs[i] + c)
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " \\\\ \\hline y & & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\centering\\begin{tabular}{|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + "\\\\ \\hline \\end{tabular}"
		xmin = -2
		xmax = 4
		if c<0:
			ymax = 1
		else:
			ymax = c + 1
		if ys[2]>0:
			ymin = -1
		else:
			ymin = ys[2] - 1
		graph = "\\begin{gnuplot}[terminal=pdf] set nokey; set grid; set border 0; set xtics axis 1; set ytics axis 1; set size ratio 2; set size 1,1; set zeroaxis linewidth 2 linetype 1; set yrange [" + str(ymin) + ":" + str(ymax) + "]; set xrange [" + str(xmin) + ":" + str(xmax) + "]; plot " + str(m) + "*x+" + str(c) + " \end{gnuplot}"
		if c==0:
			c = ""
			sign = "-"
		else:
			sign = " - "
		if m==-1:
			m = ""
		else:
			m = abs(m)
		equation = "y = " + str(c) + sign + str(m) + "x"
		question =  equation + "\\hfill" + qtable + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		answer = "\\begin{minipage}{0.2\\textwidth}" + equation + nl + atable + "\\end{minipage} \\hfill \\begin{minipage}{0.7\\textwidth}" + graph + " \\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def showperp(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nums = (1,2,1,2,1,3,2,3,4,1,5,4,3,5,2,5,3,7,4,5,6,7,8)
		dens = (5,9,4,7,3,8,5,7,9,2,9,7,5,8,3,7,4,9,5,6,7,8,9)
		dec = random.randrange(0,len(nums))
		num1 = nums[dec]
		num2 = dens[dec]
		if random.randrange(0,2)==1:
			temp = num1
			num1 = num2
			num2 = temp
		if random.randrange(0,2)==1:
			sign1 = " - "
		else:
			sign1 = " + "
		if random.randrange(0,2)==1:
			sign2 = " - "
		else:
			sign2 = " + "
		answer = "$\\dfrac{" + str(num2) + "}{" + str(num1) + "} \\times -\\dfrac{" + str(num1) + "}{" + str(num2) + "} = -1$"
		if num1==1:
			num1=""
		if num2==1:
			num2=""
		equation1 = str(num1) + "y = " + str(num2) + "x" + sign1 + str(random.randrange(1,51))
		equation2 = str(num2) + "y = -" + str(num1) + "x" + sign2 + str(random.randrange(1,51))
		if random.randrange(0,2)==1:
			temp = equation1
			equation1 = equation2
			equation2 = temp
		question = "Show that the line " + equation1 + " is perpendicular to the line " + equation2
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def equationofline1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that passes through "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		if gradient%1==0:
			gradient = int(gradient)
			x2 = random.randrange(1,6)*(-1)**random.randrange(1,3)
		else:
			x2 = random.randrange(1,4)*(-1)**random.randrange(1,3)*2
		coo1 = "\\mbox{(0 , 0)}"
		y2 = x2*gradient
		if y2%1==0:
			y2 = int(y2)
		coo2 = "\\mbox{(" + str(x2) + " , " + str(y2) + ")}"
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		equation = "\\mbox{y = " + str(gradient) + "x}"
		question = explanation + coo1 + " and " + coo2
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)



def equationofline2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that passes through "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		c = random.randrange(1,6)*(-1)**random.randrange(1,3)
		if gradient%1==0:
			gradient = int(gradient)
			x2 = random.randrange(1,6)*(-1)**random.randrange(1,3)
		else:
			x2 = random.randrange(1,4)*(-1)**random.randrange(1,3)*2
		coo1 = "\\mbox{(0 , " + str(c) + ")}"
		
		y2 = c + x2*gradient
		if y2%1==0:
			y2 = int(y2)
		coo2 = "\\mbox{(" + str(x2) + " , " + str(y2) + ")}"
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
		question = explanation + coo1 + " and " + coo2
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)


def equationofline3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that passes through "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		c = random.randrange(1,6)*(-1)**random.randrange(1,3)
		if gradient%1==0:
			gradient = int(gradient)
			xs = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
			x1 = random.choice(xs)
			xs.remove(x1)
			x2 = random.choice(xs)
		else:
			xs = [2,4,6,-2,-4,-6]
			x1 = random.choice(xs)
			xs.remove(x1)
			x2 = random.choice(xs)
		y1 = c + x1*gradient
		if y1%1==0:
			y1 = int(y1)
		coo1 = "\\mbox{(" + str(x1) + " , " + str(y1) + ")}"
		y2 = c + x2*gradient
		if y2%1==0:
			y2 = int(y2)
		coo2 = "\\mbox{(" + str(x2) + " , " + str(y2) + ")}"
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
		question = explanation + coo1 + " and " + coo2
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)



def equationofline4(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that passes "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		c = random.randrange(1,6)*(-1)**random.randrange(1,3)
		if gradient%1==0:
			gradient = int(gradient)
			xs = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
			x1 = random.choice(xs)
		else:
			xs = [2,4,6,-2,-4,-6]
			x1 = random.choice(xs)
		y1 = c + x1*gradient
		if y1%1==0:
			y1 = int(y1)
		coo1 = "\\mbox{(" + str(x1) + " , " + str(y1) + ")}"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		question = explanation + "through " + coo1 + " and has a gradient of " + str(gradient)
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)


def equationoflineperp(n,explanationn):
	import random
	from math import floor,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that is "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		c = random.randrange(1,6)*(-1)**random.randrange(1,3)
		if gradient%1==0:
			gradient = int(gradient)
			xs = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
			x1 = random.choice(xs)
		else:
			xs = [2,4,6,-2,-4,-6]
			x1 = random.choice(xs)
		y1 = c + x1*gradient
		if y1%1==0:
			y1 = int(y1)
		coo1 = "\\mbox{(" + str(x1) + " , " + str(y1) + ")}"
		gradient2 = rounddp((-1)/gradient,2)
		c2 = rounddp(y1-(((-1)/gradient) * x1),2)
		if c2%1==0:
			c2 = int(c2)
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		if gradient2%1==0:
			gradient2 = int(gradient2)
		if gradient2==1:
			gradient2 = ""
		if gradient2==-1:
			gradient2 = "-"
		if c2<0:
			sign2 = " - "
		else:
			sign2 = " + "
		c2 = abs(c2)
		if c2==0.33:
			c2 = "$\\dfrac{1}{3}$"
		elif c2==0.67:
			c2 = "$\\dfrac{2}{3}$"
		elif rounddp(c2-floor(c2),2)==0.33:
			c2 = str(floor(c2)) + "$\\dfrac{1}{3}$"
		elif rounddp(c2-floor(c2),2)==0.67:
			c2 = str(floor(c2)) + "$\\dfrac{2}{3}$"
		if gradient2==0.33:
			gradient2 = "$\\dfrac{1}{3}$"
		if gradient2==-0.33:
			gradient2 = "-$\\dfrac{1}{3}$"
		if gradient2==0.67:
			gradient2 = "$\\dfrac{2}{3}$"
		if gradient2==-0.67:
			gradient2 = "-$\\dfrac{2}{3}$"

		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
		question = explanation + "perpendicular to " + equation + " at the point " + coo1
		answer = "\\mbox{y = " + str(gradient2) + "x" + sign2 + str(c2) + "}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def equationoflinepara(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that passes "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		cs = [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
		c = random.choice(cs)
		cs.remove(c)
		c2 = random.choice(cs)
		if gradient%1==0:
			gradient = int(gradient)
			xs = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
			x1 = random.choice(xs)
		else:
			xs = [2,4,6,-2,-4,-6]
			x1 = random.choice(xs)
		y1 = c + x1*gradient
		if y1%1==0:
			y1 = int(y1)
		coo1 = "\\mbox{(" + str(x1) + " , " + str(y1) + ")}"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		if c2<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
		equationq = "\\mbox{y = " + str(gradient) + "x" + sign2 + str(abs(c2)) + "}"
		question = explanation + "through " + coo1 + " and is parallel to " + equationq
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)


def identifygraphs1(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		gradients = [0.5,1,1.5,2,2.5,3,3.5,4]
		m = random.choice(gradients) * (-1)**random.randrange(1,3)
		c = random.randrange(-8,9)
		if abs(-8 * m + c)<=8:
			x1 = -8
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -8
				x1 = (y1 - c)/m
			else:
				y1 = 8
				x1 = (y1 - c)/m
		if abs(8 * m + c)<=8:
			x2 = 8
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -8
				x2 = (y2 - c)/m
			else:
				y2 = 8
				x2 = (y2 - c)/m
		x1 = (x1+8)*0.4203125 + 0.135
		y1 = (y1+8)*0.42 + 0.18
		x2 = (x2+8)*0.4203125 + 0.135
		y2 = (y2+8)*0.42 + 0.18
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[thin]" + coo1 + " coordinate -- " + coo2 + " coordinate; \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			answer = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			answer = "y = " + str(m) + "x" + sign + str(c)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def equationoflinepara(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:	
			explanation = "Find the equation of the line that passes "
		else:
			explanation = ""
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		cs = [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
		c = random.choice(cs)
		cs.remove(c)
		c2 = random.choice(cs)
		if gradient%1==0:
			gradient = int(gradient)
			xs = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
			x1 = random.choice(xs)
		else:
			xs = [2,4,6,-2,-4,-6]
			x1 = random.choice(xs)
		y1 = c + x1*gradient
		if y1%1==0:
			y1 = int(y1)
		coo1 = "\\mbox{(" + str(x1) + " , " + str(y1) + ")}"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		if c2<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
		equationq = "\\mbox{y = " + str(gradient) + "x" + sign2 + str(abs(c2)) + "}"
		question = explanation + "through " + coo1 + " and is parallel to " + equationq
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)


def identifygraphs2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		gradients = [0.5,1,1.5,2,2.5,3,3.5,4]
		m = random.choice(gradients) * (-1)**random.randrange(1,3)
		c = random.randrange(-8,9)
		if abs(-4 * m + c)<=8:
			x1 = -4
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -8
				x1 = (y1 - c)/m
			else:
				y1 = 8
				x1 = (y1 - c)/m
		if abs(4 * m + c)<=8:
			x2 = 4
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -8
				x2 = (y2 - c)/m
			else:
				y2 = 8
				x2 = (y2 - c)/m
		x11 = (2*x1+8)*0.4203125 + 0.135
		y1 = (y1+8)*0.42 + 0.18
		x22 = (2*x2+8)*0.4203125 + 0.135
		y2 = (y2+8)*0.42 + 0.18
		coo1 = "(" + str(x11) + " , " + str(y1) + ")"
		coo2 = "(" + str(x22) + " , " + str(y2) + ")"
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid2}}; \\draw[thin]" + coo1 + " coordinate -- " + coo2 + " coordinate; \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			answer = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			answer = "y = " + str(m) + "x" + sign + str(c)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def identifygraphs3(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		gradients = [0.5,1,1.5,2,2.5,3,3.5,4]
		m = random.choice(gradients) * (-1)**random.randrange(1,3)
		c = random.randrange(-4,5)
		if abs(-8 * m + c)<=4:
			x1 = -8
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -4
				x1 = (y1 - c)/m
			else:
				y1 = 4
				x1 = (y1 - c)/m
		if abs(8 * m + c)<=4:
			x2 = 8
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -4
				x2 = (y2 - c)/m
			else:
				y2 = 4
				x2 = (y2 - c)/m
		x1 = (x1+8)*0.4203125 + 0.135
		y11 = (2*y1+8)*0.42 + 0.18
		x2 = (x2+8)*0.4203125 + 0.135
		y22 = (2*y2+8)*0.42 + 0.18
		coo1 = "(" + str(x1) + " , " + str(y11) + ")"
		coo2 = "(" + str(x2) + " , " + str(y22) + ")"
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid3}}; \\draw[thin]" + coo1 + " coordinate -- " + coo2 + " coordinate; \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			answer = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			answer = "y = " + str(m) + "x" + sign + str(c)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def threegraphsfour(n,explanationn):
	import random
	from math import gcd
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		if explanationn==1:	
			explanation = "Plot on a -8 to 8 grid: \\\\[0.2cm] "
		else:
			explanation = ""

		sf = 0.5375

#y = mx + c
		gradients = [1,2,3,4]
		m = random.choice(gradients) * (-1)**random.randrange(1,3)
		if m<0:
			grad1 = 1
		else:
			grad1 = -1
		c = random.randrange(-8,9)
		if abs(-8 * m + c)<=8:
			x1 = -8
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -8
				x1 = (y1 - c)/m
			else:
				y1 = 8
				x1 = (y1 - c)/m
		if abs(8 * m + c)<=8:
			x2 = 8
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -8
				x2 = (y2 - c)/m
			else:
				y2 = 8
				x2 = (y2 - c)/m
		x1 = (x1+8)*0.4203125*sf + 0.135*sf
		y1 = (y1+8)*0.42*sf + 0.18*sf
		x2 = (x2+8)*0.4203125*sf + 0.135*sf
		y2 = (y2+8)*0.42*sf + 0.18*sf
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		graph1 = "\\draw[thick]" + coo1 + " coordinate -- " + coo2 + " coordinate;"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			equation1 = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			equation1 = "y = " + str(m) + "x" + sign + str(c)
#cover up
		x = random.randrange(1,8)
		y = random.randrange(1,8)
		xs = [1,2,3,4,6,8,9]
		x = random.choice(xs)
		y = random.choice(xs)
		c = x * y
		hcf = abs(gcd(gcd(x,y),c))
		printx = int(x/hcf)
		printy = int(y/hcf)
		if printx==1:
			printx = ""
		if printy==1:
			printy = ""
		if grad1>0:
			if random.randrange(0,2)==1:
				equation2 = str(printx) + "y - " + str(printy) + "x = " + str(int(c/hcf))
				y = y * -1
			else:
				equation2 = str(printy) + "x - " + str(printx) + "y = " + str(int(c/hcf))
				x = x * -1
		else:
			equation2 = str(printy) + "x + " + str(printx) + "y = " + str(int(c/hcf))
		m = -1 * y/x
		c = c/x 
		if abs(-8 * m + c)<=8:
			x1 = -8
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -8
				x1 = (y1 - c)/m
			else:
				y1 = 8
				x1 = (y1 - c)/m
		if abs(8 * m + c)<=8:
			x2 = 8
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -8
				x2 = (y2 - c)/m
			else:
				y2 = 8
				x2 = (y2 - c)/m
		x1 = (x1+8)*0.4203125*sf + 0.135*sf
		y1 = (y1+8)*0.42*sf + 0.18*sf
		x2 = (x2+8)*0.4203125*sf + 0.135*sf
		y2 = (y2+8)*0.42*sf + 0.18*sf
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		graph2 = "\\draw[thick]" + coo1 + " coordinate -- " + coo2 + " coordinate;"
#simple
		temp = random.randrange(1,8) * (-1)**random.randrange(1,3)
		if random.randrange(0,2)==1:
			x1 = x2 = temp
			y1 = -8
			y2 = 8
			equation3 = "x = " + str(temp)
		else: 
			y1 = y2 = temp
			x1 = -8
			x2 = 8
			equation3 = "y = " + str(temp)
		x1 = (x1+8)*0.4203125*sf + 0.135*sf
		y1 = (y1+8)*0.42*sf + 0.18*sf
		x2 = (x2+8)*0.4203125*sf + 0.135*sf
		y2 = (y2+8)*0.42*sf + 0.18*sf
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		graph3 = "\\draw[thick]" + coo1 + " coordinate -- " + coo2 + " coordinate;"
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.43]{shape/images/coordinategrid}};" + graph1 + graph2 + graph3 + "  \\end{tikzpicture}"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			answer = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			answer = "y = " + str(m) + "x" + sign + str(c)
		question = "a) " + equation3 + "\\\\[0.2cm] b) " + equation1 + "\\\\[0.2cm] c) " + equation2
		answer = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def threegraphs(n,explanationn):
	import random
	from math import gcd
	from fractions import Fraction
	for x in range(0, n):
		if explanationn==1:	
			explanation = "Plot on a -8 to 8 grid: \\\\[0.2cm] "
		else:
			explanation = ""
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")


#y = mx + c
		gradients = [1,2,3,4]
		m = random.choice(gradients) * (-1)**random.randrange(1,3)
		if m<0:
			grad1 = 1
		else:
			grad1 = -1
		c = random.randrange(-8,9)
		if abs(-8 * m + c)<=8:
			x1 = -8
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -8
				x1 = (y1 - c)/m
			else:
				y1 = 8
				x1 = (y1 - c)/m
		if abs(8 * m + c)<=8:
			x2 = 8
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -8
				x2 = (y2 - c)/m
			else:
				y2 = 8
				x2 = (y2 - c)/m
		x1 = (x1+8)*0.4203125 + 0.135
		y1 = (y1+8)*0.42 + 0.18
		x2 = (x2+8)*0.4203125 + 0.135
		y2 = (y2+8)*0.42 + 0.18
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		graph1 = "\\draw[thick]" + coo1 + " coordinate -- " + coo2 + " coordinate;"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			equation1 = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			equation1 = "y = " + str(m) + "x" + sign + str(c)
#cover up
		x = random.randrange(1,8)
		y = random.randrange(1,8)
		xs = [1,2,3,4,6,8,9]
		x = random.choice(xs)
		y = random.choice(xs)
		c = x * y
		hcf = abs(gcd(gcd(x,y),c))
		printx = int(x/hcf)
		printy = int(y/hcf)
		if printx==1:
			printx = ""
		if printy==1:
			printy = ""
		if grad1>0:
			if random.randrange(0,2)==1:
				equation2 = str(printx) + "y - " + str(printy) + "x = " + str(int(c/hcf))
				y = y * -1
			else:
				equation2 = str(printy) + "x - " + str(printx) + "y = " + str(int(c/hcf))
				x = x * -1
		else:
			equation2 = str(printy) + "x + " + str(printx) + "y = " + str(int(c/hcf))
		m = -1 * y/x
		c = c/x 
		if abs(-8 * m + c)<=8:
			x1 = -8
			y1 = m * x1 + c
		else:
			if m>0:
				y1 = -8
				x1 = (y1 - c)/m
			else:
				y1 = 8
				x1 = (y1 - c)/m
		if abs(8 * m + c)<=8:
			x2 = 8
			y2 = m * x2 + c
		else:
			if m<0:
				y2 = -8
				x2 = (y2 - c)/m
			else:
				y2 = 8
				x2 = (y2 - c)/m
		x1 = (x1+8)*0.4203125 + 0.135
		y1 = (y1+8)*0.42 + 0.18
		x2 = (x2+8)*0.4203125 + 0.135
		y2 = (y2+8)*0.42 + 0.18
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		graph2 = "\\draw[thick]" + coo1 + " coordinate -- " + coo2 + " coordinate;"
#simple
		temp = random.randrange(1,8) * (-1)**random.randrange(1,3)
		if random.randrange(0,2)==1:
			x1 = x2 = temp
			y1 = -8
			y2 = 8
			equation3 = "x = " + str(temp)
		else: 
			y1 = y2 = temp
			x1 = -8
			x2 = 8
			equation3 = "y = " + str(temp)
		x1 = (x1+8)*0.4203125 + 0.135
		y1 = (y1+8)*0.42 + 0.18
		x2 = (x2+8)*0.4203125 + 0.135
		y2 = (y2+8)*0.42 + 0.18
		coo1 = "(" + str(x1) + " , " + str(y1) + ")"
		coo2 = "(" + str(x2) + " , " + str(y2) + ")"
		graph3 = "\\draw[thick]" + coo1 + " coordinate -- " + coo2 + " coordinate;"
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}};" + graph1 + graph2 + graph3 + "  \\end{tikzpicture}"
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			answer = "y = " + str(m) + "x"
		else:
			if c<0:
				sign = " - "
				c = abs(c)
			else:
				sign = " + "
			answer = "y = " + str(m) + "x" + sign + str(c)
		question = "a) " + equation3 + "\\\\[0.2cm] b) " + equation1 + "\\\\[0.2cm] c) " + equation2
		answer = image
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def tablemethod1(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,5)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.6cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.6cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = "Gradient = " + str(gradient) + ", y-intercept = " + str(yintercept)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def tablemethod2(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,5)*(-1)**random.randrange(0,2)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.6cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.6cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = "Gradient = " + str(gradient) + ", y-intercept = " + str(yintercept)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def tablemethod3(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,11)/2
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = "Gradient = " + str(gradient) + ", y-intercept = " + str(yintercept)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def tablemethod4(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,11)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = "Gradient = " + str(gradient) + ", y-intercept = " + str(yintercept)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def tablemethod5(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,11)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def tablemethod6(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,6) * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ys = [ys[0],ys[1],"","","","",""]
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def tablemethod7(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,11)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ys = [ys[0],ys[1],"","","","",""]
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def tablemethod8(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,5) * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		ys2 = ["","","","","","",""]
		x1 = random.randrange(0,4)
		x2 = random.randrange(x1+2,7)
		ys2[x1] = ys[x1]
		ys2[x2] = ys[x2]
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ys = ys2
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def tablemethod9(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,12)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		ys2 = ["","","","","","",""]
		x1 = random.randrange(0,4)
		x2 = random.randrange(x1+2,7)
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		ys2[x1] = ys[x1]
		ys2[x2] = ys[x2]
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ys = ys2
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		answer = atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def tablemethod10(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,5) * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		ys2 = ["","","","","","",""]
		x1 = random.randrange(0,4)
		x2 = random.randrange(x1+2,7)
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		ys2[x1] = ys[x1]
		ys2[x2] = ys[x2]
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ys = ys2
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def tablemethod11(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,12)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-5,6)
		xs = [-3,-2,-1,0,1,2,3]
		ys = [yintercept-3*gradient,yintercept-2*gradient,yintercept-gradient,yintercept,yintercept+gradient,yintercept+2*gradient,yintercept+3*gradient]
		ys2 = ["","","","","","",""]
		x1 = random.randrange(0,4)
		x2 = random.randrange(x1+2,7)
		for i in range(0,len(ys)):
			if ys[i]%1==0:
				ys[i] = int(ys[i])
		ys2[x1] = ys[x1]
		ys2[x2] = ys[x2]
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ys = ys2
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def tablemethod12(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,5) * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-10,11)
		x1 = 0
		y1 = x1 * gradient + yintercept
		x2 = x1 + random.randrange(4,11)*(-1)**random.randrange(0,2)
		y2 = x2 * gradient + yintercept
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		
		if x2<x1:
			x1,y1,x2,y2 = x2,y2,x1,y1
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\arrayrulecolor{myfg}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{C|CCC}  x & " + str(x1) + " & & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & & " + str(y2) + "\\end{tabular}\\arrayrulecolor{mybg}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def tablemethod13(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,12)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-10,11)
		x1 = 0
		y1 = x1 * gradient + yintercept
		x2 = x1 + random.randrange(4,11)*(-1)**random.randrange(0,2)
		y2 = x2 * gradient + yintercept
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		
		if x2<x1:
			x1,y1,x2,y2 = x2,y2,x1,y1
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\arrayrulecolor{myfg}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{C|CCC}  x & " + str(x1) + " & & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & & " + str(y2) + "\\end{tabular}\\arrayrulecolor{mybg}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))





def tablemethod14(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(1,5) * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-10,11)
		x1 = 0 + random.randrange(1,6) * (-1)**random.randrange(0,2)
		y1 = x1 * gradient + yintercept
		x2 = 0
		while x2==0:
			x2 = x1 + random.randrange(4,11)*(-1)**random.randrange(0,2)
		y2 = x2 * gradient + yintercept
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		
		if x2<x1:
			x1,y1,x2,y2 = x2,y2,x1,y1
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\arrayrulecolor{myfg}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{C|CCC}  x & " + str(x1) + " & & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & & " + str(y2) + "\\end{tabular}\\arrayrulecolor{mybg}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def tablemethod15(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		gradient = random.randrange(2,12)/2 * (-1)**random.randrange(0,2)
		if gradient%1==0:
			gradient = int(gradient)
		yintercept = random.randrange(-10,11)
		x1 = 0 + random.randrange(1,6) * (-1)**random.randrange(0,2)
		y1 = x1 * gradient + yintercept
		x2 = 0
		while x2==0:
			x2 = x1 + random.randrange(4,11)*(-1)**random.randrange(0,2)
		y2 = x2 * gradient + yintercept
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		
		if x2<x1:
			x1,y1,x2,y2 = x2,y2,x1,y1
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\arrayrulecolor{myfg}\\newcolumntype{C}{>{\centering\\arraybackslash} m{0.9cm} }\\begin{tabular}{C|CCC}  x & " + str(x1) + " & & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & & " + str(y2) + "\\end{tabular}\\arrayrulecolor{mybg}"
		question = qtable
		if gradient==1:
			gradient = ""
		elif gradient==-1:
			gradient = "-"
		if yintercept<0:
			sign = " - "
		else:
			sign = " + "
		if yintercept==0:
			answer = "y = " + str(gradient) + "x"
		else:
			answer = "y = " + str(gradient) + "x" + sign + str(abs(yintercept))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
