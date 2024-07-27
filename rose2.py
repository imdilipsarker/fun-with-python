import turtle

def draw_rose():
    # Set initial position
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    # Rose flower base
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    # Petals
    turtle.fillcolor('pink')
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    for _ in range(10):
        turtle.left(36)
        turtle.begin_fill()
        turtle.circle(30, steps=3)
        turtle.left(120)
        turtle.circle(30, steps=3)
        turtle.end_fill()

    # Leaves
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.right(90)
    turtle.circle(80, 90)
    turtle.left(120)
    turtle.circle(80, 90)
    turtle.end_fill()

    turtle.hideturtle()

draw_rose()
turtle.done()
