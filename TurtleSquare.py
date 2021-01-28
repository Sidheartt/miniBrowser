from turtle import Turtle, Screen


tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("coral")

for _ in range(4):
    tim.forward(100)
    tim.left(90)

S = Screen()
S.exitonclick()

