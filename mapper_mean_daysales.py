#!/usr/bin/python


#Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 0 (date) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data)==6:
		date,time,store,category,cost,pay_method = data
		weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
		print "{0}\t{1}".format(weekday,cost)
