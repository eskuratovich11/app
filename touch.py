from kivy.app import App
from kivy.graphics import Ellipse, Line
from kivy.uix.boxlayout import BoxLayout


class CustomLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)

        self.canvas_nodes = []
        self.nodesize = [25, 25]
        self.canvas_ellipses= []
        self.grabbed = []
        self.obj = []
        # declare a canvas
        with self.canvas.after:
            pass

        self.define_nodes([100, 100])
        #self.define_nodes([500, 500])
        self.canvas.add(self.canvas_ellipses[0])
        #self.canvas.add(self.canvas_ellipses[1])
    def define_nodes(self, pos):
        """создаем объекты"""

        self.obj.append(pos)
        self.object = Ellipse(
            size=self.nodesize,
            pos= self.obj[0])
        self.canvas_nodes.append(self.obj)
        self.canvas_ellipses.append(self.object)

        # в create obj self.canvas_nodes.append(self.object)
    def update(self):
        for i in range(len(self.canvas_ellipses)):
            self.object = Ellipse(
                size=self.nodesize,
                pos=self.grabbed[i][0])
    def on_touch_down(self, touch):

        for i in range(len(self.canvas_nodes)):
            if (self.canvas_nodes[i][0][0] - self.nodesize[0]) <= touch.pos[0] <= (self.canvas_nodes[i][0][0] + self.nodesize[0]):
                if (self.canvas_nodes[i][0][1] - self.nodesize[1]) <= touch.pos[1] <= (self.canvas_nodes[i][0][1] + self.nodesize[1]):
                    touch.grab(self)
                    self.grabbed = self.canvas_nodes
                    return True

    def on_touch_move(self, touch):

        if touch.grab_current is self:
            self.canvas.clear()
            for i in range(len(self.canvas_ellipses)):
                self.grabbed[i][0] = [touch.pos[0] - self.nodesize[0] / 2, touch.pos[1] - self.nodesize[1] / 2]
                self.obj[0] = self.grabbed[i][0]

                self.update()

                self.canvas.add(self.canvas_ellipses[i])

        else:
            # it's a normal touch
            pass

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            # I receive my grabbed touch, I must ungrab it!
            touch.ungrab(self)
        else:
            # it's a normal touch
            pass


class MainApp(App):

    def build(self):
        root = CustomLayout()
        return root


if __name__ == '__main__':
    MainApp().run()