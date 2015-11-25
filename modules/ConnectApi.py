#!/usr/bin/env python
import sys
sys.path.insert(0, '../')
from urllib.request import urlopen 
import json
from resources.props import *

print(apikey)
leaderboard="https://us.api.battle.net/wow/leaderboard/2v2?locale=en_US&apikey=" + apikey

print(leaderboard)
req = urlopen(leaderboard)
opened = req.read()
print(opened)

