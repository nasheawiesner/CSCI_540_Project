import requests

# read in team ids
with open('audl_team_ids.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

# get game data for all of the ids and save it to a file
file = open('game_data.json','w') 
for id in content:
    url = 'http://www.ultianalytics.com/rest/view/team/' + id + '/gamesdata'
    r = requests.get(url)
    file.write(r.content)
file.close() 
