import turtle # Import the library that we are going to use

turtle.bgcolor('black') # Change background color to black
sizes = [4, 10, 5, 19, 20] # We will use these numbers to change circles size
colors= ['white', 'yellow', 'blue', 'orange', 'pink']

def drawCircles(turt, size, sub):
    for i in range(10):
        turt.circle(size)
        size-=sub

def drawSpecial(turt, size, repeat, sub):
    for i in range(repeat):
        drawCircles(turt, size, sub)
        turt.right(360/repeat)


myTurtle = turtle.Turtle()
myTurtle.speed(0) # Change drawing speed, 0 means the maximum speed

for i in range(5):
    myTurtle.color(colors[i]) # Change turtle color
    drawSpecial(myTurtle, 100, 10, sizes[i])


turtle.done() # To not close the window at the end
