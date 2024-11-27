from distance import get_distance, get_diff
from math import sqrt


def normalize_vector(v):
    magnitude = sqrt(sum(x**2 for x in v))
    return [x / magnitude for x in v]


def do_gravity(turtle, velocity, grav_pos, grav):
    acc = grav / (get_distance(turtle.pos(), grav_pos))**2
    dir = normalize_vector(get_diff(turtle.pos(), grav_pos))
    velocity.add_velocity([x*acc for x in dir])


def do_velocity(turtle, velocity):
    prev_pos = turtle.pos()
    new_pos = []
    for i in range(2):
        new_pos.append(prev_pos[i] + velocity.get_velocity()[i])
    turtle.goto(new_pos)