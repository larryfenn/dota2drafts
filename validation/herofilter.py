import json
herojson = open('herolookup.json','r').read()
herojson = json.loads(herojson)['result']['heroes']
herolist = [""] * 113
for hero in herojson:
	herolist[hero['id']] = hero['localized_name']
def getHero(indices, offset=0):
	heronames = list()
	for i in indices:
		heronames.append(herolist[i+offset])
	return heronames
