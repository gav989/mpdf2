#cumfreq.py


def cumfreq(n,explanationn):
#in ks3 unit 2
	import random
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "Complete the table to draw a cumulative frequency graph, then use this graph to calculate estimates of the median, lower quartile and upper quartile."
		dec = random.randrange(0,5)
		if dec==0:
			scores = ["$0 \\leq (S) < 10$","$10 \\leq (S) < 20$","$20 \\leq (S) < 30$","$30 \\leq (S) < 40$","$40 \\leq (S) < 50$"]
			scores2 = ["$0 \\leq (S) < 10$","$0 \\leq (S) < 20$","$0 \\leq (S) < 30$","$0 \\leq (S) < 40$","$0 \\leq (S) < 50$"]
			bottoms = [0,10,20,30,40]
			xs = [10,20,30,40,50]
			lowest = 0
		elif dec==1:
			scores = ["$0 \\leq (S) < 5$","$5 \\leq (S) < 10$","$10 \\leq (S) < 15$","$15 \\leq (S) < 20$","$20 \\leq (S) < 25$"]
			scores2 = ["$0 \\leq (S) < 5$","$0 \\leq (S) < 10$","$0 \\leq (S) < 15$","$0 \\leq (S) < 20$","$0 \\leq (S) < 25$"]
			bottoms = [0,5,10,15,20]
			xs = [5,10,15,20,25]
			lowest = 0
		elif dec==2:
			scores = ["$0 \\leq (S) < 50$","$50 \\leq (S) < 100$","$100 \\leq (S) < 150$","$150 \\leq (S) < 200$","$200 \\leq (S) < 250$"]
			scores2 = ["$0 \\leq (S) < 50$","$0 \\leq (S) < 100$","$0 \\leq (S) < 150$","$0 \\leq (S) < 200$","$0 \\leq (S) < 250$"]
			bottoms = [0,50,100,150,200]
			xs = [50,100,150,200,250]
			lowest = 0
		elif dec==3:
			scores = ["$10 \\leq (S) < 20$","$20 \\leq (S) < 30$","$30 \\leq (S) < 40$","$40 \\leq (S) < 50$","$50 \\leq (S) < 60$"]
			scores2 = ["$10 \\leq (S) < 20$","$10 \\leq (S) < 30$","$10 \\leq (S) < 40$","$10 \\leq (S) < 50$","$10 \\leq (S) < 60$"]
			bottoms = [10,20,30,40,50]
			xs = [20,30,40,50,60]
			lowest = 10
		else:
			scores = ["$20 \\leq (S) < 40$","$40 \\leq (S) < 60$","$60 \\leq (S) < 80$","$80 \\leq (S) < 100$","$100 \\leq (S) < 120$"]
			scores2 = ["$20 \\leq (S) < 40$","$20 \\leq (S) < 60$","$20 \\leq (S) < 80$","$20 \\leq (S) < 100$","$20 \\leq (S) < 120$"]
			bottoms = [20,40,60,80,100]
			xs = [40,60,80,100,120]
			lowest = 20
		freqs = []
		inc = random.randrange(3,10)
		for i in range (0,5):
			freqs.append(random.randrange((i+1)*inc+1,(i+2)*inc+1))
		freqs = sorted(freqs)
		if random.randrange(0,2)==1:
			temp = freqs[1]
			freqs[1] = freqs[0]
			freqs[0] = temp
		if random.randrange(0,2)==1:
			temp = freqs[3]
			freqs[3] = freqs[2]
			freqs[2] = temp
		total = sum(freqs)
		difference = ceil(total/10)*10 - total
		freqs[4] = freqs[4] + difference
		freqslookup = [1,3,4,2,0]
		cumfreqs = [freqs[1],freqs[1]+freqs[3],freqs[1]+freqs[3]+freqs[4],freqs[1]+freqs[3]+freqs[4]+freqs[2],freqs[1]+freqs[3]+freqs[4]+freqs[2]+freqs[0]]



		medgroup = 0
		median = (cumfreqs[4]+1)/2
		while median>cumfreqs[medgroup]:
			medgroup = medgroup + 1
		L = bottoms[medgroup]
		n = cumfreqs[4]
		B = cumfreqs[medgroup-1]
		G = freqs[freqslookup[medgroup]]
		w = xs[medgroup]-bottoms[medgroup]
		median = L + (((n/2)-B)/G) * w



		lqgroup = 0
		lq = (cumfreqs[4]+1)/4
		while lq>cumfreqs[lqgroup]:
			lqgroup = lqgroup + 1
		L = bottoms[lqgroup]
		n = cumfreqs[4]
		B = cumfreqs[lqgroup-1]
		G = freqs[freqslookup[lqgroup]]
		w = xs[lqgroup]-bottoms[lqgroup]
		lq = L + (((n/4)-B)/G) * w



		uqgroup = 0
		uq = 3 * ((cumfreqs[4]+1)/4)
		while uq>cumfreqs[uqgroup]:
			uqgroup = uqgroup + 1
		L = bottoms[uqgroup]
		n = cumfreqs[4]
		B = cumfreqs[uqgroup-1]
		G = freqs[freqslookup[uqgroup]]
		w = xs[uqgroup]-bottoms[uqgroup]
		uq = L + (((3*n/4)-B)/G) * w


		for i in range(0,5):
			freqs[i] = str(freqs[i])
		for i in range(0,5):
			cumfreqs[i] = str(cumfreqs[i])
		for i in range(0,5):
			xs[i] = str(xs[i])
		coordinates = []
		for i in range(0,5):
			coordinates.append("(" + xs[i] + " , " + cumfreqs[i] + ")")
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[1] + " \\\\ \\hline " + scores[1] + "  & " + freqs[3] + " \\\\ \\hline " + scores[2] + " & " + freqs[4] + " \\\\ \\hline " + scores[3] + "  & " + freqs[2] + " \\\\ \\hline " + scores[4] + " & " + freqs[0] + " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.7cm} | p{0.7cm} | p{2cm} |} \\hline Score & CF & Coordinates\\\\ \\specialrule{1pt}{0pt}{0pt} " + " & & (" + str(lowest) + " , 0)" + " \\\\ \\hline " + scores2[0] + " & " + cumfreqs[0] + " & " + coordinates[0] + " \\\\ \\hline " + scores2[1] + "  & " + cumfreqs[1] + " & " + coordinates[1] + " \\\\ \\hline " + scores2[2] + " & " + cumfreqs[2] + " & " + coordinates[2] + " \\\\ \\hline " + scores2[3] + "  & " + cumfreqs[3] + " & " + coordinates[3] + " \\\\ \\hline " + scores2[4] + " & " + cumfreqs[4] + " & " + coordinates[4] + " \\\\ \\hline \\end{tabular}\\hfill"
		for i in range(0,5):
			freqs[i] = str(freqs[i])
		if lq%1==0:
			lq = str(int(lq))
		else:
			lq = str(round(lq,1))
		if median%1==0:
			median = str(int(median))
		else:
			median = str(round(median,1))
		if uq%1==0:
			uq = str(int(uq))
		else:
			uq = str(round(uq,1))
		nl = " \\\\[0.3cm] "
		question = intro + nl + qtable
		answer = "Lower Quartile = " + lq + nl + "Median = " + median + nl + "Upper Quartile = " + uq + nl + atable
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
