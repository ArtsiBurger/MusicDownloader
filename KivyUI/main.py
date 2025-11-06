import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from PlaylistSelector.scripts.selector import select_playlist

class PlaylistScreen(BoxLayout):
    base_path = StringProperty(r"C:\Users\pc\Music") # For PC: r"C:\Users\pc\Music" | For mobile: "/storage/emulated/0/Music"
    playlists = ListProperty([])

    def __init__(self, **kwargs): # Auto load playlists on start
        super().__init__(**kwargs)
        self.load_playlists()

    def load_playlists(self):
        self.playlists.clear()
        try:
            for f in os.listdir(self.base_path): # Sort out only the folders in the base path
                if os.path.isdir(os.path.join(self.base_path, f)):
                    self.playlists.append(f)
        except Exception as e:
            print(f"Error loading playlists: {e}")

    def on_playlist_selection(self, new_playlist):
        select_playlist(new_playlist)

class MusicApp(App):
    def build(self):
        return PlaylistScreen()

if __name__ == "__main__":
    MusicApp().run()