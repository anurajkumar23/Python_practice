from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwords():
    tim.forward(10)

def move_backwords():
    tim.backward(10)

def left_side():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right_side():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
 
screen.listen()
screen.onkey(move_forwords, "w")
screen.onkey(move_backwords, "s")
screen.onkey(left_side, "a")
screen.onkey(right_side, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()