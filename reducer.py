#!/usr/bin/env python
from operator import itemgetter
import sys

#simple occurence counting script

current_term = None
current_count = 0
term = None

for line in sys.stdin:
	term, count = line.split('\t', 1)

	try:
		count = int(count)
	except ValueError:
		continue

	if current_term == term:
		current_count += count
	else:
		if current_term:
			print '%s\t%s' % (current_term, current_count)
		current_count = count
		current_term = term

if current_term == term:
	print '%s\t%s' % (current_term, current_count)
