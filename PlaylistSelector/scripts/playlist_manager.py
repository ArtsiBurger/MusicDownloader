import os
import shutil

def change_playlist(new_playlist):

    base_path = "/storage/emulated/0/Music"
    playlists = []
    

    for f in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, f)):
            playlists.append(f)

    for p in playlists: 
        if not os.path.exists(os.path.join(base_path, p, ".nomedia")):
            old_playlist = p
            break
    if new_playlist == old_playlist:
        print(f"You are already on {new_playlist}.")
        return

    shutil.move(os.path.join(base_path, new_playlist, ".nomedia"), os.path.join(base_path, old_playlist, ".nomedia"))

    print(f"Now playing: {new_playlist}")
    
