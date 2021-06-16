import turtle # Import the library that we are going to use

ourTurtle = turtle.Turtle() # Create an object called 'ourTurtle'
turtle.bgcolor('black') # Change background colour to black
ourTurtle.pencolor('red') # Change drawing colour to red


ourTurtle.speed(0) # Change drawing speed, 0 means the maximum speed
ourTurtle.penup() # Stop drawing while moving
ourTurtle.goto(0,200) # Go to the point 0 (intersection between the x and y axis) and go up by 200
ourTurtle.pendown() # Start drawing again while moving


forwDistance = 0
directionRight = 0
while(True):
    ourTurtle.forward(forwDistance)
    ourTurtle.right(directionRight)
    forwDistance += 3
    directionRight += 1
    if directionRight == 210:
        break # Stop the loop
    ourTurtle.hideturtle() # To hide the arrow that draws

turtle.done() # To not close the window at the end