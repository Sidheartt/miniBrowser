from turtle import Turtle, Screen


tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("coral")

for _ in range(50):
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


S = Screen()
S.exitonclick()

