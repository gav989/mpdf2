#!/usr/bin/env python3
import subprocess, os, shutil, random
from utilities.templategen import generatetemplate,generatetitlepage,generatecontentspage
content = ""
starter = "starter"
bycolumn = "bycolumn"
#####################################

chapter = "Recurring Decimals"
filename = "Recurring Decimals"
template = "mpdf2"
from functions.recurringdecimals import *

#####################################

content = content + generatecontentspage(chapter)


title = "Recurring Decimals"
hint = "Write as a recurring decimal:"
section = "Fraction to Recurring Decimal"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,6,4,1,100,100)
tempquestions = fractorecdec(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,6,4,1,100,100)
tempquestions = fractorecdec(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Recurring Decimals"
hint = "Write as a fraction in its simplest form:"
section = "Recurring Decimal Build Up"
description = "Each column increases length of repeating phrase"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,6,bycolumn,1,100,100)
tempquestions = recdec1(6,0)
tempquestions += recdec2(6,0)	
tempquestions += recdec3(3,0)
tempquestions += recdec3hard(3,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,6,bycolumn,1,100,100)
tempquestions = recdec1(6,0)
tempquestions += recdec2(6,0)
tempquestions += recdec3(3,0)
tempquestions += recdec3hard(3,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Recurring Decimals"
hint = "Write as a fraction in its simplest form:"
section = "Recurring Decimal Mix"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,6,4,1,100,100)
tempquestions = []
qlist = [recdec1,recdec1,recdec2,recdec2,recdec3,recdec3hard] * 3
random.shuffle(qlist)
for q in qlist:
	tempquestions += q(1,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,6,4,1,100,100)
tempquestions = []
qlist = [recdec1,recdec1,recdec2,recdec2,recdec3,recdec3hard] * 3
random.shuffle(qlist)
for q in qlist:
	tempquestions += q(1,0)
print(tempquestions)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext




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
