import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def fetch_tracks(playlist_url):
    
    print("Fetching...")

    load_dotenv()
    c_id = os.getenv("SPOTIFY_CLIENT_ID")
    s_id = os.getenv("SPOTIFY_CLIENT_SECRET")

    credentials = SpotifyClientCredentials(client_id=c_id, client_secret=s_id)
    sp = spotipy.Spotify(auth_manager=credentials)

    tracks = []
    results = sp.playlist_items(playlist_url)

    while results:
        for item in results["items"]:
            track = item["track"]
            tracks.append(f"{track['name']} - {track['artists'][0]['name']}")
            
        if results['next']:
                results = sp.next(results)
        else:
            break
    print(f"Fetch completed. Fetched {len(tracks)} tracks.")
    return tracks
