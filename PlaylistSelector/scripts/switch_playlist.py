def disable_playlist():
    folder = "test"
    open(f"/storage/emulated/0/Music/{folder}/.nomedia", "a").close()
    print(f"Folder {folder} is disabled.")
    
