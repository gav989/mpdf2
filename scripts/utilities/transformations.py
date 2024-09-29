#transformations.py

def midpoint(n1,n2):
	from utilities.rounding import rounddp
	return(rounddp((n1+n2)/2,1))


def choosetriangle(xmin,xmax,ymin,ymax):    #e.g. (0,8,0,8) would be pos quadrant
	import random
	rightanglex = random.randrange(xmin,xmax+1)
	rightangley = random.randrange(ymin,ymax+1)
	if rightanglex < midpoint(xmin,xmax):
		xmult = 1
		xgap = xmax - rightanglex
	else:
		xmult = -1
		xgap = rightanglex - xmin
	if rightangley < midpoint(ymin,ymax):
		ymult = 1
		ygap = ymax - rightangley
	else:
		ymult = -1
		ygap = rightangley - ymin
	if xgap < ygap:
		if xgap==1:
			xlength = 1
		else:
			xlength = random.randrange(1,xgap)
		if xlength+1==min(ygap,xlength*3):
			ylength = xlength + 1
		else:
			ylength = random.randrange(xlength+1,min(ygap,xlength*3))
	else:
		if ygap==1:
			ylength = 1
		else:
			ylength = random.randrange(1,ygap)
		if ylength+1>=min(xgap,ylength*3):
			xlength = min(xgap,ylength*3)
		else:
			xlength = random.randrange(ylength+1,min(xgap,ylength*3))  # need to put an if statment to not run the random in case the lower and upper are the same number, which causes error
	x2 = rightanglex
	y2 = rightangley + ylength * ymult
	x3 = rightanglex + xlength * xmult
	y3 = rightangley
	return (rightanglex,rightangley,x2,y2,x3,y3)



def choosetrianglediag(coef):    #this is a horrible potentially infinite loop method
	import random
	xmin = -8
	xmax = 8
	ymin = -8
	ymax = 8
	rightanglex = 1
	rightangley = 1
	x2 = 2
	y2 = 2
	x3 = 3
	y3 = 3
	while rightanglex>=rightangley or x2>=y2 or x3>=y3:
		rightanglex = random.randrange(xmin,xmax+1)
		rightangley = random.randrange(ymin,ymax+1)
		if rightanglex < midpoint(xmin,xmax):
			xmult = 1
			xgap = xmax - rightanglex
		else:
			xmult = -1
			xgap = rightanglex - xmin
		if rightangley < midpoint(ymin,ymax):
			ymult = 1
			ygap = ymax - rightangley
		else:
			ymult = -1
			ygap = rightangley - ymin
		if xgap < ygap:
			xlength = random.randrange(1,xgap)
			if xlength+1 >= min(ygap,xlength*3):
				ylength = min(ygap,xlength*3)
			else:
				ylength = random.randrange(xlength+1,min(ygap,xlength*3))
		else:
			ylength = random.randrange(1,ygap)
			if ylength+1 >= min(xgap,ylength*3):
				xlength = min(xgap,ylength*3)
			else:
				xlength = random.randrange(ylength+1,min(xgap,ylength*3))
		x2 = rightanglex
		y2 = rightangley + ylength * ymult
		x3 = rightanglex + xlength * xmult
		y3 = rightangley
	if random.randrange(0,2)==1:
		rightanglex,rightangley,x2,y2,x3,y3 = rightangley,rightanglex,y2,x2,y3,x3
	if coef==-1:
		rightanglex,rightangley,x2,y2,x3,y3 = rightanglex*-1,rightangley*-1,x2*-1,y2*-1,x3*-1,y3*-1
	return (rightanglex,rightangley,x2,y2,x3,y3)

def reflectorvertical(x1,y1,x2,y2,x3,y3,ymirror):
	y1 = ymirror + (ymirror - y1)
	y2 = ymirror + (ymirror - y2)
	y3 = ymirror + (ymirror - y3)
	return(x1,y1,x2,y2,x3,y3)


def reflectorhorizontal(x1,y1,x2,y2,x3,y3,xmirror):
	x1 = xmirror + (xmirror - x1)
	x2 = xmirror + (xmirror - x2)
	x3 = xmirror + (xmirror - x3)
	return(x1,y1,x2,y2,x3,y3)



def reflectordiagonal(x1,y1,x2,y2,x3,y3,xco):  #reflect in line y = [xcoefficient]x, only ever 1 or -1
	x1,y1,x2,y2,x3,y3 = y1*xco,x1*xco,y2*xco,x2*xco,y3*xco,x3*xco
	return(x1,y1,x2,y2,x3,y3)


def rotator(x1,y1,x2,y2,x3,y3,angle,centrex,centrey):    #negative angle means anti-clockwise, only supports multiples of 90...
	vector1x = x1 - centrex
	vector1y = y1 - centrey
	vector2x = x2 - centrex
	vector2y = y2 - centrey
	vector3x = x3 - centrex
	vector3y = y3 - centrey
	if angle==90:
		x1 = centrex + vector1y
		y1 = centrey - vector1x
		x2 = centrex + vector2y
		y2 = centrey - vector2x
		x3 = centrex + vector3y
		y3 = centrey - vector3x
	elif angle==-90:
		x1 = centrex - vector1y
		y1 = centrey + vector1x
		x2 = centrex - vector2y
		y2 = centrey + vector2x
		x3 = centrex - vector3y
		y3 = centrey + vector3x
	else:
		x1 = centrex - vector1x
		y1 = centrey - vector1y	
		x2 = centrex - vector2x
		y2 = centrey - vector2y	
		x3 = centrex - vector3x
		y3 = centrey - vector3y	
	return(x1,y1,x2,y2,x3,y3)

def translator(x1,y1,x2,y2,x3,y3,vectorx,vectory):
	x1 = x1 + vectorx
	x2 = x2 + vectorx
	x3 = x3 + vectorx
	y1 = y1 + vectory
	y2 = y2 + vectory
	y3 = y3 + vectory
	return(x1,y1,x2,y2,x3,y3)

def enlarger(x1,y1,x2,y2,x3,y3,centrex,centrey,sf,x4=9,y4=9): #x4y4 is for enlarging a square, used only on gym enlargement
	vector1x = x1 - centrex
	vector1y = y1 - centrey
	vector2x = x2 - centrex
	vector2y = y2 - centrey
	vector3x = x3 - centrex
	vector3y = y3 - centrey
	vector4x = x4 - centrex
	vector4y = y4 - centrey
	x1 = centrex + vector1x * sf	
	x2 = centrex + vector2x * sf	
	x3 = centrex + vector3x * sf	
	y1 = centrey + vector1y * sf	
	y2 = centrey + vector2y * sf	
	y3 = centrey + vector3y * sf	
	x4 = centrex + vector4x * sf	
	y4 = centrey + vector4y * sf	
	if x4==9:
		return(x1,y1,x2,y2,x3,y3)
	else:
		x4 = centrex + vector4x * sf	
		y4 = centrey + vector4y * sf	
		return(x1,y1,x2,y2,x3,y3,x4,y4)




def drawtriangle(x1,y1,x2,y2,x3,y3,x4=9,y4=9,x5=9,y5=9,x6=9,y6=9,x7=9,y7=9): #only works with integers, x7y7 is for centre
	tester = x4
	centre = x7
	xmult = 0.4203125
	xadd = 0.135
	ymult = 0.42
	yadd = 0.18
	x1 = (x1+8)*xmult + xadd
	y1 = (y1+8)*ymult + yadd
	x2 = (x2+8)*xmult + xadd
	y2 = (y2+8)*ymult + yadd
	x3 = (x3+8)*xmult + xadd
	y3 = (y3+8)*ymult + yadd
	x4 = (x4+8)*xmult + xadd
	y4 = (y4+8)*ymult + yadd
	x5 = (x5+8)*xmult + xadd
	y5 = (y5+8)*ymult + yadd
	x6 = (x6+8)*xmult + xadd
	y6 = (y6+8)*ymult + yadd
	x7 = (x7+8)*xmult + xadd
	y7 = (y7+8)*ymult + yadd
	image = "\\begin{tikzpicture}\\node[anchor=south west,inner sep=0] at (0,0) {\\includegraphics[scale=0.8]{shape/images/coordinategrid}}; \\draw[ultra thin, fill=gray!50, fill opacity = 0.4] (" + str(x1) + "," + str(y1) + ") coordinate -- (" + str(x2) + "," + str(y2) + ") coordinate -- (" + str(x3) + " , " + str(y3) + ") coordinate -- (" + str(x1) + " , " + str(y1) + "); "
	if tester!=9:
		image = image + "\\draw[ultra thin, fill=black!100, fill opacity = 0.4] (" + str(x4) + "," + str(y4) + ") coordinate -- (" + str(x5) + "," + str(y5) + ") coordinate -- (" + str(x6) + " , " + str(y6) + ") coordinate -- (" + str(x4) + " , " + str(y4) + ");"
	if centre!=9:
		image = image + "\\draw[] (" + str(x7) + "," + str(y7) + ") node[circle,fill,inner sep=1pt]{};"
	image = image + "\\end{tikzpicture}"
	return(image)	





