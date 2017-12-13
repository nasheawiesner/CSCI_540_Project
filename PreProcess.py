import json
import re

def vectorize_day(day):
    if day == "Sun":
        day = 0
    elif day == "Mon":
        day = 1
    elif day == "Tue":
        day = 2
    elif day == "Wed":
        day = 3
    elif day == "Thurs":
        day = 4
    elif day == "Fri":
        day = 5
    elif day == "Sat":
        day = 6
    return day

def parse():
    with open("test.json", encoding='utf-8') as input_file:
        data = json.loads(input_file.read())

    possessions = []
    for i in data:  #iterate through games
        for j in i['pointsJson']: #iterate through events
            first = True
            possession = []
            poss_count = 0
            numPasses = 0
            numTouches = 0
            distinctPlayers = []
            totalTime = 0
            ours = 0
            theirs = 0
            totalPoints = 0
            wind = 0
            time = 0
            date = 0
            day = ""
            lineType = 0
            pull_start = 0
            for k in j['events']:  #iterate through actions
                index = j['events'].index(k)
                if k['type'] == "Offense":
                    numPasses += 1
                    if k['passer'] not in distinctPlayers and k['passer'] != "Anonymous":
                        distinctPlayers.append(k['passer'])
                        numTouches += 1
                    if k['receiver'] not in distinctPlayers and k['receiver'] != "Anonymous":
                        distinctPlayers.append(k['receiver'])
                        numTouches += 1
                    if j['events'][(index + 1) % len(j['events'])]['type'] != "Offense" or index == (len(j['events']) - 1):  #if the ball gets transferred to other team
                        possession = []
                        poss_count += 1
                        ours = int(j['summary']['score']['ours'])
                        theirs = int(j['summary']['score']['theirs'])
                        totalPoints = ours + theirs
                        wind = int(i['wind']['mph'])
                        time = i['time']
                        time = int(time.replace(":", ""))
                        date = i["date"]
                        day = date.split(",")
                        day = vectorize_day(day[0])
                        date = re.findall('\d+', date)
                        date = int(date[0] + date[1])
                        if i["pointsJson"][-1]['summary']['lineType'] == "O":
                            lineType = 1
                            if first == True:
                                pull_start = 1
                        else:
                            lineType = 0
                            pull_start = 0
                        possession.extend([numPasses,numTouches,ours,theirs,totalPoints, wind, time, date, day, lineType, pull_start, poss_count])
                        print(possession)
                        possessions.append(possession)
                elif k['type'] == "Defense":
                    possession = []
                    numPasses = 0
                    numTouches = 0
                    distinctPlayers = []
                    totalTime = 0
                    ours = 0
                    theirs = 0
                    totalPoints = 0
                    wind = 0
                    time = 0
                    date = 0
                    day = ""
                    lineType = 0
                    pull_start = 0
                first = False
    return possessions




