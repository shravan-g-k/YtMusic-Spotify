from yt_playlist_fetch import get_item_name
from fetch_from_spotify import search_for_song
import asyncio
youtube_songs = get_item_name()

async def display_songs():
    for indx,i in enumerate(youtube_songs):
        songs = await search_for_song(i)
        print(indx,songs)
        songs = []


asyncio.run(display_songs())