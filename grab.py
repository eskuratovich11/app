from kivy.app import App
from kivy.vector import Vector
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from random import random
from kivy.core.window import Window
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

class PainterWidget(Widget):
  r, g, b = (255, 255, 255)
  def on_touch_down(self, touch):
    with self.canvas:
      self.touch = touch
      self.configure()
  def on_touch_move(self, touch):
    self.pos = Vector(touch.x, touch.y)
    touch.ud['ellipse'].pos= self.pos
  def configure(self):
    Color(self.r, self.g, self.b, 1)
    rad = 15
    self.touch.ud['ellipse'] =  Ellipse(pos=(self.touch.x - rad/2,self.touch.y - rad/2), size = (rad, rad))
  def changeColor(self, rgb):
    self.r, self.g, self.b = rgb

class PaintApp(App):
  def build(self):
    parent = Widget()
    self.painter = PainterWidget()
    parent.add_widget(self.painter)

    parent.add_widget(Button(text = 'Clear' , on_press = self.clear_canvas, size = (100, 50)))
    parent.add_widget(Button(text = 'Save' , on_press = self.save, size = (100, 50), pos = (100, 0)))
    parent.add_widget(Button(text = 'Screen', on_press = self.screen, size = (100, 50), pos=(200, 0 )))
    parent.add_widget(Button(text = 'red', on_press = self.red, size = (100, 50), pos=(300, 0 )))
    parent.add_widget(Button(text = 'green', on_press = self.green, size = (100, 50), pos=(400, 0 )))
    parent.add_widget(Button(text = 'blue', on_press = self.blue, size = (100, 50), pos=(500, 0 )))

    return parent

  def red(self, instance):
  	self.painter.changeColor(rgb=(255, 0, 0))
  def green(self, instance):
  	self.painter.changeColor(rgb=(0, 255, 0))
  def blue(self, instance):
  	self.painter.changeColor(rgb=(0, 0, 255))

  def clear_canvas(self, instance):
      self.painter.canvas.clear()

  def save(self, instance):
    self.painter.size = (Window.size[0], Window.size[1])
    self.painter.export_to_png('mage.png')

  def screen(self, instance):
    Window.screenshot('screen.png')

if __name__ == '__main__':
  PaintApp().run()