# remember to use comments!
import turtle

turtle.speed(100)

#this makes an octagon
def makeAOctagon(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(30)
        turtle.left(45)
        turtle.forward(30)
    turtle.end_fill()

makeAOctagon("red")

#this makes sure the pen isn't drawing
turtle.penup()
#this moves the pen to a location
turtle.goto(-50,210)
#this lets the pen start drawing
turtle.pendown()

#makes the pen fill the shape
turtle.begin_fill()
makeAOctagon("blue")
#stops the filling of the shape
turtle.end_fill()

turtle.penup()
turtle.goto(120,100)
turtle.pendown()

turtle.begin_fill()
makeAOctagon("pink")
turtle.end_fill()

turtle.penup()
turtle.goto(-140,-150)
turtle.pendown()

turtle.begin_fill()
makeAOctagon("green")
turtle.end_fill()

#lets the results stay until you click exit
turtle.exitonclick()
