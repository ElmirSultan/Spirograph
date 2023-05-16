import turtle as t 
from turtle import Screen
import random


arrow = t.Turtle()
arrow.pensize(1)
arrow.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


for _ in range(100):
    arrow.color(random_color())
    arrow.circle(100)
    arrow.setheading(arrow.heading() + 10)


my_screen = Screen()
my_screen.exitonclick()

