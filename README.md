
# YtMusic To Spotify

This a python based program which adds the songs from your youtube music to spotify.  
This program run on command line or terminal . Only CUI version is released yet GUI might be released in the near future.  

## Install dependencies  

Get the async IO module to run async funtion
```bash
  pip install asyncio
```

Google Api Client to communicate with youtube Api  
Google AuthLib for authentication
```bash
  pip install --upgrade google-api-python-client
  pip install --upgrade google-auth-oauthlib google-auth-httplib2
```
[Spotipy](https://spotipy.readthedocs.io/) to communicate with Spotify
```bash
  pip install spotipy
```


## Acknowledgements

 - [Youtube Data API](https://developers.google.com/youtube/v3) 
 -  [Spotipy](https://spotipy.readthedocs.io/)
 
## Prerequisites

Have a look into the YouTube data API.  
Get your client json secret file from Google Developers.  
Also you have to get the CLIENT_ID, CLIENT_SECRET, USER_ID from Spotify Web API
