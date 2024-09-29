#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "TTProg 03 - 2 Times Table"
title = "2 Times Table"
from torture.ttprog import timestablesnormal,timestablesdivide,timestableshard
tempquestions = open("tempquestions","a")

recap = (10,11)
new = (2,2)

for x in range(0,15):
	timestablesnormal(1,random.choice(recap))

for x in range(0,15):
	timestablesdivide(1,random.choice(recap))

for x in range(0,20):
	timestableshard(1,random.choice(recap),random.randrange(0,3))

for x in range(0,25):
	timestablesnormal(1,random.choice(new))

for x in range(0,25):
	timestablesdivide(1,random.choice(new))

for x in range(0,25):
	timestableshard(1,random.choice(new),random.randrange(0,3))

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
