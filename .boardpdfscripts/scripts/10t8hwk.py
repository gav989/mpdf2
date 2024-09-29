#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "10T8 Homework Worksheet"
topic = "~"
title = "10T8 Homework"
hint = "~"
tempquestions = open("tempquestions","a")


from equations.linear import threestep1

from algebra.manipulation import collect2

from fouroperators.negatives import negadd,negsubtract

from fdp.rounding import round10,round100,round1000

from fdp.fdp import orderdecimals

from fdp.fractionoperations import fractionssubtract

from fouroperators.multiplication import twobythreemultiplication,decimalmultiplication0

from fouroperators.division import twodigitdivisioneasy

from facts.shapes import metricunits


for x in range(0,1):

	negadd(1,1)
	negsubtract(1,1)
	round10(1,1)
	round100(1,1)
	round1000(1,1)
	orderdecimals(1,1)
	collect2(1,1)
	twobythreemultiplication(1,1)
	decimalmultiplication0(1,1)
	twodigitdivisioneasy(1,1)
	metricunits(1,1)
	threestep1(1,1,0)

tempquestions.close()

#Don't edit this chunk
tempquestions = open("tempquestions","r")
all = tempquestions.read().splitlines()
lines = sum(1 for line in open('tempquestions'))
lines=int((lines - 1)/2)
#lines is now the total number of questions
questions = []
answers = []
for x in range(0, lines):
	questions.append(str(all[2*x+1]))
	answers.append(str(all[2*x+2]))
tempquestions.close()
os.remove("tempquestions")

shutil.copyfile("templates/worksheet.tex", "temp1")

temp = open("temp1","a")

temp.write("\\begin{enumerate}[label={\\arabic*)}]")

for x in range(0,lines):
	temp.write("\\item " + questions[x])
	temp.write("\n")

temp.write("\\end{enumerate}")
temp.write("\n")
temp.write("\\end{multicols*}")

temp.write("\\newpage")
temp.write("\n")
temp.write("\\thispagestyle{empty}")
temp.write("\n")
temp.write("\\centering \\underline{title - Answers}\\")
temp.write("\n")
temp.write("\\begin{multicols*}{2}")
temp.write("\n")
temp.write("\\begin{enumerate}[label={\\arabic*)}]")

for x in range(0,lines):
	temp.write("\\item " + questions[x] + "\\\\")
	temp.write(answers[x])
	temp.write("\n")

temp.write("\\end{enumerate}")
temp.write("\n")
temp.write("\\end{multicols*}")


temp.write("\n")
temp.write("\end{document}")
temp.close()

shutil.copyfile("temp1","temp2")

readdoc=open("temp2","r")
writedoc=open("temp1","w")	
for line in readdoc:
	writedoc.write(line.replace("topic",topic))
readdoc.close()
writedoc.close()
shutil.copyfile("temp1",filename+".tex")

readdoc=open("temp1","r")
writedoc=open("temp2","w")	
for line in readdoc:
	writedoc.write(line.replace("title",title ))
readdoc.close()
writedoc.close()

readdoc=open("temp2","r")
writedoc=open("temp1","w")	
for line in readdoc:
	writedoc.write(line.replace("hint",hint))
readdoc.close()
writedoc.close()
shutil.copyfile("temp1",filename+".tex")


subprocess.call(["pdflatex", filename+".tex"])
os.remove(filename + ".aux")
os.remove(filename + ".log")
os.remove(filename + ".tex")
os.remove("temp1")
os.remove("temp2")
