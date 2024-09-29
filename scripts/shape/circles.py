#circles.py

def circleareapi(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		radii = (2,3,4,5,6,8,9)
		radius = random.choice(radii)*10
		coeff = radius**2
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
#write question
		tempquestions.write(explanation + "A circle has a radius of " + str(radius) + "cm. Calculate the area of the circle, giving your answer as a multiple of " + pi)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(coeff) + pi + " cm$^2$")
			

def circlecircumferencerad(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		radius = random.randrange(2,40)*0.25
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		circumference = round(math.pi * 2 * radius,2)
		if radius%1==0:
			radius = int(radius)
#write question
		tempquestions.write(explanation + "A circle has a radius of " + str(radius) + "m. Calculate the circumference of the circle")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(circumference) + "m")
			


def circletablecircumferenceforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline &" + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline " + r[4] + " & & \\\\ \\hline" + r[5] + " & & \\\\ \\hline" + r[6]  + " & & \\\\ \\hline " + r[7] +  " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablecircumferencebackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			c[i] = random.choice(circumferences)
			circumferences.remove(c[i])
			d[i] = round(c[i]/math.pi,2)
			r[i] = round((c[i]/math.pi)/2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + c[0] + "\\\\ \\hline & & " + c[1] + "\\\\ \\hline & &" + c[2] + "\\\\ \\hline & &" + c[3] + "\\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablecircumferencefull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,4):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
		for i in range(4,8):
			c[i] = random.choice(circumferences)
			circumferences.remove(c[i])
			d[i] = round(c[i]/math.pi,2)
			r[i] = round((c[i]/math.pi)/2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline " + r[2] + " & & \\\\ \\hline " + r[3] + " & & \\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletableareaforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline " + r[2] + "&  & \\\\ \\hline " + r[3] + " & & \\\\ \\hline &" + d[4] + " & \\\\ \\hline & " + d[5] + "& \\\\ \\hline & " + d[6]  + "& \\\\ \\hline & " + d[7] +  " & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletableareabackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			a[i] = random.choice(areas)
			areas.remove(a[i])
			r[i] = round(math.sqrt(a[i]/math.pi),2)
			d[i] = round(2 * math.sqrt(a[i]/math.pi),2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + a[0] + "\\\\ \\hline & & " + a[1] + "\\\\ \\hline & & " + a[2] + "\\\\ \\hline & & " + a[3] + "\\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletableareafull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,4):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(4,8):
			a[i] = random.choice(areas)
			areas.remove(a[i])
			r[i] = round(math.sqrt(a[i]/math.pi),2)
			d[i] = round(2 * math.sqrt(a[i]/math.pi),2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline & " + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletablefullforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & & &  \\\\ \\hline " + r[1] + " & & & \\\\ \\hline " + r[2] + " & & & \\\\ \\hline " + r[3] + " & & & \\\\ \\hline &" + d[4] + " & & \\\\ \\hline & " + d[5] + " & & \\\\ \\hline & " + d[6]  + " & & \\\\ \\hline & " + d[7]   +  " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " & " + a[1]  + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " & " + a[2]  + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " & " + a[3]  + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " & " + a[4]  + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " & " + a[5]  + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " & " + a[6]  + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] + " & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablefull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,4):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(4,6):
			c[i] = random.choice(circumferences)
			circumferences.remove(c[i])
			d[i] = round(c[i]/math.pi,2)
			r[i] = round((c[i]/math.pi)/2,2)
			a[i] = round((c[i]**2)/(4*math.pi),2)
		for i in range(6,8):
			a[i] = random.choice(areas)
			areas.remove(a[i])
			r[i] = round(math.sqrt(a[i]/math.pi),2)
			d[i] = round(2 * math.sqrt(a[i]/math.pi),2)
			c[i] = round(math.sqrt(4 * a[i] * math.pi),2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & & &  \\\\ \\hline " + r[1] + " & & & \\\\ \\hline & " + d[2] + " & & \\\\ \\hline & " + d[3] + " & & \\\\ \\hline & &" + c[4] + " & \\\\ \\hline & & " + c[5] + " & \\\\ \\hline & & & " + a[6]  + " \\\\ \\hline & & & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " & " + a[1]  + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " & " + a[2]  + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " & " + a[3]  + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " & " + a[4]  + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " & " + a[5]  + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " & " + a[6]  + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] + " & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepicircumferenceforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline &" + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline " + r[4] + " & & \\\\ \\hline" + r[5] + " & & \\\\ \\hline" + r[6]  + " & & \\\\ \\hline " + r[7] +  " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepicircumferencebackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + c[0] + "\\\\ \\hline & & " + c[1] + "\\\\ \\hline & &" + c[2] + "\\\\ \\hline & &" + c[3] + "\\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepicircumferencefull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline " + r[2] + " & & \\\\ \\hline " + r[3] + " & & \\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletablepiareaforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline " + r[2] + "&  & \\\\ \\hline " + r[3] + " & & \\\\ \\hline &" + d[4] + " & \\\\ \\hline & " + d[5] + "& \\\\ \\hline & " + d[6]  + "& \\\\ \\hline & " + d[7] +  " & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepiareabackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + a[0] + "\\\\ \\hline & & " + a[1] + "\\\\ \\hline & & " + a[2] + "\\\\ \\hline & & " + a[3] + "\\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletablepiareafull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline & " + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepifull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & & &  \\\\ \\hline " + r[1] + " & & & \\\\ \\hline & " + d[2] + " & & \\\\ \\hline & " + d[3] + " & & \\\\ \\hline & &" + c[4] + " & \\\\ \\hline & & " + c[5] + " & \\\\ \\hline & & & " + a[6]  + " \\\\ \\hline & & & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " & " + a[1]  + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " & " + a[2]  + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " & " + a[3]  + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " & " + a[4]  + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " & " + a[5]  + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " & " + a[6]  + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] + " & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepifullforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & & &  \\\\ \\hline " + r[1] + " & & & \\\\ \\hline " + r[2] + " & & & \\\\ \\hline " + r[3] + " & & & \\\\ \\hline &" + d[4] + " & & \\\\ \\hline & " + d[5] + " & & \\\\ \\hline & " + d[6]  + " & & \\\\ \\hline & " + d[7]   +  " & & \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.5cm} | p{2.5cm} | p{2.5cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " & " + a[1]  + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " & " + a[2]  + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " & " + a[3]  + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " & " + a[4]  + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " & " + a[5]  + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " & " + a[6]  + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] + " & " + a[7]   +  " \\\\ \\hline \\end{tabular}"
		intro = "\\raggedright Copy and complete this table"
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circlearearadius(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area:\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			a = 60
			b = 53
		elif rotation==180:
			a = 16
			b = 53
		elif rotation==90:
			a = 52
			b = 65
		else:
			a = 52
			b = 25
		radius = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/circle1} \\put(" + str(a) + "," + str(b) + "){" + str(radius) + "cm" + "} \\end{overpic}"
		answer = rounddp(pi * radius**2,2)
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + " cm$^2$")


def circlecircumferenceradius(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the circumference:\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			a = 60
			b = 53
		elif rotation==180:
			a = 16
			b = 53
		elif rotation==90:
			a = 52
			b = 65
		else:
			a = 52
			b = 25
		radius = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/circle1} \\put(" + str(a) + "," + str(b) + "){" + str(radius) + "cm" + "} \\end{overpic}"
		answer = rounddp(pi * radius*2,2)
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + " cm")



def circleareadiameter(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area:\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,2)*90
		if rotation==0:
			a = 40
			b = 53
		else:
			a = 52
			b = 48
		diameter = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/circle2} \\put(" + str(a) + "," + str(b) + "){" + str(diameter) + "cm" + "} \\end{overpic}"
		answer = rounddp(pi * (diameter/2)**2,2)
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + " cm$^2$")



def circlecircumferencediameter(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the circumference:\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,2)*90
		if rotation==0:
			a = 40
			b = 53
		else:
			a = 52
			b = 48
		diameter = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/circle2} \\put(" + str(a) + "," + str(b) + "){" + str(diameter) + "cm" + "} \\end{overpic}"
		answer = rounddp(pi * diameter,2)
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + " cm")


def circlearearadiuspi(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		mypi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		if explanationn==1:
			explanation = "Find the area, leaving your answer in terms of " + mypi + ":\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			a = 60
			b = 53
		elif rotation==180:
			a = 16
			b = 53
		elif rotation==90:
			a = 52
			b = 65
		else:
			a = 52
			b = 25
		radius = random.randrange(2,16)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.3]{shape/images/circle1} \\put(" + str(a) + "," + str(b) + "){" + str(radius) + "cm" + "} \\end{overpic}"
		answer = radius**2
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + mypi + " cm$^2$")


def circlecircumferenceradiuspi(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		mypi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		if explanationn==1:
			explanation = "Find the circumference, leaving your answer in terms of " + mypi + ":\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			a = 60
			b = 53
		elif rotation==180:
			a = 16
			b = 53
		elif rotation==90:
			a = 52
			b = 65
		else:
			a = 52
			b = 25
		radius = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.3]{shape/images/circle1} \\put(" + str(a) + "," + str(b) + "){" + str(radius) + "cm" + "} \\end{overpic}"
		answer = radius*2
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + mypi + " cm")



def circleareadiameterpi(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		mypi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		if explanationn==1:
			explanation = "Find the area, leaving your answer in terms of " + mypi + ":\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,2)*90
		if rotation==0:
			a = 40
			b = 53
		else:
			a = 52
			b = 48
		radius = random.randrange(2,16)
		diameter = radius * 2
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.3]{shape/images/circle2} \\put(" + str(a) + "," + str(b) + "){" + str(diameter) + "cm" + "} \\end{overpic}"
		answer = radius**2
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + mypi + " cm$^2$")



def circlecircumferencediameterpi(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		mypi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		if explanationn==1:
			explanation = "Find the circumference, leaving your answer in terms of " + mypi + ":\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,2)*90
		if rotation==0:
			a = 40
			b = 53
		else:
			a = 52
			b = 48
		diameter = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.3]{shape/images/circle2} \\put(" + str(a) + "," + str(b) + "){" + str(diameter) + "cm" + "} \\end{overpic}"
		answer = diameter
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer) + mypi + " cm")




def circlestarter1(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and circumference:\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			a = 60
			b = 53
		elif rotation==180:
			a = 16
			b = 53
		elif rotation==90:
			a = 52
			b = 65
		else:
			a = 52
			b = 25
		radius = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/circle1} \\put(" + str(a) + "," + str(b) + "){" + str(radius) + "cm" + "} \\end{overpic}"
		answer = "Area = " + str(rounddp(pi * radius**2,2)) + " cm$^2$ \\\\ Circumference = " + str(rounddp(pi*radius * 2,2)) + " cm"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circlestarter2(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and circumference:\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,2)*90
		if rotation==0:
			a = 40
			b = 53
		else:
			a = 52
			b = 48
		diameter = random.randrange(3,50)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/circle2} \\put(" + str(a) + "," + str(b) + "){" + str(diameter) + "cm" + "} \\end{overpic}"
		answer = "Area = " + str(rounddp(pi * (diameter/2)**2,2)) + " cm$^2$ \\\\ Circumference = " + str(rounddp(pi * diameter,2)) + " cm"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circlestarter1pi(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		mypi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		if explanationn==1:
			explanation = "Find the area and circumference, leaving your answers in terms of " + mypi + ":\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,4)*90
		if rotation==0:
			a = 60
			b = 53
		elif rotation==180:
			a = 16
			b = 53
		elif rotation==90:
			a = 52
			b = 65
		else:
			a = 52
			b = 25
		radius = random.randrange(2,16)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.3]{shape/images/circle1} \\put(" + str(a) + "," + str(b) + "){" + str(radius) + "cm" + "} \\end{overpic}"
		answer = "Area = " + str(radius**2) + mypi + " cm$^2$ \\\\ Circumference = " + str(radius*2) + mypi + " cm"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circlestarter2pi(n,explanationn):
	import random
	from math import pi
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		mypi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		if explanationn==1:
			explanation = "Find the area and circumference, leaving your answer in terms of " + mypi + ":\\\\"
		else:
			explanation = ""
		rotation = random.randrange(0,2)*90
		if rotation==0:
			a = 40
			b = 53
		else:
			a = 52
			b = 48
		radius = random.randrange(2,16)
		diameter = radius * 2
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.3]{shape/images/circle2} \\put(" + str(a) + "," + str(b) + "){" + str(diameter) + "cm" + "} \\end{overpic}"
		answer = "Area = " + str(radius**2) + mypi + " cm$^2$ \\\\ Circumference = " + str(radius*2) + mypi + " cm"
#write question
		tempquestions.write(explanation + image)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


















def arcsector1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and perimeter:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2,2)
		perimeter = rounddp(a/360 * pi * 2 * l + 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "41,21"
			lco = "78,40"
		elif rotation==270:
			aco = "14.5,46"
			lco = "20,80"
		elif rotation==180:
			aco = "40,72"
			lco = "78,55"
		else:
			aco = "70,45" 
			lco = "52,80"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/sector1} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, P = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def arcsector1length(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and arc length:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2,2)
		perimeter = rounddp(a/360 * pi * 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "41,21"
			lco = "78,40"
		elif rotation==270:
			aco = "14.5,46"
			lco = "20,80"
		elif rotation==180:
			aco = "40,72"
			lco = "78,55"
		else:
			aco = "70,45" 
			lco = "52,80"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/sector1} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, P = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def arcsector2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and perimeter:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		A = 360-a
		area = rounddp(A/360 * pi * l**2,2)
		perimeter = rounddp(A/360 * pi * 2 * l + 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "40,25"
			lco = "63,30"
		elif rotation==270:
			aco = "22,46"
			lco = "23,68"
		elif rotation==180:
			aco = "40,68"
			lco = "61,60"
		else:
			aco = "61,46" 
			lco = "49,70"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/sector2} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, P = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def arcsector2length(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and arc length:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		A = 360-a
		area = rounddp(A/360 * pi * l**2,2)
		perimeter = rounddp(A/360 * pi * 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "40,25"
			lco = "63,30"
		elif rotation==270:
			aco = "22,46"
			lco = "23,68"
		elif rotation==180:
			aco = "40,68"
			lco = "61,60"
		else:
			aco = "61,46" 
			lco = "49,70"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/sector2} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, AL = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def arcsector3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi,sin,radians
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the shaded area\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(10,171)
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2 - 0.5 * l * l * sin(radians(a)),2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			aco = "42,27"
			lco = "78,40"
		elif rotation==270:
			aco = "19,46"
			lco = "20,80"
		elif rotation==180:
			aco = "42,65"
			lco = "78,55"
		else:
			aco = "65,45" 
			lco = "52,80"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.36]{shape/images/sector3} \\put(" + aco + "){" + str(a) + "\\mydeg} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = str(area) + "cm$^{2}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def semicircleperimeter(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and perimeter:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = 180
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2,2)
		perimeter = rounddp(a/360 * pi * 2 * l + 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			lco = "40,28"
		elif rotation==270:
			lco = "27,48"
		elif rotation==180:
			lco = "40,76"
		else:
			lco = "76,48"
		l = int(l*2)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/semicircle} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, P = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def semicirclearclength(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and arc length:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = 180
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2,2)
		perimeter = rounddp(a/360 * pi * 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			lco = "40,28"
		elif rotation==270:
			lco = "27,48"
		elif rotation==180:
			lco = "40,76"
		else:
			lco = "76,48"
		l = int(l*2)
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/semicircle} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, AL = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def quartercircleperimeter(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and perimeter:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = 90
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2,2)
		perimeter = rounddp(a/360 * pi * 2 * l + 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			lco = "39,6"
		elif rotation==270:
			lco = "39,87"
		elif rotation==180:
			lco = "40,87"
		else:
			lco = "38,6"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/quartercircle} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, P = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def quartercirclearclength(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import pi
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the area and arc length:\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = 90
		l = random.randrange(4,102)/2
		if l%1==0:
			l = int(l)
		else:
			l = rounddp(l,1)
		area = rounddp(a/360 * pi * l**2,2)
		perimeter = rounddp(a/360 * pi * 2 * l,2)
		rotation = random.randrange(0,4)*90
		if rotation==0:
			lco = "39,6"
		elif rotation==270:
			lco = "39,87"
		elif rotation==180:
			lco = "40,87"
		else:
			lco = "38,6"
		image = "\\centering\\begin{overpic}[angle=" + str(rotation) + ",scale=0.35]{shape/images/quartercircle} \\put(" + lco + "){" + str(l) + "cm} \\end{overpic}"
		question = explanation + image
		answer = "A = " + str(area) + "cm$^{2}$, AL = " + str(perimeter) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
