from turtle import Turtle,Screen
import time
from snake import Snake

screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:  
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()