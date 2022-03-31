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


Builder.load_file('my_super_app.kv')


class FirstScreen(MDScreen):
    pass


class CustomLayout(BoxLayout):
    def __init__(self, dispatcher, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        self.dispatcher = dispatcher

    def clear(self):
        self.clear_widgets()
        Object.items = []


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
        self.size_point = 0
        self.pointsize = [50, 50]
    def check_num(self):
        if Object.items == []:
            self.num = 0
        else:
            self.num += 1
    def create_object(self, x, y, vx, vy, mas, electric_charge):
        self.check_num()

        self.object = Move()

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
        event1 = my_clock.schedule_once(self.object.update(self.num), 0)
        event1()
        event = my_clock.schedule_interval(self.object.update(self.num), 0.1)
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
    def __init__(self, **kw):
        super().__init__(**kw)


    def update(self, dt, num):
        if Object.items == []:
            pass
        else:
            self.object.move(dt, num)

    def create(self, x, y, size, vx, vy, mas, electric_charge):
        self.object = Object(x=x, y=y, size=size, vx=vx, vy=vy, mas=mas, electric_charge=electric_charge)
        Object.items.append(self.object)
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