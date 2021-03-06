#!/usr/bin/python

#Loop around the data
#it will be of the format key\tval
#where key is store name and val is the sale
#
#for every store find the maximum sale made 
#by comparing with the previous maximum sale made for that store

import sys

maxSale=0
oldStore=None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	
	thisStore,thisSale=data_mapped
	
	if oldStore and oldStore!=thisStore:
		print oldStore,"\t",maxSale
		oldStore=thisStore
		maxSale=0

	oldStore=thisStore
	if float(thisSale)>float(maxSale):
		maxSale=float(thisSale)

if oldStore!=None:
	print oldStore,"\t",maxSale
