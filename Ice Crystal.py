import turtle # Import the library that we are going to use

ourTurtle = turtle.Turtle() # Create an object called 'ourTurtle'
colors=["red", "orange", "pink"]

# Move the starting point to centre the design #
ourTurtle.penup() # Stop drawing while moving
ourTurtle.setpos(-100, -50) # move back by 100 pixels and down by 50 pixels
ourTurtle.pendown() # Start drawing while moving

ourTurtle.speed(0) # Change drawing speed, 0 means the maximum speed


def designOneside(length,n):
    if n == 0:
        ourTurtle.forward(length)
    
    else:
        length /= 3
        n -= 1
        designOneside(length, n)
        ourTurtle.right(60)
        designOneside(length, n)
        ourTurtle.left(120)
        designOneside(length, n)
        ourTurtle.right(60)
        designOneside(length, n)


for side in range(3):
    ourTurtle.color(colors[side])  # Choose a colour of the side from the array
    designOneside(200, 3)
    ourTurtle.left(120)


turtle.done() # To not close the window at the end