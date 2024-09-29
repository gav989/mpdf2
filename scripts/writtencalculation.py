#!/usr/bin/env python3
import subprocess, os, shutil, random
from utilities.templategen import generatetemplate,generatetitlepage,generatecontentspage
content = ""
starter = "starter"
#####################################

chapter = "Written Calculation"
filename = "Written Calculation"
template = "mpdf2"

#####################################

content = content + generatecontentspage(chapter)

title = "Addition"
hint = "~"
section = "Single Digit Addition"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
frametext = generatetemplate(3,10,4,100,100)
from functions.writcalc import singledigitaddition
tempquestions = singledigitaddition(30,0)
####
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, len(tempquestions[0])):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[0][i])
	frametext = frametext.replace(aterm,tempquestions[1][i])
content = content + titlepage + frametext


title = "Addition"
hint = "~"
section = "Two Digit Addition"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
frametext = generatetemplate(3,10,4,100,100)
from functions.writcalc import twodigitaddition
tempquestions = twodigitaddition(30,0)
####
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, len(tempquestions[0])):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[0][i])
	frametext = frametext.replace(aterm,tempquestions[1][i])
content = content + titlepage + frametext


title = "Addition"
hint = "~"
section = "Three Digit Addition"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
frametext = generatetemplate(3,10,4,100,100)
from functions.writcalc import threedigitaddition
tempquestions = threedigitaddition(30,0)
####
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, len(tempquestions[0])):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[0][i])
	frametext = frametext.replace(aterm,tempquestions[1][i])
content = content + titlepage + frametext


title = "Addition"
hint = "~"
section = "Full Addition"
description = "A mixture of integer addition questions"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
frametext = generatetemplate(3,10,4,100,100)
from functions.writcalc import fulladdition
tempquestions = fulladdition(30,0)
####
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, len(tempquestions[0])):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[0][i])
	frametext = frametext.replace(aterm,tempquestions[1][i])
content = content + titlepage + frametext


title = "Addition"
hint = "~"
section = "Decimal Addition"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
frametext = generatetemplate(3,10,4,100,100)
from functions.writcalc import decimaladdition
tempquestions = decimaladdition(30,0)
####
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, len(tempquestions[0])):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[0][i])
	frametext = frametext.replace(aterm,tempquestions[1][i])
content = content + titlepage + frametext







#####################################
with open("templates/"+template+".tex", 'r') as file :
	templatetext = file.read()
templatetext = templatetext.replace("CONTENT",content)
with open(filename+".tex", 'w') as file:
	file.write(templatetext)
subprocess.call(["pdflatex", filename+".tex"])
subprocess.call(["pdflatex", filename+".tex"])
os.remove(filename + ".aux")
os.remove(filename + ".log")
os.remove(filename + ".tex")
os.remove(filename + ".nav")
os.remove(filename + ".out")
os.remove(filename + ".snm")
os.remove(filename + ".toc")
os.remove(filename + ".vrb")
