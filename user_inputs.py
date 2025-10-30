import os
import shutil

def get_user_inputs():
    spotify_url = input("Give an URL for your Spotify playlist: ")
    if not spotify_url:
        spotify_url ="https://open.spotify.com/playlist/66Z07tOKFQrzTnhtTtEPsL?si=1cd350c11e3a4ba6&pt=2982a41f8fb67b1b33e6537d558170af" # Dummy playlist for testing
    
    base_path = r"C:\Users\pc\Music" # For PC: r"C:\Users\pc\Music" | For mobile: "/storage/emulated/0/Music"
    user_folder = input("Give folder name inside Music-folder where the MP3s will be saved to: ")
    if not user_folder:
        user_folder = "ConvertedMP3s"

    output_dir = os.path.join(base_path,user_folder)

    if os.path.exists(output_dir):
        confirm = input(f"{output_dir} already exists. Do you want to clear it? (y/n): ").lower()
        if confirm == "y":
            shutil.rmtree(output_dir)
            os.makedirs(output_dir)
    else:
        os.makedirs(output_dir)

    return spotify_url, output_dir