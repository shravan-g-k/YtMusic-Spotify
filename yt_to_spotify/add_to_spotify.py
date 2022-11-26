import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from json import dumps,loads


with open("sp_song.json","w") as file:
    file.write("")


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="17a02e14ae594f5a97d77cabe7c2ee3a", client_secret="49dd7ce7271c4b9a9c833a00bbcef22c"))


response  = sp.search(q="ninadene Januma",market="IN",type="track")

response_js = dumps(response)
response_dict = response_js
with open("sp_song.json","w") as file:
    file.write(str(response_js))

with open("sp_song.json","r") as file:
    read_js = file.read()
    read = loads(read_js)

for indx,i in enumerate(read["tracks"]["items"]):
    print("*",indx+1,i["name"])
