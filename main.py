import pandas
import search
import isodate
#"AIzaSyBZhiI5trjy4ZFysrYD54_E9sDMR3aKfpo"

listOfTracks = pandas.read_csv("cd-tracks-1000.csv", header=None)
creator = listOfTracks[1]
title = listOfTracks[2]
length = listOfTracks[3]

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
        print (lengths)
