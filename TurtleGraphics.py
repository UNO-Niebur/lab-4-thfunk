#TurtleGraphics.py
#Name: Taran Funk
#Date: 2/15/2026
#Assignment: Lab 4 Turtles all the way down

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)
        
def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    x = ((corner-1) % 2)*50
    if corner > 2:
        y = -50
    else: y = 0
    myTurtle.penup()
    myTurtle.goto(x,y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)
    myTurtle.end_fill()
    
def squaresInSquares(myTurtle, num):
    for i in range(num):
        x= -(i+1)*10
        y= (i+1)*10
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        drawSquare(myTurtle, 20*(i+1))

def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()