#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "Harry Worksheet"
topic = "~"
title = "Algebra Questions for Harry"
hint = "~"
tempquestions = open("tempquestions","a")

from algebra.manipulation import collect1,collect2,singlebracketexpansion1,singlebracketexpansion2,singlebracketexpansion3,singlebracketexpansion4,singlebracketexpansion5,singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3,singlebracketfactorise4,singlebracketfactorise5,rearrange1
from algebra.proportion import direct,directsquare,directsquareroot,inverse,inversesquare,inversesquareroot
from algebra.fractions import quaddots

from equations.linear import twostep1,twostep2,twostep3,twostep4,twostep5,twostep6,twostep7,twostep8,threestep1

from equations.quadratics import expandquadratics1,expandquadratics2,expandquadraticsdots1,expandquadraticssquared1,factorisequadratics1,factorisequadratics2,factorisequadraticsdots1,solvequadratics1,solvequadratics2,quadraticformula,completesquare,completesquaresolve

from equations.simultaneous import simeqlin1,simeqlin2,simeqlin3,simeqquad1,simeqquad2

from graphs.coordinates import midpoint,distance


for i in range(0,1):
	collect1(1,1)
	collect2(1,1)
	singlebracketexpansion1(1,1)
	singlebracketexpansion2(1,1)
	singlebracketexpansion3(1,1)
	singlebracketexpansion4(1,1)
	singlebracketexpansion5(1,1)
	singlebracketfactorise1(1,1)
	singlebracketfactorise2(1,1)
	singlebracketfactorise3(1,1)
	singlebracketfactorise4(1,1)
	singlebracketfactorise5(1,1)
	rearrange1(1,1)
	twostep1(1,1,1)
	twostep2(1,1,1)
	twostep3(1,1,1)
	twostep4(1,1,1)
	twostep5(1,1,1)
	twostep6(1,1,1)
	twostep7(1,1,1)
	twostep8(1,1,1)
	threestep1(1,1,1)
	expandquadratics1(1,1)
	expandquadratics2(1,1)
	expandquadraticsdots1(1,1)
	expandquadraticssquared1(1,1)
	factorisequadratics1(1,1)
	factorisequadratics2(1,1)
	factorisequadraticsdots1(1,1)
	solvequadratics1(1,1)
	solvequadratics2(1,1)
	quadraticformula(1,1)
	completesquare(1,1)
	completesquaresolve(1,1)
	quaddots(1,1)
	simeqlin1(1,1)
	simeqlin2(1,1)
	simeqlin3(1,1)
	simeqquad1(1,1)
	simeqquad2(1,1)
	direct(1,1)
	directsquare(1,1)
	directsquareroot(1,1)
	inverse(1,1)
	inversesquare(1,1)
	inversesquareroot(1,1)
	midpoint(1,1)
	distance(1,1)
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
