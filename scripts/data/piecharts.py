#piecharts.py

def pietable(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Copy and complete the table for a pie chart:\\\\"
		else:
			explanation = ""
		l1 = ["Maths","English","Science","French"]
		l2 = ["Tea","Coffee","Hot Chocolate","Warm Milk"]
		l3 = ["Red","Green","Blue","Yellow"]
		l4 = ["Bus","Car","Walk","Bike"]
		l5 = ["French","Spanish","German","Latin"]
		l6 = ["iPhone","Android","Blackberry","Windows"]
		l7 = ["Guitar","Bass","Drums","Piano"]
		l8 = ["Rock","Pop","Jazz","Classical"]
		l9 = ["Football","Tennis","Rugby","Golf"]
		l10 = ["Chess","Draughts","Backgammon","Risk"]
		l11 = ["Apple","Orange","Strawberry","Banana"]
		l12 = ["Boat","Train","Plane","Coach"]
		l13 = ["Crisps","Nuts","Nachos","Pretzels"]
		l14 = ["Cat","Dog","Fish","Squirrel"]
		l15 = ["Peppa Pig","Teletubbies","Dora","Clangers"]
		l16 = ["Xbox","PS4","Switch","PC"]
		lists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16]
		titles = random.choice(lists)
		random.shuffle(lists)
		totals = [20,30,36,40,45,60,90,120,180]
		total = random.choice(totals)
		base = int(floor(total/16))
		n1 = base
		n2 = base * 2
		n3 = base * 4
		n4 = base * 8
		nums = [n1,n2,n3,n4]
		while nums[0] + nums[1] + nums[2] + nums[3] < total:
			temp = random.randrange(0,4)
			nums[temp] = nums[temp] + 1
		random.shuffle(nums)
		mult = int(360/total)
		angles = []
		for i in range(0,4):
			angles.append(str(mult * nums[i]) + "\\mydeg")
			nums[i] = str(nums[i])
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ M{1.7cm} | M{1.6cm} | M{1.2cm} } & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & \\\\ \\hline " + titles[1] + "  & " + nums[1] + " & \\\\ \\hline " + titles[2] + " & " + nums[2] + " & \\\\ \\hline " + titles[3] + "  & " + nums[3] + " & \\\\ \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ M{1.7cm} | M{1.6cm} | M{1.2cm} } & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & " + angles[0] + "\\\\ \\hline " + titles[1] + "  & " + nums[1] + " & " + angles[1] + "\\\\ \\hline " + titles[2] + " & " + nums[2] + " & " + angles[2] + "\\\\ \\hline " + titles[3] + "  & " + nums[3] + " & " + angles[3] + "\\\\ \\end{tabular}"

#		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{1.7cm} | M{1.6cm} | M{1.2cm} |} \\hline & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & \\\\ \\hline " + titles[1] + "  & " + nums[1] + " & \\\\ \\hline " + titles[2] + " & " + nums[2] + " & \\\\ \\hline " + titles[3] + "  & " + nums[3] + " & \\\\ \\hline \\end{tabular}"
#		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{1.7cm} | M{1.6cm} | M{1.2cm} |} \\hline & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & " + angles[0] + "\\\\ \\hline " + titles[1] + "  & " + nums[1] + " & " + angles[1] + "\\\\ \\hline " + titles[2] + " & " + nums[2] + " & " + angles[2] + "\\\\ \\hline " + titles[3] + "  & " + nums[3] + " & " + angles[3] + "\\\\ \\hline \\end{tabular}"

		question = explanation + qtable
		answer = explanation + atable
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pietable2(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Copy and complete the table for a pie chart:\\\\"
		else:
			explanation = ""
		l1 = ["Maths","English","Science","French"]
		l2 = ["Tea","Coffee","Hot Chocolate","Warm Milk"]
		l3 = ["Red","Green","Blue","Yellow"]
		l4 = ["Bus","Car","Walk","Bike"]
		l5 = ["French","Spanish","German","Latin"]
		l6 = ["iPhone","Android","Blackberry","Windows"]
		l7 = ["Guitar","Bass","Drums","Piano"]
		l8 = ["Rock","Pop","Jazz","Classical"]
		l9 = ["Football","Tennis","Rugby","Golf"]
		l10 = ["Chess","Draughts","Backgammon","Risk"]
		l11 = ["Apple","Orange","Strawberry","Banana"]
		l12 = ["Boat","Train","Plane","Coach"]
		l13 = ["Crisps","Nuts","Nachos","Pretzels"]
		l14 = ["Cat","Dog","Fish","Squirrel"]
		l15 = ["Peppa Pig","Teletubbies","Dora","Clangers"]
		l16 = ["Xbox","PS4","Switch","PC"]
		lists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16]
		titles = random.choice(lists)
		random.shuffle(lists)
		totals = [20,30,36,40,45,60,90,120,180]
		total = random.choice(totals)
		base = int(floor(total/16))
		n1 = base
		n2 = base * 2
		n3 = base * 4
		n4 = base * 8
		nums = [n1,n2,n3,n4]
		while nums[0] + nums[1] + nums[2] + nums[3] < total:
			temp = random.randrange(0,4)
			nums[temp] = nums[temp] + 1
		random.shuffle(nums)
		mult = int(360/total)
		angles = []
		for i in range(0,4):
			angles.append(str(mult * nums[i]) + "\\mydeg")
			nums[i] = str(nums[i])
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ M{1.7cm} | M{1.6cm} | M{1.2cm} } & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & " + "\\\\ \\hline " + titles[1] + "  & " + nums[1] + " & " + angles[1] + "\\\\ \\hline " + titles[2] + " & "  + " & " + angles[2] + "\\\\ \\hline " + titles[3] + "  & " + nums[3] + " & " + "\\\\ \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ M{1.7cm} | M{1.6cm} | M{1.2cm} } & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & " + angles[0] + "\\\\ \\hline " + titles[1] + "  & " + nums[1] + " & " + angles[1] + "\\\\ \\hline " + titles[2] + " & " + nums[2] + " & " + angles[2] + "\\\\ \\hline " + titles[3] + "  & " + nums[3] + " & " + angles[3] + "\\\\ \\end{tabular}"

#		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{1.7cm} | M{1.6cm} | M{1.2cm} |} \\hline & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & \\\\ \\hline " + titles[1] + "  & " + nums[1] + " & \\\\ \\hline " + titles[2] + " & " + nums[2] + " & \\\\ \\hline " + titles[3] + "  & " + nums[3] + " & \\\\ \\hline \\end{tabular}"
#		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | M{1.7cm} | M{1.6cm} | M{1.2cm} |} \\hline & Frequency & Angle \\\\ \\specialrule{1pt}{0pt}{0pt} " + titles[0] + " & " + nums[0] + " & " + angles[0] + "\\\\ \\hline " + titles[1] + "  & " + nums[1] + " & " + angles[1] + "\\\\ \\hline " + titles[2] + " & " + nums[2] + " & " + angles[2] + "\\\\ \\hline " + titles[3] + "  & " + nums[3] + " & " + angles[3] + "\\\\ \\hline \\end{tabular}"

		question = explanation + qtable
		answer = explanation + atable
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
