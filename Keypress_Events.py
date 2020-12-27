import turtle

# screen and turtle.

screen = turtle.Screen()
screen.title('Handling Keypresses!')
screen.bgcolor('lightblue')
tess = turtle.Turtle()
tess.color('red')
tess.pensize(2)
tess.speed(6)



# The next 4 functions are our 'event handlers'.


def h1():
    tess.forward(50)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    tess.penup()


def h5():
    tess.pendown()


def h6():
    screen.bye()  # close down the turtle window


# These lines 'wire up' keypresses to the handlers we've defined.

screen.onkey(h1, 'Up')
screen.onkey(h2, 'Left')
screen.onkey(h3, 'Right')
screen.onkey(h4, 'a')
screen.onkey(h5, 'b')
screen.onkey(h6, 'x')

# Now we need to tell the window to start listening for events,
# If any of the keys that we’re monitoring is pressed,
# handler will be called.

screen.listen()   # makes the windows notice the keypresses
screen.mainloop()
