import turtle

def drawATriangle(side_length, Tcolor):
    turtle.color(Tcolor)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(side_length)
        turtle.left(45)
    turtle.end_fill()

drawATriangle(100, "red")

turtle.penup()
turtle.forward(200)
turtle.pendown()

def makeASquare(side_length, Rcolor):
    turtle.color(Rcolor)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

makeASquare(100,"blue")

turtle.penup()
turtle.goto(-40,170)
turtle.forward(100)
turtle.pendown()



turtle.exitonclick()















