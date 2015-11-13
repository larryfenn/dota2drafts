import glob
import pandas as pd

path =r'.\collection'
allfiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allfiles:
	df = pd.read_csv(file_, index_col=0, header=None, names=['match_id', 'radiant_win', 'duration', '1is_pick', '1team_id', '1hero_id', '2is_pick', '2team_id', '2hero_id', '3is_pick', '3team_id', '3hero_id', '4is_pick', '4team_id', '4hero_id', '5is_pick', '5team_id', '5hero_id', '6is_pick', '6team_id', '6hero_id', '7is_pick', '7team_id', '7hero_id', '8is_pick', '8team_id', '8hero_id', '9is_pick', '9team_id', '9hero_id', '10is_pick', '10team_id', '10hero_id', '11is_pick', '11team_id', '11hero_id', '12is_pick', '12team_id', '12hero_id', '13is_pick', '13team_id', '13hero_id', '14is_pick', '14team_id', '14hero_id', '15is_pick', '15team_id', '15hero_id', '16is_pick', '16team_id', '16hero_id', '17is_pick', '17team_id', '17hero_id', '18is_pick', '18team_id', '18hero_id', '19is_pick', '19team_id', '19hero_id', '20is_pick', '20team_id', '20hero_id'])
	list_.append(df)
frame = pd.concat(list_).dropna() # some games have fewer than 10 bans; omit these
frame.to_csv("capmodedata.csv")
