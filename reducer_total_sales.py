#!/usr/bin/python

#Loop around the data
#count the number of sales
#and also total value of sales
#
#the input is of the form store\tsale

import sys

totalSales=0
totalValue=0
oldStore=None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	
	thisStore,thisSale=data_mapped

	if oldStore and oldStore!=thisStore:
		oldStore=thisStore
	
	oldStore=thisStore
	totalSales+=1
	totalValue+=float(thisSale)

if oldStore!=None:
	print "Total Number of sales: ",totalSales
	print "Total Value: ", totalValue
	
