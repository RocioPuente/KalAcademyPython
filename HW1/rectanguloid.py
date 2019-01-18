import turtle

def draw_rectanguloid():
    for rec in range (1):
        turtle.goto(0,0)
        for i in range (2):
            turtle.fd(200)
            turtle.left(90)
            turtle.fd(80)
            turtle.lt(90)
        turtle.goto(50,50)
        for i in range (2):
            turtle.fd(200)
            turtle.left(90)
            turtle.fd(80)
            turtle.lt(90)
        turtle.penup()
        turtle.goto(0,80)
        turtle.pendown()
        turtle.goto(50,130)
        
        turtle.penup()
        turtle.goto(200,80)
        turtle.pendown()
        turtle.goto(250,130)

        turtle.penup()
        turtle.goto(200,0)
        turtle.pendown()
        turtle.goto(250,50)
        
draw_rectanguloid ()
