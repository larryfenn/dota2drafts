import pandas as pd
f = open('output.txt', 'r')
index = list()
for i in range(10, 0, -1):
	index.append(str(i) + "pick")
for i in range(1, 11):
	index.append(str(i) + "ban")
column = range(1, 114)
picksbans = pd.DataFrame(0, index, column)
for line in f:
	idtag, count = line.split('\n')[0].split('\t')
	hero_id, pickflag, order = idtag.split(':')
	if (pickflag == "1"):
		picksbans.ix[str(int(order) + 1) + "pick", int(hero_id)] = int(count)
	else:
		picksbans.ix[str(int(order) + 1) + "ban", int(hero_id)] = int(count)
