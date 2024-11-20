#!/usr/bin/env python3
import subprocess, os, shutil, random
from utilities.templategen import generatetemplate,generatetitlepage,generatecontentspage
content = ""
starter = "starter"
bycolumn = "bycolumn"
#####################################

chapter = "Negative Numbers"
filename = "Negative Numbers"
template = "mpdf2"
from functions.negativenumbers import *

#####################################

content = content + generatecontentspage(chapter)


title = "Negative Numbers"
hint = "Calculate:"
section = "Count Up"
description = "Practise using a number line"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = negcountup(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = negcountup(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Negative Numbers"
hint = "Calculate:"
section = "Count Down"
description = "Practise using a number line"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = negcountdown(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = negcountdown(18,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Negative Numbers"
hint = "Calculate:"
section = "Count Mix"
description = "Practise using a number line"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = []
qlist = [negcountup,negcountdown] * 9
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
frametext = generatetemplate(2,9,4,1,100,100)
tempquestions = []
qlist = [negcountup,negcountdown] * 9
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




title = "Negative Numbers"
hint = "Calculate:"
section = "Addition"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negadd(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negadd(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Negative Numbers"
hint = "Calculate:"
section = "Subtraction"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negsubtract(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negsubtract(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext

title = "Negative Numbers"
hint = "Calculate:"
section = "Addition and Subtraction"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negadd,negsubtract] * 14
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
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negadd,negsubtract] * 14
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


title = "Negative Numbers"
hint = "Calculate:"
section = "Multiply"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negmultiply(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negmultiply(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Negative Numbers"
hint = "Calculate:"
section = "Divide"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negdivide(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negdivide(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext

title = "Negative Numbers"
hint = "Calculate:"
section = "Multiplication and Division"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negmultiply,negdivide] * 14
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
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negmultiply,negdivide] * 14
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


title = "Negative Numbers"
hint = "Calculate:"
section = "Addition, Subtraction, Multiplication and Division"
description = "Separate Columns"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = negadd(9,0)
tempquestions += negsubtract(9,0)
tempquestions += negmultiply(9,0)
tempquestions += negdivide(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = negadd(9,0)
tempquestions += negsubtract(9,0)
tempquestions += negmultiply(9,0)
tempquestions += negdivide(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



title = "Negative Numbers"
hint = "Calculate:"
section = "Mix"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negsquaring,negadd,negsubtract,negmultiply,negdivide,negadd,negsubtract,negmultiply,negdivide] * 3
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
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negsquaring,negadd,negsubtract,negmultiply,negdivide,negadd,negsubtract,negmultiply,negdivide] * 3
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


title = "Negative Numbers"
hint = "Calculate:"
section = "Addition (Large)"
description = "For simultaneous equations prep"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negaddbig(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negaddbig(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Negative Numbers"
hint = "Calculate:"
section = "Subtraction (Large)"
description = "For simultaneous equations prep"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negsubtractbig(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = negsubtractbig(27,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "Negative Numbers"
hint = "Calculate:"
section = "Addition and Subtraction (Large)"
description = "For simultaneous equations prep"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negaddbig,negsubtractbig] * 14
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
frametext = generatetemplate(3,9,4,1,100,100)
tempquestions = []
qlist = [negaddbig,negsubtractbig] * 14
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
