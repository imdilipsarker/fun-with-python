import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Happy Birthday to you!")
screen.bgcolor("black")

# Create the turtle for drawing the cake
cake = turtle.Turtle()
cake.speed(3)

def draw_rectangle(turtle, width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_cake():
    # Bottom layer
    cake.penup()
    cake.goto(-150, -200)
    cake.pendown()
    draw_rectangle(cake, 300, 50, "white")
    
    # Second layer
    cake.penup()
    cake.goto(-125, -150)
    cake.pendown()
    draw_rectangle(cake, 250, 50, "deeppink")
    
    # Third layer
    cake.penup()
    cake.goto(-100, -100)
    cake.pendown()
    draw_rectangle(cake, 200, 50, "hotpink")
    
    # Top layer
    cake.penup()
    cake.goto(-75, -50)
    cake.pendown()
    draw_rectangle(cake, 150, 50, "pink")

def draw_candles():
    candle_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta"]
    
    for i in range(9):
        cake.penup()
        cake.goto(-65 + i*15, 0)
        cake.pendown()
        cake.color(candle_colors[i])
        cake.begin_fill()
        for _ in range(2):
            cake.forward(10)
            cake.left(90)
            cake.forward(30)
            cake.left(90)
        cake.end_fill()
        
        # Draw the flame
        cake.penup()
        cake.goto(-60 + i*15, 30)
        cake.pendown()
        cake.color("orange")
        cake.begin_fill()
        cake.circle(5)
        cake.end_fill()

def draw_fireworks():
    fireworks = turtle.Turtle()
    fireworks.speed(5)
    fireworks.color("white")  
    
    def draw_firework(turtle, radius):
        for _ in range(36):
            turtle.forward(radius)
            turtle.backward(radius)
            turtle.right(10)
    
    positions = [(-200, 150), (200, 150)]
    for pos in positions:
        fireworks.penup()
        fireworks.goto(pos)
        fireworks.pendown()
        draw_firework(fireworks, 50)
    
    fireworks.hideturtle()

def draw_balloon(x, y, color):
    balloon = turtle.Turtle()
    balloon.speed(1)
    balloon.color(color)
    balloon.penup()
    balloon.goto(x, y)
    balloon.pendown()
    balloon.begin_fill()
    balloon.circle(20)
    balloon.end_fill()
    
    # Draw the string
    balloon.right(90)
    balloon.forward(50)
    balloon.hideturtle()

def draw_balloons():
    colors = ["red", "blue", "yellow", "green", "purple"]
    positions = [(-100, 100), (-50, 120), (0, 140), (50, 120), (100, 100)]
    for i in range(5):
        draw_balloon(positions[i][0], positions[i][1], colors[i])

def write_text():
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(0, 195)
    writer.color("lightyellow")
    writer.hideturtle()
    writer.write("Happy Birthday!", align="center", font=("Arial", 16, "bold"))

# Draw the cake, candles, decorations, balloons, and text
draw_cake()
draw_candles()
draw_fireworks()
draw_balloons()
write_text()

# Hide the main turtle
cake.hideturtle()

# Keep the window open
turtle.done()
