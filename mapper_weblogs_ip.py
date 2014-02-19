#!/usr/bin/python

#Format of each line is 
#10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
#
#we want to get the elements into a tuple and then seperate them into respective variables
#we want to get the web_page requested


import sys
for line in sys.stdin:
	data = line.strip().split(" ")
	ip=data[0]
	timestamp=data[3]+" "+data[4]
	http_method= data[5]
	web_page = data[6]
	http_version = data[7]
	status_code=data[8]
	return_object_size=data[9]
	print "{0}".format(ip)
	
	
	


