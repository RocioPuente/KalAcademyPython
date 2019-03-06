import turtle
turtle.speed(0)

def square(size, alternate, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(size)

def row_square (size, alternate, color1, color2):
    for i in range (4):
        if (alternate ==True):
            square(size, alternate, color1)
            square(size, alternate, color2)
        else:
            square(size, alternate, color2)
            square(size, alternate, color1)

def chessboard(size, alternate, color1, color2):
    for i in range(8):
        row_square(size, alternate, color1, color2)
        turtle.bk(size*8)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        if(alternate==True):
            alternate=False
        else:
            alternate=True
    turtle.goto(-80,80)
    turtle.pencolor('black')
    turtle.pendown()
    for i in range (4):
        turtle.forward(size*8)
        turtle.left(90)

chessboard(50, True, black, white)
