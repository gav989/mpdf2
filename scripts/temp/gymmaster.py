#!/usr/bin/env python3
import subprocess, os, shutil, random, time
from math import floor
tempquestions = open("tempquestions","a")
template = "gym2"
session = 1

#########
#Settings
#########
hsessionmax = 200
fsessionmax = 199
isessionmax = 200
#hsessionmax = 1
#fsessionmax = 1
#isessionmax = 1

########
#Imports
########
from gym.gym import fexamquestions,hexamquestions,fexamquestionsbeamer,hexamquestionsbeamer,foundationformulae,higherformulae,suvat,fanglefacts2,hanglefacts2,exacttrigvalues, identifygraphs,  calc1,calc2,calc3,calc4,calc5,calc6,calc7,calc8,calc9,calc10,calc11,calc12,calc13,fracadd,fracsub,mixnumadd,mixnumsub,compoundinterestgym, equationcirclegym,fdpsix,fdpfive,donothing,shapenames,gymmetric,fmpscwallgym,coordinatesgym,suvattrig,meantablegroupedgym,meantablegym,histotablegym,cumfreqgym,hbearingsmem,fbearingsmem
from facts.fmp import fm,listfactors,listprimes
from graphs.linear import writegradient,writeintercept,writeequation
from fouroperators.addition import fulladdition,decimaladdition
from fouroperators.subtraction import fullsubtraction,decimalsubtraction
from fouroperators.multiplication import threebyonemultiplication,twobytwomultiplication,twobythreemultiplication,decimalmultiplication0,decimalmultiplication1,decimalmultiplication2
from fouroperators.division import singledigitdivision, twodigitdivisioneasy,decimaldivision1,decimaldivision2
from fouroperators.ten import multten,multhundred,multthousand,divten,divhundred,divthousand
from fouroperators.bidmas import bidmas1,bidmas2,bidmas3,bidmas4,bidmas5,bidmas6,bidmas7, bidmas8,bidmas9,bidmas10,bidmas11,bidmas12,bidmas13,bidmas14, bidmas15,bidmas16,bidmas17,bidmas18,bidmas19,bidmas20, bidmas21,bidmas22,bidmas23,bidmas24,bidmas25,bidmasbracs1,bidmasbracs2,bidmasbracs3,bidmasbracs4,bidmasbracs5, bidmasbracs6,bidmasbracs7,bidmasbracs8,bidmasbracs9,bidmasbracs10, bidmasbracs11,bidmasbracs12,bidmasbracs13,bidmasbracs14,bidmasbracs15, bidmasbracs16,bidmasbracs17,bidmasbracs18,bidmasbracs19,bidmasbracs20, bidmasbracs21,bidmasbracs22,bidmasbracs23,bidmasbracs24,bidmasbracs25, bidmasbracs26,bidmasbracs27,bidmasbracs28,bidmasbracs29
from fdp.fractionoperations import fractionsmultiply,fractionsmultiplyinteger,fractionsdivide,fractionsdivideinteger,mixednumbersmultiply,mixednumbersdivide,fractionofamount2
from fdp.percentages import perctestscore,percchange,percreverse,percincdec,percofamount,percofamount5gym,perc50,perc25,perc10,perc5,percincdec5
from indices.fracneg import negindices,negfrac1,negfrac2,fraction1pos,fraction1neg,fraction2pos,fraction2neg,zero, writeaspower1,writeaspower2,writeaspower3,writeaspower4, writeaspower5,writeaspower6,writeaspower7,writeaspower8, writeaspowermult,writeaspowerdiv
from indices.laws import multind,divind,indind,multindpos,divindpos,indindpos,multindneg,divindneg,indindneg
from indices.surds import simplifysurd1,simplifysurdmult1,simplifysurddiv1,simplifysurdadd,simplifysurdsubtract, surdquadratic1,surdquadratic1squared,surdquadratic2,ratden1,ratden2,ratdenDOTS,ratden3
from indices.standardform import sfconvert1,sfconvert2,sfmultiplyint,sfmultiply,sfdivide,sfadd,sfsubtract,sfconvertpos1,sfconvertpos2, sfconvertneg1,sfconvertneg2,sfdividepos,sfaddpos,sfsubtractpos,sfmultiplypos
from equations.linear import twostep1,twostep2,twostep5,twostep7,twostep8,threestep1,threestep2,threestep4,onestepadd,onestepsubtract,onestepmultiply,onestepdivide
from algebra.manipulation import collect1,collect2,multiplyterms1,multiplyterms2,multiplyterms3,multiplyterms4,multiplyterms5,multiplyterms6,multiplyterms7,multiplyterms8, singlebracketexpansion1,singlebracketexpansion2,singlebracketexpansion3,singlebracketexpansion4,singlebracketexpansion5,singlebracketexpansion6, singlebracketexpansion7,singlebracketexpansion8,singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3,singlebracketfactorise4, singlebracketfactorise5,singlebracketfactorise8
from equations.quadratics import expandquadraticspos,expandquadraticsneg
from algebra.substitution import subs1pos,subs1neg,subs2pos,subs2neg
from graphs.quadratic import substitution1pos,substitution1neg,substitution2pos,substitution2neg,substitution3pos,substitution3neg,substitution4pos,substitution4neg
from fdp.ratio import ratiosimplify,ratioshare1,ratioshare2,ratioreverse1,ratioreverse2,ratioreverse3,ratiopopulationlite
from fdp.rounding import round10,round100,round1000,round0dp,round1dp,round2dp,round1sf1,round2sf1,round3sf1,round1sf2,round2sf2,round3sf2, errorintervals10,errorintervalsdp,errorintervalssf,errorintervalstruncdp,errorintervalstruncsf
from fouroperators.negatives import negcountup,negcountdown,negadd,negsubtract,negmultiply,negdivide
from shape.pythagoras import pythagoras1bf,pythagoras2bf
from shape.trig import sinangle,cosangle,tanangle,sinside1,sinside2,cosside1,cosside2,tanside1,tanside2, trigareatriangle,cosineruleside,cosineruleangle,sineruleside,sineruleangle,trigareatriangle2
from shape.circles import arcsector1,arcsector2,arcsector3
from probability.trees import treesind2col,treesind2col2,treesind3col,treesdep2col,treesdep2col2,treesdep3col
from algebra.proportion import direct,directsquare,directsquareroot,inverse,inversesquare,inversesquareroot, directtable,directsquaretable,directsquareroottable,inversetable,inversesquaretable,inversesquareroottable
from fdp.fdp import recurringdec1,recurringdec2,recurringdec3
from data.venn import venn1,venn2,venn3,venn4,venn5,venn6,venn7,venn8,venn9,venn10,venn11,venn12
from primes.primefactors import hcflcm,hcflcmreverse
from shape.circles import circlearearadius,circlecircumferenceradius,circleareadiameter,circlecircumferencediameter
from shape.area import arealshape,areatrapezium
from starters.starters import nthtermlineargym,fibseq
from algebra.sequences import nthtermquad1,nthtermquad2,nthtermquad3,nthtermquad4,nthtermquad5,nthtermpos,nthtermneg,geoseqnthterm,geosurdseqnthterm
from algebra.manipulation import rearrangeonestepadd,rearrangeonestepsubtract1,rearrangeonestepsubtract2,rearrangeonestepmultiply, rearrangeonestepdivide1,rearrangeonestepdivide2,rearrangeonestepsquare,rearrangeonestepsquareroot, rearrangetwostep1,rearrangetwostep2,rearrangetwostep3, rearrangetwostep4,rearrangetwostep5,rearrangetwostep6, rearrangetwostep7,rearrangetwostep8,rearrangetwostep9, rearrangetwostep10,rearrangetwostep11,rearrangetwostep12, rearrangetwostep13,rearrangetwostep14,rearrangetwostep15, rearrangetwostep16, rearrangemulti
from equations.simultaneous import simeqlin1,simeqlin2,simeqlin3,simeqlinpos1,simeqquad1,simeqquad2
from equations.quadratics import quadcourse16pospos,quadcourse16negpos,quadcourse16posneg,quadcourse16negneg, quadcourse11,quadcourse12,quadcourse3,quadcourse6,factorisequadratics2pospos, factorisequadratics2posneg,factorisequadratics2negneg,solvequadratics2,quadraticformula,completesquare,completesquaresolve
from shape.names import circlepartsstarter
from measures.metricconversions import mcdistance1,mcdistance2,mcmass1,mcmass2,mccapacity1,mccapacity2
from gym.gym import gymreflect,gymrotate,gymtranslate,gymenlargepos,gymenlargeneg,gymenlargeposfrac,gymenlargenegfrac, gymreflectdescribe,gymrotatedescribe,gymtranslatedescribe,gymenlargeposdescribe,gymenlargenegdescribe,gymenlargeposfracdescribe, gymenlargenegfracdescribe





###############
#Question Packs
###############
adds = [fulladdition,decimaladdition]
subtracts = [fullsubtraction,decimalsubtraction]
mults = [threebyonemultiplication,twobytwomultiplication, twobythreemultiplication,decimalmultiplication0,decimalmultiplication1,decimalmultiplication2]
divs = [singledigitdivision, twodigitdivisioneasy,decimaldivision1,decimaldivision2]
mult10 = [multten,multhundred,multthousand]
div10 = [divten,divhundred,divthousand]
multdiv10 = [multten,multhundred,multthousand,divten,divhundred,divthousand]
calca = [calc3,calc4]
calcb = [calc5,calc10]
calcc = [calc6,calc8]
calcd = [calc7,calc9]
calce = [calc1,calc2]
calcf = [calc12,calc2]
fracaddsub = [fracadd,fracsub]
fracmultdiv = [fractionsmultiply,fractionsdivide]
fracint = [fractionsdivideinteger,fractionsmultiplyinteger]
fracintamount = [fractionsdivideinteger,fractionsmultiplyinteger,fractionofamount2,fractionofamount2]
mixnumaddsub = [mixnumadd,mixnumsub]
mixnummultdiv = [mixednumbersmultiply,mixednumbersdivide]
indlaws = [multind,divind,indind,zero]
indfraction = [fraction1pos,fraction1neg,fraction2pos,fraction2neg]
surdaddsubtract = [simplifysurdadd,simplifysurdsubtract]
surdquad = [surdquadratic1,surdquadratic1squared,surdquadratic2]
surdmultdiv = [simplifysurdmult1,simplifysurddiv1]
ratden = [ratden1,ratden2,ratdenDOTS,ratden3]
sfmult = [sfmultiplyint,sfmultiply]
sfaddsubtract = [sfadd,sfsubtract]
sfaddsubtractpos = [sfaddpos,sfsubtractpos]	
onestepaddsub = [onestepadd,onestepsubtract]
lineqs = [threestep4,twostep5]
multterms = [multiplyterms1,multiplyterms2,multiplyterms3,multiplyterms4,multiplyterms5,multiplyterms6,multiplyterms7,multiplyterms8]
collect = [collect1,collect2]
expandsingle = [singlebracketexpansion1,singlebracketexpansion2,singlebracketexpansion3,singlebracketexpansion4,singlebracketexpansion5,singlebracketexpansion8]
expandsimplifysingle = [singlebracketexpansion6,singlebracketexpansion7]
factorisesingle = [singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3,singlebracketfactorise4, singlebracketfactorise5,singlebracketfactorise8]
subs = [subs1pos,subs1neg,subs2pos,subs2neg,subs1pos,subs1neg,subs2pos,subs2neg,substitution1pos,substitution1neg,substitution2pos,substitution2neg, substitution3pos,substitution3neg,substitution4pos,substitution4neg]
numexpand = [singlebracketexpansion1,singlebracketexpansion2]
letterexpand = [singlebracketexpansion3,singlebracketexpansion4]
bothexpand = [singlebracketexpansion5,singlebracketexpansion8]
expandquad = [expandquadraticspos,expandquadraticsneg]
round1 = [round10,round100,round1000]
round2 = [round1sf1,round2sf1,round3sf1]
round3 = [round1sf2,round2sf2,round3sf2]
round4 = [round1dp,round2dp]
ratioshares = [ratioshare1,ratioshare2]
negcount = [negcountup,negcountdown]
pythags = [pythagoras1bf,pythagoras2bf,pythagoras1bf,pythagoras2bf]
trigsides = [sinside1,sinside2,cosside1,cosside2,tanside1,tanside2]
trigangles = [sinangle,cosangle,tanangle]
arcsectors = [arcsector1,arcsector2]
probtrees = [treesind2col,treesind2col2,treesind3col,treesdep2col,treesdep2col2,treesdep3col]
proportion = [direct,directsquare,directsquareroot,inverse,inversesquare,inversesquareroot, directtable,directsquaretable,directsquareroottable,inversetable,inversesquaretable,inversesquareroottable]
recdec = [recurringdec1,recurringdec2,recurringdec3]
venn = [venn1,venn2,venn3,venn4,venn5,venn6,venn7,venn8,venn9,venn10,venn11,venn12]
circles = [circlearearadius,circlecircumferenceradius,circleareadiameter,circlecircumferencediameter]
areas = [arealshape,areatrapezium]
bidmasa = [bidmas1,bidmas2,bidmas3,bidmas4,bidmas8,bidmas10,bidmas12,bidmas20,bidmas22,bidmas24]
bidmasbb = [bidmas5,bidmas6,bidmas7,bidmas9]
bidmasc = [bidmas14,bidmas15,bidmas17,bidmas18,bidmas19,bidmas25]
quadseq = [nthtermquad1,nthtermquad2,nthtermquad3,nthtermquad4,nthtermquad5]
rearrangesubs = [rearrangeonestepsubtract1,rearrangeonestepsubtract2]
rearrangedivs = [rearrangeonestepdivide1,rearrangeonestepdivide2]
rearrangesquares = [rearrangeonestepsquare,rearrangeonestepsquareroot]
rearrangetwos1 = [rearrangetwostep1,rearrangetwostep2]
rearrangetwos2 = [rearrangetwostep3,rearrangetwostep4]
rearrangetwos3 = [rearrangetwostep5,rearrangetwostep6]
rearrangetwos4 = [rearrangetwostep7,rearrangetwostep8]
rearrangetwos5 = [rearrangetwostep9,rearrangetwostep10]
rearrangetwos6 = [rearrangetwostep11,rearrangetwostep12]
rearrangetwos7 = [rearrangetwostep13,rearrangetwostep14]
quads21 = [quadcourse16pospos,quadcourse16negpos,quadcourse16posneg,quadcourse16negneg]
wap1 = [writeaspower1,writeaspower2]
wap2 = [writeaspower3,writeaspower4]
wap3 = [writeaspower5,writeaspower6]
wap4 = [writeaspower7,writeaspower8]
wap5 = [writeaspowermult,writeaspowerdiv]
errorintervals = [errorintervals10,errorintervalsdp,errorintervalssf,errorintervalstruncdp,errorintervalstruncsf]
negfracs = [negfrac1,negfrac2]
ftransformations = [gymreflect,gymrotate,gymtranslate,gymenlargepos,gymreflectdescribe,gymrotatedescribe,gymtranslatedescribe, gymenlargeposdescribe]
htransformations = [gymreflect,gymrotate,gymtranslate,gymenlargepos,gymenlargeneg,gymenlargeposfrac,gymenlargenegfrac, gymreflectdescribe,gymrotatedescribe,gymtranslatedescribe,gymenlargeposdescribe,gymenlargenegdescribe,gymenlargeposfracdescribe, gymenlargenegfracdescribe]
ftransformationsdescribe = [gymreflectdescribe,gymrotatedescribe,gymtranslatedescribe, gymenlargeposdescribe]
htransformationsdescribe = [gymreflectdescribe,gymrotatedescribe,gymtranslatedescribe,gymenlargeposdescribe,gymenlargenegdescribe,gymenlargeposfracdescribe, gymenlargenegfracdescribe]

#############
#Memorisation
#############
graphmem = [writegradient,writeintercept,writeequation,equationcirclegym,hbearingsmem]
fmem = [foundationformulae]
identifygraphslist = list(range(0,16))
random.shuffle(identifygraphslist)
hanglefactslist = list(range(0,14))
random.shuffle(hanglefactslist)
fanglefactslist = list(range(0,8))
random.shuffle(fanglefactslist)
shapenameslist = list(range(0,20))
random.shuffle(shapenameslist)
fmpscwallgymlist = list(range(0,5))
random.shuffle(fmpscwallgymlist)
metricconversionslist = list(range(0,10))
random.shuffle(metricconversionslist)
suvattriglist = list(range(0,19))
random.shuffle(suvattriglist)
higherformulaelist = list(range(0,12))
random.shuffle(higherformulaelist)



#8        88 88   ,ad8888ba,  88        88 88888888888 88888888ba 
#8        88 88  d8"'    `"8b 88        88 88          88      "8b
#8        88 88 d8'           88        88 88          88      ,8P
#8aaaaaaaa88 88 88            88aaaaaaaa88 88aaaaa     88aaaaaa8P'
#8""""""""88 88 88      88888 88""""""""88 88"""""     88""""88'  
#8        88 88 Y8,        88 88        88 88          88    `8b  
#8        88 88  Y8a.    .a88 88        88 88          88     `8b 
#8        88 88   `"Y88888P"  88        88 88888888888 88      `8b

highertitles = []
while session!=hsessionmax+1:
##########################
#Create higher table packs
##########################
	writcalc = [random.choice(multdiv10),random.choice(adds),random.choice(subtracts),random.choice(mults), random.choice(divs)]
	random.shuffle(writcalc)
	hcalculator = [random.choice(calce),random.choice(calca),random.choice(calcb),random.choice(calcc),random.choice(calcd)]
	hfractions = [random.choice(fracaddsub),random.choice(fracmultdiv),random.choice(fracintamount), random.choice(mixnumaddsub),random.choice(mixnummultdiv)]
	hperc = [percincdec,percreverse,percchange,perctestscore,compoundinterestgym]
	random.shuffle(indlaws)
	hindices = [indlaws[0],indlaws[1],negindices,random.choice(negfracs),random.choice(indfraction)]
	hsurds = [simplifysurd1,random.choice(surdmultdiv),random.choice(surdaddsubtract),random.choice(surdquad),random.choice(ratden)]
	hsf = [sfconvert1,sfconvert2,random.choice(sfmult),sfdivide,random.choice(sfaddsubtract)]
	hlineq = [twostep2,twostep7,twostep8,threestep2,random.choice(lineqs)]
	halgebra = [random.choice(multterms),random.choice(expandsingle),random.choice(expandsimplifysingle),random.choice(factorisesingle), random.choice(subs)]
	nthterm1 = [nthtermlineargym,donothing,donothing,donothing,donothing]
	hseqs = [quadseq[random.randrange(0,3)],quadseq[random.randrange(3,5)],nthtermpos,nthtermneg,geoseqnthterm,geosurdseqnthterm]
	random.shuffle(hseqs)
	bidmas = []
	bidmasb = [bidmas11,bidmas13,bidmas16,bidmas21,bidmas23,random.choice(bidmasbb)]
	random.shuffle(bidmasa)
	random.shuffle(bidmasb)
	random.shuffle(bidmasc)
	for i in range(0,1):
		bidmas.append(bidmasa[i])
	for i in range(0,1):
		bidmas.append(bidmasb[i])
	for i in range(0,1):
		bidmas.append(bidmasc[i])
	bracshard1 = [bidmasbracs8,bidmasbracs9,bidmasbracs10,bidmasbracs11,bidmasbracs12,bidmasbracs24,bidmasbracs25,bidmasbracs27]
	bracshard2 = [bidmasbracs1,bidmasbracs2,bidmasbracs3,bidmasbracs15,bidmasbracs18,bidmasbracs19, bidmasbracs20,bidmasbracs21,bidmasbracs22,bidmasbracs23,bidmasbracs26]
	bracshard22 = [bidmasbracs13,bidmasbracs14]
	bracshard3 = [bidmasbracs4,bidmasbracs5,bidmasbracs6,bidmasbracs7,bidmasbracs16,bidmasbracs17,bidmasbracs28,bidmasbracs29]
	random.shuffle(bracshard1)
	bracshard2.append(random.choice(bracshard22))
	bracshard23 = bracshard2 + bracshard3
	random.shuffle(bracshard23)
	bidmasbracs = [bracshard1[0],bracshard1[1],bracshard2[0],bracshard2[1],bracshard3[0]]
	bidmas.append(bracshard1[0])
	bidmas.append(bracshard23[0])
	rearrangeones = [rearrangeonestepadd,random.choice(rearrangesubs),rearrangeonestepmultiply, random.choice(rearrangedivs),random.choice(rearrangesquares)]
	rearrangetwos = [random.choice(rearrangetwos1),random.choice(rearrangetwos2),random.choice(rearrangetwos3),random.choice(rearrangetwos4), random.choice(rearrangetwos5),random.choice(rearrangetwos6),random.choice(rearrangetwos7),rearrangetwostep15, rearrangetwostep16]
	random.shuffle(rearrangeones)
	random.shuffle(rearrangetwos)
	rearrange = [rearrangeones[0],rearrangetwos[0],rearrangetwos[1],rearrangetwos[2],rearrangemulti]
	quads2 = [quadcourse16negpos,quadcourse16posneg,quadcourse16negneg]
	quads3 = [factorisequadratics2posneg,factorisequadratics2negneg]
	quadfacts = [quadcourse3,random.choice(quads2),factorisequadratics2pospos,random.choice(quads3),solvequadratics2]
	#hardquads = [random.choice(quads21),solvequadratics2,completesquare,completesquaresolve,quadraticformula]
	#wap = [random.choice(wap1),random.choice(wap2),random.choice(wap3),random.choice(wap4)]
	#random.shuffle(wap)
	#wap.append(random.choice(wap5))
#########################################################
#Create lists of table packs - bottom always memorisation
#########################################################
	if session==1:
		htoptable = [writcalc,hfractions,hperc,hlineq,halgebra,bidmas]
		htoptitles = ["Written Calculation (non-calc)","Fractions (non-calc)","Percentages (calc)","Solving Linear Equations (calc)","Algebra (non-calc)","BIDMAS (non-calc)"]
	hbottomtitles = ["Memorisation (non-calc)"]
#####################################
#Add in new content at various stages
#####################################
	if session==21:
		htoptable = htoptable + [hcalculator,hindices,hsurds,hsf,nthterm1,rearrange]
		htoptitles = htoptitles + ["Calculator Skills - Round to 2 d.p.","Indices (non-calc)","Surds (non-calc)","Standard Form (non-calc)","Sequences (non-calc)","Rearranging Formulae (non-calc)"]
	if session==101:
		htoptable = htoptable + [hseqs,quadfacts]
		htoptitles = htoptitles + ["Sequences (calc)","Factorising Quadractics (non-calc)"]
######################
#Create higher cyclers
######################
	topcycler = session%len(htoptable)
##########################
#Generate higher questions
##########################
	for i in range(0,5):
		htoptable[topcycler][i](1,1)
	graphcycler = session%len(graphmem)
	if session%len(identifygraphslist)==1:
		random.shuffle(identifygraphslist)
	if session%len(hanglefactslist)==1:
		random.shuffle(hanglefactslist)
	if session%len(suvattriglist)==1:
		random.shuffle(suvattriglist)
	if session%len(higherformulaelist)==1:
		random.shuffle(higherformulaelist)
	higherformulae(1,higherformulaelist[session%len(higherformulaelist)])
	suvattrig(1,suvattriglist[session%len(suvattriglist)])
	graphmem[graphcycler](1,1)
	diag1 = "Question 9 \\\\" + identifygraphs(1,identifygraphslist[session%len(identifygraphslist)])
	diag2 = "Question 10 \\\\" + hanglefacts2(1,hanglefactslist[session%len(hanglefactslist)])
	title1 = htoptitles[topcycler]
	title2 = "Memorisation (non-calc)"
	highertitles.append(title1)
#############
#Big Question
#############
	simeqhigher = [simeqlin1,simeqlin2,simeqlin3,simeqquad1,simeqquad2]
	bqsimeqhigher = random.choice(simeqhigher)
	bqpythag = random.choice(pythags)
	bqtrigsides = random.choice(trigsides)
	bqtrigangles = random.choice(trigangles)
	bqarcsectors = random.choice(arcsectors)
	bqprobtrees = random.choice(probtrees)
	bqprop = random.choice(proportion)
	bqrecdec = random.choice(recdec)	#delete when added to top five
	bqvenn = random.choice(venn)
	bqtransformations = random.choice(htransformations)
	bqtransformationsdescribe = random.choice(htransformationsdescribe)



##############new - doesn't shuffle bq order but prevents always havign the same type of simeq etc.
	hbigquestions = [bqtransformations,bqtransformationsdescribe,meantablegym,hcflcm,circlepartsstarter,meantablegroupedgym,histotablegym,cumfreqgym,hcflcmreverse]
	hbqpack1 = [fibseq,bqpythag,bqprobtrees,bqprop]
	hbqpack2 = [bqsimeqhigher,bqtrigsides,bqtrigangles,bqarcsectors,bqrecdec,bqvenn]
	if session > 30:
		hbigquestions += hbqpack1
	if session > 60:
		hbigquestions += hbqpack2
	bigquestioncycler = session%len(hbigquestions)
	hbigquestions[bigquestioncycler](1,1)

#############
#	if session==1:
#		hbigquestions = [meantablegym,hcflcm,circlepartsstarter,meantablegroupedgym,histotablegym,cumfreqgym,hcflcmreverse]
#		random.shuffle(hbigquestions)
#	if session%len(hbigquestions)==1:
#		random.shuffle(hbigquestions)
#	if session==31:
#		hbigquestions = hbigquestions + [fibseq,bqpythag,bqprobtrees,bqprop]
#	if session==61:
#		hbigquestions = hbigquestions + [bqsimeqhigher,bqtrigsides,bqtrigangles,bqarcsectors,bqrecdec,bqvenn]
#	bigquestioncycler = session%len(hbigquestions)
#	hbigquestions[bigquestioncycler](1,1)



#####################
#Set up higher footer
#####################
	footer = "Q9: $\\rule[-1.5mm]{6cm}{0.3mm}$ \\hspace{1cm} Q10: $\\rule[-1.5mm]{16cm}{0.3mm}$"

###################
#Set up first slide
###################
	graphanswers = ["$\\text{y} = \\text{x}$","$\\text{y} = -\\text{x}$","$\\text{y} = \\text{x}^{2}$","$\\text{y} = -\\text{x}^{2}$","$\\text{y} = \\text{x}^{3}$","$\\text{y} = -\\text{x}^{3}$","$\\text{y} = \\dfrac{1}{\\text{x}}$","$\\text{y} = -\\dfrac{1}{\\text{x}}$","$\\text{y} = \\text{Sin\,x}\\mydeg$","$\\text{y} = -\\text{Sin\,x}\\mydeg$","$\\text{y} = \\text{Cos\,x}\\mydeg$","$\\text{y} = -\\text{Cos\,x}\\mydeg$","$\\text{y} = \\text{Tan\,x}\\mydeg$","$\\text{y} = -\\text{Tan\,x}\\mydeg$","$\\text{y} = 2^{\\text{x}}$","$\\text{y} = -2^{\\text{x}}$"]
#	random.shuffle(graphanswers)
	for i in range(0,int(len(graphanswers)/2)): #MUST BE AN EVEN NUMBER OF GRAPHS
		diag1 = diag1 + "\\\\[0.2cm]" + graphanswers[2*i] + "\\hfill" + graphanswers[2*i+1]
########################
#Create Higher Documents
########################
	title3 = "Question 11"
	hexamquestions(session)
	hexamquestionsbeamer(session)
	tempquestions.close()
	sessiontext = "Session H" + str(session)
	sessiontext2 = "H" + str(session)
	if session<10:
		sessionnum = "00" + str(session)
	elif session<100:
		sessionnum = "0" + str(session)
	else:
		sessionnum = str(session)
	filename = "Higher Session " + sessionnum
	tempquestions = open("tempquestions","r")
	all = tempquestions.read().splitlines()
	lines = sum(1 for line in open('tempquestions'))
	lines=int((lines - 1)/2)
	#lines is now the total number of questions
	questions = []
	answers = []
	for x in range(0, lines):
		questions.append(str(all[2*x+1]))
		answers.append(str(all[2*x+2]))
	tempquestions.close()
	os.remove("tempquestions")

	# Read template to RAM
	filedata = None
	with open("templates/"+template+"q.tex", 'r') as qfile :
		qfiledata = qfile.read()
	with open("templates/"+template+"a.tex", 'r') as afile :
		afiledata = afile.read()

	# Replace text strings
	qfiledata = qfiledata.replace("title1",title1)
	afiledata = afiledata.replace("title1",title1)
	qfiledata = qfiledata.replace("title2",title2)
	afiledata = afiledata.replace("title2",title2)
	qfiledata = qfiledata.replace("title3",title3)
	afiledata = afiledata.replace("title3",title3)
	afiledata = afiledata.replace("diag1",diag1)
	afiledata = afiledata.replace("diag2",diag2)
	afiledata = afiledata.replace("sessiontext2",sessiontext2)
	qfiledata = qfiledata.replace("sessiontext",sessiontext)
	afiledata = afiledata.replace("sessiontext",sessiontext)
	qfiledata = qfiledata.replace("footer",footer)
	for x in range(0, lines):
		qterm = "q" + str(x+1) + " "
		aterm = "a" + str(x+1) + " "
		qfiledata = qfiledata.replace(qterm,questions[x])
		afiledata = afiledata.replace(qterm,questions[x])
		afiledata = afiledata.replace(aterm,answers[x])

	# Write to tex file
	with open(filename+"|hgymq.tex", 'w') as qfile:
		qfile.write(qfiledata)
	with open(filename+" - ANSWERS|hgym|.tex", 'w') as afile:
		afile.write(afiledata)

	subprocess.call(["pdflatex", filename+"|hgymq.tex"])
	subprocess.call(["pdflatex", filename+" - ANSWERS|hgym|.tex"])
	os.remove(filename + "|hgymq.aux")
	os.remove(filename + "|hgymq.log")
	os.remove(filename + "|hgymq.tex")
	os.remove(filename + " - ANSWERS|hgym|.aux")
	os.remove(filename + " - ANSWERS|hgym|.log")
	os.remove(filename + " - ANSWERS|hgym|.tex")
	os.remove(filename + " - ANSWERS|hgym|.vrb")
	os.remove(filename + " - ANSWERS|hgym|.toc")
	os.remove(filename + " - ANSWERS|hgym|.out")
	os.remove(filename + " - ANSWERS|hgym|.nav")
	os.remove(filename + " - ANSWERS|hgym|.snm")
	session = session + 1
#####################
#Create Higher Covers
#####################
#FRONT
hsessionnumberranges = []
for i in range(0,floor(hsessionmax/30)):
	a = i * 30 + 1
	b = a + 29
	if a<10:
		a = "00" + str(a)
	elif a<100:
		a = "0" + str(a)
	else:
		a = str(a)
	if b<10:
		b = "00" + str(b)
	elif b<100:
		b = "0" + str(b)
	else:
		b = str(b)
	hsessionnumberranges.append(a + " - " + b)
leftovermin = floor(hsessionmax/30)*30 + 1
if leftovermin < hsessionmax:
	hsessionnumberranges.append(str(leftovermin) + " - " + str(hsessionmax))
#BACK
for i in range(0,len(highertitles)):
	highertitles[i] = highertitles[i] + "$\\rule[-0.5mm]{1cm}{0.15mm}$/5 \\hfill Overall $\\rule[-0.5mm]{1cm}{0.15mm}$/$\\rule[-0.5mm]{1cm}{0.15mm}$"
highertitlecounter = 0

#MAKEDOCS
for i in range(0,len(hsessionnumberranges)):
	# Read template to RAM
	filedata = None
	with open("templates/gymfront.tex", 'r') as gfront :
		gfrontdata = gfront.read()
	with open("templates/gymback.tex", 'r') as gback :
		gbackdata = gback.read()

	# Replace text strings
	gfrontdata = gfrontdata.replace("tiertext","Higher")
	gfrontdata = gfrontdata.replace("sessionnumberrangetext",hsessionnumberranges[i])
	if i==len(hsessionnumberranges)-1:
		for j in range(1,hsessionmax-leftovermin+2):
			gbackdata = gbackdata.replace("sesh"+str(j) + " ",str(highertitlecounter+1))
			gbackdata = gbackdata.replace("s"+str(j) + " ",highertitles[highertitlecounter])
			highertitlecounter+=1
	else:	
		for j in range(1,31):
			gbackdata = gbackdata.replace("sesh"+str(j) + " ",str(highertitlecounter+1))
			gbackdata = gbackdata.replace("s"+str(j) + " ",highertitles[highertitlecounter])
			highertitlecounter+=1
	# Write to tex file
	with open("hgymfront" + str(i+1) + ".tex", 'w') as gfront:
		gfront.write(gfrontdata)
	with open("hgymback" + str(i+1) + ".tex", 'w') as gback:
		gback.write(gbackdata)

	subprocess.call(["pdflatex", "hgymfront" + str(i+1) + ".tex"])
	subprocess.call(["pdflatex", "hgymback" + str(i+1) + ".tex"])
	os.remove("hgymfront" + str(i+1) + ".aux")
	os.remove("hgymfront" + str(i+1) + ".log")
	os.remove("hgymfront" + str(i+1) + ".tex")
	os.remove("hgymback" + str(i+1) + ".aux")
	os.remove("hgymback" + str(i+1) + ".log")
	os.remove("hgymback" + str(i+1) + ".tex")
	

#8888888888 ,ad8888ba,   88        88 888b      88 88888888ba,        db   888888888888 88   ,ad8888ba,   888b      88
#8         d8"'    `"8b  88        88 8888b     88 88      `"8b      d88b       88      88  d8"'    `"8b  8888b     88
#8        d8'        `8b 88        88 88 `8b    88 88        `8b    d8'`8b      88      88 d8'        `8b 88 `8b    88
#8aaaaa   88          88 88        88 88  `8b   88 88         88   d8'  `8b     88      88 88          88 88  `8b   88
#8"""""   88          88 88        88 88   `8b  88 88         88  d8YaaaaY8b    88      88 88          88 88   `8b  88
#8        Y8,        ,8P 88        88 88    `8b 88 88         8P d8""""""""8b   88      88 Y8,        ,8P 88    `8b 88
#8         Y8a.    .a8P  Y8a.    .a8P 88     `8888 88      .a8P d8'        `8b  88      88  Y8a.    .a8P  88     `8888
#8          `"Y8888Y"'    `"Y8888Y"'  88      `888 88888888Y"' d8'          `8b 88      88   `"Y8888Y"'   88      `888

foundationtitles=[]
session = 1
while session!=fsessionmax+1:
##########################
#Create foundation table packs
##########################
	writcalc = [random.choice(adds),random.choice(subtracts),random.choice(mults), random.choice(divs),random.choice(multdiv10)]
	random.shuffle(writcalc)
	if random.randrange(0,2)==1:
		frac = [fractionofamount2,fracadd,fracsub,fractionsmultiply,fractionsdivideinteger]
	else:
		frac = [fractionofamount2,fracadd,fracsub,fractionsdivide,fractionsmultiplyinteger]
	perc = [perc50,perc25,perc10,perc5,percofamount5gym]
	fdp = [fdpfive,donothing,donothing,donothing,donothing]
	if random.randrange(0,2)==1:
		sf = [sfconvertpos1,sfconvertneg2,random.choice(sfaddsubtractpos),sfmultiplypos,sfdividepos]
	else:
		sf = [sfconvertneg1,sfconvertpos2,random.choice(sfaddsubtractpos),sfmultiplypos,sfdividepos]
	indices = [multindpos,multindneg,divindpos,divindneg,indindpos,indindneg]
	random.shuffle(indices)
	del indices[-1]
	equations = [random.choice(onestepaddsub),onestepmultiply,onestepdivide,twostep1,threestep1]
	ratio = [ratiosimplify,random.choice(ratioshares),ratioreverse1,ratioreverse3,ratiopopulationlite]
	calc = [calc1,random.choice(calcf),calc11,calc13,random.choice(calca)]
	brackets = [random.choice(numexpand),random.choice(letterexpand),random.choice(bothexpand),random.choice(expandsimplifysingle),random.choice(expandquad)]
	rounding = [random.choice(round1),round0dp,random.choice(round4),random.choice(round2),random.choice(round3)]
	negs1 = [negadd,negsubtract,negmultiply,negdivide]
	random.shuffle(negs1)
	negs = [random.choice(negcount),negs1[0],negs1[1],negs1[2],negs1[3]]
	bidmas = []
	bidmasb = [bidmas11,bidmas13,bidmas16,bidmas21,bidmas23,random.choice(bidmasbb)]
	random.shuffle(bidmasa)
	random.shuffle(bidmasb)
	random.shuffle(bidmasc)
	for i in range(0,2):
		bidmas.append(bidmasa[i])
	for i in range(0,2):
		bidmas.append(bidmasb[i])
	for i in range(0,1):
		bidmas.append(bidmasc[i])
	bracseasy1 = [bidmasbracs8,bidmasbracs9,bidmasbracs10,bidmasbracs11,bidmasbracs12,bidmasbracs24,bidmasbracs25,bidmasbracs27]
	bracseasy2 = [bidmasbracs13,bidmasbracs14,bidmasbracs15,bidmasbracs18]
	random.shuffle(bracseasy1)
	random.shuffle(bracseasy2)
	bidmasbracs = [bracseasy1[0],bracseasy1[1],bracseasy1[2],bracseasy1[3],bracseasy2[0]]
	rearrangeones = [rearrangeonestepadd,random.choice(rearrangesubs),rearrangeonestepmultiply, random.choice(rearrangedivs),random.choice(rearrangesquares)]
	rearrangetwos = [random.choice(rearrangetwos1),random.choice(rearrangetwos2),random.choice(rearrangetwos3),random.choice(rearrangetwos4), random.choice(rearrangetwos5),random.choice(rearrangetwos6),random.choice(rearrangetwos7),rearrangetwostep15, rearrangetwostep16]
	random.shuffle(rearrangeones)
	random.shuffle(rearrangetwos)
	rearrange = [rearrangeones[0],rearrangeones[1],rearrangeones[2],rearrangetwos[0],rearrangetwos[1]]
	quads1 = [quadcourse11,quadcourse12,quadcourse6]
	quads2 = [quadcourse16negpos,quadcourse16posneg]
	quadfacts = [quadcourse3,random.choice(quads1),quadcourse16pospos,random.choice(quads2),quadcourse16negneg]
	metricconversions = [mcdistance1,mcdistance2,mcmass1,mcmass2,mccapacity1,mccapacity2]
	random.shuffle(metricconversions)
	del metricconversions[-1]
#########################################################
#Create lists of table packs - bottom always memorisation
#########################################################
	if session==1:
		ftoptable = [writcalc,frac,perc,fdp,rounding,negs,bidmas, bidmasbracs,metricconversions]
		ftoptitles = ["Written Calculation (non-calc)","Fractions (non-calc)","Percentages (non-calc)","FDP (non-calc)","Rounding (non-calc)","Negative Numbers (non-calc)","BIDMAS (non-calc)","BIDMAS (non-calc)", "Metric Conversions (non-calc)"]
	fbottomtable = [fmem]
	fbottomtitles = ["Memorisation (non-calc)"]
#####################################
#Add in new content at various stages
#####################################
	if session==21:
		ftoptable = ftoptable + [sf,indices,equations,ratio,calc,brackets,errorintervals]
		ftoptitles = ftoptitles + ["Standard Form (non-calc)","Indices (non-calc)","Solving Equations (non-calc)","Ratio (non-calc)","Calculator Skills - Round to 2 d.p.","Expanding Brackets (non-calc)","Error Intervals (non-calc)"]
	if session==61:
		ftoptable = ftoptable + [rearrange,quadfacts]
		ftoptitles = ftoptitles + ["Rearranging Formulae (non-calc)","Quadratic Equations (non-calc)"]
##########################
#Create foundation cyclers
##########################
	topcycler = session%len(ftoptable)
	bottomcycler = session%len(fbottomtable)
##############################
#Generate foundation questions
##############################
	if session%len(fanglefactslist)==1:
		random.shuffle(fanglefactslist)
	if session%len(shapenameslist)==1:
		random.shuffle(shapenameslist)
	if session%len(metricconversionslist)==1:
		random.shuffle(metricconversionslist)
	if session%len(fmpscwallgymlist)==1:
		random.shuffle(fmpscwallgymlist)
	for i in range(0,5):
		ftoptable[topcycler][i](1,1)
	for i in range(0,1):
		fbottomtable[bottomcycler][i](1,session)
	diag1 = "Question 7 \\\\" + fmpscwallgym(1,fmpscwallgymlist[session%len(fmpscwallgymlist)])
	if random.randrange(0,4)==1:
		fbearingsmem(1,1)
	else:
		gymmetric(1,metricconversionslist[session%len(metricconversionslist)])
	diag1 = diag1 + "\\\\[1cm] Question 9 \\\\" + shapenames(1,shapenameslist[session%len(shapenameslist)])
	diag2 = "Question 10 \\\\" + fanglefacts2(1,fanglefactslist[session%len(fanglefactslist)])
	title1 = ftoptitles[topcycler]
	title2 = fbottomtitles[bottomcycler]
	foundationtitles.append(title1)
#############
#Big Question
#############
	simeqfoundation = [simeqlinpos1,simeqlinpos1,simeqlin1,simeqlin2,simeqlin3]
	bqsimeq = random.choice(simeqfoundation)
	bqpythag = random.choice(pythags)
	bqtrigsides = random.choice(trigsides)
	bqtrigangles = random.choice(trigangles)
	bqcircles = random.choice(circles)
	bqareas = random.choice(areas)
	bqtransformations = random.choice(ftransformations)
	bqtransformationsdescribe = random.choice(ftransformationsdescribe)
	


##############new - doesn't shuffle bq order but prevents always havign the same type of simeq etc.
	fbigquestions = [meantablegym,hcflcm,circlepartsstarter,bqcircles,bqareas]
	fbqpack1 = [meantablegroupedgym,fibseq,bqtransformations]
	fbqpack2 = [bqpythag,bqtrigsides,bqtrigangles,bqsimeq,bqtransformationsdescribe]
	if session > 30:
		fbigquestions += fbqpack1
	if session > 60:
		fbigquestions += fbqpack2
	bigquestioncycler = session%len(fbigquestions)
	fbigquestions[bigquestioncycler](1,1)





#	if session==1:
#		fbigquestions = [meantablegym,hcflcm,circlepartsstarter,bqcircles,bqareas]
#		random.shuffle(fbigquestions)
#	if session==21:
#		fbigquestions = fbigquestions + [meantablegroupedgym,fibseq]
#	if session==61:
#		fbigquestions = fbigquestions + [bqpythag,bqtrigsides,bqtrigangles,bqsimeq]
#	bigquestioncycler = session%len(fbigquestions)
#	fbigquestions[bigquestioncycler](1,1)
#########################
#Set up foundation footer
#########################
	footer = "Q9: $\\rule[-1.5mm]{6cm}{0.3mm}$ \\hspace{1cm} Q10: $\\rule[-1.5mm]{16cm}{0.3mm}$"
###################
#Set up first slide
###################

############################
#Create Foundation Documents
############################
	title3 = "Question 11"
	fexamquestions(session)
	fexamquestionsbeamer(session)
	tempquestions.close()
	sessiontext = "Session F" + str(session)
	sessiontext2 = "F" + str(session)
	if session<10:
		sessionnum = "00" + str(session)
	elif session<100:
		sessionnum = "0" + str(session)
	else:
		sessionnum = str(session)
	filename = "Foundation Session " + sessionnum
	tempquestions = open("tempquestions","r")
	all = tempquestions.read().splitlines()
	lines = sum(1 for line in open('tempquestions'))
	lines=int((lines - 1)/2)
	#lines is now the total number of questions
	questions = []
	answers = []
	for x in range(0, lines):
		questions.append(str(all[2*x+1]))
		answers.append(str(all[2*x+2]))
	tempquestions.close()
	os.remove("tempquestions")

	# Read template to RAM
	filedata = None
	with open("templates/"+template+"q.tex", 'r') as qfile :
		qfiledata = qfile.read()
	with open("templates/"+template+"a.tex", 'r') as afile :
		afiledata = afile.read()

	# Replace text strings
	qfiledata = qfiledata.replace("title1",title1)
	afiledata = afiledata.replace("title1",title1)
	qfiledata = qfiledata.replace("title2",title2)
	afiledata = afiledata.replace("title2",title2)
	qfiledata = qfiledata.replace("title3",title3)
	afiledata = afiledata.replace("title3",title3)
	afiledata = afiledata.replace("diag1",diag1)
	afiledata = afiledata.replace("diag2",diag2)
	afiledata = afiledata.replace("sessiontext2",sessiontext2)
	qfiledata = qfiledata.replace("sessiontext",sessiontext)
	afiledata = afiledata.replace("sessiontext",sessiontext)
	qfiledata = qfiledata.replace("footer",footer)
	for x in range(0, lines):
		qterm = "q" + str(x+1) + " "
		aterm = "a" + str(x+1) + " "
		qfiledata = qfiledata.replace(qterm,questions[x])
		afiledata = afiledata.replace(qterm,questions[x])
		afiledata = afiledata.replace(aterm,answers[x])

	# Write to tex file
	with open(filename+"|fgymq.tex", 'w') as qfile:
		qfile.write(qfiledata)
	with open(filename+" - ANSWERS|fgym|.tex", 'w') as afile:
		afile.write(afiledata)

	subprocess.call(["pdflatex", filename+"|fgymq.tex"])
	subprocess.call(["pdflatex", filename+" - ANSWERS|fgym|.tex"])
	os.remove(filename + "|fgymq.aux")
	os.remove(filename + "|fgymq.log")
	os.remove(filename + "|fgymq.tex")
	os.remove(filename + " - ANSWERS|fgym|.aux")
	os.remove(filename + " - ANSWERS|fgym|.log")
	os.remove(filename + " - ANSWERS|fgym|.tex")
	os.remove(filename + " - ANSWERS|fgym|.vrb")
	os.remove(filename + " - ANSWERS|fgym|.toc")
	os.remove(filename + " - ANSWERS|fgym|.out")
	os.remove(filename + " - ANSWERS|fgym|.nav")
	os.remove(filename + " - ANSWERS|fgym|.snm")
	session = session + 1

#########################
#Create Foundation Covers
#########################
#FRONT
fsessionnumberranges = []
for i in range(0,floor(fsessionmax/30)):
	a = i * 30 + 1
	b = a + 29
	if a<10:
		a = "00" + str(a)
	elif a<100:
		a = "0" + str(a)
	else:
		a = str(a)
	if b<10:
		b = "00" + str(b)
	elif b<100:
		b = "0" + str(b)
	else:
		b = str(b)
	fsessionnumberranges.append(a + " - " + b)
leftovermin = floor(fsessionmax/30)*30 + 1
if leftovermin < fsessionmax:
	fsessionnumberranges.append(str(leftovermin) + " - " + str(fsessionmax))
#BACK
for i in range(0,len(foundationtitles)):
	foundationtitles[i] = foundationtitles[i] + "$\\rule[-0.5mm]{1cm}{0.15mm}$/5 \\hfill Overall $\\rule[-0.5mm]{1cm}{0.15mm}$/$\\rule[-0.5mm]{1cm}{0.15mm}$"
foundationtitlecounter = 0

#MAKEDOCS
for i in range(0,len(fsessionnumberranges)):
	# Read template to RAM
	filedata = None
	with open("templates/gymfront.tex", 'r') as gfront :
		gfrontdata = gfront.read()
	with open("templates/gymback.tex", 'r') as gback :
		gbackdata = gback.read()

	# Replace text strings
	gfrontdata = gfrontdata.replace("tiertext","Foundation")
	gfrontdata = gfrontdata.replace("sessionnumberrangetext",fsessionnumberranges[i])
	if i==len(fsessionnumberranges)-1:
		for j in range(1,fsessionmax-leftovermin+2):
			gbackdata = gbackdata.replace("sesh"+str(j) + " ",str(foundationtitlecounter+1))
			gbackdata = gbackdata.replace("s"+str(j) + " ",foundationtitles[foundationtitlecounter])
			foundationtitlecounter+=1
	else:	
		for j in range(1,31):
			gbackdata = gbackdata.replace("sesh"+str(j) + " ",str(foundationtitlecounter+1))
			gbackdata = gbackdata.replace("s"+str(j) + " ",foundationtitles[foundationtitlecounter])
			foundationtitlecounter+=1
	# Write to tex file
	with open("fgymfront" + str(i+1) + ".tex", 'w') as gfront:
		gfront.write(gfrontdata)
	with open("fgymback" + str(i+1) + ".tex", 'w') as gback:
		gback.write(gbackdata)

	subprocess.call(["pdflatex", "fgymfront" + str(i+1) + ".tex"])
	subprocess.call(["pdflatex", "fgymback" + str(i+1) + ".tex"])
	os.remove("fgymfront" + str(i+1) + ".aux")
	os.remove("fgymfront" + str(i+1) + ".log")
	os.remove("fgymfront" + str(i+1) + ".tex")
	os.remove("fgymback" + str(i+1) + ".aux")
	os.remove("fgymback" + str(i+1) + ".log")
	os.remove("fgymback" + str(i+1) + ".tex")


#8 888b      88 888888888888 88888888888 88888888ba  88b           d88 88888888888 88888888ba,   88        db   888888888888 88888888888  
#8 8888b     88      88      88          88      "8b 888b         d888 88          88      `"8b  88       d88b       88      88           
#8 88 `8b    88      88      88          88      ,8P 88`8b       d8'88 88          88        `8b 88      d8'`8b      88      88           
#8 88  `8b   88      88      88aaaaa     88aaaaaa8P' 88 `8b     d8' 88 88aaaaa     88         88 88     d8'  `8b     88      88aaaaa      
#8 88   `8b  88      88      88"""""     88""""88'   88  `8b   d8'  88 88"""""     88         88 88    d8YaaaaY8b    88      88"""""      
#8 88    `8b 88      88      88          88    `8b   88   `8b d8'   88 88          88         8P 88   d8""""""""8b   88      88           
#8 88     `8888      88      88          88     `8b  88    `888'    88 88          88      .a8P  88  d8'        `8b  88      88           
#8 88      `888      88      88888888888 88      `8b 88     `8'     88 88888888888 88888888Y"'   88 d8'          `8b 88      88888888888  


intermediatetitles = []
session = 1
while session!=isessionmax+1:
##########################
#Create intermediate table packs
##########################
	writcalc = [random.choice(multdiv10),random.choice(adds),random.choice(subtracts),random.choice(mults), random.choice(divs)]
	random.shuffle(writcalc)
	hcalculator = [random.choice(calce),random.choice(calca),random.choice(calcb),random.choice(calcc),random.choice(calcd)]
	hfractions = [random.choice(fracaddsub),random.choice(fracmultdiv),random.choice(fracintamount), random.choice(mixnumaddsub),random.choice(mixnummultdiv)]
	hperc = [percincdec,percreverse,percchange,perctestscore,compoundinterestgym]
	random.shuffle(indlaws)
	hindices = [indlaws[0],indlaws[1],negindices,random.choice(negfracs),random.choice(indfraction)]
	hsurds = [simplifysurd1,random.choice(surdmultdiv),random.choice(surdaddsubtract),random.choice(surdquad),random.choice(ratden)]
	hsf = [sfconvert1,sfconvert2,random.choice(sfmult),sfdivide,random.choice(sfaddsubtract)]
	hlineq = [twostep2,twostep7,twostep8,threestep2,random.choice(lineqs)]
	halgebra = [random.choice(multterms),random.choice(expandsingle),random.choice(expandsimplifysingle),random.choice(factorisesingle), random.choice(subs)]
	nthterm1 = [nthtermlineargym,donothing,donothing,donothing,donothing]
	hseqs = [quadseq[random.randrange(0,3)],quadseq[random.randrange(3,5)],nthtermpos,nthtermneg,geoseqnthterm,geosurdseqnthterm]
	random.shuffle(hseqs)
	bidmas = []
	bidmasb = [bidmas11,bidmas13,bidmas16,bidmas21,bidmas23,random.choice(bidmasbb)]
	random.shuffle(bidmasa)
	random.shuffle(bidmasb)
	random.shuffle(bidmasc)
	for i in range(0,1):
		bidmas.append(bidmasa[i])
	for i in range(0,1):
		bidmas.append(bidmasb[i])
	for i in range(0,1):
		bidmas.append(bidmasc[i])
	bracshard1 = [bidmasbracs8,bidmasbracs9,bidmasbracs10,bidmasbracs11,bidmasbracs12,bidmasbracs24,bidmasbracs25,bidmasbracs27]
	bracshard2 = [bidmasbracs1,bidmasbracs2,bidmasbracs3,bidmasbracs15,bidmasbracs18,bidmasbracs19, bidmasbracs20,bidmasbracs21,bidmasbracs22,bidmasbracs23,bidmasbracs26]
	bracshard22 = [bidmasbracs13,bidmasbracs14]
	bracshard3 = [bidmasbracs4,bidmasbracs5,bidmasbracs6,bidmasbracs7,bidmasbracs16,bidmasbracs17,bidmasbracs28,bidmasbracs29]
	random.shuffle(bracshard1)
	bracshard2.append(random.choice(bracshard22))
	random.shuffle(bracshard2)
	random.shuffle(bracshard3)
	bidmasbracs = [bracshard1[0],bracshard1[1],bracshard2[0],bracshard2[1],bracshard3[0]]
	bracshard23 = bracshard2 + bracshard3
	random.shuffle(bracshard23)
	bidmasbracs = [bracshard1[0],bracshard1[1],bracshard2[0],bracshard2[1],bracshard3[0]]
	bidmas.append(bracshard1[0])
	bidmas.append(bracshard23[0])
	rearrangeones = [rearrangeonestepadd,random.choice(rearrangesubs),rearrangeonestepmultiply, random.choice(rearrangedivs),random.choice(rearrangesquares)]
	rearrangetwos = [random.choice(rearrangetwos1),random.choice(rearrangetwos2),random.choice(rearrangetwos3),random.choice(rearrangetwos4), random.choice(rearrangetwos5),random.choice(rearrangetwos6),random.choice(rearrangetwos7),rearrangetwostep15, rearrangetwostep16]
	random.shuffle(rearrangeones)
	random.shuffle(rearrangetwos)
	rearrange = [rearrangeones[0],rearrangetwos[0],rearrangetwos[1],rearrangetwos[2],rearrangemulti]
	quads2 = [quadcourse16negpos,quadcourse16posneg,quadcourse16negneg]
	quads3 = [factorisequadratics2posneg,factorisequadratics2negneg]
	quadfacts = [quadcourse3,random.choice(quads2),factorisequadratics2pospos,random.choice(quads3),solvequadratics2]
	hardquads = [random.choice(quads21),solvequadratics2,completesquare,completesquaresolve,quadraticformula]
	wap = [random.choice(wap1),random.choice(wap2),random.choice(wap3),random.choice(wap4)]
	random.shuffle(wap)
	wap.append(random.choice(wap5))
#########################################################
#Create lists of table packs - bottom always memorisation
#########################################################
	if session==1:
		itoptable = [writcalc,hfractions,hperc,hlineq,halgebra,bidmas]
		itoptitles = ["Written Calculation (non-calc)","Fractions (non-calc)","Percentages (calc)","Solving Linear Equations (calc)","Algebra (non-calc)","BIDMAS (non-calc)"]
	hbottomtitles = ["Memorisation (non-calc)"]
#####################################
#Add in new content at various stages
#####################################
	if session==21:
		itoptable = itoptable + [hcalculator,hsf,nthterm1]
		itoptitles = itoptitles + ["Calculator Skills - Round to 2 d.p.","Standard Form (non-calc)","Sequences (non-calc)"]
	if session==61:
		itoptable = itoptable + [rearrange]
		itoptitles = itoptitles + ["Rearranging Formulae (non-calc)"]
	if session==101:
		itoptable = itoptable + [hseqs,quadfacts]
		itoptitles = itoptitles + ["Sequences (calc)","Factorising Quadractics (non-calc)"]
######################
#Create intermediate cyclers
######################
	topcycler = session%len(itoptable)
##########################
#Generate intermediate questions
##########################
	for i in range(0,5):
		itoptable[topcycler][i](1,1)
	graphcycler = session%len(graphmem)
	if session%len(identifygraphslist)==1:
		random.shuffle(identifygraphslist)
	if session%len(hanglefactslist)==1:
		random.shuffle(hanglefactslist)
	if session%len(suvattriglist)==1:
		random.shuffle(suvattriglist)
	if session%len(higherformulaelist)==1:
		random.shuffle(higherformulaelist)
	higherformulae(1,higherformulaelist[session%len(higherformulaelist)])
	suvattrig(1,suvattriglist[session%len(suvattriglist)])
	graphmem[graphcycler](1,1)
	diag1 = "Question 9 \\\\" + identifygraphs(1,identifygraphslist[session%len(identifygraphslist)])
	diag2 = "Question 10 \\\\" + hanglefacts2(1,hanglefactslist[session%len(hanglefactslist)])
	title1 = itoptitles[topcycler]
	title2 = "Memorisation (non-calc)"
	intermediatetitles.append(title1)
#############
#Big Question
#############
	simeqint = [simeqlin1,simeqlin2,simeqlin3]
	bqsimeqint = random.choice(simeqint)
	bqpythag = random.choice(pythags)
	bqtrigsides = random.choice(trigsides)
	bqtrigangles = random.choice(trigangles)
	bqarcsectors = random.choice(arcsectors)
	bqprobtrees = random.choice(probtrees)
	bqprop = random.choice(proportion)
	bqrecdec = random.choice(recdec)	#delete when added to top five
	bqvenn = random.choice(venn)
	bqtransformations = random.choice(ftransformations)
	bqtransformationsdescribe = random.choice(ftransformationsdescribe)
	


##############new - doesn't shuffle bq order but prevents always havign the same type of simeq etc.
	ibigquestions = [meantablegym,hcflcm,circlepartsstarter,meantablegroupedgym,cumfreqgym,bqtransformations]
	ibqpack1 = [meantablegroupedgym,fibseq]
	ibqpack2 = [bqpythag,bqtrigsides,bqtrigangles,bqsimeq,bqtransformationsdescribe]
	if session > 30:
		ibigquestions += ibqpack1
	if session > 60:
		ibigquestions += ibqpack2
	bigquestioncycler = session%len(ibigquestions)
	ibigquestions[bigquestioncycler](1,1)




#	if session==1:
#		ibigquestions = [meantablegym,hcflcm,circlepartsstarter,meantablegroupedgym,cumfreqgym]
#		random.shuffle(ibigquestions)
#	if session%len(ibigquestions)==1:
#		random.shuffle(ibigquestions)
#	if session==21:
#		ibigquestions = ibigquestions + [fibseq,bqpythag,hcflcmreverse]
#	if session==61:
#		ibigquestions = ibigquestions + [bqarcsectors,bqprop,bqsimeqint]
#	if session==101:
#		ibigquestions = ibigquestions + [bqprobtrees,bqvenn,bqrecdec,bqtrigsides,bqtrigangles]
#	bigquestioncycler = session%len(ibigquestions)
#	ibigquestions[bigquestioncycler](1,1)


#####################
#Set up intermediate footer
#####################
	footer = "Q9: $\\rule[-1.5mm]{6cm}{0.3mm}$ \\hspace{1cm} Q10: $\\rule[-1.5mm]{16cm}{0.3mm}$"

###################
#Set up first slide
###################
	graphanswers = ["$\\text{y} = \\text{x}$","$\\text{y} = -\\text{x}$","$\\text{y} = \\text{x}^{2}$","$\\text{y} = -\\text{x}^{2}$","$\\text{y} = \\text{x}^{3}$","$\\text{y} = -\\text{x}^{3}$","$\\text{y} = \\dfrac{1}{\\text{x}}$","$\\text{y} = -\\dfrac{1}{\\text{x}}$","$\\text{y} = \\text{Sin\,x}\\mydeg$","$\\text{y} = -\\text{Sin\,x}\\mydeg$","$\\text{y} = \\text{Cos\,x}\\mydeg$","$\\text{y} = -\\text{Cos\,x}\\mydeg$","$\\text{y} = \\text{Tan\,x}\\mydeg$","$\\text{y} = -\\text{Tan\,x}\\mydeg$","$\\text{y} = 2^{\\text{x}}$","$\\text{y} = -2^{\\text{x}}$"]
#	random.shuffle(graphanswers)
	for i in range(0,int(len(graphanswers)/2)): #MUST BE AN EVEN NUMBER OF GRAPHS
		diag1 = diag1 + "\\\\[0.2cm]" + graphanswers[2*i] + "\\hfill" + graphanswers[2*i+1]
########################
#Create intermediate Documents
########################
	title3 = "Question 11"
	hexamquestions(session)
	hexamquestionsbeamer(session)
	tempquestions.close()
	sessiontext = "Session I" + str(session)
	sessiontext2 = "I" + str(session)
	if session<10:
		sessionnum = "00" + str(session)
	elif session<100:
		sessionnum = "0" + str(session)
	else:
		sessionnum = str(session)
	filename = "Intermediate Session " + sessionnum
	tempquestions = open("tempquestions","r")
	all = tempquestions.read().splitlines()
	lines = sum(1 for line in open('tempquestions'))
	lines=int((lines - 1)/2)
	#lines is now the total number of questions
	questions = []
	answers = []
	for x in range(0, lines):
		questions.append(str(all[2*x+1]))
		answers.append(str(all[2*x+2]))
	tempquestions.close()
	os.remove("tempquestions")

	# Read template to RAM
	filedata = None
	with open("templates/"+template+"q.tex", 'r') as qfile :
		qfiledata = qfile.read()
	with open("templates/"+template+"a.tex", 'r') as afile :
		afiledata = afile.read()

	# Replace text strings
	qfiledata = qfiledata.replace("title1",title1)
	afiledata = afiledata.replace("title1",title1)
	qfiledata = qfiledata.replace("title3",title3)
	afiledata = afiledata.replace("title3",title3)
	qfiledata = qfiledata.replace("title2",title2)
	afiledata = afiledata.replace("title2",title2)
	afiledata = afiledata.replace("diag1",diag1)
	afiledata = afiledata.replace("diag2",diag2)
	afiledata = afiledata.replace("sessiontext2",sessiontext2)
	qfiledata = qfiledata.replace("sessiontext",sessiontext)
	afiledata = afiledata.replace("sessiontext",sessiontext)
	qfiledata = qfiledata.replace("footer",footer)
	for x in range(0, lines):
		qterm = "q" + str(x+1) + " "
		aterm = "a" + str(x+1) + " "
		qfiledata = qfiledata.replace(qterm,questions[x])
		afiledata = afiledata.replace(qterm,questions[x])
		afiledata = afiledata.replace(aterm,answers[x])

	# Write to tex file
	with open(filename+"|igymq.tex", 'w') as qfile:
		qfile.write(qfiledata)
	with open(filename+" - ANSWERS|igym|.tex", 'w') as afile:
		afile.write(afiledata)

	subprocess.call(["pdflatex", filename+"|igymq.tex"])
	subprocess.call(["pdflatex", filename+" - ANSWERS|igym|.tex"])
	os.remove(filename + "|igymq.aux")
	os.remove(filename + "|igymq.log")
	os.remove(filename + "|igymq.tex")
	os.remove(filename + " - ANSWERS|igym|.aux")
	os.remove(filename + " - ANSWERS|igym|.log")
	os.remove(filename + " - ANSWERS|igym|.tex")
	os.remove(filename + " - ANSWERS|igym|.vrb")
	os.remove(filename + " - ANSWERS|igym|.toc")
	os.remove(filename + " - ANSWERS|igym|.out")
	os.remove(filename + " - ANSWERS|igym|.nav")
	os.remove(filename + " - ANSWERS|igym|.snm")
	session = session + 1
#####################
#Create Intermediate Covers
#####################
#FRONT
isessionnumberranges = []
for i in range(0,floor(isessionmax/30)):
	a = i * 30 + 1
	b = a + 29
	if a<10:
		a = "00" + str(a)
	elif a<100:
		a = "0" + str(a)
	else:
		a = str(a)
	if b<10:
		b = "00" + str(b)
	elif b<100:
		b = "0" + str(b)
	else:
		b = str(b)
	isessionnumberranges.append(a + " - " + b)
leftovermin = floor(isessionmax/30)*30 + 1
if leftovermin < isessionmax:
	isessionnumberranges.append(str(leftovermin) + " - " + str(isessionmax))
#BACK
for i in range(0,len(intermediatetitles)):
	intermediatetitles[i] = intermediatetitles[i] + "$\\rule[-0.5mm]{1cm}{0.15mm}$/5 \\hfill Overall $\\rule[-0.5mm]{1cm}{0.15mm}$/$\\rule[-0.5mm]{1cm}{0.15mm}$"
intermediatetitlecounter = 0

#MAKEDOCS
for i in range(0,len(isessionnumberranges)):
	# Read template to RAM
	filedata = None
	with open("templates/gymfront.tex", 'r') as gfront :
		gfrontdata = gfront.read()
	with open("templates/gymback.tex", 'r') as gback :
		gbackdata = gback.read()

	# Replace text strings
	gfrontdata = gfrontdata.replace("tiertext","Intermediate")
	gfrontdata = gfrontdata.replace("sessionnumberrangetext",isessionnumberranges[i])
	if i==len(isessionnumberranges)-1:
		for j in range(1,isessionmax-leftovermin+2):
			gbackdata = gbackdata.replace("sesh"+str(j) + " ",str(intermediatetitlecounter+1))
			gbackdata = gbackdata.replace("s"+str(j) + " ",intermediatetitles[intermediatetitlecounter])
			intermediatetitlecounter+=1
	else:	
		for j in range(1,31):
			gbackdata = gbackdata.replace("sesh"+str(j) + " ",str(intermediatetitlecounter+1))
			gbackdata = gbackdata.replace("s"+str(j) + " ",intermediatetitles[intermediatetitlecounter])
			intermediatetitlecounter+=1
	# Write to tex file
	with open("igymfront" + str(i+1) + ".tex", 'w') as gfront:
		gfront.write(gfrontdata)
	with open("igymback" + str(i+1) + ".tex", 'w') as gback:
		gback.write(gbackdata)

	subprocess.call(["pdflatex", "igymfront" + str(i+1) + ".tex"])
	subprocess.call(["pdflatex", "igymback" + str(i+1) + ".tex"])
	os.remove("igymfront" + str(i+1) + ".aux")
	os.remove("igymfront" + str(i+1) + ".log")
	os.remove("igymfront" + str(i+1) + ".tex")
	os.remove("igymback" + str(i+1) + ".aux")
	os.remove("igymback" + str(i+1) + ".log")
	os.remove("igymback" + str(i+1) + ".tex")
	
