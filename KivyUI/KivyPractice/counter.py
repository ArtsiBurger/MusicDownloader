from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class CounterButton(BoxLayout):
   color = ListProperty([1, 1, 1, 1])

class CounterApp(App):
    def build(self):
        return CounterButton()
    
if __name__ == "__main__":
    CounterApp().run()

    