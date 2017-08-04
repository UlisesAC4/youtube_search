import pandas
import search
import isodate
#"AIzaSyBZhiI5trjy4ZFysrYD54_E9sDMR3aKfpo"

listOfTracks = pandas.read_csv("cd-tracks-1000.csv", header=None)
creator = listOfTracks[1]
title = listOfTracks[2]
length = listOfTracks[3]
idOfVideo = listOfTracks[4]

for index in range(1000):
    query =  "{} {}".format(creator[index], title[index])
    print(query)
    possibleResults = search.searchVideos(query)
    lengths = [0, 0, 0]

    if len(possibleResults) != 0:
        lengths[0] = search.getLengthOfVideo(possibleResults[0])
        lengths[1] = search.getLengthOfVideo(possibleResults[1])
        lengths[2] = search.getLengthOfVideo(possibleResults[2])
        lengths = [isodate.parse_duration(x).total_seconds() for x in lengths]
        r = range(int(length[index]) - 10, int(length[index] + 11))
        print(r)
        isInRange = []
        for x in range(3):
            if lengths[x] in r:
                isInRange.append({x: lengths[x], "inRange": True})
            else:
                isInRange.append({x: lengths[x], "inRange": False})
        isInRange = [x for x in isInRange if x["inRange"] == True]
        print(isInRange)
        if len(isInRange) == 1:
            key = list(isInRange[0])
            print(key[0])
            listOfTracks.set_value(4, index, possibleResults[key[0]])
        elif len(isInRange) > 1:
            for x in isInRange:
                x.pop("inRange", None)
            newList = []
            for x in isInRange:
                newList.append(min(x.items()))
            lesserTuple = min(newList, key=lambda x: x[1])
            print(lesserTuple[0])
            listOfTracks.set_value(4, index, possibleResults[lesserTuple[0]])
listOfTracks.to_csv("final.csv")
