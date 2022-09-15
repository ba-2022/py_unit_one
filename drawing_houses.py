
import turtle

turtle.speed(100)
def makeASquare(side_length, Rcolor):
    turtle.color(Rcolor)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.end_fill()

turtle.penup()
turtle.goto(20,-20)

makeASquare(100,"blue")

turtle.forward(100)
turtle.pendown()

turtle.goto(20,80)
def drawATriangle(side_length, Tcolor):
    turtle.color(Tcolor)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()


drawATriangle(100, "red")




turtle.penup()
turtle.goto(20,-20)
turtle.forward(100)
turtle.left(120)
turtle.goto(-180,-20)


makeASquare(150, "purple")
turtle.forward(100)
turtle.pendown

turtle.goto(-180,130)
drawATriangle(150, "yellow")


turtle.penup()
turtle.goto(20,-20)
turtle.forward(100)
turtle.left(120)
turtle.goto(-230,-20)


makeASquare(30, "green")
turtle.forward(100)
turtle.pendown

turtle.goto(-230,10)
drawATriangle(30,"black")

turtle.penup()
turtle.goto(20,-20)
turtle.forward(100)
turtle.left(120)
turtle.goto(-300,-20)


makeASquare(50, "orange")
turtle.forward(100)
turtle.pendown

turtle.goto(-300,30)
drawATriangle(50, "orange")




turtle.exitonclick()


