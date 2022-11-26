import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from json import dumps,loads

# emptying the json file every time the program is run
with open("sp_song.json","w") as file:
    file.write("")

# initialze the spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="17a02e14ae594f5a97d77cabe7c2ee3a", client_secret="49dd7ce7271c4b9a9c833a00bbcef22c"))

#search for the song in spotofy
response  = sp.search(q="ninadene Januma",market="IN",type="track")

#converting *response to json so that it can be written into the json file
response_js = dumps(response)

# writing the response into json so that it can be retrived aferward
with open("sp_song.json","w") as file:
    file.write(str(response_js))

#reading the json that we have just written
with open("sp_song.json","r") as file:
    read_js = file.read()
    read = loads(read_js)

#printing the names of the song
for indx,i in enumerate(read["tracks"]["items"]):
    print("*",indx+1,i["name"])
