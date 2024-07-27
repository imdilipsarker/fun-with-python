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
    draw_rectangle(cake, 300, 50, "brown")
    
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