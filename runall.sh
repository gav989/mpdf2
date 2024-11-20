#!/bin/sh
chmod +x ./scripts/*.py

( cd ./scripts/ && for f in *.py; do python "$f"; done )

mkdir -p ./MathsPDF2-`date +"%Y-%m-%d"`

rm ./scripts/deleteme*
rm ./scripts/*.vrb

mv ./scripts/*.pdf ./MathsPDF2-`date +"%Y-%m-%d"`/


rm ../mathspdfpublic/MathsPDF2.zip
zip -r ../mathspdfpublic/MathsPDF2.zip MathsPDF2-`date +"%Y-%m-%d"`
rm -R ./MathsPDF2-*
