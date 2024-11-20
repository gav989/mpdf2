#!/usr/bin/env python3
import subprocess, os, shutil, random
tempquestions = open("tempquestions","a")
#####################################
#ONLY EDIT THIS PART
#####################################

filename = "9T3"
hint = "~"
title = "Revision"
template = "mpdf2starter"




from equations.quadratics import expandquadratics1
from algebra.manipulation import singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3,singlebracketfactorise4,singlebracketfactorise5
from equations.linear import equationsmulti1starter
from shape.pythagoras import pythagstarter
from shape.circles import circlearearadius,circlecircumferenceradius,circleareadiameter,circlecircumferencediameter
from fdp.percentages import percreverse
from graphs.linear import equationofline3
from graphs.linear import threegraphsfour

from algebra.manipulation import singlebracketexpansion6,singlebracketexpansion7, singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3,singlebracketfactorise4,singlebracketfactorise5,singlebracketfactorise8
from data.averages import mmmr
from fdp.percentages import percreverse
from data.cumfreq import cumfreqmixer
from data.piecharts import pietable,pietable2
from data.mean import meantablemixer,meantablegroupedmixer
from graphs.linear import threegraphsfour
from equations.linear import equationsmulti1starter

#tier1
q1 = [singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3,singlebracketfactorise4,singlebracketfactorise5,singlebracketfactorise8]
q2 = [equationsmulti1starter]
q3 = [singlebracketexpansion6,singlebracketexpansion7]

#tier2

q4 = [pietable,pietable2,threegraphsfour,threegraphsfour]
q5 = [cumfreqmixer,meantablemixer,meantablegroupedmixer]
#tier3

q6 = [mmmr,percreverse]


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