#Module for searching videos from the youtube api
import pandas
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

#
DEVELOPER_KEY = "AIzaSyBZhiI5trjy4ZFysrYD54_E9sDMR3aKfpo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def searchVideos(query="fate grand order"):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    response = youtube.search().list(
        q = query,
        part = "id",
        maxResults = 3,
        type = ["video"]
    ).execute()

    listOfIds = []
    for video in response["items"]:
        listOfIds.append(video["id"]["videoId"])

    return listOfIds

def getLengthOfVideo(video=searchVideos()[0]):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    response = youtube.videos().list(
        part = "id,contentDetails",
        id = video
    ).execute()
    return response["items"][0]["contentDetails"]["duration"]

print(getLengthOfVideo())
