import turtle

wn = turtle.Screen() # Get a reference to the window
wn.title("Handling mouse clicks!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")
tess.speed(10)
tess.pensize(3)

alex = turtle.Turtle()
alex.forward(200)
alex.speed(10)
alex.pensize(3)


def handler_for_tess(x, y):
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(50)


def handler_for_alex(x, y):
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    alex.right(184)
    alex.forward(60)


tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)
wn.mainloop()
