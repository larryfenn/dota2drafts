Dota 2 Drafting
==========

Dota 2 drafting involves two team captains taking turns banning and picking heroes in sequence. The Dota 2 web API allows for access to the almost 2 billion Dota 2 games. The goal will be to have a model for suggesting picks and bans, trained on the existing Dota 2 game records.

httprequest.py
--------

httprequest.py is a python script that combs the Dota 2 web API for captain's mode games and stores the records in "\collection\data.csv" for later analysis. It requires two files, not included:

* key.dat - a file that has only the API key in it (http://steamcommunity.com/dev/apikey)
* record.dat - a file with only the "seq num" that the program will start collecting at. Consult the Dota 2 web API documentation for which seq num you wish to start at.

httprequest.py will start at the seq num in record.dat and grab matches until a fixed seq num, 1704492188. Edit httprequest.py for more matches as desired.

datap.py
---------

A simple pandas script that concatenates all the data csv files in "\collection" into a single output file "capmodedata.csv" for later analysis.