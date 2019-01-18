import turtle

turtle.pensize (2)

def drawCircle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)

drawCircle(0, 0)
drawCircle(100, 0)
drawCircle(100,-100)
drawCircle(0,-100)
