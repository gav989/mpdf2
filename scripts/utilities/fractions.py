#rounding.py

def simpfrac(num,den):
	from math import floor,gcd
	if num==den:
		frac = str(1)
	elif num>den:
		integer = int(floor(num/den))
		num = num - integer*den
		if num==0:
			frac = str(integer)
		else:
			hcf = gcd(num,den)
			num = int(num/hcf)
			den = int(den/hcf)
			frac = str(integer) + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
	else:
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		frac = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
	frac = "\\mbox{" + frac + "}"
	return frac


def simpfrac2(num,den):
	from math import floor,gcd
	if num==den:
		frac = str(1)
	elif num>den:
		integer = int(floor(num/den))
		num = num - integer*den
		if num==0:
			frac = str(integer)
		else:
			hcf = gcd(num,den)
			num = int(num/hcf)
			den = int(den/hcf)
			frac = str(integer) + "$\\frac{" + str(num) + "}{" + str(den) + "}$"
	else:
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		frac = "$\\frac{" + str(num) + "}{" + str(den) + "}$"
	frac = "\\mbox{" + frac + "}"
	return frac