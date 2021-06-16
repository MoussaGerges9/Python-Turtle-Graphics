import turtle # Import the library that we are going to use

colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']

turtle.bgcolor('black') # Change background colour to black
turtle.speed(0) #Change drawing speed, 0 means the maximum speed


for i in range(360):
    turtle.pencolor(colors[i%6]) # Choose a colour from the array
    turtle.width(i/100 +1)
    turtle.forward(i)
    turtle.left(59)


turtle.done() # To not close the window at the end
