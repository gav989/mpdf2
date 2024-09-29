#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "Piers Worksheet"
topic = "~"
title = "Questions For Piers"
hint = "~"
tempquestions = open("tempquestions","a")

from fouroperators.addition import singledigitaddition,twodigitaddition,threedigitaddition,fulladdition,decimaladdition
from fouroperators.subtraction import singledigitsubtraction,twodigitsubtraction,threedigitsubtraction,fullsubtraction,decimalsubtraction
from fdp.rounding import round10,round100,round1000,round0dp
from fouroperators.ten import multten,multhundred,multthousand,divten,divhundred,divthousand
from fdp.fractionoperations import fractionofamount1,fractionsadd,fractionssubtract
from fdp.fdp import orderdecimals
from algebra.sequences import seqnext
from fouroperators.figwords import figwordsnomill, wordfigsnomill
for i in range(0,1):
	twodigitaddition(2,0)
	threedigitaddition(2,0)
	fulladdition(2,0)
	decimaladdition(2,0)
	twodigitsubtraction(2,0)
	threedigitsubtraction(2,0)
	fullsubtraction(2,0)
	decimalsubtraction(2,0)
	round10(2,1)
	round100(2,1)
	round1000(2,1)
	round0dp(2,1)
	multten(2,1)
	multhundred(2,1)
	multthousand(2,1)
	divten(2,1)
	divhundred(2,1)
	divthousand(2,1)
	fractionofamount1(2,1)
	seqnext(2,1)
	orderdecimals(2,1)
	wordfigsnomill(2,1)
	figwordsnomill(2,1)
	fractionsadd(8,1)
	fractionssubtract(8,1)
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
