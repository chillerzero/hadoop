#!/usr/bin/python

import sys

totalHits=0
oldIP= None

#Loop around the data
#Find the number of times a request has been made to a certain page
#Print the number of requests to /assets/js/the-associates.js

for line in sys.stdin:
	thisIP = line
	
	if oldIP and oldIP!=thisIP:
		print oldIP,":",totalHits
		oldIP=thisIP
		totalHits=0

	oldIP = thisIP
	totalHits+=1

if oldIP!=None:
	 print oldIP,":",totalHits
