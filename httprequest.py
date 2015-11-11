# python 3
import urllib.request
# python 2.7
#import urllib2
import json
#get last 100
lastid = open('record.dat', 'r').read()
apikey = open('key.dat', 'r').read()
data = urllib.request.urlopen("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?min_players=10&key=" + apikey + "&skill=3&start_at_match_id=" + lastid).read()
#todo: add in file i/o, track last match processed, to automatically sift through all of them
#ultimately want to set up a CRON job and store the things in a database (just a CSV?)
#implement a try catch in case of error 503
matches = json.loads(data)
for i in range(100):
	match_id = matches['result']['matches'][i]['match_id']
	match_data = json.loads(urllib2.urlopen("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id= " + str(match_id) + "&key=" + apikey).read())
	print(match_data['result']['game_mode'])
	if (match_data['result'].has_key('picks_bans')):
		print(match_data['result']['picks_bans'])
		#print(match_data['result']['duration'])
