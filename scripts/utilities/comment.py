#!/usr/bin/env python3

def comment(words):
	tempquestions = open("tempquestions","a")
	tempquestions.write("\n")
#create question

#write question
	tempquestions.write(words)
	tempquestions.write("\n")
#write answer
	tempquestions.write("Comment")