from turtle import Turtle, Screen


tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("coral")

for _ in range(6):
    tim.forward(150)
    tim.left(60)

tim.color("teal")
tim.left(60)
tim.forward(150)
tim.right(120)
tim.forward(150)

tim.color("Yellow")
for _ in range(3):
    tim.left(118)
    for _ in range(6):
        tim.forward(200)
        tim.left(60)


tim.color("black")
for _ in range(3):
    tim.left(118)
    for _ in range(6):
        tim.forward(200)
        tim.left(60)

tim.color("pink")
for _ in range(3):
    tim.left(118)
    for _ in range(6):
        tim.forward(200)
        tim.left(60)


S = Screen()
S.exitonclick()

