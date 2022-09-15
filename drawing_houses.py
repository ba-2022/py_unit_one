
import turtle

#this controls the speed of the turtle
turtle.speed(100)

#makes the square house
def makeASquare(side_length, Rcolor):
    turtle.color(Rcolor)
    turtle.begin_fill()
    #repeats the movement 4 times to create square
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

#makes the roof
def drawATriangle(side_length, Tcolor):
    turtle.color(Tcolor)
    turtle.begin_fill()
    #repeats the movement 2 times to create triangle
    for x in range(2):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()


drawATriangle(100, "red")

#moves the turtle to a certain point to align with the rest of the house
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

#makes the results stay unitl you click exit
turtle.exitonclick()


