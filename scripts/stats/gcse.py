#gcse.py

def weightedindexnumbers(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the weighted index number.\\\\ "
		else:
			explanation = ""
		ws = [random.randrange(1,10),random.randrange(10,30),random.randrange(30,60)]
		while ws[0] + ws[1] + ws[2] < 100:
			temp = random.randrange(0,3)
			ws[temp] = ws[temp] + 1
		random.shuffle(ws)
		w1 = ws[0]
		w2 = ws[1]
		w3 = ws[2]
		p1 = random.randrange(50,401)
		p2 = random.randrange(50,401)
		p3 = random.randrange(50,401)
		s1 = random.randrange(50,401)
		s2 = random.randrange(50,401)
		s3 = random.randrange(50,401)
		x = ((p1*w1)+(p2*w2)+(p3*w3))/100
		y = ((s1*w1)+(s2*w2)+(s3*w3))/100
		if x%1==0:
			x = int(x)
		if y%1==0:
			y = int(y)
		answer = "$\\dfrac{" + str(rounddp(y,2)) + "}{" + str(rounddp(x,2)) + "} \\times 100 = " + str(rounddp(100 * y / x,2)) + "$"
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{1cm} | M{1cm} | M{1cm} | M{1cm} | } \\hline Item & Weight & Price 2014 & Price 2015 \\\\ \\specialrule{1pt}{0pt}{0pt} Flour & " + str(w1) + "\\% & " + str(p1) + "p & " + str(s1) + "p  \\\\ \\hline Sugar & " + str(w2) + "\\% & " + str(p2) + "p & " + str(s2) + "p  \\\\ \\hline Butter & " + str(w3) + "\\% & " + str(p3) + "p & " + str(s3) + "p  \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
