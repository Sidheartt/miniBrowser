from turtle import Turtle, Screen
import random

tim = Turtle()
print(tim)
tim.shape("turtle")

colors = ["orange", "maroon", "cyan", "yellow", "navy"]


def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for side in range(3, 11):
    tim.color(random.choice(colors))
    draw(side)


S = Screen()
S.exitonclick()

