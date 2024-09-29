#templategen.py


def generatetemplate(x=2,y=2,n=1,a=100,b=100): #x = width/columns, y = rows, n = number of answers to replace on semi-answer slide a=border b=box
	if x=="starter":
		frametext = r"""
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,height=9.4cm,valign=top]{tttitle} hint
	\begin{columns}
		\column{0.33\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myred2!300!, colback=myred2!30!,colframe=myred2!300!,boxed title style={colback=myred2!300!}]{\contour{myfg}{1}}{q1 }\end{questionbox}
		\column{0.33\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myorange!300!, colback=myorange!30!,colframe=myorange!300!,boxed title style={colback=myorange!300!}]{\contour{myfg}{2}}{q2 }\end{questionbox}
		\column{0.33\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myyellow!300!, colback=myyellow!30!,colframe=myyellow!300!,boxed title style={colback=myyellow!300!}]{\contour{myfg}{3}}{q3 }\end{questionbox}
	\end{columns}
	\begin{columns}
		\column{0.5085\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=mygreen!300!, colback=mygreen!30!,colframe=mygreen!300!,boxed title style={colback=mygreen!300!}]{\contour{myfg}{4}}{q4 }\end{questionbox}
		\column{0.5085\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myblue!300!, colback=myblue!30!,colframe=myblue!300!,boxed title style={colback=myblue!300!}]{\contour{myfg}{5}}{q5 }\end{questionbox}
	\end{columns}
	\begin{columns}
		\column{1.0432\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myviolet!300!, colback=myviolet!30!,colframe=myviolet!300!,boxed title style={colback=myviolet!300!}]{\contour{myfg}{6}}{q6 }\end{questionbox}
	\end{columns}
	\end{borderbox}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,height=9.4cm,valign=top]{tttitle - Answers} hint
	\begin{columns}
		\column{0.33\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myred2!300!, colback=myred2!30!,colframe=myred2!300!,boxed title style={colback=myred2!300!}]{\contour{myfg}{1}}{\textcolor{myred}{a1 }}\end{questionbox}
		\column{0.33\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myorange!300!, colback=myorange!30!,colframe=myorange!300!,boxed title style={colback=myorange!300!}]{\contour{myfg}{2}}{\textcolor{myred}{a2 }}\end{questionbox}
		\column{0.33\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myyellow!300!, colback=myyellow!30!,colframe=myyellow!300!,boxed title style={colback=myyellow!300!}]{\contour{myfg}{3}}{\textcolor{myred}{a3 }}\end{questionbox}
	\end{columns}
	\begin{columns}
		\column{0.5085\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=mygreen!300!, colback=mygreen!30!,colframe=mygreen!300!,boxed title style={colback=mygreen!300!}]{\contour{myfg}{4}}{\textcolor{myred}{a4 }}\end{questionbox}
		\column{0.5085\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myblue!300!, colback=myblue!30!,colframe=myblue!300!,boxed title style={colback=myblue!300!}]{\contour{myfg}{5}}{\textcolor{myred}{a5 }}\end{questionbox}
	\end{columns}
	\begin{columns}
		\column{1.0432\textwidth}
		\begin{questionbox}[left=1mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colbacktitle=myviolet!300!, colback=myviolet!30!,colframe=myviolet!300!,boxed title style={colback=myviolet!300!}]{\contour{myfg}{6}}{\textcolor{myred}{a6 }}\end{questionbox}
	\end{columns}
	\end{borderbox}
	\CopyrightNotice{}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	"""
	else:
		numberofquestions = x*y
		if n==0:
			frametext = r"""
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,colframe=myfg!FRAMEOPACITY!,height=9.4cm,valign=top]{tttitle} hint
	\begin{columns}
		QCONTENT
	\end{columns}
	\end{borderbox}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,colframe=myfg!FRAMEOPACITY!,height=9.4cm,valign=top]{tttitle - Answers} hint
	\begin{columns}
		ACONTENT
	\end{columns}
	\end{borderbox}
	\CopyrightNotice{}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	"""
		else:
			frametext = r"""
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,colframe=myfg!FRAMEOPACITY!,height=9.4cm,valign=top]{tttitle} hint
	\begin{columns}
		QCONTENT
	\end{columns}
	\end{borderbox}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\frame{%%%%%%%%%%%%%%%%%%%%%%%%%%%%Semi%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,colframe=myfg!FRAMEOPACITY!,height=9.4cm,valign=top]{tttitle} hint
	\begin{columns}
		SEMICONTENT
	\end{columns}
	\end{borderbox}
	\CopyrightNotice{}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Semi%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\begin{borderbox}[left=3.5mm,right=3.5mm,top=1mm,bottom=1mm,before skip = 0.2cm,colback=white,colframe=myfg!FRAMEOPACITY!,height=9.4cm,valign=top]{tttitle - Answers} hint
	\begin{columns}
		ACONTENT
	\end{columns}
	\end{borderbox}
	\CopyrightNotice{}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	"""
		if numberofquestions==1:
			qbox = r"""\column{\textwidth} \\[-0.2cm] q1 
		"""
			abox = r"""\column{\textwidth} \\[-0.2cm] \textcolor{myred}{a1 }
		"""
		else:
			qbox = r"""\begin{questionbox}[left=3mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colframe=myfg!BOXOPACITY!]{QNUM}{QTEXT }\end{questionbox}
		"""
			abox = r"""\begin{questionbox}[left=3mm,right=0mm,top=0mm,bottom=0mm,before skip = 0.05cm,colframe=myfg!BOXOPACITY!]{QNUM}{\textcolor{myred}{ATEXT }}\end{questionbox}
		"""
		coltext = r"""\column{COLWIDTH\textwidth}
		"""
		if x==1:
			colwidth = "1.0432"
		elif x==2:
			colwidth = "0.5085"
		elif x==3:
			colwidth = "0.33"
		coltext = coltext.replace("COLWIDTH",colwidth)
		frametext = frametext.replace("FRAMEOPACITY",str(a))
		qbox = qbox.replace("BOXOPACITY",str(b))
		abox = abox.replace("BOXOPACITY",str(b))
		qlist = []
		alist = []
		qnumcounter = 1
		for i in range(0,x):
			qlist.append(coltext)
			alist.append(coltext)
			for j in range(0,y):
				qlist.append(qbox.replace("QNUM",str(qnumcounter)).replace("QTEXT","q" + str(qnumcounter)))
				alist.append(abox.replace("QNUM",str(qnumcounter)).replace("ATEXT","a" + str(qnumcounter)))
				qnumcounter += 1
		semilist = qlist.copy()
		for i in range(0,n):
			semilist[i] = alist[i]
		qcontent = ""
		acontent = ""
		semicontent = ""
		for i in range(0,len(qlist)):
			qcontent = qcontent + qlist[i]
			acontent = acontent + alist[i]
			semicontent = semicontent + semilist[i]
		frametext = frametext.replace("QCONTENT",qcontent).replace("ACONTENT",acontent).replace("SEMICONTENT",semicontent)
	return frametext






def generatetitlepage(section,description,examples):
	frametext = r"""\section{seccction}
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\centering
	\begin{Huge}seccction\end{Huge}\\[5mm]
	\begin{Large}description\end{Large}\\[5mm]
	examples
	\vfill
	\raggedright
	\hyperlink{toc}{Return to Contents}
	\CopyrightNotice{}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	"""
	frametext = frametext.replace("seccction",section).replace("description",description).replace("examples",examples)
	return frametext



def generatecontentspage(title):
	frametext = r"""
\frame{%%%%%%%%%%%%%%%%%%%%%%%%Questions%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\centering
	\begin{Huge}tittle\end{Huge}\\[5mm]
	\raggedright
	\addtocontents{toc}{\protect\hypertarget{toc}{}}
	\tableofcontents
	\CopyrightNotice{}
}%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Answers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	"""
	frametext = frametext.replace("tittle",title)
	return frametext
