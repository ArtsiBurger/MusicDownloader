from spotify_fetch import fetch_tracks
from youtube_search import search_tracks
from mp3_download import download_mp3_list
from user_inputs import get_user_inputs
import time

start = time.time()

playlist_url, output_dir = get_user_inputs()
spotify_tracks = fetch_tracks(playlist_url)
youtube_urls = search_tracks(spotify_tracks)
download_mp3_list(youtube_urls, output_dir)

end = time.time()

print(f"Execution time: {(end-start)/60:.0f} minutes and {(end-start)%60:.0f} seconds.")


