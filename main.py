from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Home(Screen):

    def count(self):
        self.ids.label.text = str(int(self.ids.label.text) + 1)

class MyApp(App):

    def build(self):
        return Home()



MyApp().run()
