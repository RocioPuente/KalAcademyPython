import turtle


turtle.goto(0, 0)
for i in range (3):
    turtle.fd(100); turtle.rt(120)

turtle.penup()

turtle.goto(100, -174)
turtle.pendown()
for i in range (3):
    turtle.lt(120); turtle.fd(100)
