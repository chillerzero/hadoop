#!/usr/bin/python

import sys

totalHits=0
oldPage= None

#Loop around the data
#Find the number of times a request has been made to a certain page
#Print the number of requests to /assets/js/the-associates.js

for line in sys.stdin:
	thisPage = line
	
	if oldPage and oldPage!=thisPage:
		print oldPage,":",totalHits
		oldPage=thisPage
		totalHits=0

	oldPage = thisPage
	totalHits+=1

if oldPage!=None:
	 print oldPage,":",totalHits
