from event import run_function_at_frequency
from turtle import Turtle
from velocity import Velocity
from physics_stuff import do_velocity, do_gravity

GRAVITY = 10000
height = 200
velocity = Velocity(4,0)
SUN_RADIUS = 50


t = Turtle()
t.teleport(0, height + SUN_RADIUS)


t2 = Turtle()
t2.speed(0)
t2.teleport(0, -SUN_RADIUS)
t2.circle(SUN_RADIUS)
t2.hideturtle()


def event_loop():
    do_gravity(t, velocity, (0, 0), GRAVITY)
    do_velocity(t, velocity)
    print(t.pos())


run_function_at_frequency(event_loop, 50, 5)
