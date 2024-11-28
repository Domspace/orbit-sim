from turtle import Turtle
from velocity import Velocity
from physics_stuff import do_gravity, do_velocity

class SpaceObject:
	def __init__(self, color, height, velocity):
	    self.t = Turtle()
	    self.v = velocity
	    self.color = color
	    self.height = height
	    self.init_turtle()
	
	def get_turtle(self):
	    return self.t
	def get_velocity(self):
	    return self.v
	
	def init_turtle(self):
	    self.t.speed(0)
	    self.t.color(self.color)
	    self.t.teleport(0, self.height)


def update_objects(list, grav_pos, grav_str):
    for i in list:
        do_gravity(i.get_turtle(), i.get_velocity(), grav_pos, grav_str)
        do_velocity(i.get_turtle(), i.get_velocity())

	
