from turtle import  Turtle,Screen
import random

tim =Turtle()
tim.shape('turtle')
tim.color('red')

########### Challenge 1 - Draw Square ########

# tim.forward(100)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(100)


########### Challenge 2 - Draw Dashed Line ########

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    
########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(no_sides):
    angle = 360 / no_sides
    for _ in range(no_sides):
        tim.forward(100)
        tim.right(angle)

for shape_size_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_size_n)



screen = Screen()
screen.exitonclick()