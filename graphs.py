import pandas as pd
import numpy as np
import matplotlib.pyplot as pp
import herofilter as hf

raw = pd.read_csv("capmodedata.csv", index_col=0)

count = 10
picklistindex = 10
#firstbanstop10 = raw.icol(1 + 3*picklistindex).value_counts()[:10]
firstbanstop10 = raw.xs('1hero_id', axis=1).value_counts()[:10]
pp.figure(figsize=(20,20))
pp.bar(range(10), firstbanstop10)

pp.xticks(np.arange(10) + .5, hf.getHero(list(firstbanstop10.index)))
pp.savefig('top10firstban.png')

#firstbans = raw.icol(1 + 3*picklistindex).value_counts()
firstbans = raw.xs('1hero_id', axis=1).value_counts()
pp.bar(range(len(firstbans)), firstbans)
pp.savefig('firstban.png')

# simple computation: grab N most popular heroes
N = 5 #top N most banned/picked heroes
totalprevalence = raw.icol(4).value_counts()
for i in range(19):
	totalprevalence += raw.icol(7 + 3*i).value_counts()
totalprevalence.sort(ascending=False)
Nmostpopular = list(totalprevalence[:N].index)
print(hf.getHero(Nmostpopular)) #just for kicks





heroactivity = pd.DataFrame(index=('pick10', 'pick9', 'pick8', 'pick7', 'pick6', 'pick5', 'pick4', 'pick3', 'pick2', 'pick1', 'ban1', 'ban2', 'ban3', 'ban4', 'ban5', 'ban6', 'ban7', 'ban8', 'ban9', 'ban10'), columns=range(113))



def getPicks(phase, isPick):
	return raw.loc[raw[str(phase) + 'is_pick'] == isPick].xs(str(phase) + 'hero_id', axis=1).value_counts()
