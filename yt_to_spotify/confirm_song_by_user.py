from yt_playlist_fetch import get_item_name
from fetch_from_spotify import search_for_song,get_uris
from add_song_spotify import add_songs_to_playlist
import asyncio

youtube_songs = get_item_name()
list_of_songs = {}
list_of_uris = []
async def add_songs_to_dict():
    for indx,i in enumerate(youtube_songs):
        songs = await search_for_song(i)
        list_of_songs[i] = songs[0]
        songs = []
    return list_of_songs

def get_confirmation():
    print("\nDoes the song written next to your playlist song match them ?")
    a = input("If yes PRESS 'Y'   else PRESS 'N' : ")
    if a == "Y":
        print(list(list_of_songs.values()))
        add_songs_to_playlist(get_uris())
    elif a == 'N':
        print("SORRY , Looks like there isnt any perfect match for the song you are looking for")
        rm_s_n  = int(input("Enter the Number present left to the song to remove it from adding to spotify : "))
        list_of_songs.pop(list(list_of_songs)[rm_s_n])
        format_output()

def format_output():
    print("\t*** CONFIRMATION SECTION ***")
    for i,j in enumerate(list_of_songs):
        print(i,j,":",list_of_songs[j])
    get_confirmation()

async def main():
    await add_songs_to_dict()
    format_output()


asyncio.run(main())