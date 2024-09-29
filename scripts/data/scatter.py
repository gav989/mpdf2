#scatter.py



def scatter(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		xs = []
		xs.append(random.randrange(5,11))
		for i in range(0,11):
			xs.append(xs[i]+random.randrange(2,9))
		ys = []
		ys.append(random.randrange(5,21))
		for i in range(0,11):
			ys.append(ys[i]+random.randrange(2,8))
		if random.randrange(0,2)==1:
			temp = xs
			xs = ys
			ys = temp
		for i in range(1,len(ys)):
			ys[i] = ys[i] + random.randrange(1,10)*(-1)**random.randrange(1,3)
		if random.randrange(0,2)==1:
			for i in range(0,len(ys)):
				ys[i] = 100 - ys[i]
		shuffler = list(range(0,12))
		random.shuffle(shuffler)
		xstemp = xs
		ystemp = ys
		xs = []
		ys = []
		xnums = list(range(15,86))
		for i in range(0,len(xstemp)):
			xs.append(str(xstemp[shuffler[i]]))
			ys.append(str(ystemp[shuffler[i]]))
			if xs[i] in xnums:
				xnums.remove(xs[i])
		bobscore = random.choice(xnums)
		
		
		sub1 = "Maths"
		sub2 = "English"
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c |} \\hline " + sub1 + " & " + xs[0] + " & " + xs[1] + " & " + xs[2] + " & " + xs[3] + " & " + xs[4] + " & " + xs[5] + " & " + xs[6] + " & " + xs[7] + " & " + xs[8] + " & " + xs[9] + " & " + xs[10] + " & " + xs[11] + " \\\\ \\hline " + sub2 + " & " + ys[0] + " & " + ys[1] + " & " + ys[2] + " & " + ys[3] + " & " + ys[4] + " & " + ys[5] + " & " + ys[6] + " & " + ys[7] + " & " + ys[8] + " & " + ys[9] + " & " + ys[10] + " & " + ys[11] + " \\\\ \\hline \\end{tabular}"
		l1 = "Plot the following data on a scatter graph."
		l2 = "State the correlation shown."
		l3 = "Draw a line of best fit on your graph."
		l4 = "Bob scored " + str(bobscore) + " in the " + sub1 + " test, but missed the " + sub2 + " test. Use your graph to estimate the score Bob would have got in the " + sub2 + " test."
		nl = "\\\\[0.1cm]"
		question = l1 + nl + qtable + nl + l2 + nl + l3 + nl + l4
		answer = "testing"


#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


