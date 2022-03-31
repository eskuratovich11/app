import phys as phys
from random import random
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.vector import Vector


Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<FirstScreen>:
    md_bg_color: app.theme_cls.bg_light
    MDFillRoundFlatButton:
        id:start
        text: "start"
        size_hint: None, None
        size: 800, 500
        pos_hint: {"center_x": 0.5, "center_y": 0.7}

        on_release: root.manager.current= 'dvizhuha'
        md_bg_color: app.theme_cls.primary_light

    MDFillRoundFlatButton:
        id: set1
        text: "settings"
        size_hint: None, None
        size: 800, 500
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: root.manager.current= 'settings'

    MDFillRoundFlatIconButton:
        id: exit
        icon: "exit-to-app"
        size_hint: None, None
        size: 800, 500
        md_bg_color: app.theme_cls.primary_dark
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.stop()

<MainScreen> :
    md_bg_color: app.theme_cls.bg_light
    MDFillRoundFlatButton:
        id: create
        text: "create"
        size_hint: None, None
        size: 300, 100
        pos_hint: {"center_x": 0.15, "center_y": 0.05}
        on_release: on_release: root.open()
    MDFillRoundFlatButton:
        id: clearb
        text: "clear"
        size_hint: None, None
        size: 300, 100
        pos_hint: {"center_x": 0.5, "center_y": 0.05}
        on_release: root.child.clear()
    MDFillRoundFlatIconButton:
        id: back_main
        icon: "arrow-left-bold-circle"
        size_hint: None, None
        size: 300, 200
        text: "back"
        md_bg_color: app.theme_cls.primary_dark
        icon_size: "64sp"
        pos_hint: {"center_x": 0.85, "center_y": 0.05}
        on_release: root.manager.current= 'first'
<CustomLayout> :
    id: custom
    size_hint: None, None
    size: 1000, 1900
    pos: 0,1900

<SecondScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        adaptive_size: True
        MDTextField:
            id:x
            max_text_length: 4
            hint_text: ' x'
            multiline: False

        MDTextField:
            id:y
            max_text_length: 4
            hint_text: ' y'
            multiline: False

        MDTextField:
            id:vx
            max_text_length: 6
            hint_text: ' vx'
            multiline: False
        MDTextField:
            id:vy
            max_text_length: 6
            hint_text: ' vy'
            multiline: False
        MDTextField:
            id:m
            max_text_length: 10
            hint_text: ' m'
            multiline: False
        MDTextField:
            id:q
            max_text_length: 5
            hint_text: ' q'
            multiline: False
        MDBoxLayout:
            adaptive_size: True
            MDIconButton:
                icon: "minus"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.1, "center_y": 0.5}
                on_release: root.m_p(size, 1)
            MDTextButton:
                id: size
                text: "50"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDIconButton:
                icon: "plus"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.7, "center_y": 0.5}
                on_release: root.m_p(size, 0)
        MDBoxLayout:
            adaptive_size: True
            MDIconButton:
                icon: "check-outline"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.4, "center_y": 0.5}
                on_release:
                    root.create_object(x.text, y.text, vx.text, vy.text, m.text, q.text)
                    root.dismiss()
            MDIconButton:
                icon: "arrow-left-bold"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.6, "center_y": 0.5}
                on_release: root.dismiss()

<SettingScreen>:
    md_bg_color: app.theme_cls.bg_light
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: tool
            title: "Settings"
        MDRelativeLayout:

            orientation: 'vertical'


            MDFillRoundFlatButton:
                id:change
                text:'Change language'
                size_hint: None, None
                size: 500, 300
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                on_release: dropdown.open(self)
            MDRelativeLayout:

                MDIconButton:
                    id: purple
                    icon: "circle"
                    size_hint: None, None
                    size: 200, 200
                    md_bg_color: get_color_from_hex('9C27B0')
                    pos_hint: {"center_x": 0.3, "center_y": 0.5}
                    on_release:
                        app.theme_cls.primary_palette = "Purple"
                        root.manager.get_screen('settings').ids.purple.md_bg_color = get_color_from_hex('9C27B0')
                        root.manager.get_screen('settings').ids.red.md_bg_color = get_color_from_hex('D32F2F')
                        root.manager.get_screen('settings').ids.green.md_bg_color = get_color_from_hex('388E3C')
                        root.manager.get_screen('first').ids.start.md_bg_color = app.theme_cls.primary_light
                        root.manager.get_screen('first').ids.exit.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('dvizhuha').ids.back_main.md_bg_color = app.theme_cls.primary_dark

                MDIconButton:
                    id: red
                    icon: "circle"
                    size_hint: None, None
                    size: 200, 200
                    md_bg_color: get_color_from_hex('D32F2F')
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    on_release:
                        app.theme_cls.primary_palette = "Red"
                        root.manager.get_screen('settings').ids.purple.md_bg_color = get_color_from_hex('9C27B0')
                        root.manager.get_screen('settings').ids.red.md_bg_color = get_color_from_hex('D32F2F')
                        root.manager.get_screen('settings').ids.green.md_bg_color = get_color_from_hex('388E3C')
                        root.manager.get_screen('first').ids.start.md_bg_color = app.theme_cls.primary_light
                        root.manager.get_screen('first').ids.exit.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('dvizhuha').ids.back_main.md_bg_color = app.theme_cls.primary_dark
                MDIconButton:
                    id: green
                    icon: "circle"
                    size_hint: None, None
                    size: 200, 200
                    md_bg_color: get_color_from_hex('388E3C')
                    pos_hint: {"center_x": 0.7, "center_y": 0.5}
                    on_release:
                        app.theme_cls.primary_palette = "Green"
                        root.manager.get_screen('settings').ids.purple.md_bg_color = get_color_from_hex('9C27B0')
                        root.manager.get_screen('settings').ids.red.md_bg_color = get_color_from_hex('D32F2F')
                        root.manager.get_screen('settings').ids.green.md_bg_color = get_color_from_hex('388E3C')
                        root.manager.get_screen('first').ids.start.md_bg_color = app.theme_cls.primary_light
                        root.manager.get_screen('first').ids.exit.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('dvizhuha').ids.back_main.md_bg_color = app.theme_cls.primary_dark
            MDFillRoundFlatIconButton:
                id: back_set
                icon: "arrow-left-bold-circle"
                size_hint: None, None
                size: 300, 200
                text: "back"
                md_bg_color: app.theme_cls.primary_dark
                icon_size: "64sp"
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                on_release: root.manager.current= 'first'

    DropDown:
        id:dropdown
        dropdown : self.dismiss()

        MDTextButton:
            text: 'rus'
            size_hint:  None, None
            size:  100, 30
            on_release:
                root.change(
                root.manager.get_screen('settings').ids.change,
                root.manager.get_screen('settings').ids.tool,
                root.manager.get_screen('first').ids.start,
                root.manager.get_screen('first').ids.set1,
                root.manager.get_screen('dvizhuha').ids.create,
                root.manager.get_screen('dvizhuha').ids.clearb,
                root.manager.get_screen('dvizhuha').ids.back_main,
                root.manager.get_screen('settings').ids.back_set,
                1 )

        MDTextButton:
            text: 'eng'
            size_hint:  None, None
            size:  100, 30

            on_release:
                root.change(
                root.manager.get_screen('settings').ids.change,
                root.manager.get_screen('settings').ids.tool,
                root.manager.get_screen('first').ids.start,
                root.manager.get_screen('first').ids.set1,
                root.manager.get_screen('dvizhuha').ids.create,
                root.manager.get_screen('dvizhuha').ids.clearb,
                root.manager.get_screen('dvizhuha').ids.back_main,
                root.manager.get_screen('settings').ids.back_set,
                0 )
<Object>
    size_hint: None, None
    size: self.size
    pos: 0,100
<Move>
    size_hint: None, None
    size: 1000, 1900
    pos: 0,100''')


class FirstScreen(MDScreen):
    pass


class CustomLayout(BoxLayout):
    def __init__(self, dispatcher, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        self.dispatcher = dispatcher

    def clear(self):
        self.clear_widgets()
        Object.items.clear()


class MainScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.child = CustomLayout(Widget())
        self.second = SecondScreen(self.child)
        self.add_widget(self.child)

    def open(self):
        self.second.open()


class SecondScreen(ModalView):
    def __init__(self, child_screen, **kw):
        super().__init__(**kw)
        self.child_screen = child_screen
        self.num = -1
        self.size_point = 0
        self.pointsize = [50, 50]

    def create_object(self, x, y, vx, vy, mas, electric_charge):
        if Object.items == []:
            self.num = -1
        self.num += 1
        self.object = Move(self.num)
        self.object.create(x=float(x) + 100, y=float(y) + 200, size=self.pointsize,
                           vx=float(vx), vy=float(vy),
                           mas=float(mas), electric_charge=float(electric_charge))

        self.child_screen.add_widget(self.object)

        self.clock()

    def m_p(self, size, n):
        if n == 1 and self.size_point != 10:
            size.text = str(int(size.text) - 10)
            self.size_point = int(size.text)
            self.pointsize = [self.size_point, self.size_point]
        elif n == 0 and self.size_point != 100:
            size.text = str(int(size.text) + 10)
            self.size_point = int(size.text)
            self.pointsize = [self.size_point, self.size_point]
        else:
            pass

    def clock(self):
        my_clock = Clock
        event1 = my_clock.schedule_once(self.object.update, 0)
        event1()
        event = my_clock.schedule_interval(self.object.update, 0.1)
        event()


class Object(Widget):
    items = []

    def __init__(self, x, y, size, vx, vy, mas, electric_charge, **kw):
        super(Object, self).__init__(**kw)
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.size = size
        self.vx = vx
        self.vy = vy
        self.mas = mas
        self.electric_charge = electric_charge

        self.coords = []
        Object.items.append(self)

    def draw(self):

        color = (random(), random(), random())
        with self.canvas:
            Color(*color)

        self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.line = Line(points=(self.pos[0], self.pos[1]))
        self.canvas.add(self.ellipse)
        self.canvas.add(self.line)

    def move(self, dt, num):
        self.interact = phys.Solver(num, Object.items)
        self.coords = ((self.interact.output_coords_func()[0], self.interact.output_coords_func()[1]))
        self.pos = Vector(self.coords)
        self.ellipse.pos = self.pos
        self.line.points += (self.pos[0], self.pos[1])

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
        self.line.points += (self.pos[0], self.pos[1])
        self.vx = self.vx
        self.vy = self.vy

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            if (self.pos[0] - 1.5 * self.size[0]) <= touch.pos[0] <= (
                    self.pos[0] + 1.5 * self.size[0]):
                if (self.pos[1] - 1.5 * self.size[1]) <= touch.pos[1] <= (
                        self.pos[1] + 1.5 * self.size[1]):
                    self.x = touch.pos[0] - 1.5 * self.size[0] / 2
                    self.y = touch.pos[1] - 1.5 * self.size[1] / 2
                    self.move_pos = [self.x, self.y]
                    self.move_touch()
        else:
            pass

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
        else:
            pass


class Move(Widget):
    def __init__(self, num, **kw):
        super().__init__(**kw)
        self.num = num

    def update(self, dt):
        if Object.items == []:
            pass
        else:
            self.object.move(dt, self.num)

    def create(self, x, y, size, vx, vy, mas, electric_charge):
        self.object = Object(x=x, y=y, size=size, vx=vx, vy=vy, mas=mas, electric_charge=electric_charge)
        self.object.draw()
        self.add_widget(self.object)


class SettingScreen(MDScreen):

    def change(self, change, tool, start, set1, create, clearb, back_main, back_set, lang ):
        if lang == 1:
            change.text = 'Изменить язык'
            tool.title = 'Настройки'
            start.text = 'начать'
            set1.text = 'настройки'
            create.text = 'создать'
            clearb.text = 'очистить'
            back_main.text = 'назад'
            back_set.text = 'назад'
        else:
            change.text = 'Change language'
            tool.title = 'settings'
            start.text = 'start'
            set1.text = 'settings'
            create.text = 'create'
            clearb.text = 'clear'
            back_main.text = 'back'
            back_set.text = 'back'


class CustomDropDown(DropDown):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SettingScreen(name='settings'))
        sm.add_widget(MainScreen(name='dvizhuha'))

        return sm


if __name__ == '__main__':
    TestApp().run()