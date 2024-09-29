#!/usr/bin/env python3
import subprocess, os, shutil
filename = "9T3 EQ Worksheet"
topic = "~"
title = "9T3 Exam Questions"
hint = "~"
tempquestions = open("tempquestions","a")

from examquestions.shape import circlesquare,toy,circletable
from examquestions.number import populationcross,sftable,conversiongraph


for x in range(0,1):

	toy(1,0)
	circlesquare(1,0)
	populationcross(1,0)
	sftable(1,0)

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

shutil.copyfile("templates/eqworksheet.tex", "temp1")
decision = 1


for x in range(0, lines):
	if decision==1:
		readdoc=open("temp1","r")
		writedoc=open("temp2","w")	
	else:
		readdoc=open("temp2","r")
		writedoc=open("temp1","w")	
	qterm = "q" + str(x+1) + " "
	for line in readdoc:
		writedoc.write(line.replace(qterm, questions[x]))
	decision*=-1
	readdoc.close()
	writedoc.close()


for x in range(0, lines):
	if decision==1:
		readdoc=open("temp1","r")
		writedoc=open("temp2","w")	
	else:
		readdoc=open("temp2","r")
		writedoc=open("temp1","w")	
	aterm = "a" + str(x+1) + " "
	for line in readdoc:
		writedoc.write(line.replace(aterm, answers[x]))
	decision*=-1
	readdoc.close()
	writedoc.close()


if decision==1:
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
os.remove(filename + ".nav")
os.remove(filename + ".out")
os.remove(filename + ".snm")
os.remove(filename + ".toc")
os.remove("temp1")
os.remove("temp2")
