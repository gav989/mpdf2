#mean.py

def meantable(n,explanationn):
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
		intro = "Use the table below to calculate the mean score."
		scores = [0,1,2,3,4,5]
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		answer = round((scores[0]*freqs[0] + scores[1]*freqs[1] + scores[2]*freqs[2] + scores[3]*freqs[3] + scores[4]*freqs[4] + scores[5]*freqs[5])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4] + freqs[5]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			scores[i] = str(scores[i])
			freqs[i] = str(freqs[i])
		table = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline " + scores[5] + " & " + freqs[5] + " \\\\ \\hline \\end{tabular}\\hfill"
		nl = " \\\\[0.3cm] "
		question = intro + nl + table
		answer = str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def meantablegrouped(n,explanationn):
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
		intro = "Use the table below to calculate an estimate of the mean score."
		dec = random.randrange(0,5)
		if dec==0:
			scores = ["$0 \\leq (S) < 10$","$10 \\leq (S) < 20$","$20 \\leq (S) < 30$","$30 \\leq (S) < 40$","$40 \\leq (S) < 50$"]
			midpoints = [5,15,25,35,45]
		elif dec==1:
			scores = ["$0 \\leq (S) < 5$","$5 \\leq (S) < 10$","$10 \\leq (S) < 15$","$15 \\leq (S) < 20$","$20 \\leq (S) < 30$"]
			midpoints = [2.5,7.5,12.5,17.5,25]
		elif dec==2:
			scores = ["$0 \\leq (S) < 10$","$10 \\leq (S) < 15$","$15 \\leq (S) < 20$","$20 \\leq (S) < 30$","$30 \\leq (S) < 50$"]
			midpoints = [5,12.5,17.5,25,40]
		elif dec==3:
			scores = ["$0 \\leq (S) < 50$","$50 \\leq (S) < 100$","$100 \\leq (S) < 200$","$200 \\leq (S) < 500$","$500 \\leq (S) < 800$"]
			midpoints = [25,75,150,350,650]
		else:
			scores = ["$0 \\leq (S) < 40$","$40 \\leq (S) < 60$","$60 \\leq (S) < 100$","$100 \\leq (S) < 200$","$200 \\leq (S) < 500$"]
			midpoints = [20,50,80,150,350]
		freqs = []
		for i in range (0,6):
			freqs.append(random.randrange(0,31))
		answer = round((midpoints[0]*freqs[0] + midpoints[1]*freqs[1] + midpoints[2]*freqs[2] + midpoints[3]*freqs[3] + midpoints[4]*freqs[4])/(freqs[0] + freqs[1] + freqs[2] + freqs[3] + freqs[4]),2)
		if answer%1==0:
			answer = int(answer)
		for i in range(0,6):
			freqs[i] = str(freqs[i])
		table = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{2cm} | } \\hline Score & Frequency \\\\ \\specialrule{1pt}{0pt}{0pt} " + scores[0] + " & " + freqs[0] + " \\\\ \\hline " + scores[1] + "  & " + freqs[1] + " \\\\ \\hline " + scores[2] + " & " + freqs[2] + " \\\\ \\hline " + scores[3] + "  & " + freqs[3] + " \\\\ \\hline " + scores[4] + " & " + freqs[4] + " \\\\ \\hline \\end{tabular}\\hfill"
		nl = " \\\\[0.3cm] "
		question = intro + nl + table
		answer = str(answer)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)