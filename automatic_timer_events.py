# alarm clocks are set to create an automatic event after a certain interval.
# Python has a timer that can cause an event when its time is up.

import turtle

wn = turtle.Screen()
wn.title('automatic events')
wn.bgcolor('light blue')

tess = turtle.Turtle()
tess.pensize(2)
tess.speed(10)
tess.color('red')

alex = turtle.Turtle()
alex.pensize(2)
alex.speed(10)
alex.color('blue')
alex.penup()
alex.forward(300)
alex.pendown()

alex2 = turtle.Turtle()
alex2.pensize(2)
alex2.speed(10)
alex2.color('black')
alex2.penup()
alex2.forward(-300)
alex2.pendown()


def h1():
    tess.forward(150)
    tess.left(56)
    wn.ontimer(h1, 100)


def h2():
    alex.forward(150)
    alex.left(56)
    wn.ontimer(h2, 100)


def h3():
    alex2.forward(150)
    alex2.left(56)
    wn.ontimer(h3, 100)


h2()
h1()
h3()
wn.mainloop()

