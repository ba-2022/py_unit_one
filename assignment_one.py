# remember to use comments!
import turtle

turtle.speed(100)

def makeAOctagon(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(30)
        turtle.left(45)
        turtle.forward(30)
    turtle.end_fill()


makeAOctagon("red")




turtle.penup()
turtle.goto(-50,210)
turtle.pendown()

turtle.begin_fill()
makeAOctagon("blue")
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


turtle.exitonclick()
