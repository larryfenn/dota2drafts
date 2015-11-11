# python 3
import urllib.request
# python 2.7
#import urllib2
import json
import time
recordfile = open('record.dat', 'r')
lastid = recordfile.read()
recordfile.close()

apikey = open('key.dat', 'r').read()

while (True):
	matches = open('data.csv', 'a')
	data = json.loads(urllib.request.urlopen("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?min_players=10&key=" + apikey + "&skill=3&start_at_match_id=" + lastid).read().decode("utf-8"))
	#implement a try catch in case of error 503
	for i in range(100):
		match_id = data['result']['matches'][i]['match_id']
		print(match_id)
		match_data = json.loads(urllib.request.urlopen("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=" + apikey + "&match_id=" + str(match_id)).read().decode("utf-8"))
		if 'picks_bans' in match_data['result']:
			matches.write(str(match_id) + ",")
			matches.write(str(match_data['result']['radiant_win']) + ",")
			matches.write(str(match_data['result']['duration']))
			picklist = match_data['result']['picks_bans']
			for i in range(len(picklist)):
				matches.write("," + str(picklist[i]['order']) + "," + str(picklist[i]['is_pick']) + "," + str(picklist[i]['hero_id']) + "," + str(picklist[i]['team']))
			matches.write("\n")
	matches.close()
	lastid = match_id
	recordfile = open('record.dat', 'w')
	recordfile.write(str(lastid))
	recordfile.close()
	print("CYCLE FINISHED")
	time.sleep(5)
