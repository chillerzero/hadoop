#!/usr/bin/python

import sys

salesTotal=0
oldCategory=None

# Loop around the data
# It will be in the format key\tval
# Where key is the category, val is the sale amount
#
# All the sales for a particular category will be presented,
# then the key will change and we'll be dealing with the next category

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	

	thisCategory,thisSale=data_mapped

	if oldCategory and oldCategory!=thisCategory:
		print oldCategory,"\t",salesTotal
		oldCategory=thisCategory
		salesTotal=0

	oldCategory=thisCategory
	salesTotal+=float(thisSale)

if oldCategory!=None:
	print oldCategory,"\t",salesTotal

	
