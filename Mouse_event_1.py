# Mouse event handlers require 2 parameters to receive x, y
# coordinate info telling us where the mouse was when the event occurred.

import turtle

wn = turtle.Screen()
wn.title("Mouse events.")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")
tess.pensize(2)
tess.speed(10)


def h1(x, y):
    """makes tess move from position x to y"""

    wn.title('Got click at coords {0}, {1}'.format(x, y))
    tess.goto(x, y)


def h2():
    tess.penup()


def h3():
    tess.pendown()


wn.onkey(h2, 'a')
wn.onkey(h3, 'b')


wn.listen()
wn.onclick(h1)  # wire up a click on the window.
wn.mainloop()
