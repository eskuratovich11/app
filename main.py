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
class Tasks (MDScreen):
    pass


class CustomLayout(BoxLayout):
    def __init__(self, dispatcher, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        self.dispatcher = dispatcher

    def clear(self):
        self.clear_widgets()
        Object.num_new = Object.num +1

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
    def create_object(self, x, y, vx, vy, mas, electric_charge, x_error, y_error, vx_error, vy_error, m_error, q_error):
        if x_error == True:
            pass
        elif y_error == True:
            pass
        elif vx_error == True:
            pass
        elif vy_error == True:
            pass
        elif m_error == True:
            pass
        elif q_error== True:
            pass
        else:
            Object.num += 1
            self.object = Move(Object.num)
            self.object.create(x=float(x) + 100, y=float(y) + 100, size=self.pointsize,
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
        my_clock.schedule_once(self.object.update, 0)
        my_clock.schedule_interval(self.object.update, 0.1)

    def set_error_message(self, text_field):
        try:
            float(text_field.text)
            text_field.error = False
        except ValueError:
            text_field.error = True
    def set_error_message_m(self, m):
        try:
            float(m.text)
            m.error = False
            if float(m.text) <= 0:
                m.error = True
        except ValueError:
            m.error = True



class Object(Widget):
    items = []
    num = -1
    num_new = 0

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
        num = num-Object.num_new
        self.interact = phys.Solver( num, Object.items[Object.num_new : Object.num +1 ])
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
        if self.num < Object.num_new :
            pass
        else:
            self.point.move(dt, self.num)

    def create(self, x, y, size, vx, vy, mas, electric_charge):
        self.point = Object(x=x, y=y, size=size, vx=vx, vy=vy, mas=mas, electric_charge=electric_charge)

        self.point.draw()
        self.add_widget(self.point)



class SettingScreen(MDScreen):

    def change(self, change, tool, start, set1, task, create, clearb, back_main, back_set, toolbar, task1_1, task2_1, task3_1 , task4_1, task5_1, task1, task2, task3, task4, task5, scale, x_y, vx_vy, m_s, q_s, back_tasks, lang ):
        if lang == 1:
            change.text = 'Изменить язык'
            tool.title = 'Настройки'
            start.text = 'начать'
            set1.text = 'настройки'
            task.text = 'задачи'
            create.text = 'создать'
            clearb.text = 'очистить'
            back_main.text = 'назад'
            back_set.text = 'назад'
            toolbar.title = 'Задачи'
            task1_1.text = 'Задача 1'
            task2_1.text = 'Задача 2'
            task3_1.text = 'Задача 3'
            task4_1.text = 'Задача 4'
            task5_1.text = 'Задача 5'
            task1.text = 'Разместите 2 разноименно заряженных тела на экране. Добавьте 3 тело так, чтобы избежать столкновения 1 и 2.'
            task2.text = 'Создайте систему из массивного тела и 3 объектов, обращающихся вокруг него.'
            task3.text = 'Создайте 2 объекта так, чтобы тело 2 вращалось вокруг тела 1, при этом одно из тел должно двигаться по оси х, другок по оси у. Далее добавьте 3 неподвижный объект, который притянет оба.'
            task4.text = 'Расположите на одной диагонали 2 разноименных заряда. Сделайте так, чтобы они не притянулись друг к другу, добавив два дополнительных объекта.'
            task5.text = 'Расположите в нижней части экрана 3 тела с небольшой массой. В верхней части расположите тело с большей массой. Скорости тел равны 0. Не перемещая объекты, заставьте три первых объекта притянуться к большему.'
            scale.text = 'Масштаб'
            x_y.text = 'x, y : 100 = 1 а. е (149*10^9 м)'
            vx_vy.text = 'vx, vy : 1 = 1 м/с'
            m_s.text = 'm: 1 = 10^ 24 кг'
            q_s.text = 'q: 1= 10^18 Кл'
            back_tasks.text = 'назад'
        else:
            change.text = 'Change language'
            tool.title = 'settings'
            start.text = 'start'
            set1.text = 'settings'
            task.text = 'tasks'
            create.text = 'create'
            clearb.text = 'clear'
            back_main.text = 'back'
            back_set.text = 'back'
            toolbar.title = 'Tasks'
            task1_1.text = 'Task 1'
            task2_1.text = 'Task 2'
            task3_1.text = 'Task 3'
            task4_1.text = 'Task 4'
            task5_1.text = 'Task 5'
            task1.text = 'Place 2 oppositely charged objects on the screen. Add object 3 so as to avoid collision 1 and 2.'
            task2.text = 'Create a system from a massive object and 3 objects revolving around it.'
            task3.text = 'Create 2 objects so that body 2 rotates around body 1, with one of the bodies moving along the x-axis and the other moving along the y-axis. Next, add 3 stationary objects that will pull both.'
            task4.text = 'Place 2 opposite charges on the same diagonal. They must not pulled each other. You can add two extra objects.'
            task5.text = 'Place 3 bodies with a small mass at the bottom of the screen. In the upper part, place the body with more mass. The velocities of the bodies are 0. Without moving the objects, make the first three objects be pulled to the larger one.'
            scale.text = 'Scale'
            x_y.text = 'x, y : 100 = 1 а. u (149*10^9 m)'
            vx_vy.text = 'vx, vy : 1 = 1 m/s'
            m_s.text = 'm: 1 = 10^ 24 kg'
            q_s.text = 'q: 1= 10^18 C'
            back_tasks.text = 'back'


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
        sm.add_widget(Tasks(name='tasks'))

        return sm


if __name__ == '__main__':
    TestApp().run()