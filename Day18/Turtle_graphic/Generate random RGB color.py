import turtle as t
from turtle import Screen
import random

########### Challenge 5 - Generate random RGB color ########
tim =t.Turtle()
# set the colormode to 255
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.pensize(15)
tim.speed('fastest')
direction = [0,90,180,270]


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))




screen = Screen()
screen.exitonclick()
