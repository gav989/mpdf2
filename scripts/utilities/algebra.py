#algebra.py

def algesort(n): #takes a list and sorts it, for rearranging, only supports single digits, then makes it a single string
	n = sorted(n)
	output = ""
	for i in range(0,len(n)):
		output = output + n[i]
	return output
