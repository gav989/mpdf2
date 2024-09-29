#!/bin/sh
chmod +x ./scripts/*.py

#old sequential command
#( cd ./scripts/ && for f in *.py; do python "$f"; done )

#xargs version
#( cd ./scripts/ && ls *.py | xargs -n 1 -P 3 python )

#parallel command
( cd ./scripts/ && ls *.py | parallel python )

#runner.sh
#( cd ./scripts/ && sh runner.sh )

mkdir -p ./MathsPDF-`date +"%Y-%m-%d"`/{Board/{Algebra/{Substitution,Simplifying\ Expressions,Single\ Bracket\ Expansion,Single\ Bracket\ Factorisation,Algebraic\ Fractions,Equations\ Cubic,Equations\ Linear,Equations\ Quadratic,Equations\ Simultaneous,Graphs,Inequalities,Rearranging\ Formulae,Sequences},Data/{Averages,Venn\ Diagrams},Measures/{Metric\ Units,Speed\ Distance\ Time,SUVAT,Time},Number/{FDP/{Fractions\ +-×÷,Fractions\ Of\ Amounts,Fraction\ Equivalence\ and\ Conversions,FDP\ Equivalence,Percentages,Recurring\ Decimals},Factors\ Multiples\ Primes\ Squares\ Cubes,Indices,Negative\ Numbers,Place\ Value,Prime\ Factors,Rounding,Truncation,Standard\ Form,Surds,Writing\ Numbers,Written\ Methods\ +-×÷},Ratio\ and\ Proportion/{Ratio,Proportion},Shape/{Area\ and\ Perimeter,Volume\ and\ Surface\ Area,Bearings,Names,Pythagoras,Trigonometry}},Exam\ Questions,Homeworks,Starters/{KS3,KS4,Other},Times\ Tables\ Programme/{2\ -\ 9,2\ -\ 12},Worksheets,Error}

rm ./scripts/deleteme*
rm ./scripts/*.vrb

mv ./scripts/*\|subs\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Substitution/
mv ./scripts/*\|simpexp\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Simplifying\ Expressions/
mv ./scripts/*\|sbexp\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Single\ Bracket\ Expansion/
mv ./scripts/*\|sbfac\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Single\ Bracket\ Factorisation/
mv ./scripts/*\|algfrac\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Algebraic\ Fractions/
mv ./scripts/*\|lineq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Equations\ Linear/
mv ./scripts/*\|quadeq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Equations\ Quadratic/
mv ./scripts/*\|cubeq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Equations\ Cubic/
mv ./scripts/*\|simeq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Equations\ Simultaneous/
mv ./scripts/*\|graphs\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Graphs/
mv ./scripts/*\|ineq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Inequalities/
mv ./scripts/*\|rearr\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Rearranging\ Formulae/
mv ./scripts/*\|seq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Algebra/Sequences/

mv ./scripts/*\|aver\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Data/Averages/
mv ./scripts/*\|venn\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Data/Venn\ Diagrams/
mv ./scripts/*\|data\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Data/

mv ./scripts/*\|metric\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Measures/Metric\ Units/
mv ./scripts/*\|sdt\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Measures/Speed\ Distance\ Time/
mv ./scripts/*\|suvat\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Measures/SUVAT/
mv ./scripts/*\|time\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Measures/Time/

mv ./scripts/*\|fracop\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/Fractions\ +-×÷/
mv ./scripts/*\|fracam\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/Fractions\ Of\ Amounts/
mv ./scripts/*\|fraceq\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/Fraction\ Equivalence\ and\ Conversions/
mv ./scripts/*\|fdp\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/FDP\ Equivalence/
mv ./scripts/*\|perc\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/Percentages/
mv ./scripts/*\|recdec\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/Recurring\ Decimals/
mv ./scripts/*\|fdptop\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/FDP/

mv ./scripts/*\|fmpsc\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Factors\ Multiples\ Primes\ Squares\ Cubes/
mv ./scripts/*\|indices\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Indices/
mv ./scripts/*\|negs\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Negative\ Numbers/
mv ./scripts/*\|plaval\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Place\ Value/
mv ./scripts/*\|primfac\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Prime\ Factors/
mv ./scripts/*\|round\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Rounding/
mv ./scripts/*\|trunc\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Truncation/
mv ./scripts/*\|sf\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Standard\ Form/
mv ./scripts/*\|surds\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Surds/
mv ./scripts/*\|wordfig\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Writing\ Numbers/
mv ./scripts/*\|writmeth\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Number/Written\ Methods\ +-×÷/

mv ./scripts/*\|ratio\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Ratio\ and\ Proportion/Ratio/
mv ./scripts/*\|prop\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Ratio\ and\ Proportion/Proportion/
mv ./scripts/*\|ratprop\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Ratio\ and\ Proportion/

mv ./scripts/*\|areaperi\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Shape/Area\ and\ Perimeter/
mv ./scripts/*\|volsurf\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Shape/Volume\ and\ Surface\ Area/
mv ./scripts/*\|bear\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Shape/Bearings/
mv ./scripts/*\|names\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Shape/Names/
mv ./scripts/*\|pythag\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Shape/Pythagoras/
mv ./scripts/*\|trig\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Board/Shape/Trigonometry/

mv ./scripts/*\|ks3\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Starters/KS3/
mv ./scripts/*\|ks4\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Starters/KS4/
mv ./scripts/*\|other\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Starters/Other/

mv ./scripts/*\|tt\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme/2\ -\ 12/
mv ./scripts/*\|ttn\|.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme/2\ -\ 9/

mv ./scripts/*Worksheet.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Worksheets/
mv ./scripts/*Homework.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Homeworks/
mv ./scripts/*EQ.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Exam\ Questions/
mv ./scripts/TTProg*.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme/2\ -\ 12
mv ./scripts/newTTProg*.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme/2\ -\ 9
mv ./scripts/*.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Error/

rmdir ./scripts/*.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Error
for file in ./MathsPDF-`date +"%Y-%m-%d"`/* ./MathsPDF-`date +"%Y-%m-%d"`/**/* ./MathsPDF-`date +"%Y-%m-%d"`/**/**/* ./MathsPDF-`date +"%Y-%m-%d"`/**/**/**/* ./MathsPDF-`date +"%Y-%m-%d"`/**/**/**/**/*; do mv "$file" "${file/|*|/}"; done
( cd ./MathsPDF-`date +"%Y-%m-%d"`/Exam\ Questions && for f in *.pdf; do rename " EQ.pdf" .pdf "$f"; done )
cp ./scripts/examquestions/pounddollarsprint.pdf ./MathsPDF-`date +"%Y-%m-%d"`/Exam\ Questions/Conversion\ Graph\ Printout.pdf
rm ../mathspdfpublic/MathsPDF.zip
zip -r ../mathspdfpublic/MathsPDF.zip MathsPDF-`date +"%Y-%m-%d"`
rm -R ./MathsPDF-*