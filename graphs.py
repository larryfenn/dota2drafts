import pandas as pd
import numpy as np
import matplotlib.pyplot as pp
import herofilter as hf

raw = pd.read_csv("capmodedata.csv", index_col=0)
picksbans = pd.read_csv("picksbans.csv", index_col=0)

#count = 10
#picklistindex = 10
#firstbanstop10 = raw.xs('1hero_id', axis=1).value_counts()[:10]
#pp.figure(figsize=(20,20))
#pp.bar(range(10), firstbanstop10)

#pp.xticks(np.arange(10) + .5, hf.getHero(list(firstbanstop10.index)))
#pp.savefig('top10firstban.png')

#firstbans = raw.xs('1hero_id', axis=1).value_counts()
#pp.bar(range(len(firstbans)), firstbans)
#pp.savefig('firstban.png')

# simple computation: grab N most popular heroes
N = 5 #top N most banned/picked heroes
totalprevalence = raw.icol(4).value_counts()
for i in range(19):
	totalprevalence += raw.icol(7 + 3*i).value_counts()
totalprevalence.sort(ascending=False)
Nmostpopular = list(totalprevalence[:N].index)
print(hf.getHero(Nmostpopular)) #just for kicks

selected = list()
for i in range(N):
	selected.append(Nmostpopular[i] - 1)
N = len(selected)
names = hf.getHero(selected, 1)
ind = np.arange(N)
width = 1

pick10 = picksbans.iloc[0][selected]
pick9 = picksbans.iloc[1][selected]
pick8 = picksbans.iloc[2][selected]
pick7 = picksbans.iloc[3][selected]
pick6 = picksbans.iloc[4][selected]
pick5 = picksbans.iloc[5][selected]
pick4 = picksbans.iloc[6][selected]
pick3 = picksbans.iloc[7][selected]
pick2 = picksbans.iloc[8][selected]
pick1 = picksbans.iloc[9][selected]
ban1 = -picksbans.iloc[10][selected]
ban2 = -picksbans.iloc[11][selected]
ban3 = -picksbans.iloc[12][selected]
ban4 = -picksbans.iloc[13][selected]
ban5 = -picksbans.iloc[14][selected]
ban6 = -picksbans.iloc[15][selected]
ban7 = -picksbans.iloc[16][selected]
ban8 = -picksbans.iloc[17][selected]
ban9 = -picksbans.iloc[18][selected]
ban10 = -picksbans.iloc[19][selected]


p6 = pp.bar(ind, pick6, width, color='#aa9900', bottom=pick5+pick4+pick3+pick2+pick1)
p5 = pp.bar(ind, pick5, width, color='#aaaa00', bottom=pick4+pick3+pick2+pick1)
p4 = pp.bar(ind, pick4, width, color='#ccaa00', bottom=pick3+pick2+pick1)
p3 = pp.bar(ind, pick3, width, color='#ddaa00', bottom=pick2 + pick1)
p2 = pp.bar(ind, pick2, width, color='#dd0000', bottom=pick1)
p1 = pp.bar(ind, pick1, width, color='#ff0000')
b1 = pp.bar(ind, ban1, width, color='#0000ff')
b2 = pp.bar(ind, ban2, width, color='#0000dd', bottom=ban1)
b3 = pp.bar(ind, ban3, width, color='#00aadd', bottom=ban1 + ban2)
b4 = pp.bar(ind, ban4, width, color='#00aacc', bottom = ban1 + ban2 + ban3)
b5 = pp.bar(ind, ban5, width, color='#00aaaa', bottom=ban1+ban2+ban3+ban4)
b6 = pp.bar(ind, ban6, width, color='#0099aa', bottom=ban1+ban2+ban3+ban4+ban5)

#pp.ylabel('Scores')
#pp.title('Scores by group and gender')
pp.xticks(ind+width/2., names)
pp.yticks(np.arange(0, 100000, 100000))
#pp.legend((p1[0], p2[0]), ('men', 'women'))

pp.show()
