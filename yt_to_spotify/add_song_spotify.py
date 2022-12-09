from spotipy import util
from privates import CLIENT_ID,CLIENT_SECRET,USER_ID #refer to the readmd of this repo in github
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:9005/",#You also have to add this redirect url in your Spotify web api
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        cache_path="token.txt"
    )
)


def create_playlist() -> str:
    """Creating playlist with the preferred name given by the user"""
    name = input("what would you like to name the playlist : ")
    playlist = sp.user_playlist_create(user=USER_ID,name=name,public=False,collaborative=False,description="test")
    return playlist["id"]

def add_songs_to_playlist(songs:list):
    """Adding the songs to spotify"""
    playlist_id = create_playlist()
    sp.playlist_add_items(playlist_id=playlist_id,items=songs)

