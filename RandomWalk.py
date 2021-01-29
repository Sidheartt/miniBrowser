from turtle import Turtle, Screen
import random

tim = Turtle()
Turtle.colormode(255)
print(tim)
tim.shape("turtle")


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ra = (r, g, b)
    return ra


turn = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")


def walk():
    tim.forward(30)
    tim.setheading(random.choice(turn))
    tim.color(rand_color())


for i in range(1, 900):
    walk()


S = Screen()
S.exitonclick()

