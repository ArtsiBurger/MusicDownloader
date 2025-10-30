from yt_dlp import YoutubeDL

def download_mp3(youtube_url, output_dir):

    ydl_opts = {
        "format": "bestaudio/best",
        "no_warnings": True,
        "quiet": True,
        "noplaylist": True,
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
        
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except Exception as e:
        print(f"Failed to download {youtube_url}: {e}")

def download_mp3_list(url_list, output_dir):
    print("Downloading...")
    j = 0
    text = ""
    for i, url in enumerate(url_list, 1):
        if url is None:
            j += 1
            text = f"Skipped {j} songs."
            if j == 1:
                text = f"Skipped {j} song."
        else:
            download_mp3(url, output_dir)

        print(f"Progress {i}/{len(url_list)} | Downloaded {i-j}/{len(url_list)} songs. {text}")

    print(f"Download completed. The songs can be found in {output_dir}.")
