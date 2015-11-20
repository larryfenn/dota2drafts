import pandas as pd
import numpy as np
import matplotlib.pyplot as pp
import herofilter as hf

raw = pd.read_csv("capmodedata.csv", index_col=0)
picksbans = pd.read_csv("picksbans.csv", index_col=0)

# simple computation: grab N most popular heroes
N = 5 #top N most banned/picked heroes
totalprevalence = raw.icol(4).value_counts()
for i in range(19):
	totalprevalence += raw.icol(7 + 3*i).value_counts()
totalprevalence.sort(ascending=False)
Nmostpopular = list(totalprevalence[:N].index)
print(hf.getHero(Nmostpopular)) #just for kicks


# graphing code
selected = list()
for i in range(N):
	selected.append(Nmostpopular[i] - 1)
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

pp.figure()
# plot picks
#elegant way...
#for i in range(10):
#	pp.bar(ind, picksbans.iloc[9-i][selected], width, color=(1,i*.1,i*.1), bottom=sum(#thing goes here)
#	pp.bar(ind, picksbans.iloc[10+i][selected], width, color=(i*.1,i*.1,1), bottom=sum(#thing goes here)

p10 = pp.bar(ind, pick10, width, color='#ffcccc', bottom=pick9+pick8+pick7+pick6+pick5+pick4+pick3+pick)
p9 = pp.bar(ind, pick9, width, color='#ffb3b3', bottom=pick8+pick7+pick6+pick5+pick4+pick3+pick2+pick1)
p8 = pp.bar(ind, pick8, width, color='#ff9999', bottom=pick7+pick6+pick5+pick4+pick3+pick2+pick1)
p7 = pp.bar(ind, pick7, width, color='#ff8080', bottom=pick6+pick5+pick4+pick3+pick2+pick1)
p6 = pp.bar(ind, pick6, width, color='#ff6666', bottom=pick5+pick4+pick3+pick2+pick1)
p5 = pp.bar(ind, pick5, width, color='#ff4d4d', bottom=pick4+pick3+pick2+pick1)
p4 = pp.bar(ind, pick4, width, color='#ff3333', bottom=pick3+pick2+pick1)
p3 = pp.bar(ind, pick3, width, color='#ff1a1a', bottom=pick2 + pick1)
p2 = pp.bar(ind, pick2, width, color='#ff0000', bottom=pick1)
p1 = pp.bar(ind, pick1, width, color='#e60000')
b1 = pp.bar(ind, ban1, width, color='#0000e6')
b2 = pp.bar(ind, ban2, width, color='#0000ff', bottom=ban1)
b3 = pp.bar(ind, ban3, width, color='#1a1aff', bottom=ban1+ban2)
b4 = pp.bar(ind, ban4, width, color='#3333ff', bottom=ban1+ban2+ban3)
b5 = pp.bar(ind, ban5, width, color='#4d4dff', bottom=ban1+ban2+ban3+ban4)
b6 = pp.bar(ind, ban6, width, color='#6666ff', bottom=ban1+ban2+ban3+ban4+ban5)
b7 = pp.bar(ind, ban7, width, color='#8080ff', bottom=ban1+ban2+ban3+ban4+ban5+ban6)
b8 = pp.bar(ind, ban8, width, color='#9999ff', bottom=ban1+ban2+ban3+ban4+ban5+ban6+ban7)
b9 = pp.bar(ind, ban9, width, color='#b3b3ff', bottom=ban1+ban2+ban3+ban4+ban5+ban6+ban7+ban8)
b10 = pp.bar(ind, ban10, width, color='ccccff', bottom=ban1+ban2+ban3+ban4+ban5+ban6+ban7+ban8+ban9)

pp.ylabel('Ban/pick frequency')
pp.title('Top banned/picked heroes')
pp.xticks(ind+width/2., names)
pp.yticks(np.arange(0, 100000, 100000))
#pp.legend()

pp.show()
