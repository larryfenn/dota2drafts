#!/usr/bin/env python
import sys
import itertools

#map values: ((1hero_id, 2hero_id):win(1)/loss(0), 1)

#Create two separate lists and export them
# list 1: radiant picks: all connections
# list 2: dire picks: all connections

for line in sys.stdin:
	choices = line.split(",")
	team_win = choices[1] # True = radiant won, False = dire won
	choices = choices[3:len(choices)]
	radiantpicks = list()
	direpicks = list()
	for i in range(len(choices)/3): # initial loop: scan and grab all the picks and create the sets
		if (choices[3*i] == "True"): # is a pick
			if (int(float(choices[3*i + 1])) == 0): # radiant team pick
				radiantpicks.append(int(float(choices[3*i + 2])))
			else:
				direpicks.append(int(float(choices[3*i + 2])))

	# now radiantpicks and direpicks are known, along with winning team: begin export
	radiantpicks.sort()
	direpicks.sort()

	radiantcliq = list(itertools.combinations(radiantpicks, 2)) # edit this if one wants triads, etc.
	direcliq = list(itertools.combinations(direpicks, 2))

	for c in radiantcliq: # :1 if it was a winning clique
		print '%s,%s:%s\t%s' % (c[0], c[1], int(team_win == 'True'), 1)
	for c in direcliq:
		print '%s,%s:%s\t%s' % (c[0], c[1], int(team_win == 'False'), 1)
