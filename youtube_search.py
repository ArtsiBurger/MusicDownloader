from yt_dlp import YoutubeDL

# Searches for a single track and returns the URL
def search_track (track_name):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "best",
        "noplaylist": True,
        "skip_download": True
    }
    with YoutubeDL(ydl_opts) as ydl:
        
        fallback_limit = 5 # Change this for the amount of fallback searches if the first one was age-restricted
        try: 
            info = ydl.extract_info(f"ytsearch1:{track_name}", download=False)
        except Exception:
            info = None

        if info:
            entry = info["entries"][0]
            return entry["webpage_url"]

        try:
            info = ydl.extract_info(f"ytsearch{fallback_limit}:{track_name}", download=False)
        except Exception:
            info = None

        if info:
            entries = info.get("entries") or []

            for entry in entries:
                if entry:
                    return entry["webpage_url"]

        print(f"No non-age-restricted were found for {track_name}")
        return None
    
    
# Search for the whole playlist of tracks
def search_tracks(tracks):
    print("Searching...")
    urls = []
    j = 0
    text = ""
    for i, track in enumerate(tracks, 1):
        try:
            url = search_track(track)
            urls.append(url)
            if url is None:
                j += 1
                text = f"Did not find {j} URLs."
                if j == 1:
                    text = f"Did not find {j} URL."
            print(f"Progress {i}/{len(tracks)} | Found {i-j}/{len(tracks)} URLs. {text}")
        except Exception as e:
            print(f"Error searching '{track}': {e}")
            urls.append(None)
    print(f"Search completed.")
    return urls
        

