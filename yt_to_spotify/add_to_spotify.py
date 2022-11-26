import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from json import dumps
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="17a02e14ae594f5a97d77cabe7c2ee3a", client_secret="49dd7ce7271c4b9a9c833a00bbcef22c"))


response = sp.search(q="marethuhoyithe",market="IN",type="track")

response_js = dumps(response)
with open("sp_song.json","w") as file:
    file.write(str(response_js))