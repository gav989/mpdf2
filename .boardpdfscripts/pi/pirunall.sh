#!/bin/sh
rm -R /home/gav/boardpdf/BoardPDF-*
rm /home/gav/boardpdf/boardpdf.zip
rm -R /home/gav/boardpdf/scripts
rm /home/gav/boardpdf/scripts.zip
sh /home/gav/boardpdf/dropbox_uploader.sh download /scripts.zip /home/gav/boardpdf/
unzip /home/gav/boardpdf/scripts.zip -d /home/gav/boardpdf/
chmod +x /home/gav/boardpdf/scripts/*.py
( cd /home/gav/boardpdf/scripts/ && for f in *.py; do python "$f"; done )
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Board
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Exam\ Questions
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Torture
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Starters
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Worksheets
mkdir /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme
rm /home/gav/boardpdf/scripts/deleteme*
mv /home/gav/boardpdf/scripts/*Torture.pdf /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Torture/
mv /home/gav/boardpdf/scripts/*Worksheet.pdf /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Worksheets/
mv /home/gav/boardpdf/scripts/*Starter.pdf /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Starters/
mv /home/gav/boardpdf/scripts/*EQ.pdf /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Exam\ Questions/
mv /home/gav/boardpdf/scripts/TTProg* /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme
mv /home/gav/boardpdf/scripts/*.pdf /home/gav/boardpdf/BoardPDF-`date +"%Y-%m-%d"`/Board/
( cd /home/gav/boardpdf/ && zip -r boardpdf BoardPDF-`date +"%Y-%m-%d"` )
sh /home/gav/boardpdf/dropbox_uploader.sh upload /home/gav/boardpdf/boardpdf.zip /
