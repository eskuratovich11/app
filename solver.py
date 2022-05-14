import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class Parameters:
  def __init__(self, mass = 0, charge = 0):
    self.mas = mass
    self.electric_charge = charge

class Point:
  def __init__(self, x: float, y:float, vx:float, vy:float, params: Parameters):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.params = params

class Solver:
  def __init__(self, objects):
    self.objects = objects
    self.N = int(len(self.objects))
	self.edge= 2*3*10**11
	self.stena= 3*10**11

	self.frame = 5000
	self.seconds_in_year = 365 * 24 * 60 *60
	self.years = 5
	self.time = self.years * self.seconds_in_year
	self.t = np.linspace(0, self.time, self.frame)
	self.radius_earth= 100
	self.dt= self.t[1]
	self.ms =1.5

	self.G =6.67 * 10**(-11)
	self.k= 8.987551787 * 10**9

  def get_dvx_dt(self, a: Point, b: Point):

    ax = 0.0

    ax += (-self.G *
            b.params.mas  *(
            a.x - b.x) /
            ((a.x - b.x) ** 2 + (a.y -  b.y) ** 2) ** 1.5)
    ax += (self.k *
            a.params.electric_charge * b.params.electric_charge /a.params.mas *(
            a.x - b.x) /
            ((a.x - b.x) ** 2 + (a.y -  b.y) ** 2) ** 1.5)
    return float(ax)
  def get_dvy_dt(self, a: Point, b: Point):

    ay = 0.0

    ay += (-G*
            b.params.mas  *(
            a.y - b.y) /
            ((a.x - b.x) ** 2 + (a.y -  b.y) ** 2) ** 1.5)
    ay += (k *
            a.params.electric_charge * b.params.electric_charge /a.params.mas *(
            a.y - b.y) /
            ((a.x - b.x) ** 2 + (a.y -  b.y) ** 2) ** 1.5)
    return float (ay)


  def ydar(self, a: Point, b: Point):
      r= (a.x-b.x)**2+(a.y-b.y)**2
      if r <=(radius_earth*2)**2:
          a.vx =(2*b.params.mas*b.vx+a.vx*(a.params.mas-b.params.mas) )/(a.params.mas+b.params.mas)/ms
          a.vy =(2*b.params.mas*b.vy+a.vy*(a.params.mas-b.params.mas) )/(a.params.mas+b.params.mas)/ms

      else:
          a.vx = a.vx
          b.vy = b.vy
      return a.vx , b.vy

  def stena(self, a: Point):

        if a.x<= -self.tena:
           a.vx =-a.vx/self.ms
           a.x = -self.stena
        if a.x>= self.stena:
           a.vx =-a.vx/self.ms
           a.x = self.stena
        if a.y <= -2*self.stena:
           a.vy =-a.vy/self.ms
           a.y  =- 2*self.stena
        if a.y >= 2*self.stena :
           a.vy =-self.vy/self.ms
           a.y = 2*self.stena
        else:
           a.vx= a.vx
           a.vy= a.vy
        return a.vx , a.vy
  def calc_object(self, object: Point):
    for object_n in self.objects:
      if object == object_n:
        continue
      object.vx += self.dt* self.get_dvx_dt(object, object_n)
      object.vy += self.dt* self.get_dvy_dt(object, object_n)
      self.stena(object)
      self.ydar(object, object_n)
    self.euler(object)

  def euler(self, object: Point):
    object.x +=  self.dt * object.vx
    object.y +=  self.dt * object.vy

  def output_coords_func(self):
    x_coords=np.zeros((len(self.t), self.N ))
    y_coords=np.zeros((len(self.t), self.N ))

    for j in range(len(self.t)):
       for i in range(len(self.objects) ):
          self.calc_object(self.objects[i])
          x_coords[j,i]= self.objects[i].x
          y_coords[j,i]= self.objects[i].y

    return x_coords, y_coords

particles = [
  Point( 0,  0, 0, 0, Parameters(1.99*10**30, 0)),
  Point(149*10**9, 0, 0, 29780, Parameters(5.97*10**24, 0)),
  Point(2.27*10**11, 0, 0, 24130, Parameters(6.42*10**23, 0)),
]
sim = Solver(particles)









# crating some rocket model representation
class SomeRocketModel:

	# some inicialization
	def __init__(self, config, output, job):

		# keep incomming parameters inside 'self'
		self.config = config
		self.output = output
		self.job = job
		self.particles = [
		  Point( 0,  0, 0, 0, Parameters(1.99*10**30, 0)),
		  Point(149*10**9, 0, 0, 29780, Parameters(5.97*10**24, 0)),
		  Point(2.27*10**11, 0, 0, 24130, Parameters(6.42*10**23, 0)),
		]
		self.sim = Solver(self.particles)

	def animate(self,i):
	  for j in range(self.sim.N):
	    points[j].set_data(x[i][j], y[i][j])
	    lines[j].set_data(xl[j][:i], yl[j] [:i])

	def animation(self):
		points = []
		lines = []
		fig, ax = plt.subplots()

		b = sim.output_coords_func()
		x = b[0]
		y = b[1]

		for j in range(sim.N):
		    # создаём графический элемент "шар"
		    point, = plt.plot([], [], 'o', ms=5)
		    points.append(point)
		    line, = plt.plot([], [], '-')
		    lines.append(line)

		xl = np.zeros((sim.N, len(t)))
		yl = np.zeros((sim.N, len(t)))

		for j in range (sim.N):

		    for i in range(len(t)):
		    		xl[j][i] = x[i][j]
		    		yl[j][i] = y[i][j]
		plt.axis('equal')

		ax.set_xlim(-edge, edge)
		ax.set_ylim(-edge, edge)

	def saver(self):
		ani = FuncAnimation(fig,
		                    self.animate,
		                    frames=frame,
		                    interval=50    )
"""		with open(self.output, 'w') as logfile:

			# write all output suff
			log = logfile.write(self.output + '.txt')
		# ani.save(self.output + '.gif')"""
		return ani.write(self.output + '.gif')
