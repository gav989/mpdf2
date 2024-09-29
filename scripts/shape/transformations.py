#transformations.py

def reflecty(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			y = random.randrange(-6,7)
			xs = list(range(-8,9))
			ys = []
			if y>=0:
				for i in range(y,9):
					ys.append(i)
			else:
				for i in range(-8,y+1):
					ys.append(i)
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		Ax = ax
		Bx = bx
		Cx = cx
		Ay = y + y - ay
		By = y + y - by
		Cy = y + y - cy
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if y==0:
			if random.randrange(0,2)==1:
				end = "line \\mbox{y = 0}."
			else:
				end = "x-axis."
		else:
			end = "line \\mbox{y = $" + str(y) + "$}."
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been reflected in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def reflectx(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			x = random.randrange(-6,7)
			ys = list(range(-8,9))
			xs = []
			if x>=0:
				for i in range(x,9):
					xs.append(i)
			else:
				for i in range(-8,x+1):
					xs.append(i)
			ay = random.choice(ys)
			by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			cy = random.choice(ys)
			ax = random.choice(xs)
			if ay==by:
				xs.remove(ax)
				bx = random.choice(xs)
				xs.append(ax)
			else:
				bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			if ay==cy:
				while ax in xs:
					xs.remove(ax)
				cx = random.choice(xs)
			elif by==cy:
				while bx in xs:
					xs.remove(bx)
				cx = random.choice(xs)
			else:
				cx = random.choice(xs)
		Ay = ay
		By = by
		Cy = cy
		Ax = x + x - ax
		Bx = x + x - bx
		Cx = x + x - cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if x==0:
			if random.randrange(0,2)==1:
				end = "line \\mbox{x = 0}."
			else:
				end = "y-axis."
		else:
			end = "line \\mbox{x = $" + str(x) + "$}."
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been reflected in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def reflectyx(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = x}."
			ys = []
			if ax==8:
				ay = 8
			else:
				for i in range(ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==8:
				by = 8
			else:
				for i in range(bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==8:
				cy = 8
			else:
				for i in range(cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = ay
		Bx = by
		Cx = cy
		Ay = ax
		By = bx
		Cy = cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been reflected in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def reflectynegx(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==-8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==-8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = $-$x}."
	
			ys = []
			if ax==-8:
				ay = 8
			else:
				for i in range(-ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==-8:
				by = 8
			else:
				for i in range(-bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==-8:
				cy = 8
			else:
				for i in range(-cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = -ay
		Bx = -by
		Cx = -cy
		Ay = -ax
		By = -bx
		Cy = -cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been reflected in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflecty(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			y = random.randrange(-6,7)
			xs = list(range(-8,9))
			ys = []
			if y>=0:
				for i in range(y,9):
					ys.append(i)
			else:
				for i in range(-8,y+1):
					ys.append(i)
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		Ax = ax
		Bx = bx
		Cx = cx
		Ay = y + y - ay
		By = y + y - by
		Cy = y + y - cy
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if y==0:
			end = "line \\mbox{y = 0} (or x-axis)"
		else:
			end = "line \\mbox{y = $" + str(y) + "$}"
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Reflection in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflectx(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			x = random.randrange(-6,7)
			ys = list(range(-8,9))
			xs = []
			if x>=0:
				for i in range(x,9):
					xs.append(i)
			else:
				for i in range(-8,x+1):
					xs.append(i)
			ay = random.choice(ys)
			by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			cy = random.choice(ys)
			ax = random.choice(xs)
			if ay==by:
				xs.remove(ax)
				bx = random.choice(xs)
				xs.append(ax)
			else:
				bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			if ay==cy:
				while ax in xs:
					xs.remove(ax)
				cx = random.choice(xs)
			elif by==cy:
				while bx in xs:
					xs.remove(bx)
				cx = random.choice(xs)
			else:
				cx = random.choice(xs)
		Ay = ay
		By = by
		Cy = cy
		Ax = x + x - ax
		Bx = x + x - bx
		Cx = x + x - cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if x==0:
			end = "line \\mbox{x = 0} (or y-axis)"
		else:
			end = "line \\mbox{x = $" + str(x) + "$}"
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been reflected in the " + end
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Reflection in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectyx(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = x}."
			ys = []
			if ax==8:
				ay = 8
			else:
				for i in range(ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==8:
				by = 8
			else:
				for i in range(bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==8:
				cy = 8
			else:
				for i in range(cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = ay
		Bx = by
		Cx = cy
		Ay = ax
		By = bx
		Cy = cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectynegx(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==-8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==-8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = $-$x}."
	
			ys = []
			if ax==-8:
				ay = 8
			else:
				for i in range(-ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==-8:
				by = 8
			else:
				for i in range(-bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==-8:
				cy = 8
			else:
				for i in range(-cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = -ay
		Bx = -by
		Cx = -cy
		Ay = -ax
		By = -bx
		Cy = -cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflectyxDEAD(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = x}"
			ys = []
			if ax==8:
				ay = 8
			else:
				for i in range(ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==8:
				by = 8
			else:
				for i in range(bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==8:
				cy = 8
			else:
				for i in range(cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		ax = ay
		bx = by
		cx = cy
		ay = ax
		by = bx
		cy = cx
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 

		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		question = "triangle a has coordinates " + coords + ". triangle b has coordinates " + answer + ". describe the single transformation that maps triangle a onto triangle b."
		answer = "reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectynegxDEAD(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==-8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==-8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = $-$x}"
	
			ys = []
			if ax==-8:
				ay = 8
			else:
				for i in range(-ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==-8:
				by = 8
			else:
				for i in range(-bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==-8:
				cy = 8
			else:
				for i in range(-cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		ax = -ay
		bx = -by
		cx = -cy
		ay = -ax
		by = -bx
		cy = -cx
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 

		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		question = "triangle a has coordinates " + coords + ". triangle b has coordinates " + answer + ". describe the single transformation that maps triangle a onto triangle b."
		answer = "reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def rotate(n,explanationn): #DONT USE
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			if random.randrange(0,2)==1:	
				centre = "the origin"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = random.randrange(1,4)
		if rotation==1:
			rotation = "90\\mydeg clockwise"
			xdist = ax - centrex
			ydist = ay - centrey
			nxdist = ydist
			nydist = -xdist
			Ax = centrex + nxdist
			Ay = centrey + nydist
			xdist = bx - centrex
			ydist = by - centrey
			nxdist = ydist
			nydist = -xdist
			Bx = centrex + nxdist
			By = centrey + nydist
			xdist = cx - centrex
			ydist = cy - centrey
			nxdist = ydist
			nydist = -xdist
			Cx = centrex + nxdist
			Cy = centrey + nydist
		elif rotation==2:
			rotation = "180\\mydeg"
			xdist = ax - centrex
			ydist = ay - centrey
			nxdist = -xdist
			nydist = -ydist
			Ax = centrex + nxdist
			Ay = centrey + nydist
			xdist = bx - centrex
			ydist = by - centrey
			nxdist = -xdist
			nydist = -ydist
			Bx = centrex + nxdist
			By = centrey + nydist
			xdist = cx - centrex
			ydist = cy - centrey
			nxdist = -xdist
			nydist = -ydist
			Cx = centrex + nxdist
			Cy = centrey + nydist
		else:
			rotation = "90\\mydeg anti-clockwise"
			xdist = ax - centrex
			ydist = ay - centrey
			nxdist = -ydist
			nydist = xdist
			Ax = centrex + nxdist
			Ay = centrey + nydist
			xdist = bx - centrex
			ydist = by - centrey
			nxdist = -ydist
			nydist = xdist
			Bx = centrex + nxdist
			By = centrey + nydist
			xdist = cx - centrex
			ydist = cy - centrey
			nxdist = -ydist
			nydist = xdist
			Cx = centrex + nxdist
			Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been rotated " + rotation + " about centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def rotate90(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			if random.randrange(0,2)==1:	
				centre = "the origin"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = ydist
		nydist = -xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = ydist
		nydist = -xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = ydist
		nydist = -xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been rotated " + rotation + " about centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def rotate180(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			if random.randrange(0,2)==1:	
				centre = "the origin"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		if direction==0:
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2:
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "180\\mydeg"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -xdist
		nydist = -ydist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -xdist
		nydist = -ydist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -xdist
		nydist = -ydist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been rotated " + rotation + " about centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def rotate90ac(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			if random.randrange(0,2)==1:	
				centre = "the origin"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xdist = min(xdist,ydist)
		ydist = xdist
		xs = []
		ys = []
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg anti-clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -ydist
		nydist = xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -ydist
		nydist = xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -ydist
		nydist = xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been rotated " + rotation + " about centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describerotate(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = random.randrange(1,4)
		if rotation==1:
			rotation = "90\\mydeg clockwise"
			xdist = ax - centrex
			ydist = ay - centrey
			nxdist = ydist
			nydist = -xdist
			Ax = centrex + nxdist
			Ay = centrey + nydist
			xdist = bx - centrex
			ydist = by - centrey
			nxdist = ydist
			nydist = -xdist
			Bx = centrex + nxdist
			By = centrey + nydist
			xdist = cx - centrex
			ydist = cy - centrey
			nxdist = ydist
			nydist = -xdist
			Cx = centrex + nxdist
			Cy = centrey + nydist
		elif rotation==2:
			rotation = "180\\mydeg"
			xdist = ax - centrex
			ydist = ay - centrey
			nxdist = -xdist
			nydist = -ydist
			Ax = centrex + nxdist
			Ay = centrey + nydist
			xdist = bx - centrex
			ydist = by - centrey
			nxdist = -xdist
			nydist = -ydist
			Bx = centrex + nxdist
			By = centrey + nydist
			xdist = cx - centrex
			ydist = cy - centrey
			nxdist = -xdist
			nydist = -ydist
			Cx = centrex + nxdist
			Cy = centrey + nydist
		else:
			rotation = "90\\mydeg anti-clockwise"
			xdist = ax - centrex
			ydist = ay - centrey
			nxdist = -ydist
			nydist = xdist
			Ax = centrex + nxdist
			Ay = centrey + nydist
			xdist = bx - centrex
			ydist = by - centrey
			nxdist = -ydist
			nydist = xdist
			Bx = centrex + nxdist
			By = centrey + nydist
			xdist = cx - centrex
			ydist = cy - centrey
			nxdist = -ydist
			nydist = xdist
			Cx = centrex + nxdist
			Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describerotate90(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = ydist
		nydist = -xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = ydist
		nydist = -xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = ydist
		nydist = -xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describerotate180(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		if direction==0:
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2:
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "180\\mydeg"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -xdist
		nydist = -ydist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -xdist
		nydist = -ydist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -xdist
		nydist = -ydist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describerotate90ac(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg anti-clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -ydist
		nydist = xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -ydist
		nydist = xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -ydist
		nydist = xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def translate(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

		xtop = random.randrange(7,10)
		ytop = random.randrange(7,10)
		xbottom = xtop - 15
		ybottom = ytop - 15
		xs = list(range(xbottom,xtop))
		ys = list(range(ybottom,ytop))
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		xs = sorted([ax,bx,cx])
		ys = sorted([ay,by,cy])
		xmax = 8 - xs[2]
		xmin = -8 - xs[0]
		ymax = 8 - ys[2]
		ymin = -8 - ys[0]
		xs = list(range(xmin,xmax+1))
		ys = list(range(ymin,ymax+1))
		vx = random.choice(xs)
		if vx==0:
			if 0 in ys:
				ys.remove(0)
		vy = random.choice(ys)
		Ax = ax + vx
		Bx = bx + vx
		Cx = cx + vx
		Ay = ay + vy
		By = by + vy
		Cy = cy + vy
		vector = "\\Large{$\\left(\\begin{smallmatrix}" + str(vx) + "\\\\" + str(vy) + "\\end{smallmatrix}\\right)$}"
#create question
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been translated by " + vector + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describetranslate(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

		xtop = random.randrange(7,10)
		ytop = random.randrange(7,10)
		xbottom = xtop - 15
		ybottom = ytop - 15
		xs = list(range(xbottom,xtop))
		ys = list(range(ybottom,ytop))
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		xs = sorted([ax,bx,cx])
		ys = sorted([ay,by,cy])
		xmax = 8 - xs[2]
		xmin = -8 - xs[0]
		ymax = 8 - ys[2]
		ymin = -8 - ys[0]
		xs = list(range(xmin,xmax+1))
		ys = list(range(ymin,ymax+1))
		vx = random.choice(xs)
		if vx==0:
			if 0 in ys:
				ys.remove(0)
		vy = random.choice(ys)
		Ax = ax + vx
		Bx = bx + vx
		Cx = cx + vx
		Ay = ay + vy
		By = by + vy
		Cy = cy + vy
		vector = "\\Large{$\\left(\\begin{smallmatrix}" + str(vx) + "\\\\" + str(vy) + "\\end{smallmatrix}\\right)$}"
#create question
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Translation by " + vector
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def enlargepos(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)


			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been enlarged by scale factor " + str(sf) + ", centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def enlargeposfrac(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		sf = "$\\dfrac{1}{" + str(sf) + "}$"
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been enlarged by scale factor " + str(sf) + ", centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describeenlargepos(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)


			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def describeenlargeposfrac(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		sf = "$\\dfrac{1}{" + str(sf) + "}$"
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def enlargeneg(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = list(range(-4,5))
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(1,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$" + str(0 - sf) + "$"
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been enlarged by scale factor " + sf + ", centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def enlargenegfrac(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-4,-3,-2,2,3,4,1,-1]
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$-\\dfrac{1}{" + str(sf) + "}$"
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "A triangle has vertices at " + coords + ", find the triangle's coordinates after it has been enlarged by scale factor " + sf + ", centre " + centre + "."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describeenlargeneg(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = list(range(-4,5))
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(1,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$" + str(0 - sf) + "$"
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describeenlargenegfrac(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-4,-3,-2,2,3,4,1,-1]
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$-\\dfrac{1}{" + str(sf) + "}$"
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		question = "Triangle A has coordinates " + coords + ". Triangle B has coordinates " + answer + ". Describe the single transformation that maps triangle A onto triangle B."
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflecty2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			y = random.randrange(-6,7)
			xs = list(range(-8,9))
			ys = []
			if y>=0:
				for i in range(y,9):
					ys.append(i)
			else:
				for i in range(-8,y+1):
					ys.append(i)
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		Ax = ax
		Bx = bx
		Cx = cx
		Ay = y + y - ay
		By = y + y - by
		Cy = y + y - cy
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if y==0:
			end = "line \\mbox{y = 0} (or x-axis)"
		else:
			end = "line \\mbox{y = $" + str(y) + "$}"

		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"


		answer = "Reflection in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describereflectx2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			x = random.randrange(-6,7)
			ys = list(range(-8,9))
			xs = []
			if x>=0:
				for i in range(x,9):
					xs.append(i)
			else:
				for i in range(-8,x+1):
					xs.append(i)
			ay = random.choice(ys)
			by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			cy = random.choice(ys)
			ax = random.choice(xs)
			if ay==by:
				xs.remove(ax)
				bx = random.choice(xs)
				xs.append(ax)
			else:
				bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			if ay==cy:
				while ax in xs:
					xs.remove(ax)
				cx = random.choice(xs)
			elif by==cy:
				while bx in xs:
					xs.remove(bx)
				cx = random.choice(xs)
			else:
				cx = random.choice(xs)
		Ay = ay
		By = by
		Cy = cy
		Ax = x + x - ax
		Bx = x + x - bx
		Cx = x + x - cx
		answer = "\\mbox{($" + str(Ax) + "$ , $" + str(Ay) + "$)} " + "\\mbox{($" + str(Bx) + "$ , $" + str(By) + "$)}" + " \\mbox{($" + str(Cx) + "$ , $" + str(Cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		if x==0:
			end = "line \\mbox{x = 0} (or y-axis)"
		else:
			end = "line \\mbox{x = $" + str(x) + "$}"

		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"

		answer = "Reflection in the " + end
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectyx2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = x}"
			ys = []
			if ax==8:
				ay = 8
			else:
				for i in range(ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==8:
				by = 8
			else:
				for i in range(bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==8:
				cy = 8
			else:
				for i in range(cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = ay
		Bx = by
		Cx = cy
		Ay = ax
		By = bx
		Cy = cx
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describereflectynegx2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			xs = list(range(-8,9))
			ax = random.choice(xs)
			if ax==-8:
				xs.remove(ax)
			bx = random.choice(xs)
			if bx==-8:
				xs.remove(bx)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			line = "\\mbox{y = $-$x}"
	
			ys = []
			if ax==-8:
				ay = 8
			else:
				for i in range(-ax,9):
					ys.append(i)
				ay = random.choice(ys)
			ys = []
			if bx==-8:
				by = 8
			else:
				for i in range(-bx,9):
					ys.append(i)
				if ax==bx:
					if ay in ys:
						ys.remove(ay)
				by = random.choice(ys)
			ys = []
			if cx==-8:
				cy = 8
			else:
				for i in range(-cx,9):
					ys.append(i)
				if ax==cx:
					if ay in ys:
						ys.remove(ay)
				if bx==cx:
					if by in ys:
						ys.remove(by)
				if ay==by:
					if ay in ys:
						ys.remove(ay)
				cy = random.choice(ys)
		Ax = -ay
		Bx = -by
		Cx = -cy
		Ay = -ax
		By = -bx
		Cy = -cx
		answer = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		coords = "\\mbox{($" + str(ax) + "$ , $" + str(ay) + "$)} " + "\\mbox{($" + str(bx) + "$ , $" + str(by) + "$)}" + " \\mbox{($" + str(cx) + "$ , $" + str(cy) + "$)}" 
		if random.randrange(0,2)==1:
			temp = answer
			answer = coords
			coords = temp
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "reflection in the line " + line
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describerotate902(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = ydist
		nydist = -xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = ydist
		nydist = -xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = ydist
		nydist = -xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def rotate902(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg \\hspace{.5mm} clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = ydist
		nydist = -xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = ydist
		nydist = -xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = ydist
		nydist = -xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		question = "Rotate this triangle " + rotation + " about " + centre
		question = question + "\\\\ \\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\end{tikzpicture}"
		answer = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"

#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def describerotate1802(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		if direction==0:
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2:
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else:
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "180\\mydeg"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -xdist
		nydist = -ydist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -xdist
		nydist = -ydist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -xdist
		nydist = -ydist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describerotate90ac2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		centrex = random.randrange(-3,4)
		centrey = random.randrange(-3,4)
		centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
		if centrex==centrey==0:
			centre = centre + " (or the origin)"
		if centrex<0:
			xdist = -8 - centrex
		else:
			xdist = 8 - centrex
		if centrey<0:
			ydist = -8 - centrey
		else:
			ydist = 8 - centrey
		xdist = abs(xdist)
		ydist = abs(ydist)
		direction = random.randrange(0,4)
		xs = []
		ys = []
		xdist = min(xdist,ydist)
		ydist = xdist
		if direction==0: #up
			for i in range(centrey,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		elif direction==1: #right
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex,centrex+xdist+1):
				xs.append(i)
		elif direction==2: #down
			for i in range(centrey-ydist,centrey+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+xdist+1):
				xs.append(i)
		else: #3=left
			for i in range(centrey-ydist,centrey+ydist+1):
				ys.append(i)
			for i in range(centrex-xdist,centrex+1):
				xs.append(i)
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		print(xs)
		print(xdist)
		print(ydist)
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		rotation = "90\\mydeg anti-clockwise"
		xdist = ax - centrex
		ydist = ay - centrey
		nxdist = -ydist
		nydist = xdist
		Ax = centrex + nxdist
		Ay = centrey + nydist
		xdist = bx - centrex
		ydist = by - centrey
		nxdist = -ydist
		nydist = xdist
		Bx = centrex + nxdist
		By = centrey + nydist
		xdist = cx - centrex
		ydist = cy - centrey
		nxdist = -ydist
		nydist = xdist
		Cx = centrex + nxdist
		Cy = centrey + nydist
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Rotation " + rotation + " about centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describetranslate2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

		xtop = random.randrange(7,10)
		ytop = random.randrange(7,10)
		xbottom = xtop - 15
		ybottom = ytop - 15
		xs = list(range(xbottom,xtop))
		ys = list(range(ybottom,ytop))
		ax = 2
		bx = 3
		cx = 4
		ay = 3
		by = 4
		cy = 5	
		while ax!=bx and ax!=cx and bx!=cx and ay!=by and ay!=cy and by!=cy and ((ay - by) / (ax - bx)) == ((by - cy) / (bx - cx)):
			ax = random.choice(xs)
			bx = random.choice(xs)
			if ax==bx:
				xs.remove(ax)
			cx = random.choice(xs)
			ay = random.choice(ys)
			if ax==bx:
				ys.remove(ay)
				by = random.choice(ys)
				ys.append(ay)
			else:
				by = random.choice(ys)
			if ay==by:
				ys.remove(ay)
			if ax==cx:
				while ay in ys:
					ys.remove(ay)
				cy = random.choice(ys)
			elif bx==cx:
				while by in ys:
					ys.remove(by)
				cy = random.choice(ys)
			else:
				cy = random.choice(ys)
		xs = sorted([ax,bx,cx])
		ys = sorted([ay,by,cy])
		xmax = 8 - xs[2]
		xmin = -8 - xs[0]
		ymax = 8 - ys[2]
		ymin = -8 - ys[0]
		xs = list(range(xmin,xmax+1))
		ys = list(range(ymin,ymax+1))
		vx = random.choice(xs)
		if vx==0:
			if 0 in ys:
				ys.remove(0)
		vy = random.choice(ys)
		Ax = ax + vx
		Bx = bx + vx
		Cx = cx + vx
		Ay = ay + vy
		By = by + vy
		Cy = cy + vy
		vector = "\\Large{$\\left(\\begin{smallmatrix}" + str(vx) + "\\\\" + str(vy) + "\\end{smallmatrix}\\right)$}"
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
#create question
		answer = "Translation by " + vector
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describeenlargepos2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)


			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def describeenlargeposfrac2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrex = random.choice(xs)
			if centrex<-3 or centrex>3:
				ys = list(range(-8,9))
			else:
				ys = [-8,-7,-6,-5,-4,4,5,6,7,8]
			centrey = random.choice(ys)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey>0:
				zone = 13
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex==0 and centrey<0:
				zone = 15
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex<0:
				zone = 16
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrey==0 and centrex>0:
				zone = 14
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey>=4:
				zone = 1
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>=4 and centrey>=4:
				zone = 4
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<=-4:
				zone = 7
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<=-4 and centrey<=-4:
				zone = 10
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<0 and centrey>=4:
				zone = 2
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey>=4:
				zone = 3
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey>0:
				zone = 5
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex>=4 and centrey<0:
				zone = 6
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex>0 and centrey<=-4:
				zone = 8
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
			elif centrex<0 and centrey <=-4:
				zone = 9
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey<0:
				zone = 11
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(mediumgradients[i])
			elif centrex<=-4 and centrey>0:
				zone = 12
				for i in range(0,4):
					gradients.append(shallowgradients[i])
					gradients.append(0-shallowgradients[i])
					gradients.append(0-mediumgradients[i])
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0

			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = ag
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = bg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				


			leftzones = [4,5,6,7,14]
			rightzones = [1,12,16,11,10]
			m = cg
			if zone==2 and m<0 or zone==3 and m>=0 or zone==8 and mx<=0 or zone==9 and m<0:
				leftzones.append(zone)
			else:
				rightzones.append(zone)
			if zone in leftzones:
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
			steps = sorted([len(axs),len(bxs),len(cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = axs[second-1]
		Bx = bxs[second-1]
		Cx = cxs[second-1]
		Ay = ays[second-1]
		By = bys[second-1]
		Cy = cys[second-1]
		sf = "$\\dfrac{1}{" + str(sf) + "}$"
		aax = (ax+8)*0.4203125 + 0.135
		aay = (ay+8)*0.42 + 0.18
		bbx = (bx+8)*0.4203125 + 0.135
		bby = (by+8)*0.42 + 0.18
		ccx = (cx+8)*0.4203125 + 0.135
		ccy = (cy+8)*0.42 + 0.18
		AAx = (Ax+8)*0.4203125 + 0.135
		AAy = (Ay+8)*0.42 + 0.18
		BBx = (Bx+8)*0.4203125 + 0.135
		BBy = (By+8)*0.42 + 0.18
		CCx = (Cx+8)*0.4203125 + 0.135
		CCy = (Cy+8)*0.42 + 0.18
		ax = AAx
		bx = BBx
		cx = CCx
		ay = AAy
		by = BBy
		cy = CCy
		Ay = aay
		By = bby
		Cy = ccy
		Ax = aax
		Bx = bbx
		Cx = ccx
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def describeenlargeneg2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = list(range(-4,5))
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(1,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$" + str(0 - sf) + "$"
		ax = (ax+8)*0.4203125 + 0.135
		ay = (ay+8)*0.42 + 0.18
		bx = (bx+8)*0.4203125 + 0.135
		by = (by+8)*0.42 + 0.18
		cx = (cx+8)*0.4203125 + 0.135
		cy = (cy+8)*0.42 + 0.18
		Ax = (Ax+8)*0.4203125 + 0.135
		Ay = (Ay+8)*0.42 + 0.18
		Bx = (Bx+8)*0.4203125 + 0.135
		By = (By+8)*0.42 + 0.18
		Cx = (Cx+8)*0.4203125 + 0.135
		Cy = (Cy+8)*0.42 + 0.18
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def describeenlargenegfrac2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
		error=1
		while error==1:
			xs = [-4,-3,-2,2,3,4,1,-1]
			centrex = random.choice(xs)
			centrey = random.choice(xs)
			centre = "\\mbox{($" + str(centrex) + "$ , $" + str(centrey) + "$)}"
			steepgradients = [4,3,2,Fraction(3,2)]
			mediumgradients = [Fraction(4,3),1,Fraction(3,4),Fraction(2,3)]
			shallowgradients = [Fraction(1,2),Fraction(1,3),Fraction(1,4),0]
			gradients = []

			if centrex==0 and centrey==0:
				zone = 0
				directions = [0,1,2,3]
			elif centrex==0 and centrey>0:
				zone = 1
				directions = [1,2,3]
			elif centrex>0 and centrey==0:
				zone = 2
				directions = [0,2,3]
			elif centrex==0 and centrey<0:
				zone = 3
				directions = [3,0,1]
			elif centrex<0 and centrey==0:
				zone = 4
				directions = [0,1,2]
			elif centrex<0 and centrey>0:
				zone = 5
				directions = [1,2]
			elif centrex>0 and centrey>0:
				zone = 6
				directions = [3,2]
			elif centrex>0 and centrey<0:
				zone = 7
				directions = [0,3]
			elif centrex<0 and centrey<0:
				zone = 8
				directions = [0,1]
			direction = random.choice(directions)
			if zone<5:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
			elif zone==6 or zone==8:
				for i in range(0,4):
					gradients.append(steepgradients[i])
					gradients.append(mediumgradients[i])
					gradients.append(shallowgradients[i])
			else:
				for i in range(0,4):
					gradients.append(0-steepgradients[i])
					gradients.append(0-mediumgradients[i])
					gradients.append(0-shallowgradients[i])
				
			ag = random.choice(gradients)
			gradients.remove(ag)
			bg = random.choice(gradients)
			gradients.remove(bg)
			cg = random.choice(gradients)
			axs = []
			ays = []
			bxs = []
			bys = []
			cxs = []
			cys = []
			Axs = []
			Ays = []
			Bxs = []
			Bys = []
			Cxs = []
			Cys = []
			
			m = ag
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Axs.append(i)
						Ays.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						axs.append(i)
						ays.append(centrey - abs(centrex - i)*m)



			m = bg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Bxs.append(i)
						Bys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						bxs.append(i)
						bys.append(centrey - abs(centrex - i)*m)



			m = cg
			if m>=0 and direction==2 or m<0 and direction==0 or direction==3:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey - abs(centrex - i)*m)
			else:
				for i in range(centrex+1,9):
					if (centrey + abs(centrex - i)*m)%1==0 and abs(centrey + abs(centrex - i)*m)<=8:
						Cxs.append(i)
						Cys.append(centrey + abs(centrex - i)*m)
				for i in range(centrex-1,-9,-1):
					if (centrey - abs(centrex - i)*m)%1==0 and abs(centrey - abs(centrex - i)*m)<=8:
						cxs.append(i)
						cys.append(centrey - abs(centrex - i)*m)
			


			steps = sorted([len(Axs),len(Bxs),len(Cxs)])
			stepmax = steps[0]
			sfs = []
			for i in range(2,5):
				if i<=stepmax:
					sfs.append(i)
			sf = random.choice(sfs)
			firsts = []
			for i in range(1,8):
				if i*sf<=stepmax:
					firsts.append(i)
			first = random.choice(firsts)
			second = first * sf
			first = 1
			second = sf
			ax = axs[first-1]
			bx = bxs[first-1]
			cx = cxs[first-1]
			ay = ays[first-1]
			by = bys[first-1]
			cy = cys[first-1]
			try:
				g1 = ((ay - by) / (ax - bx))
			except:
				g1 = 20
			try:
				g2 = ((ay - cy) / (ax - cx))
			except:
				g2 = 20
			try:
				g3 = ((cy - by) / (cx - bx))
			except:
				g3 = 20
			if g1==g2==g3 or ax==bx and ay==by or ax==cx and ay==cy or bx==cx and by==cy:
				error = 1
			else:
				error = 0
		Ax = Axs[second-1]
		Bx = Bxs[second-1]
		Cx = Cxs[second-1]
		Ay = Ays[second-1]
		By = Bys[second-1]
		Cy = Cys[second-1]
		sf = "$-\\dfrac{1}{" + str(sf) + "}$"
		aax = (ax+8)*0.4203125 + 0.135
		aay = (ay+8)*0.42 + 0.18
		bbx = (bx+8)*0.4203125 + 0.135
		bby = (by+8)*0.42 + 0.18
		ccx = (cx+8)*0.4203125 + 0.135
		ccy = (cy+8)*0.42 + 0.18
		AAx = (Ax+8)*0.4203125 + 0.135
		AAy = (Ay+8)*0.42 + 0.18
		BBx = (Bx+8)*0.4203125 + 0.135
		BBy = (By+8)*0.42 + 0.18
		CCx = (Cx+8)*0.4203125 + 0.135
		CCy = (Cy+8)*0.42 + 0.18
		ax = AAx
		bx = BBx
		cx = CCx
		ay = AAy
		by = BBy
		cy = CCy
		Ay = aay
		By = bby
		Cy = ccy
		Ax = aax
		Bx = bbx
		Cx = ccx
		
		image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(ax) + "," + str(ay) + ") coordinate -- (" + str(bx) + "," + str(by) + ") coordinate -- (" + str(cx) + " , " + str(cy) + ") coordinate -- (" + str(ax) + " , " + str(ay) + "); \\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(Ax) + "," + str(Ay) + ") coordinate -- (" + str(Bx) + "," + str(By) + ") coordinate -- (" + str(Cx) + " , " + str(Cy) + ") coordinate -- (" + str(Ax) + " , " + str(Ay) + "); \\end{tikzpicture}"
		question = "\\begin{center} " + image + "\\end{center}~"
		answer = "Enlargement by scale factor " + str(sf) + ", centre " + centre
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
