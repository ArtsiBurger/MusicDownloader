from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class InputScreen(BoxLayout):
    def show_text(self):
        user_input = self.ids.user_input.text
        print(f"You typed: {user_input}")
        self.ids.output_label.text = f"You typed: {user_input}"

class InputApp(App):
    def build(self):
        return InputScreen()
    
if __name__ == '__main__':
    InputApp().run()