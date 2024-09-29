#cumfreq.py


def cumfreq(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "Complete the table to draw a cumulative frequency graph, then use this graph to calculate estimates of the median, lower quartile and upper quartile."

		if random.randrange(0,3)==1:
			lowest = random.randrange(1,5)*10
		else:
			lowest = 0
		diffs = [5,10,20,30,40,50]
		diff = random.choice(diffs)
		scorest = [lowest]
		bottoms = []
		xs = []
		scores = []
		scores2 = []
		for i in range(0,5):
			scorest.append(scorest[i]+diff)
			xs.append(scorest[i]+diff)
			bottoms.append(scorest[i])
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
			scores2.append("$" + str(scorest[0]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		inc = random.randrange(3,10)
		for i in range (0,5):
			freqs.append(random.randrange((i+1)*inc+1,(i+2)*inc+1))
		ofreqs = sorted(freqs)
		total = sum(freqs)
		difference = ceil(total/10)*10 - total
		ofreqs[4] = freqs[4] + difference

		dec = random.randrange(0,5)
		if dec==0:
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]
		elif dec==1:
			freqs = [ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1],ofreqs[0]]
		elif dec==2:
			freqs = [ofreqs[0],ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1]]
		elif dec==3:
			freqs = [ofreqs[0],ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2]]
		else:
			if random.randrange(0,2)==1:
				temp = freqs[1]
				freqs[1] = freqs[0]
				freqs[0] = temp
			if random.randrange(0,2)==1:
				temp = freqs[3]
				freqs[3] = freqs[2]
				freqs[2] = temp
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]

		freqslookup = [0,1,2,3,4]
		cumfreqs = [freqs[0],freqs[0]+freqs[1],freqs[0]+freqs[1]+freqs[2],freqs[0]+freqs[1]+freqs[2]+freqs[3],freqs[0]+freqs[1]+freqs[2]+freqs[3]+freqs[4]]



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
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.7cm} | p{0.7cm} | p{2cm} |} \\hline Score & CF & Coordinates\\\\ \\specialrule{1pt}{0pt}{0pt} " + " & & (" + str(lowest) + " , 0)" + " \\\\ \\hline " + scores2[0] + " & " + cumfreqs[0] + " & " + coordinates[0] + " \\\\ \\hline " + scores2[1] + "  & " + cumfreqs[1] + " & " + coordinates[1] + " \\\\ \\hline " + scores2[2] + " & " + cumfreqs[2] + " & " + coordinates[2] + " \\\\ \\hline " + scores2[3] + "  & " + cumfreqs[3] + " & " + coordinates[3] + " \\\\ \\hline " + scores2[4] + " & " + cumfreqs[4] + " & " + coordinates[4] + " \\\\ \\hline \\end{tabular}"
		for i in range(0,5):
			freqs[i] = str(freqs[i])
		if lq%1==0:
			lq = str(int(lq))
		else:
			lq = str(rounddp(lq,1))
		if median%1==0:
			median = str(int(median))
		else:
			median = str(rounddp(median,1))
		if uq%1==0:
			uq = str(int(uq))
		else:
			uq = str(rounddp(uq,1))
		nl = " \\\\[0.3cm] "
		question = intro + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = "\\begin{center}" + atable + "\\end{center}~" + nl + "Lower Quartile = " + lq + nl + "Median = " + median + nl + "Upper Quartile = " + uq
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def cumfreqmixer(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "Cumulative Frequency."
		if random.randrange(0,3)==1:
			lowest = random.randrange(1,5)*10
		else:
			lowest = 0
		diffs = [5,10,20,30,40,50]
		diff = random.choice(diffs)
		scorest = [lowest]
		bottoms = []
		xs = []
		scores = []
		scores2 = []
		for i in range(0,5):
			scorest.append(scorest[i]+diff)
			xs.append(scorest[i]+diff)
			bottoms.append(scorest[i])
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
			scores2.append("$" + str(scorest[0]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		inc = random.randrange(3,10)
		for i in range (0,5):
			freqs.append(random.randrange((i+1)*inc+1,(i+2)*inc+1))
		ofreqs = sorted(freqs)
		total = sum(freqs)
		difference = ceil(total/10)*10 - total
		ofreqs[4] = freqs[4] + difference

		dec = random.randrange(0,5)
		if dec==0:
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]
		elif dec==1:
			freqs = [ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1],ofreqs[0]]
		elif dec==2:
			freqs = [ofreqs[0],ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1]]
		elif dec==3:
			freqs = [ofreqs[0],ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2]]
		else:
			if random.randrange(0,2)==1:
				temp = freqs[1]
				freqs[1] = freqs[0]
				freqs[0] = temp
			if random.randrange(0,2)==1:
				temp = freqs[3]
				freqs[3] = freqs[2]
				freqs[2] = temp
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]

		freqslookup = [0,1,2,3,4]
		cumfreqs = [freqs[0],freqs[0]+freqs[1],freqs[0]+freqs[1]+freqs[2],freqs[0]+freqs[1]+freqs[2]+freqs[3],freqs[0]+freqs[1]+freqs[2]+freqs[3]+freqs[4]]



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
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{1.9cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"

		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2.7cm} | p{0.7cm} | p{2cm} |} \\hline Score & CF & Coordinates\\\\ \\specialrule{1pt}{0pt}{0pt} " + " & & (" + str(lowest) + " , 0)" + " \\\\ \\hline " + scores2[0] + " & " + cumfreqs[0] + " & " + coordinates[0] + " \\\\ \\hline " + scores2[1] + "  & " + cumfreqs[1] + " & " + coordinates[1] + " \\\\ \\hline " + scores2[2] + " & " + cumfreqs[2] + " & " + coordinates[2] + " \\\\ \\hline " + scores2[3] + "  & " + cumfreqs[3] + " & " + coordinates[3] + " \\\\ \\hline " + scores2[4] + " & " + cumfreqs[4] + " & " + coordinates[4] + " \\\\ \\hline \\end{tabular}"
		for i in range(0,5):
			freqs[i] = str(freqs[i])
		if lq%1==0:
			lq = str(int(lq))
		else:
			lq = str(rounddp(lq,1))
		if median%1==0:
			median = str(int(median))
		else:
			median = str(rounddp(median,1))
		if uq%1==0:
			uq = str(int(uq))
		else:
			uq = str(rounddp(uq,1))
		nl = " \\\\[0.3cm] "
		question = "Cumulative Frequency: \\\\ \\begin{center}" + qtable + "\\end{center}"
		answer = "\\begin{center}" + atable + "\\end{center}"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def cumfreqhorizontal(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		intro = "Complete the table to draw a cumulative frequency graph, then use this graph to calculate estimates of the median, lower quartile and upper quartile."

		if random.randrange(0,3)==1:
			lowest = random.randrange(1,5)*10
		else:
			lowest = 0
		diffs = [5,10,20,30,40,50]
		diff = random.choice(diffs)
		scorest = [lowest]
		bottoms = []
		xs = []
		scores = []
		scores2 = []
		for i in range(0,5):
			scorest.append(scorest[i]+diff)
			xs.append(scorest[i]+diff)
			bottoms.append(scorest[i])
			scores.append("\\footnotesize{$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$}")
			scores2.append("\\footnotesize{$" + str(scorest[0]) + " \\leq (S) < " + str(scorest[i+1]) + "$}")
		freqs = []
		inc = random.randrange(3,10)
		for i in range (0,5):
			freqs.append(random.randrange((i+1)*inc+1,(i+2)*inc+1))
		ofreqs = sorted(freqs)
		total = sum(freqs)
		difference = ceil(total/10)*10 - total
		ofreqs[4] = freqs[4] + difference

		dec = random.randrange(0,5)
		if dec==0:
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]
		elif dec==1:
			freqs = [ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1],ofreqs[0]]
		elif dec==2:
			freqs = [ofreqs[0],ofreqs[2],ofreqs[4],ofreqs[3],ofreqs[1]]
		elif dec==3:
			freqs = [ofreqs[0],ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2]]
		else:
			if random.randrange(0,2)==1:
				temp = freqs[1]
				freqs[1] = freqs[0]
				freqs[0] = temp
			if random.randrange(0,2)==1:
				temp = freqs[3]
				freqs[3] = freqs[2]
				freqs[2] = temp
			freqs = [ofreqs[1],ofreqs[3],ofreqs[4],ofreqs[2],ofreqs[0]]

		freqslookup = [0,1,2,3,4]
		cumfreqs = [freqs[0],freqs[0]+freqs[1],freqs[0]+freqs[1]+freqs[2],freqs[0]+freqs[1]+freqs[2]+freqs[3],freqs[0]+freqs[1]+freqs[2]+freqs[3]+freqs[4]]



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
			freqs[i] = "\\footnotesize{" + str(freqs[i]) + "}"
		for i in range(0,5):
			cumfreqs[i] = "\\footnotesize{" + str(cumfreqs[i]) + "}"
		for i in range(0,5):
			xs[i] = "\\footnotesize{" + str(xs[i]) + "}"
		coordinates = []
		for i in range(0,5):
			coordinates.append("(" + xs[i] + " , " + cumfreqs[i] + ")")


		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | c | c | c | c | c | } \\hline " + scores[0] + " & " + scores[1] + " & " + scores[2] + " & " + scores[3] + " & " + scores[4] + " \\\\ \\hline " + freqs[0] + " & " + freqs[1] + " & " + freqs[2] + " & " + freqs[3] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"

		atableblank = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | c | c | c | c | c | } \\hline " + scores2[0] + " & " + scores2[1] + " & " + scores2[2] + " & " + scores2[3] + " & " + scores2[4] + " \\\\ \\hline \\phantom{" + scores[0] + "} & \\phantom{" + scores[1] + "} & \\phantom{" + scores[2] + "} & \\phantom{" + scores[3] + "} & \\phantom{" + scores[4] + "}\\\\ \\hline \\end{tabular}"

		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | c | c | c | c | c | } \\hline " + scores2[0] + " & " + scores2[1] + " & " + scores2[2] + " & " + scores2[3] + " & " + scores2[4] + " \\\\ \\hline " + cumfreqs[0] + " & " + cumfreqs[1] + " & " + cumfreqs[2] + " & " + cumfreqs[3] + " & " + cumfreqs[4] + " \\\\ \\hline " + coordinates[0] + " & " + coordinates[1] + " & " + coordinates[2] + " & " + coordinates[3] + " & " + coordinates[4] + " \\\\ \\hline \\end{tabular}"


		for i in range(0,5):
			freqs[i] = str(freqs[i])
		if lq%1==0:
			lq = str(int(lq))
		else:
			lq = str(rounddp(lq,1))
		if median%1==0:
			median = str(int(median))
		else:
			median = str(rounddp(median,1))
		if uq%1==0:
			uq = str(int(uq))
		else:
			uq = str(rounddp(uq,1))
		nl = " \\\\[0.1cm] "
		question = intro + "\\begin{center}" + qtable + nl + atableblank + "\\end{center}~"
		answer = "\\begin{center}" + atable + "\\end{center}~" + nl + "Lower Quartile = " + lq + "\\hspace{1cm} Median = " + median + "\\hspace{1cm}Upper Quartile = " + uq
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


