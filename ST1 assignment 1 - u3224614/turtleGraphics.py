    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 22/09/2021                                                                                         ###
    ### Date Last Changed: 22/09/2021                                                                                    ###
    ### A simple program to... answer question 5 I guess? And also draw a stop sign using the turtle lib                 ###
    ########################################################################################################################
    ########################################################################################################################


from turtle import Turtle, Screen
screen = Screen()
turtle = Turtle()


def drawHexagon():
    turtle.fillcolor("red") 
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(200)
        turtle.left(60)
    turtle.end_fill()
    turtle.hideturtle()
    print(turtle.fillcolor())


def writeStop():
    turtle.penup()
    turtle.right(240)
    turtle.forward(115)
    turtle.right(100)
    turtle.forward(35)
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write("STOP", font=("Comic Sans", 70, "normal"))


def main():
    drawHexagon()
    writeStop()    
    screen.exitonclick()
    
main()