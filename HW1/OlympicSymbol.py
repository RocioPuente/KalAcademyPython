import turtle

turtle.pensize (5)

def drawCircle(color, x, y=-25):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(45)


drawCircle ("blue", -110)
drawCircle ("black", 0)
drawCircle("red", 110)
drawCircle("yellow", -55, -75)
drawCircle("green", 55, -75)
