from confirm_song_by_user import add_songs_to_dict,format_output
import asyncio

async def initialize():
    '''Intializing program by fetching the users playlist'''
    await add_songs_to_dict()
    format_output()

def fetch_and_add():
    asyncio.run(initialize())