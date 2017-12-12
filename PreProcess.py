import json
import ast
from pprint import pprint

possession = []
with open("./data/4860723440123904.json", encoding='utf-8') as input_file:
    data = json.loads(input_file.read())

#Number of Passes
numPasses = 0
numTouches = 0
distinctPlayers = []
for i in data['pointsJson'][0]['events']:
    if i['type'] == "Offense":
        numPasses += 1
        if i['passer'] not in distinctPlayers:
            distinctPlayers.append(i['passer'])
            numTouches += 1
#numPasses = data[0]['pointsJson'][0]['events']
pprint(numPasses)
pprint(numTouches)