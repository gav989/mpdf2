#histograms.py

def histotable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		score1 = random.randrange(0,10)*10
		diffs = [5,10,20,40]
		diff1 = random.choice(diffs)
		if diff1==5:
			freq1 = random.randrange(1,11)
		else:
			freq1 = random.randrange(1,21) * int(diff1/10)
		diff2 = random.choice(diffs)
		if diff2==5:
			freq2 = random.randrange(1,11)
		else:
			freq2 = random.randrange(1,21) * int(diff2/10)
		diff3 = random.choice(diffs)
		if diff3==5:
			freq3 = random.randrange(1,11)
		else:
			freq3 = random.randrange(1,21) * int(diff3/10)
		diff4 = random.choice(diffs)
		if diff4==5:
			freq4 = random.randrange(1,11)
		else:
			freq4 = random.randrange(1,21) * int(diff4/10)
		diff5 = random.choice(diffs)
		if diff5==5:
			freq5 = random.randrange(1,11)
		else:
			freq5 = random.randrange(1,21) * int(diff5/10)
		diffs = [diff1,diff2,diff3,diff4,diff5]
		freqs = [freq1,freq2,freq3,freq4,freq5]
		scores = [score1]
		for i in range(0,len(diffs)):
			scores.append(scores[i] + diffs[i])
		intervals = []
		for i in range(1,len(scores)):
			intervals.append("$" + str(scores[i-1]) + " \\leq (S) < " + str(scores[i]) + "$")
		densities = []	
		for i in range(0,len(diffs)):
			densities.append(rounddp(freqs[i]/diffs[i],1))
		for i in range(0,len(diffs)):
			if densities[i]%1==0:
				densities[i] = int(densities[i])
		for i in range(0,len(diffs)):
			freqs[i] = str(freqs[i])
			densities[i] = str(densities[i])
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + intervals[0] + " & " + freqs[0] + " \\\\ \\hline " + intervals[1] + "  & " + freqs[1] + " \\\\ \\hline " + intervals[2] + " & " + freqs[2] + " \\\\ \\hline " + intervals[3] + "  & " + freqs[3] + " \\\\ \\hline " + intervals[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency Density \\\\ \\specialrule{1pt}{0pt}{0pt} " + intervals[0] + " & " + densities[0] + " \\\\ \\hline " + intervals[1] + "  & " + densities[1] + " \\\\ \\hline " + intervals[2] + " & " + densities[2] + " \\\\ \\hline " + intervals[3] + "  & " + densities[3] + " \\\\ \\hline " + intervals[4] + " & " + densities[4] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = "\\centering" + qtable
		answer = "\\centering" + atable
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def histotablemixer(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		score1 = random.randrange(0,10)*10
		diffs = [5,10,20,40]
		diff1 = random.choice(diffs)
		if diff1==5:
			freq1 = random.randrange(1,11)
		else:
			freq1 = random.randrange(1,21) * int(diff1/10)
		diff2 = random.choice(diffs)
		if diff2==5:
			freq2 = random.randrange(1,11)
		else:
			freq2 = random.randrange(1,21) * int(diff2/10)
		diff3 = random.choice(diffs)
		if diff3==5:
			freq3 = random.randrange(1,11)
		else:
			freq3 = random.randrange(1,21) * int(diff3/10)
		diff4 = random.choice(diffs)
		if diff4==5:
			freq4 = random.randrange(1,11)
		else:
			freq4 = random.randrange(1,21) * int(diff4/10)
		diff5 = random.choice(diffs)
		if diff5==5:
			freq5 = random.randrange(1,11)
		else:
			freq5 = random.randrange(1,21) * int(diff5/10)
		diffs = [diff1,diff2,diff3,diff4,diff5]
		freqs = [freq1,freq2,freq3,freq4,freq5]
		scores = [score1]
		for i in range(0,len(diffs)):
			scores.append(scores[i] + diffs[i])
		intervals = []
		for i in range(1,len(scores)):
			intervals.append("$" + str(scores[i-1]) + " \\leq (S) < " + str(scores[i]) + "$")
		densities = []	
		for i in range(0,len(diffs)):
			densities.append(rounddp(freqs[i]/diffs[i],1))
		for i in range(0,len(diffs)):
			if densities[i]%1==0:
				densities[i] = int(densities[i])
		for i in range(0,len(diffs)):
			freqs[i] = str(freqs[i])
			densities[i] = str(densities[i])
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + intervals[0] + " & " + freqs[0] + " \\\\ \\hline " + intervals[1] + "  & " + freqs[1] + " \\\\ \\hline " + intervals[2] + " & " + freqs[2] + " \\\\ \\hline " + intervals[3] + "  & " + freqs[3] + " \\\\ \\hline " + intervals[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency Density \\\\ \\specialrule{1pt}{0pt}{0pt} " + intervals[0] + " & " + densities[0] + " \\\\ \\hline " + intervals[1] + "  & " + densities[1] + " \\\\ \\hline " + intervals[2] + " & " + densities[2] + " \\\\ \\hline " + intervals[3] + "  & " + densities[3] + " \\\\ \\hline " + intervals[4] + " & " + densities[4] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = "Histogram \\\\ \\centering" + qtable
		answer = "\\begin{center}" + atable + "\\end{center}"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
