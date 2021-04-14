import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
screen = turtle_module.Screen()


tim.hideturtle()

colors = [
(236, 225, 199), (215, 219, 229), (241, 213, 231), (206, 155, 104), (211, 237, 219),
 (105, 111, 130), (137, 141, 160), (221, 216, 113), (180, 76, 36),
 (201, 141, 174), (182, 158, 31), (100, 106, 186), (12, 21, 65), (234, 162, 201), (9, 42, 17)
]

tim.setheading(225)
tim.penup()
tim.forward(350)
tim.setheading(0)

number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen.exitonclick()