from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.modalview import ModalView
from kivy.lang.builder import Builder


Builder.load_string('''
<SomeScreen1>:
    Button:
        text:'Please, push me!'
        on_release:root.view()

<Win>:
    auto_dismiss:False
    size_hint:(.8,.8)
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'some text'
        Button:
            text:'leave win!'
            on_release:root.leave()
''')


class SomeScreen1(Screen):
    def __init__(self,main_screen,**kwargs):
        super().__init__(**kwargs)
        self.main_screen=main_screen
        #Создаём и передаём и себя и TestApp
        self.win = Win(self,self.main_screen)
        self.my_name = 'second'

    def view(self):
        self.win.open()

    def print_func1(self):
        print(self.my_name)


class Win(ModalView):
    def __init__(self,some_screen1,main_screen,**kwargs):
        super().__init__(**kwargs)
        self.main_screen=main_screen
        self.some_screen1=some_screen1

    def leave(self):
        self.dismiss()
        #вызываем метод класса SomeScreen1
        self.some_screen1.print_func1()
        #вызывем метод класса TestApp
        self.main_screen.print_func()


class TestApp(App):
    def build(self):
        sm=ScreenManager()
        #Создаём и передаём себя
        sm.add_widget(SomeScreen1(self,name='screen one'))
        self.my_name='main'
        return sm

    def print_func(self):
        print(self.my_name)


TestApp().run()