from kivymd.app import MDApp
from kivymd.uix.screen import Screen


class Home(Screen):

    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if email == 'admin' and password == 'admin':
            self.ids.login.text = 'Login Success'
            self.ids.login.md_bg_color = "green"
        else:
            self.ids.login.text = 'Login Failed'
            self.ids.login.md_bg_color = "yellow"
            self.ids.login.text_color = "black"


    def count(self):
        self.ids.label.text = str(int(self.ids.label.text) + 1)


class MyApp(MDApp):

    def build(self):
        return Home()


MyApp().run()
