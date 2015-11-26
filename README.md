Dota 2 Drafting
==========

Dota 2 drafting involves two team captains taking turns banning and picking heroes in sequence. The Dota 2 web API allows for access to the almost 2 billion Dota 2 games. The goal will be to have a model for suggesting picks and bans, trained on the existing Dota 2 game records.

Use: `httprequest.py` grabs data from Valve servers and writes it as a csv. Send the csv through MapReduce with the mapper and reducer py files, and parse the output. The result can then be graphed.


datap.py
---------

A simple pandas script that concatenates all the data csv files in "\collection" into a single output file "capmodedata.csv" for later analysis.

graphs.py
--------

A pandas script currently used to graph the most popular picked/banned heroes. Uses the output from `mapreduceoutputparse.py`, which itself depends on successful execution of MapReduce on the data set.

herofilter.py
--------

A simple lookup for hero names based on id values.

herolookup.json
--------

JSON object containing hero id names and localization tags.

httprequest.py
--------

httprequest.py is a python script that combs the Dota 2 web API for captain's mode games and stores the records in "\collection\data.csv" for later analysis. It requires two files, not included:

* key.dat - a file that has only the API key in it (http://steamcommunity.com/dev/apikey)
* record.dat - a file with only the "seq num" that the program will start collecting at. Consult the Dota 2 web API documentation for which seq num you wish to start at.

httprequest.py will start at the seq num in record.dat and grab matches until a fixed seq num, 1704492188. Edit httprequest.py for more matches as desired.

mapper.py, reducer.py
--------

Components of a MapReduce framework.

mapreduceoutputparse.py
--------

Loads the MapReduce output into a pandas dataframe for further processing.