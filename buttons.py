from kivy.config import Config
from kivymd.app import MDApp
Config.set('graphics', 'resizable', True)
from kivy.app import App
from kivymd.uix.button import MDIconButton
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.uix.screen import MDScreen
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Ellipse
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from random import randint
from kivy.vector import Vector
from kivymd.uix.boxlayout  import MDBoxLayout

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<FirstScreen>:
    md_bg_color: get_color_from_hex("#f7f2fa")
    MDBoxLayout:
        size: 2000, 1000
    	orientation: "vertical"
        MDIconButton: 
            id:start
        	text: "start"
        	size_hint: 1, .5
        	on_release: root.manager.current= 'dvizhuha'


        MDIconButton:
            id: set1
            text: "settings"        	
            size_hint: 1 , .5
            on_release: root.manager.current= 'settings'	

        MDIconButton:
            id: exit
        	text: "exit"

        	size_hint: 1, .5
        	on_release: app.stop()
<MainScreen> : 
    MDBoxLayout:  
        orientation: "vertical"      
        size: 1000, 2500	
        MDIconButton:
            text: "create" 
            size_hint: None, None       	
            size: 1000, 100
            pos: 0, 0
            on_release: root.open()
<CustomLayout> :     
    size_hint: None, None       	
    size: 1000, 2400
    pos: 0,100
<SecondScreen>:   
    auto_dismiss:False

    MDBoxLayout:
        size: 1000, 2500
    	orientation: "vertical"
        MDLabel:
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
        MDIconButton: 
        	text:'OK'
        	pos: .3, .3
        	on_release:
        	    root.create_object(x.text, y.text)
                root.dismiss()


<SettingScreen>:   
    MDBoxLayout:
        size: 1000, 2500
    	orientation: "vertical"
        MDLabel:
        	id: field2
        	text: 'settings'
        MDIconButton: 
            id:change
        	text:'Change language'
        	size_hint: None, None 
            size: 1000, 300  
            pos_hint: {'center_y': .5, 'center_x': .5}  
        	on_release: dropdown.open(self)
        MDIconButton:
            id: back_set
            text: "back"
            size_hint: None, None 
            size: 1000, 300    	
            pos_hint: {'center_y': .5, 'center_x': .5}
            on_release: root.manager.current= 'first' 

        DropDown:
            id:dropdown
            dropdown : self.dismiss()

            MDIconButton:           
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

            MDIconButton:
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
<Object>
    size_hint: None, None       	
    size: self.size
    pos: 0,100
<Move>
    size_hint: None, None       	
    size: 1000, 2400
    pos: 0,100
""")


class FirstScreen(MDScreen):
    pass


class CustomLayout(MDBoxLayout):
    def __init__(self, dispatcher, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        self.dispatcher = dispatcher


class MainScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.child = CustomLayout(Widget())
        self.second = SecondScreen(self.child)
        self.add_widget(self.child)

    def open(self):
        self.second.open()


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

    def move(self, i, dt):
        a = randint(0, 15)
        b = randint(10, 20)
        self.coords.append((self.pos[0] + a * dt, self.pos[1] + b * dt))
        self.pos = Vector(self.coords[i])
        self.ellipse.pos = self.pos



    def on_touch_down(self, touch):

        if (self.pos[0] - self.size[0]) <= touch.pos[0] <= (
                self.pos[0] + self.size[0]):
            if (self.pos[1] - self.size[1]) <= touch.pos[1] <= (
                    self.pos[1] + self.size[1]):
                touch.grab(self)
                return True

    def move_touch(self):
        self.pos = Vector(self.move_pos)
        self.ellipse.pos = self.pos

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            if (self.pos[0] - self.size[0]) <= touch.pos[0] <= (
                    self.pos[0] + self.size[0]):
                if (self.pos[1] - self.size[1]) <= touch.pos[1] <= (
                        self.pos[1] + self.size[1]):
                    self.move_pos = [touch.pos[0] - self.size[0] / 2, touch.pos[1] - self.size[1] / 2]
                    self.move_touch()
        else:
            pass

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
        else:
            pass

class Move(Widget):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.counter = 0
    def create(self, pos, size):
        self.object = Object(pos=pos, size=size)
        self.object.draw()
        self.add_widget(self.object)
    def update(self, dt):
        self.object.move(self.counter, dt)
        self.counter += 1

class SecondScreen(ModalView):
    def __init__(self, child_screen, **kw):
        super().__init__(**kw)

        self.child_screen = child_screen

        self.pointsize = [50, 50]

    def create_object(self, x, y):
        self.object = Move()
        self.object.create(pos=[int(x), int(y) + 100], size=self.pointsize)
        self.child_screen.add_widget(self.object)
        self.clock()
    def clock(self):
        Clock.schedule_once(self.object.update, 0)
        Clock.schedule_interval(self.object.update, 0.1)

class SettingScreen(MDScreen):

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


class TestApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SettingScreen(name='settings'))
        sm.add_widget(MainScreen(name='dvizhuha'))
        return sm


if __name__ == '__main__':
    TestApp().run()