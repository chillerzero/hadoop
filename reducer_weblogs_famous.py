#!/usr/bin/python

import sys

totalHits=0
oldPage= None
hits=[]
dictionary={}

#Loop around the data
#Find the number of times a request has been made to a certain page
#Find the page with maximum number of hist

for line in sys.stdin:
	thisPage = line
	
	if oldPage and oldPage!=thisPage:
		hits.append(totalHits)
		dictionary[totalHits]=oldPage
		#print oldPage,":",totalHits
		oldPage=thisPage
		totalHits=0

	oldPage = thisPage
	totalHits+=1

if oldPage!=None:
	  hits.append(totalHits)
          dictionary[totalHits]=oldPage
	 #print oldPage,":",totalHits
print dictionary[max(hits)]
print max(hits)
