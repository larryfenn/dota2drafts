import json
import numpy as np
import herofilter as hf
import networkx as nx
from networkx.readwrite import json_graph

total = 0

f = open('output.txt', 'r')
# first pass: build solo hero winrates
heropickcount = np.zeros(114)
herowincount = np.zeros(114)
while True:
	line1 = f.readline()
	line2 = f.readline()
	if not line2: break
	line1 = line1.rstrip()
	line2 = line2.rstrip()
	edge_id, losscount = line1.split('\t')
	wincount = line2.split('\t')[1]
	edge_id = edge_id.split(':')[0]
	nodes = map(int, edge_id.split(','))
	pickcount = int(losscount) + int(wincount)
	for i in nodes:
		heropickcount[i] += int(pickcount)
		herowincount[i] += int(wincount)

f = open('output.txt', 'r')
popularitygraph = nx.Graph()
winrategraph = nx.Graph()
while True:
	line1 = f.readline()
	line2 = f.readline()
	if not line2: break
	line1 = line1.rstrip()
	line2 = line2.rstrip()
	edge_id, losscount = line1.split('\t')
	wincount = line2.split('\t')[1]
	edge_id  = edge_id.split(':')[0]
	nodes = map(int, edge_id.split(','))
	pickcount = int(losscount) + int(wincount)
	popularitygraph.add_edge(*hf.getHero(nodes), weight=pickcount)
	winrate = float(wincount)/pickcount
	winratetarget = max(herowincount[nodes[0]]/heropickcount[nodes[0]],
	                    herowincount[nodes[1]]/heropickcount[nodes[1]])
	winrategraph.add_edge(*hf.getHero(nodes), weight=(winrate - winratetarget))

d = json_graph.node_link_data(popularitygraph)
json.dump(d, open('popularitygraph.json','w'))
d = json_graph.node_link_data(winrategraph)
json.dump(d, open('winrategraph.json', 'w'))
