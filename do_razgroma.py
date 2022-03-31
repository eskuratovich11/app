from kivy.config import Config

Config.set('graphics', 'resizable', True)
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Ellipse
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from random import randint
from kivy.vector import Vector

Builder.load_string("""
<FirstScreen>:

    BoxLayout:

    	orientation: "vertical"
        spacing:20
        Button: 
            id:start
        	text: "start"

        	size_hint: 1, .5

        	on_release: root.manager.current= 'dvizhuha'


        Button:
            id: set1
            text: "settings"        	
            size_hint: 1 , .5

            on_release: root.manager.current= 'settings'	
        Button:
            id: exit
        	text: "exit"

        	size_hint: 1, .5
        	on_release: app.stop()
<MainScreen> :     
    BoxLayout:

        Button:
        	text: "start"       
        	size_hint: .2, .2	
        	pos: 0, 0	
        	on_release: root.start()	
        Button:
        	text: "create"        	
        	size_hint: .2, .2
        	pos: 200, 200

        	on_release: root.open()

<SecondScreen>:   
    auto_dismiss:False
    BoxLayout:
    	orientation: "vertical"
        Label:
        	id:field
        	text: 'Input'
        TextInput:
        	id:x        	
        	hint_text: 'write x'
        	multiline: False
        TextInput:
        	id:y       	
        	hint_text: 'write y'
        	multiline: False
        Button: 
        	text:'OK'
        	pos: .5, .5
        	on_release:
        	    root.create_object(x.text, y.text)
                root.dismiss()
        	

<SettingScreen>:   
    BoxLayout:
    	orientation: "vertical"
        Label:
        	id: field2
        	text: 'settings'
        Button: 
            id:change
        	text:'Change language'
        	on_release: dropdown.open(self)
        Button:
            id: back_set
            text: "back"
            size: 500, 500    	
            pos_hint: {'center_y': .5, 'center_x': .5}
            on_release: root.manager.current= 'first' 

        DropDown:
            id:dropdown
            dropdown : self.dismiss()

            Button:           
                text: 'rus'
                size_hint_y:  None
                height:  44
     
                on_release: 
                    root.change(
                    root.manager.get_screen('settings').ids.back_set,
                    root.manager.get_screen('settings').ids.change,
                    root.manager.get_screen('settings').ids.field2,
                    root.manager.get_screen('first').ids.start,
                    root.manager.get_screen('first').ids.set1,
                    root.manager.get_screen('first').ids.exit, 1)

            Button:
                text: 'eng'
                size_hint_y:  None
                height:  44
                
                on_release:  
                    root.change(
                    root.manager.get_screen('settings').ids.back_set,
                    root.manager.get_screen('settings').ids.change,
                    root.manager.get_screen('settings').ids.field2,
                    root.manager.get_screen('first').ids.start,
                    root.manager.get_screen('first').ids.set1,
                    root.manager.get_screen('first').ids.exit, 0)	

""")


class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class Object(Widget):

    def __init__(self, pos, size, **kw):
        super(Object, self).__init__(**kw)
        self.counter = 0
        self.pos = pos
        self.size = size
        self.coords = []

    def draw(self):
        self.canvas.add(Color(0, 1, 0, 1))
        self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.canvas.add(self.ellipse)

    def move(self, i):
        self.pos = Vector(self.coords[i])
        self.ellipse.pos = self.pos

    def update(self, dt):
        a = randint(0, 15)
        b = randint(10, 20)
        self.coords.append((self.pos[0] + a * dt, self.pos[1] + b * dt))
        self.move(self.counter)
        self.counter += 1

    def create(self):
        self.draw()


class SecondScreen(ModalView):
    def __init__(self, some_screen1, main_screen, **kw):
        super().__init__(**kw)
        self.main_screen = main_screen
        self.some_screen1 = some_screen1
        self.pointsize = [50, 50]

    def create_object(self, x, y):
        self.object= Object(pos=[int(x), int(y)], size= self.pointsize)
        self.object.create()
        self.some_screen1.add_widget(self.object)
        self.clock()
    def clock(self):
        for i in range(self.object.counter+1):
            Clock.schedule_interval(self.object.update, 0.1)




class MainScreen(Screen):
    def __init__(self, main_screen, **kw):
        super().__init__(**kw)
        self.main_screen = main_screen
        self.second = SecondScreen(self, self.main_screen)

    def open(self):
        self.second.open()

    def start(self):
        self.second.clock()



class SettingScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def change(self, back_set, change, field2, start, set1, exit, lang):
        if lang == 1:
            back_set.text = 'назад'
            change.text = 'изменить язык'
            field2.text = 'настройки'
            start.text = 'начать'
            set1.text = 'настройки'
            exit.text = 'выход'
        else:
            back_set.text = 'back'
            change.text = 'change language'
            field2.text = 'settings'
            start.text = 'start'
            set1.text = 'settings'
            exit.text = 'exit'


class CustomDropDown(DropDown):
    pass


class TestApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SettingScreen(name='settings'))
        sm.add_widget(MainScreen(self, name='dvizhuha'))
        return sm


if __name__ == '__main__':
    TestApp().run()