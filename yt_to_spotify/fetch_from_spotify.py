import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from json import dumps, loads

CLIENT_ID = "17a02e14ae594f5a97d77cabe7c2ee3a"
CLIENT_SECRET = "49dd7ce7271c4b9a9c833a00bbcef22c"



# EMPTYING the json file every time the program is run
with open("sp_song.json", "w") as file:
    file.write("")

# INITIALIZING the spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


async def search_for_song(song: str) -> list[str]:
    song_match = []
    # SEARCH for the song in spotofy
    response = sp.search(
        q=song, market="IN", type="track",limit=5)

    # CONVERTING response to json so that it can be written into the json file
    response_js = dumps(response)

    # WRITING the response into json so that it can be retrived aferward
    with open("sp_song.json", "w") as file:
        file.write(str(response_js))

    # READING the json that we have just written
    with open("sp_song.json", "r") as file:
      read_js = file.read()
      read = loads(read_js)

    # PRINTING the names of the song
    for  i in read["tracks"]["items"]:
        # print("*", indx+1, i["name"])
        song_match.append(i["name"])

    return song_match
    song_match = []

    





# if __name__ == "__main__":
    # search_for_song("shoorveer")
    # print(song_match)