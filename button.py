from random import random
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition


Builder.load_file('button.kv')


class FirstScreen(MDScreen):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FirstScreen(name='first'))
        return sm


if __name__ == '__main__':
    TestApp().run()
