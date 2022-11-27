# -*- coding: utf-8 
# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from json import dumps
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def _get_playlist():
    """returns the json response from youtube API
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_584712830766-gna15omj36n9ofm2bu9m9qh24gbm7qun.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=500,
        playlistId="PLkOtn-AIw1wJpmuEcckRb9n4y1TlmdPbu"
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