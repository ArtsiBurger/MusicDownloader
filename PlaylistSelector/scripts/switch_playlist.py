def disable_playlist():
    folder = "LDN"
    open(f"/storage/emulated/0/Music/{folder}/.nomedia", "a").close()
    print(f"Folder {folder} is disabled.")

