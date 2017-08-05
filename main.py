import pandas
import search
import isodate
#"AIzaSyBZhiI5trjy4ZFysrYD54_E9sDMR3aKfpo"

listOfTracks = pandas.read_csv("cd-tracks-1000.csv", header=None, encoding = 'utf8')
creator = listOfTracks[1]
title = listOfTracks[2]
length = listOfTracks[3]
idOfVideo = listOfTracks[4]
listOfTracks[4] = listOfTracks[4].astype(str)
listOfTracks[5] = listOfTracks[5].astype(str)

for index in range(1000):
    query =  "{} {}".format(creator[index], title[index])
    print(query)
    possibleResults = search.searchVideos(query)
    lengths = []
    if len(possibleResults) > 0:
        for x in possibleResults:
            lengths.append(search.getLengthOfVideo(x))
        lengths = [isodate.parse_duration(x).total_seconds() for x in lengths]
        r = range(int(length[index]) - 10, int(length[index] + 11))
        print(r)
        isInRange = []
        for x in range(len(possibleResults)):
            if lengths[x] in r:
                isInRange.append({x: lengths[x], "inRange": True})
            else:
                isInRange.append({x: lengths[x], "inRange": False})
        isInRange = [x for x in isInRange if x["inRange"] == True]
        print(isInRange)
        if len(isInRange) == 1:
            key = list(isInRange[0])
            print(key[0])
            print(possibleResults[key[0]])
            listOfTracks.set_value(index, 4, "https://www.youtube.com/watch?v=" + possibleResults[key[0]])
        elif len(isInRange) > 1:
            for x in isInRange:
                x.pop("inRange", None)
            newList = []
            for x in isInRange:
                newList.append(min(x.items()))
            #min(myList, key=lambda x:abs(x-myNumber))
            lesserTuple = min(newList, key=lambda x: abs(x[1]-length[index]))
            print(lesserTuple[0])
            print(possibleResults[lesserTuple[0]])
            listOfTracks.set_value(index, 4, "https://www.youtube.com/watch?v=" + possibleResults[lesserTuple[0]])
        listOfTracks.set_value(index, 5, "")
        print(listOfTracks)
    else:
        listOfTracks.set_value(index, 4, "")
        listOfTracks.set_value(index, 5, "")
        print(listOfTracks)
listOfTracks.to_csv("final.csv")
