#!/usr/bin/python

import sys

salesTotal=0
noOfSales=0
oldDay=None

# Loop around the data
# It will be in the format key\tval
# Where key is the day, val is the sale amount
#
# All the sales for a particular day will be presented,
# then the key will change and we'll be dealing with the next day

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	

	thisDay,thisSale=data_mapped

	if oldDay and oldDay!=thisDay:
		print oldDay,"\t",salesTotal/noOfSales
		oldDay=thisDay
		salesTotal=0
		noOfSales=0

	oldDay=thisDay
	salesTotal+=float(thisSale)
	noOfSales+=1.0

if oldDay!=None:
	print oldDay,"\t",salesTotal/noOfSales

	
