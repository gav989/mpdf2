#loci.py

def recperp(n,explanationn):
	import random
	from math import ceil,floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\ "
		height = random.randrange(4,7)
		width = height + random.randrange(1,int(ceil(height/2)))
		wco = "43,54" 
		hco = "89,28" 
		image = "\\centering\\begin{overpic}[scale=0.53]{shape/images/rectangleloci} \\put(" + wco + "){" + str(width) + "cm} \\put(" + hco + "){" + str(height) + "cm} \\end{overpic}"
		if random.randrange(0,2)==0:
			arc = random.randrange(floor(width/2)+1,width)
			if random.randrange(0,2)==0:
				if random.randrange(0,2)==0:
					point2 = "\\item Closer to A than B"
				else:
					point2 = "\\item Closer to D than C"
				dec = random.randrange(0,4)
				if dec==0:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from A"
					else:
						point1 = "\\item More than " + str(arc) + "cm from D"
				elif dec==1:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from A"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from D"
				elif dec==2:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from B"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from C"
				else:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from B"
					else:
						point1 = "\\item More than " + str(arc) + "cm from C"
			else:
				if random.randrange(0,2)==0:
					point2 = "\\item Closer to B than A"
				else:
					point2 = "\\item Closer to C than D"
				dec = random.randrange(0,4)
				if dec==0:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from A"
					else:
						point1 = "\\item More than " + str(arc) + "cm from D"
				elif dec==1:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from A"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from D"
				elif dec==2:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from B"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from C"
				else:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from B"
					else:
						point1 = "\\item More than " + str(arc) + "cm from C"
		else:
			arc = random.randrange(floor(height/2)+1,height)
			if random.randrange(0,2)==0:
				if random.randrange(0,2)==0:
					point2 = "\\item Closer to A than D"
				else:
					point2 = "\\item Closer to B than C"
				dec = random.randrange(0,4)
				if dec==0:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from A"
					else:
						point1 = "\\item More than " + str(arc) + "cm from D"
				elif dec==1:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from A"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from D"
				elif dec==2:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from B"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from C"
				else:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from B"
					else:
						point1 = "\\item More than " + str(arc) + "cm from C"
			else:
				if random.randrange(0,2)==0:
					point2 = "\\item Closer to D than A"
				else:
					point2 = "\\item Closer to C than B"
				dec = random.randrange(0,4)
				if dec==0:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from A"
					else:
						point1 = "\\item More than " + str(arc) + "cm from D"
				elif dec==1:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from A"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from D"
				elif dec==2:
					if random.randrange(0,2)==0:
						point1 = "\\item Less than " + str(arc) + "cm from B"
					else:
						point1 = "\\item Less than " + str(arc) + "cm from C"
				else:
					if random.randrange(0,2)==0:
						point1 = "\\item More than " + str(arc) + "cm from B"
					else:
						point1 = "\\item More than " + str(arc) + "cm from C"
		intro = "Shade the region which is:"
		question = image + nl + intro + "\\begin{itemize}" + point1 + point2 + "\\end{itemize}"
		answer = "~"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def recangle(n,explanationn):
	import random
	from math import ceil,floor,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\ "
		height = random.randrange(4,7)
		width = height + random.randrange(1,int(ceil(height/2)))
		wco = "43,54" 
		hco = "89,28" 
		image = "\\centering\\begin{overpic}[scale=0.53]{shape/images/rectangleloci} \\put(" + wco + "){" + str(width) + "cm} \\put(" + hco + "){" + str(height) + "cm} \\end{overpic}"

		if random.randrange(0,2)==0:
			arcwords = "More than "
		else:
			arcwords = "Less than "

		arc0 = random.randrange(2,height+1)
		arc1 = random.randrange(height,width)
		arc2 = random.randrange(width - height + 1,width)
#		arc3min = int(ceil(sqrt((width-height)**2+height**2)))
#		arc3 = random.randrange(arc3min,width)
		arc3 = "blank"
		arcs = [str(arc0),str(arc1),str(arc2),str(arc3)]

		dec1 = random.randrange(0,4)
		if dec1==0:
			if random.randrange(0,2)==0:
				point2 = "\\item Closer to AB than AD"
			else:
				point2 = "\\item Closer to AD than AB"
			arcletters = ["A","B","C","D"]
		elif dec1==1:
			if random.randrange(0,2)==0:
				point2 = "\\item Closer to AB than BC"
			else:
				point2 = "\\item Closer to BC than AB"
			arcletters = ["B","C","D","A"]
		elif dec1==2:
			if random.randrange(0,2)==0:
				point2 = "\\item Closer to BC than CD"
			else:
				point2 = "\\item Closer to CD than BC"
			arcletters = ["C","B","A","D"]
		else:
			if random.randrange(0,2)==0:
				point2 = "\\item Closer to AD than CD"
			else:
				point2 = "\\item Closer to CD than AD"
			arcletters = ["D","A","B","C"]

		dec2 = random.randrange(0,3) #needs updating!
		point1 = "\\item " + arcwords + arcs[dec2] + "cm from " + arcletters[dec2]
		intro = "Shade the region which is:"
		question = image + nl + intro + "\\begin{itemize}" + point1 + point2 + "\\end{itemize}"
		answer = "~"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
