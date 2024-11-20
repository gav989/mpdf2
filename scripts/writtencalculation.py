#!/usr/bin/env python3
import subprocess, os, shutil, random
from utilities.templategen import generatetemplate,generatetitlepage,generatecontentspage
content = ""
starter = "starter"
bycolumn = "bycolumn"
#####################################

chapter = "Written Calculation"
filename = "Written Calculation"
template = "mpdf2"
from functions.writcalc import *

#####################################

content = content + generatecontentspage(chapter)


title = "Addition"
hint = "~"
section = "Addition Build Up"
description = "Single-digit, two-digit and three-digit addition"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,12,1,100,100)
tempquestions = singledigitaddition(10,0)
tempquestions += twodigitaddition(10,0)
tempquestions += threedigitaddition(10,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Addition"
hint = "~"
section = "Full Addition"
description = "A mixture of integer addition questions"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = fulladdition(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = fulladdition(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Addition"
hint = "~"
section = "Decimal Addition"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = decimaladdition(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = decimaladdition(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Subtraction"
hint = "~"
section = "Subtraction Build Up"
description = "Single-digit, two-digit and three-digit subtraction"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,12,1,100,100)
tempquestions = singledigitsubtraction(10,0)
tempquestions += twodigitsubtraction(10,0)
tempquestions += threedigitsubtraction(10,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Subtraction"
hint = "~"
section = "Full Subtraction"
description = "A mixture of integer subtraction questions"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = fullsubtraction(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = fullsubtraction(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Subtraction"
hint = "~"
section = "Decimal Subtraction"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = decimalsubtraction(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = decimaladdition(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Multiplication"
hint = "~"
section = "Times Tables"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,0,1,100,100)
tempquestions = timestables(36,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(4,9,0,1,100,100)
tempquestions = timestables(36,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "~"
section = "Lattice 2x1"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,3,0,1,100,0)
tempquestions = multnapier21(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,3,0,1,100,0)
tempquestions = multnapier21(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "~"
section = "Lattice 2x2"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,2,0,1,100,0)
tempquestions = multnapier22(12,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,2,0,1,100,0)
tempquestions = multnapier22(12,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "~"
section = "Lattice 3x2"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,2,0,1,100,0)
tempquestions = multnapier32(12,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,2,0,1,100,0)
tempquestions = multnapier32(12,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "~"
section = "Lattice 3x3"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,2,0,0,0,0)
tempquestions = multnapier33(12,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,2,0,0,0,0)
tempquestions = multnapier33(12,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "~"
section = "Integer Multiplication"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = twobyonemultiplication(6,0)
tempquestions += threebyonemultiplication(6,0)
tempquestions += fourbyonemultiplication(6,0)
tempquestions += twobytwomultiplication(6,0)
tempquestions += twobythreemultiplication(6,0)
tempquestions += threebythreemultiplication(6,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = twobyonemultiplication(6,0)
tempquestions += threebyonemultiplication(6,0)
tempquestions += fourbyonemultiplication(6,0)
tempquestions += twobytwomultiplication(6,0)
tempquestions += twobythreemultiplication(6,0)
tempquestions += threebythreemultiplication(6,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "~"
section = "Decimal Multiplication"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,bycolumn,1,100,100)
tempquestions = decimalmultiplication0(9,0)
tempquestions += decimalmultiplication1(9,0)
tempquestions += decimalmultiplication2(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,bycolumn,1,100,100)
tempquestions = decimalmultiplication0(9,0)
tempquestions += decimalmultiplication1(9,0)
tempquestions += decimalmultiplication2(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Multiplication"
hint = "Given that:"
section = "Decimal Multiplication Given"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,6,bycolumn,0,0,100)
tempquestions = decimalmultiplicationgiven1(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Division"
hint = "Given that:"
section = "Decimal Division Given"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,6,bycolumn,0,0,100)
tempquestions = decimalmultiplicationgiven2(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Multiplication and Division"
hint = "Given that:"
section = "Decimal Multiplication and Division Given"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,6,bycolumn,0,0,100)
tempquestions = []
qlist = [decimalmultiplicationgiven1,decimalmultiplicationgiven2] * 9
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


title = "Division"
hint = "~"
section = "Division Tables"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,0,1,100,100)
tempquestions = divisiontables(27,0)
tempquestions += divisiontablesten(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Division"
hint = "~"
section = "Single Digit Division"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,4,1,100,100)
tempquestions = singledigitdivision(36,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext

title = "Division"
hint = "Write down the first five numbers in these times tables:"
section = "Two Digit Times Tables"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = twodigittables(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Division"
hint = "~"
section = "Two Digit Division"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = twodigitdivisioneasy(10,0)
tempquestions += twodigitdivision(17,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Division"
hint = "~"
section = "Decimal Division 1"
description = "Divisor is an integer"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = decimaldivision1(18,0)
tempquestions += decimaldivision2(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Division"
hint = "~"
section = "Decimal Division 2"
description = "Divisor is a decimal"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = divisionbydecimal(9,0)
tempquestions += decimaldivision3(9,0)
tempquestions += divisionbydecimal2(9,0)
tempquestions += decimaldivision4(9,0)
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
