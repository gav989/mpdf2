#!/usr/bin/env python3
import subprocess, os, shutil, random
tempquestions = open("tempquestions","a")
#####################################
#ONLY EDIT THIS PART
#####################################

filename = "Maisie|starter|"
hint = "~"
title = "Revision"
template = "mpdf2starter"

from shape.angles import polygonanglestable
from graphs.linear import equationoflinepara
from graphs.linear import equationoflineperp
from equations.quadratics import factorisequadratics1
from equations.quadratics import factorisequadratics2
from equations.quadratics import factorisequadraticsdots1
from equations.quadratics import factorisequadraticsdots2
from indices.surds import simplifysurd1
from fdp.fractionoperations import fractionsmultiplysimplifyfirst
from algebra.proportion import direct,directsquare,directsquareroot,inverse,inversesquare,inversesquareroot

from fdp.percentages import percreverse
from shape.trig import sinangle,cosangle,tanangle,sinside1,sinside2,cosside1,cosside2,tanside1,tanside2
from equations.simultaneous import simeqlin1,simeqlin2,simeqlin3
from primes.primefactors import hcf

#tier1
q1 = [hcf]
q2 = [simeqlin1,simeqlin2,simeqlin3]
q3 = [factorisequadratics1]

#tier2

q4 = [sinangle,cosangle,tanangle,sinside1,sinside2,cosside1,cosside2,tanside1,tanside2]
q5 = [polygonanglestable]
#tier3

q6 = [percreverse]


for i in range(0,8):
	random.choice(q1)(1,1)
	random.choice(q2)(1,1)
	random.choice(q3)(1,1)
	random.choice(q4)(1,1)
	random.choice(q5)(1,1)
	random.choice(q6)(1,1)



#####################################
tempquestions.close()
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

# Read template to RAM
filedata = None
with open("templates/"+template+".tex", 'r') as file :
	filedata = file.read()

# Replace text strings
filedata = filedata.replace("hint",hint)
filedata = filedata.replace("tttitle",title)
for x in range(0, lines):
	qterm = "q" + str(x+1) + " "
	aterm = "a" + str(x+1) + " "
	filedata = filedata.replace(qterm,questions[x])
	filedata = filedata.replace(aterm,answers[x])

# Write to tex file
with open(filename+".tex", 'w') as file:
	file.write(filedata)

subprocess.call(["pdflatex", filename+".tex"])
os.remove(filename + ".aux")
os.remove(filename + ".log")
os.remove(filename + ".tex")
os.remove(filename + ".nav")
os.remove(filename + ".out")
os.remove(filename + ".snm")
os.remove(filename + ".toc")
os.remove(filename + ".vrb")