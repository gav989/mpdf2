#!/bin/sh
chmod +x ./scripts/*.py

( cd ./scripts/ && for f in *.py; do python "$f"; done )

mkdir -p ./MathsPDF2-`date +"%Y-%m-%d"`/{Starters}

mkdir -p ./GCSE-Gym-`date +"%Y-%m-%d"`/{Higher,Foundation,Intermediate}

rm ./scripts/deleteme*
rm ./scripts/*.vrb

pdfunite ./scripts/hgymfront1.pdf ./scripts/Higher\ Session\ {001..030}*gymq.pdf ./scripts/hgymback1.pdf ./scripts/Higher\ 001-030\|hgym\|.pdf
pdfunite ./scripts/hgymfront2.pdf ./scripts/Higher\ Session\ {031..060}*gymq.pdf ./scripts/hgymback2.pdf ./scripts/Higher\ 031-060\|hgym\|.pdf
pdfunite ./scripts/hgymfront3.pdf ./scripts/Higher\ Session\ {061..090}*gymq.pdf ./scripts/hgymback3.pdf ./scripts/Higher\ 061-090\|hgym\|.pdf
pdfunite ./scripts/hgymfront4.pdf ./scripts/Higher\ Session\ {091..120}*gymq.pdf ./scripts/hgymback4.pdf ./scripts/Higher\ 091-120\|hgym\|.pdf
pdfunite ./scripts/hgymfront5.pdf ./scripts/Higher\ Session\ {121..150}*gymq.pdf ./scripts/hgymback5.pdf ./scripts/Higher\ 121-150\|hgym\|.pdf
pdfunite ./scripts/hgymfront6.pdf ./scripts/Higher\ Session\ {151..180}*gymq.pdf ./scripts/hgymback6.pdf ./scripts/Higher\ 151-180\|hgym\|.pdf
pdfunite ./scripts/hgymfront7.pdf ./scripts/Higher\ Session\ {181..200}*gymq.pdf ./scripts/hgymback7.pdf ./scripts/Higher\ 181-200\|hgym\|.pdf

pdfunite ./scripts/fgymfront1.pdf ./scripts/Foundation\ Session\ {001..030}*gymq.pdf ./scripts/fgymback1.pdf ./scripts/Foundation\ 001-030\|fgym\|.pdf
pdfunite ./scripts/fgymfront2.pdf ./scripts/Foundation\ Session\ {031..060}*gymq.pdf ./scripts/fgymback2.pdf ./scripts/Foundation\ 031-060\|fgym\|.pdf
pdfunite ./scripts/fgymfront3.pdf ./scripts/Foundation\ Session\ {061..090}*gymq.pdf ./scripts/fgymback3.pdf ./scripts/Foundation\ 061-090\|fgym\|.pdf
pdfunite ./scripts/fgymfront4.pdf ./scripts/Foundation\ Session\ {091..120}*gymq.pdf ./scripts/fgymback4.pdf ./scripts/Foundation\ 091-120\|fgym\|.pdf
pdfunite ./scripts/fgymfront5.pdf ./scripts/Foundation\ Session\ {121..150}*gymq.pdf ./scripts/fgymback5.pdf ./scripts/Foundation\ 121-150\|fgym\|.pdf
pdfunite ./scripts/fgymfront6.pdf ./scripts/Foundation\ Session\ {151..180}*gymq.pdf ./scripts/fgymback6.pdf ./scripts/Foundation\ 151-180\|fgym\|.pdf
pdfunite ./scripts/fgymfront7.pdf ./scripts/Foundation\ Session\ {181..199}*gymq.pdf ./scripts/fgymback7.pdf ./scripts/Foundation\ 181-199\|fgym\|.pdf

pdfunite ./scripts/igymfront1.pdf ./scripts/Intermediate\ Session\ {001..030}*gymq.pdf ./scripts/igymback1.pdf ./scripts/Intermediate\ 001-030\|igym\|.pdf
pdfunite ./scripts/igymfront2.pdf ./scripts/Intermediate\ Session\ {031..060}*gymq.pdf ./scripts/igymback2.pdf ./scripts/Intermediate\ 031-060\|igym\|.pdf
pdfunite ./scripts/igymfront3.pdf ./scripts/Intermediate\ Session\ {061..090}*gymq.pdf ./scripts/igymback3.pdf ./scripts/Intermediate\ 061-090\|igym\|.pdf
pdfunite ./scripts/igymfront4.pdf ./scripts/Intermediate\ Session\ {091..120}*gymq.pdf ./scripts/igymback4.pdf ./scripts/Intermediate\ 091-120\|igym\|.pdf
pdfunite ./scripts/igymfront5.pdf ./scripts/Intermediate\ Session\ {121..150}*gymq.pdf ./scripts/igymback5.pdf ./scripts/Intermediate\ 121-150\|igym\|.pdf
pdfunite ./scripts/igymfront6.pdf ./scripts/Intermediate\ Session\ {151..180}*gymq.pdf ./scripts/igymback6.pdf ./scripts/Intermediate\ 151-180\|igym\|.pdf
pdfunite ./scripts/igymfront7.pdf ./scripts/Intermediate\ Session\ {181..200}*gymq.pdf ./scripts/igymback7.pdf ./scripts/Intermediate\ 181-200\|igym\|.pdf

rm ./scripts/*gymq.pdf
rm ./scripts/*gymback*
rm ./scripts/*gymfront*

mv ./scripts/*\|starter\|.pdf ./MathsPDF2-`date +"%Y-%m-%d"`/Starters/

for file in ./MathsPDF2-`date +"%Y-%m-%d"`/* ./MathsPDF2-`date +"%Y-%m-%d"`/**/* ./MathsPDF2-`date +"%Y-%m-%d"`/**/**/* ./MathsPDF2-`date +"%Y-%m-%d"`/**/**/**/* ./MathsPDF2-`date +"%Y-%m-%d"`/**/**/**/**/*; do mv "$file" "${file/|*|/}"; done
for file in ./GCSE-Gym-`date +"%Y-%m-%d"`/* ./GCSE-Gym-`date +"%Y-%m-%d"`/**/* ./GCSE-Gym-`date +"%Y-%m-%d"`/**/**/* ./GCSE-Gym-`date +"%Y-%m-%d"`/**/**/**/* ./GCSE-Gym-`date +"%Y-%m-%d"`/**/**/**/**/*; do mv "$file" "${file/|*|/}"; done

cp ./scripts/examquestions/pounddollarsprint.pdf ./MathsPDF2-`date +"%Y-%m-%d"`/Exam\ Questions/Conversion\ Graph\ Printout.pdf
cp ./scripts/shape/Grids.pdf ./MathsPDF2-`date +"%Y-%m-%d"`/Board/Transformations/Grids.pdf
cp ./scripts/data/scattergrids1.pdf ./MathsPDF2-`date +"%Y-%m-%d"`/Board/Scatter\ Graphs/Scatter\ Grids\ 1.pdf
cp ./scripts/data/scattergrids2.pdf ./MathsPDF2-`date +"%Y-%m-%d"`/Board/Scatter\ Graphs/Scatter\ Grids\ 2.pdf
rm ../mathspdfpublic/MathsPDF2.zip
rm ../mathspdfpublic/GCSE-Gym2.zip
zip -r ../mathspdfpublic/MathsPDF2.zip MathsPDF2-`date +"%Y-%m-%d"`
zip -r ../mathspdfpublic/GCSE-Gym2.zip GCSE-Gym-`date +"%Y-%m-%d"`
rm -R ./MathsPDF-*
rm -R ./GCSE-Gym-*
