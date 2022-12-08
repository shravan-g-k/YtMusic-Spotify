import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from json import dumps, loads
from privates import CLIENT_ID,CLIENT_SECRET




# EMPTYING the json file every time the program is run
with open("sp_song.json", "w") as file:
    file.write("")

# INITIALIZING the spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

list_of_uri = []


async def search_for_song(song: str) -> list[str]:
    song_match = []
    
    # SEARCH for the song in spotofy
    response = sp.search(
        q=song, market="IN", type="track",limit=1)

    # CONVERTING response to json so that it can be written into the json file
    response_js = dumps(response)

    # WRITING the response into json so that it can be retrived aferward
    with open("sp_song.json", "w") as file:
        file.write(str(response_js))

    # READING the json that we have just written
    with open("sp_song.json", "r") as file:
      read_js = file.read()
    #READING the response json we have recieved
    read = loads(str(response_js))

    # PRINTING the names of the song
    for  i in read["tracks"]["items"]:
        song_match.append(i["name"])
    list_of_uri.append(read["tracks"]["items"][0]["uri"])
    # print(list_of_uri)
    return song_match


    #WRITING the song in a json so that we can use it all across the project

def get_uris():
    """Return List of the spotify song URI's"""
    return list_of_uri