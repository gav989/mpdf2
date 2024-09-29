#mean.py


def mean1(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the mean of "
		else:
			explanation = ""
		terms = random.randrange(3,8)
		mean = random.randrange(2,13)
		nums = []
		for i in range (0,terms):
			nums.append(1)
		total = mean * terms - terms
		for i in range (0,total):
			dec = random.randrange(0,terms)
			nums[dec] = nums[dec] + 1
		allnums = ""
		for i in range(0,terms):
			if i==0:
				allnums = allnums + str(nums[i])
			else:
				allnums = allnums + ", " + str(nums[i])
		question = explanation + allnums
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(mean))

def mean2(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the mean of "
		else:
			explanation = ""
		terms = random.randrange(3,8)
		nums = []
		for i in range (0,terms):
			nums.append(1)
		total = random.randrange(10,101)
		mean = rounddp(total/terms,2)
		if mean%1==0:
			mean = int(mean)
		for i in range (0,total-terms):
			dec = random.randrange(0,terms)
			nums[dec] = nums[dec] + 1
		allnums = ""
		for i in range(0,terms):
			if i==0:
				allnums = allnums + str(nums[i])
			else:
				allnums = allnums + ", " + str(nums[i])
		question = explanation + allnums
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(mean))


def mean3(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		terms = random.randrange(3,8)
		mean = random.randrange(2,13)
		nums = []
		for i in range (0,terms):
			nums.append(1)
		total = mean * terms - terms
		for i in range (0,total):
			dec = random.randrange(0,terms)
			nums[dec] = nums[dec] + 1
		answer = nums[terms-1]
		nums[terms-1] = "$\\Box$"
		allnums = ""
		for i in range(0,terms):
			if i==0:
				allnums = allnums + str(nums[i])
			else:
				allnums = allnums + ", " + str(nums[i])
		question = "The numbers " + allnums + " have a mean of " + str(mean) + ", find the value of $\\Box$"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def mean3prep(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		mean = random.randrange(3,13)
		nums = random.randrange(3,13)
		total = mean * nums
		question = str(nums) + " numbers have a mean of " + str(mean) + ". What do the numbers all add up to?"
		answer = str(total)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def mean4(n,explanationn):
#in ks3 unit 2
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
		freqs = [3,4,5,6,7,8,9,10,11,12]
		scores = [3,4,5,6,7,8,9,10,11,12]
		girlfreq = random.choice(freqs)
		freqs.remove(girlfreq)
		boyfreq = random.choice(freqs)
		girlscore = random.choice(scores)
		scores.remove(girlscore)
		boyscore = random.choice(scores)
		words = ("Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve")
		mean = rounddp((girlfreq*girlscore + boyfreq*boyscore) / (boyfreq + girlfreq),2)
		if mean%1==0:
			mean = int(mean)
		girlfreq = words[girlfreq-3]
		boyfreq = words[boyfreq-3]
		question = girlfreq + " girls have a mean test score of " + str(girlscore) + ". " + boyfreq + " boys have a mean test score of " + str(boyscore) + ". What is the overall mean test score?"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(mean))

def meantable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Use the table below to calculate the mean score. \\\\[0.3cm] "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			interval = 1
		else:
			interval = random.randrange(2,6)
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*interval
		scores = []
		for i in range(0,6):
			scores.append(scorestart+interval*i)
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]
		multsum = scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5]
		answer = rounddp((scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			scores[i] = str(scores[i])
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline " + scores[5] + " & " + freqs[5] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table 
		answer = str(multsum) + " $\\div$ " + str(freqsum) + " = " + str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def meantablemixer(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the mean: \\\\"
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			interval = 1
		else:
			interval = random.randrange(2,6)
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*interval
		scores = []
		for i in range(0,6):
			scores.append(scorestart+interval*i)
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]
		multsum = scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5]
		answer = rounddp((scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			scores[i] = str(scores[i])
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{2cm} | p{2cm} } Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline " + scores[5] + " & " + freqs[5] + " \\\\ \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table 
		answer = str(multsum) + " $\\div$ " + str(freqsum) + " = " + str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def meantableworksheet(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the mean \\\\"
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			interval = 1
		else:
			interval = random.randrange(2,6)
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*interval
		scores = []
		for i in range(0,6):
			scores.append(scorestart+interval*i)
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]
		multsum = scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5]
		answer = rounddp((scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			scores[i] = str(scores[i])
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline " + scores[5] + " & " + freqs[5] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table 
		answer = str(multsum) + " $\\div$ " + str(freqsum) + " = " + str(answer)
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\end{minipage}"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def meantablegrouped(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Use the table below to calculate an estimate of the mean score. \\\\[0.3cm] "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*10
		if random.randrange(0,2)==1:
			diffs = [5,10,15,20,25,30,40,50]
		else:
			diffs = [50,100,150,200,250,300,350,400,450,500]
		scorest = [scorestart]
		for i in range(0,5):
			scorest.append(scorest[i]+random.choice(diffs))
		midpoints = []
		for i in range(0,5):
			a = scorest[i]
			b = scorest[i + 1]
			if (a+b)/2%1==0:
				midpoints.append(int((a+b)/2))
			else:
				midpoints.append(rounddp((a+b)/2,1))
		scores = []
		for i in range(0,5):
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]
		freqpointsum = midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4]
		answer = rounddp((midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table
		answer = str(freqpointsum) + " $\\div$ " + str(freqsum) + " = " + str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def meantablegroupedmixer(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the mean: \\\\ "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*10
		if random.randrange(0,2)==1:
			diffs = [5,10,15,20,25,30,40,50]
		else:
			diffs = [50,100,150,200,250,300,350,400,450,500]
		scorest = [scorestart]
		for i in range(0,5):
			scorest.append(scorest[i]+random.choice(diffs))
		midpoints = []
		for i in range(0,5):
			a = scorest[i]
			b = scorest[i + 1]
			if (a+b)/2%1==0:
				midpoints.append(int((a+b)/2))
			else:
				midpoints.append(rounddp((a+b)/2,1))
		scores = []
		for i in range(0,5):
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]
		freqpointsum = midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4]
		answer = rounddp((midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{3cm} | p{2cm} } Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table
		answer = str(freqpointsum) + " $\\div$ " + str(freqsum) + " = " + str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def meantablegroupedworksheet(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Estimate the mean. \\\\ "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			scorestart = 0
		else:
			scorestart = random.randrange(1,6)*10
		if random.randrange(0,2)==1:
			diffs = [5,10,15,20,25,30,40,50]
		else:
			diffs = [50,100,150,200,250,300,350,400,450,500]
		scorest = [scorestart]
		for i in range(0,5):
			scorest.append(scorest[i]+random.choice(diffs))
		midpoints = []
		for i in range(0,5):
			a = scorest[i]
			b = scorest[i + 1]
			if (a+b)/2%1==0:
				midpoints.append(int((a+b)/2))
			else:
				midpoints.append(rounddp((a+b)/2,1))
		scores = []
		for i in range(0,5):
			scores.append("$" + str(scorest[i]) + " \\leq (S) < " + str(scorest[i+1]) + "$")
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		freqsum = freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]
		freqpointsum = midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4]
		answer = rounddp((midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			freqs[i] = str(freqs[i])
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3.5cm} | p{1.6cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = explanation + "\\centering" + table
		answer = str(freqpointsum) + " $\\div$ " + str(freqsum) + " = " + str(answer)
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\end{minipage}"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
