import pandas as pd
import numpy as np
import matplotlib.pyplot as pp
from matplotlib import colors
import herofilter as hf
import mapreduceoutputparse as mp

# simple computation: grab N most popular heroes
N = 5
totals = mp.picksbans.sum(axis=0)
totals.sort(ascending=False)
Nmostpopular = list(totals[:N].index)

# graphing code
selected = list()
for i in range(N):
	selected.append(Nmostpopular[i])
names = hf.getHero(selected)
ind = np.arange(N)
width = 1

pp.figure()

for i in range(10):
	pp.bar(ind, mp.picksbans.iloc[9-i][selected], width, color=(1,i*.1,i*.1), bottom=mp.picksbans.iloc[10-i:10].sum(axis=0)[selected])
	pp.bar(ind, -mp.picksbans.iloc[10+i][selected], width, color=(i*.1,i*.1,1), bottom=-mp.picksbans.iloc[10:10+i].sum(axis=0)[selected])

pp.ylabel('Ban & pick frequency')
pp.title('Top ' + str(N) + ' banned/picked heroes')
pp.xticks(ind+width/2., names)
pp.yticks(np.arange(-40000, 40000, 10000))

pp.show()
