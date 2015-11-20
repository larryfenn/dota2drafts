#!/usr/bin/env python
import sys

#map values: (hero_id:[0 if pick 1 if ban]:[which pick or ban out of 10], 1)

for line in sys.stdin:
	choices = line.split(",")
	choices = choices[3:len(choices)]
	pickCount = 0
	banCount = 0
	for i in range(len(choices)/3):
		if (choices[3*i] == "True"):
			print '%s\t%s' % (str(int(float(choices[3*i+2]))) + ":1:" + str(pickCount), 1)
			pickCount += 1
		else:
			print '%s\t%s' % (str(int(float(choices[3*i+2]))) + ":0:" + str(banCount), 1)
			banCount += 1
