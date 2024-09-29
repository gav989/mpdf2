#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "Multiplying and Dividing by 10 100 and 1000 Torture"
title = "Multiplying and Dividing by 10, 100 and 1000"
from torture.torture import multten, multhundred, multthousand, divten, divhundred, divthousand, multdivtht1, multdivtht2, multdivtht3
tempquestions = open("tempquestions","a")
for x in range(0,1):
	multten(5)
	multhundred(5)
	multthousand(5)
	for y in range(0,10):
		dec = random.randrange(1,4)
		if dec==1:
			multten(1)
		elif dec==2:
			multhundred(1)
		else:
			multthousand(1)
	divten(5)
	divhundred(5)
	divthousand(5)
	for y in range(0,10):
		dec = random.randrange(1,4)
		if dec==1:
			divten(1)
		elif dec==2:
			divhundred(1)
		else:
			divthousand(1)
	multdivtht1(25)
	multdivtht2(25)
	multdivtht3(25)
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

shutil.copyfile("templates/torture.tex", "temp1")
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
	writedoc.write(line.replace("title",title))
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
