#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
#We want two peices of data
#store and sale of that store

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data)==6:
		date,time,store,category,cost,method=data
		print "{0}\t{1}".format(store,cost)
