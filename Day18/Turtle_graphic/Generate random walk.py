from turtle import Turtle,Screen
import random

tim =Turtle()
tim.shape('turtle')
tim.pensize(15)
tim.speed('fastest')


########### Challenge 4 - Generate random walk ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0,90,180,270]

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))



screen =Screen()
screen.exitonclick()