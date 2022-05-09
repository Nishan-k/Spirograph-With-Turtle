import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
jimmy = Turtle()


def color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_combo = (r, g, b)
    return color_combo


def spirograph():
    direction = 0
    for i in range(0, 100):
        if direction > 360:
            break
        else:
            jimmy.color(color_generator())
            jimmy.pensize(1)
            jimmy.speed(12)
            jimmy.circle(100)
            jimmy.setheading(direction)
            direction += 5


spirograph()
screen = Screen()
screen.exitonclick()
