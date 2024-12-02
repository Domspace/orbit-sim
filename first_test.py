from fake_turtle import Turtle
from velocity import Velocity
from spaceobject import SpaceObject, update_objects


GRAVITY = 10000
height = 200
SUN_RADIUS = 50

objs = []


#t = Turtle()
#t.color("red")
#t.teleport(0, height + SUN_RADIUS)

objs.append(SpaceObject("red", 200 + SUN_RADIUS, Velocity(6.5,0)))
objs.append(SpaceObject("blue", 100 + SUN_RADIUS, Velocity(8,0)))
objs.append(SpaceObject("green", 400 + SUN_RADIUS, Velocity(3,0)))
objs.append(SpaceObject("gray", 100 + SUN_RADIUS, Velocity(6,0)))


t2 = Turtle()
t2.speed(0)
t2.teleport(0, -SUN_RADIUS)
t2.color("yellow")
t2.fillcolor("yellow")
t2.begin_fill()
t2.getscreen().bgcolor("black")
t2.circle(SUN_RADIUS)
t2.end_fill()
t2.hideturtle()


def event_loop():
    update_objects(objs, (0,0), GRAVITY)


#run_function_at_frequency(event_loop, 500, 30)
for i in range(400):
    event_loop()
