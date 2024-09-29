#!/bin/sh
rm -R /home/gav/boardpdfscripts/BoardPDF-*
rm /home/gav/boardpdfscripts/scripts.zip
chmod +x /home/gav/boardpdfscripts/scripts/*.py
( cd /home/gav/Dropbox/Apps/boardpdfscripts/scripts/ && for f in *.py; do python "$f"; done )
rm /home/gav/Dropbox/Apps/boardpdfscripts/deleteme*
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Board
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Exam\ Questions
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Torture
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Starters
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Worksheets
mkdir /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme
rm /home/gav/Dropbox/Apps/boardpdfscripts/scripts/deleteme*
rm /home/gav/Dropbox/Apps/boardpdfscripts/scripts/*.vrb
mv /home/gav/Dropbox/Apps/boardpdfscripts/scripts/*Torture.pdf /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Torture/
mv /home/gav/Dropbox/Apps/boardpdfscripts/scripts/*Worksheet.pdf /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Worksheets/
mv /home/gav/Dropbox/Apps/boardpdfscripts/scripts/*Starter.pdf /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Starters/
mv /home/gav/Dropbox/Apps/boardpdfscripts/scripts/*EQ.pdf /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Exam\ Questions/
mv /home/gav/Dropbox/Apps/boardpdfscripts/scripts/TTProg*.pdf /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Times\ Tables\ Programme/
mv /home/gav/Dropbox/Apps/boardpdfscripts/scripts/*.pdf /home/gav/Dropbox/Apps/boardpdfscripts/BoardPDF-`date +"%Y-%m-%d"`/Board/
( cd /home/gav/Dropbox/Apps/boardpdfscripts/ && zip -r boardpdf BoardPDF-`date +"%Y-%m-%d"` )

