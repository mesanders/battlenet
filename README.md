#BATTLENET API

Battlnet offers a rest API that returns JSON content located at *https://us.api.battle.net*. There are already APIs for this in python or nodejs; however that would be no fun :)

There are some interesting things that you can do with the data, but it isn't intuitive for mining large amounts of data, but seem to be targeting primarily web app type of interactivity. 

##Limitations
Key Rate Limit:

*100* Calls Per Second
*36,000* Calls per hour

Although these are limitations, they are more than enough for the type of snapshot data that will be collected. 

##WOW APIs worth noting
"Worth Noting" means that are useful for data mining. The problem is that you can't just get a list of all the characters etc available on a server. You can however get a bigger list of character names through the PVP Leader board sand then go from there. Then you can get Statistics on any given player. Some of the other APIs mentioned would be good to understand the ids associated with the json returns. Example looking up Talents by talent id. Some of these calls can be used one time and then saved into a table for quick lookups. Or they can be denormalized and referenced. It might be worth hitting a majority of the APIs just to build a data model. That is only if time is available :)

1. PVP Leaderboard: /WOW/LEADERBOARD/:BRACK
	Bracket can be 2v2, 3v3, 5v5 or rbg
2. STATISTICS /WOW/CHARACTER/:REALM/:CHARACTERNAME
3. STATS /WOW/CHARACTER/:REALM/:CHARACTERNAME
4. MEMBERS /WOW/GUILD/:GUILDNAME
5. TALENTS /WOW/DATA/TALENTS

##Starcraft II APIs worth noting.
Just off the top of my head one of the things, that can be useful is to look at the ladders and then the matches. Pull some data from the top players and cross reference match history. Maybe we can see some patterns on people who have had a battle against opponents whom their opponents have played. Need to find a seed list of players though. 

1. Match History /SC2/PROFILE/:ID/:REGION/:NAME/MATCHES
2. LADDERS /SC2/PROFILE/:ID/REGION/:NAME/LADDERS
3. /SC2/PROFILE/:ID/:REGION/:NAME
