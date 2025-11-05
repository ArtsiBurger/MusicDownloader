from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class ColorButton(BoxLayout):
    color = ListProperty([1, 0, 0, 1])

    def change_color(self):
        if self.color == [1, 0, 0, 1]:
            self.color = [0, 0, 1, 1]
        else:
            self.color = [1, 0, 0, 1]   

class ColorApp(App):
    def build(self):
        return ColorButton()
    
if __name__ == "__main__":
    ColorApp().run()