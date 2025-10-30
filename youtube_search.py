from yt_dlp import YoutubeDL

# Searches for a single track and returns the URL
def search_track (track_name):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "best",
        "noplaylist": True,
        "skip_download": True,
        "extract_flat": True
    }
    with YoutubeDL(ydl_opts) as ydl:
        
        search_limit = 5 # Change this for the amount of search results

        try: 
            info = ydl.extract_info(f"ytsearch{search_limit}:{track_name}", download=False)
        except Exception:
            print(f"Search failed for {track_name}.")
            return None

        entries = info.get("entries") or []
        
        if not entries:
            print(f"No search hits for {track_name}.")
            return None


        for entry in entries:
            if not entry:
                continue

            candidate_id = entry.get("id") or entry.get("url")
            if not candidate_id:
                continue
            if ":" in candidate_id:
                candidate_id = candidate_id.split(":")[-1]
            candidate_url = f"https://www.youtube.com/watch?v={candidate_id}"

            try:
                candidate_info = ydl.extract_info(candidate_url, download=False)
            except Exception:
                print("The video was unusable. Searching for an other version.")
                continue

            return candidate_info.get("webpage_url") or candidate_url

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
        

