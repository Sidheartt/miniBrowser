import turtle as t
import random

tim = t
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ra = (r, g, b)
    return ra


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


