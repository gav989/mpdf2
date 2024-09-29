#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "9T2 Worksheet"
topic = "~"
title = "9T2 Questions"
hint = "~"

from indices.standardform import sfconvert1,sfconvert2,sfmultiplyint,sfdividepos,sfsubtractpos
from indices.surds import surdquadratic1pos,surdquadratic1squaredpos,ratden3
from fouroperators.multiplication import decimalmultiplication1
from fdp.percentages import percofamount5,percincdec,percreverse,percchangeinc,compoundinterestincmon
from fdp.estimation import estimation2
from indices.fracneg import fracindices2

tempquestions = open("tempquestions","a")


for i in range(0,1):
	estimation2(1,1)
	fracindices2(1,1)
	sfconvert1(1,1)
	sfconvert2(1,1)
	sfmultiplyint(1,1)
	sfdividepos(1,1)
	sfsubtractpos(1,1)
	surdquadratic1pos(1,1)
	surdquadratic1squaredpos(1,1)
	ratden3(1,1)
	decimalmultiplication1(1,1)
	percofamount5(1,1)
	percincdec(1,1)
	percreverse(1,1)
	percchangeinc(1,1)
	compoundinterestincmon(1,1)

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
