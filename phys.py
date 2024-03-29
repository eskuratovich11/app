scale = 149 * 10 ** 7 # масштаб в 1 пк
scale_m = 10**24
scale_q = 10**18
wall_x1 = 0 * scale
wall_x2 = 1000 * scale
wall_y1 = 100 * scale
wall_y2 = 2200 * scale

dt = 30000
ms = 1.5

G = 6.67 * 10 ** (-11)
k = 8.987551787 * 10 ** 9


class Solver:
    def __init__(self, num, particles) :
        self.objects = particles
        self.num = num
        self.N = int(len(self.objects))
        self.ax = 0
        self.ay = 0
    def get_dvx_dt(self, a, b):
        try:
            self.ax += (-G *
                   b.mas * scale_m * (
                           a.x * scale - b.x * scale) /
                   ((a.x * scale - b.x * scale) ** 2 + (a.y * scale - b.y * scale) ** 2) ** 1.5)
            self.ax += (k *
                   a.electric_charge * scale_q * b.electric_charge * scale_q / (a.mas * scale_m) * (
                           a.x * scale - b.x * scale) /
                   ((a.x * scale - b.x * scale) ** 2 + (a.y * scale - b.y * scale) ** 2) ** 1.5)
        except ZeroDivisionError:
            self.ax = 0

        return float(self.ax)

    def get_dvy_dt(self, a, b):


        try:
            self.ay += (-G *
                   b.mas*scale_m * (
                           a.y*scale - b.y*scale) /
                   ((a.x*scale - b.x*scale) ** 2 + (a.y*scale - b.y*scale) ** 2) ** 1.5)
            self.ay += (k *
                   a.electric_charge*scale_q * b.electric_charge*scale_q / (a.mas*scale_m) * (
                           a.y*scale - b.y*scale) /
                   ((a.x*scale - b.x*scale) ** 2 + (a.y*scale - b.y*scale) ** 2) ** 1.5)
        except ZeroDivisionError:
            self.ay = 0
        return float(self.ay)

    def hit(self, a, b):
        r = (a.x - b.x) ** 2 + (a.y - b.y) ** 2
        if r <= (a.size[0]) ** 2:
            a.vx = ((2 * b.mas*scale_m * b.vx + a.vx * (a.mas*scale_m - b.mas*scale_m )) / (a.mas*scale_m + b.mas*scale_m))/ ms
            a.vy = ((2 * b.mas*scale_m * b.vy + a.vy * (a.mas*scale_m - b.mas*scale_m )) / (a.mas*scale_m + b.mas*scale_m))/ ms

        else:
            a.vx = a.vx
            b.vy = b.vy
        return a.vx, b.vy

    def wall(self, a):

        if a.x*scale < wall_x1:
            if a.vx <= 0:
                a.vx = -a.vx/ms
            else:
                a.vx = a.vx/ms
            a.x = wall_x1 / scale + 5
        elif a.x*scale > wall_x2:
            if a.vx >= 0:
                a.vx = -a.vx/ms
            else:
                a.vx = a.vx/ms
            a.x = wall_x2 / scale - 5
        elif a.y*scale < wall_y1:
            if a.vy <= 0:
                a.vy = -a.vy/ms
            else:
                a.vy = a.vy/ms
            a.y = wall_y1 / scale + 5
        elif a.y*scale > wall_y2:
            if a.vy >= 0:
                a.vy = -a.vy/ms
            else:
                a.vy = a.vy/ms
            a.y = wall_y2 / scale - 5
        else:
            a.vx = a.vx
            a.vy = a.vy
        return a.vx, a.vy

    def calc_object(self, object):
        for object_n in self.objects:
            if object == object_n:
                continue
            object.vx += dt * self.get_dvx_dt(object, object_n)
            object.vy += dt * self.get_dvy_dt(object, object_n)
            self.hit(object, object_n)

        self.euler(object)

    def euler(self, object):
        self.wall(object)
        object.x = (object.x * scale + dt * object.vx)/scale
        object.y = (object.y * scale + dt * object.vy)/scale

    def output_coords_func(self):
        coords = []
        self.calc_object(self.objects[self.num])
        coords.append(self.objects[self.num].x)
        coords.append(self.objects[self.num].y)

        return coords
