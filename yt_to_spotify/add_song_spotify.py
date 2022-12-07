from spotipy import util
from consts import CLIENT_ID,CLIENT_SECRET
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:9005/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        cache_path="token.txt"
    )
)

sp.user_playlist_create(user="8kma5a2y9xte2uojzhz7qhtqy",name="hello world",public=False)
