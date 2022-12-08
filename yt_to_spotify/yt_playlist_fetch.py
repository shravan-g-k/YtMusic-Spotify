# -*- coding: utf-8 
# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

from json import dumps
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from consts import SCOPES,API_SERVICE_NAME
from privates import CLIENT_SECRET_FILE

def _get_playlist():
    playlist_id = input("Enter the playlist Id : ")
    """returns the json response from youtube API
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    
    api_version = "v3"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=500,
        playlistId=playlist_id
           )
    response = request.execute()
    return response
    # json_response = dumps(response)
    # with open("playlist.json" , "w") as file:
    #     file.write(json_response)
playlist_items = []

def get_item_name():
    """returns list os songs present in your youtube playlist
    """
    response = _get_playlist()
    for i in response["items"]:
        playlist_items.append(i["snippet"]["title"])
    return playlist_items
    
    
# print(get_item_name())