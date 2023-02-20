from turtle import Turtle,Screen
import time

screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


starting_position =[(0,0),(-20,0),(-40,0)]

segment = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)


is_game_on = True
while is_game_on:  
    screen.update()
    time.sleep(0.1)
    for seg in segment:  
        seg.forward(20)
        
       


screen.exitonclick()