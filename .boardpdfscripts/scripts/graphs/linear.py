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
		question =  " Complete this table for " + equation + " and draw the graph." + nl + qtable
		answer = equation + atable + graph
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
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + "\\\\ \\hline \\end{tabular}"
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
		question =  " Complete this table for " + equation + " and draw the graph." + nl + qtable
		answer = equation + atable + graph
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
