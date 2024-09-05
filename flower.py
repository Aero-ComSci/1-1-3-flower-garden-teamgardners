import turtle
turtle.speed(2000)

def rose():
    def draw_flower():
        turtle.penup()
        turtle.left(90)
        turtle.fd(200)
        turtle.pendown()
        turtle.right(90)

    # Flower base
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(10, 180)
        turtle.circle(25, 110)
        turtle.left(50)
        turtle.circle(60, 45)
        turtle.circle(20, 170)
        turtle.right(24)
        turtle.fd(30)
        turtle.left(10)
        turtle.circle(30, 110)
        turtle.fd(20)
        turtle.left(40)
        turtle.circle(90, 70)
        turtle.circle(30, 150)
        turtle.right(30)
        turtle.fd(15)
        turtle.circle(80, 90)
        turtle.left(15)
        turtle.fd(45)
        turtle.right(165)
        turtle.fd(20)
        turtle.left(155)
        turtle.circle(150, 80)
        turtle.left(50)
        turtle.circle(150, 90)
        turtle.end_fill()

    # Petal 1
        turtle.left(150)
        turtle.circle(-90, 70)
        turtle.left(20)
        turtle.circle(75, 105)
        turtle.setheading(60)
        turtle.circle(80, 98)
        turtle.circle(-90, 40)

    # Petal 2
        turtle.left(180)
        turtle.circle(90, 40)
        turtle.circle(-80, 98)
        turtle.setheading(-83)

    # Leaves 1
        turtle.fd(30)
        turtle.left(90)
        turtle.fd(25)
        turtle.left(45)
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(-80, 90)
        turtle.right(90)
        turtle.circle(-80, 90)
        turtle.end_fill()
        turtle.right(135)
        turtle.fd(60)
        turtle.left(180)
        turtle.fd(85)
        turtle.left(90)
        turtle.fd(80)

    # Leaves 2
        turtle.right(90)
        turtle.right(45)
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(80, 90)
        turtle.left(90)
        turtle.circle(80, 90)
        turtle.end_fill()
        turtle.left(135)
        turtle.fd(60)
        turtle.left(180)
        turtle.fd(60)
        turtle.right(90)
        turtle.circle(200, 60)

        
# Call the function to draw the flower
        draw_flower()

def lily():

    def DrawFlower(radius,pedals):
     """
     Draws a flower using arcs of a circle with Turtle graphics.
    The length of the pedal is 0.5 * pi * radius. The second argument
    specifies the number of pedals to be drawn.
    """
    
    for p in range(pedals):
        pedals=0
        radius=0
        # Draws a flower pedal
        turtle.circle(radius,90)
        turtle.left(90)
        turtle.circle(radius,90)
        turtle.left(90)
        
        # Rotates the turtle 
        turtle.left(360/pedals)

        DrawFlower(100, 15)

def poppy():
    def draw_petal(turtle_obj, color, radius):
        turtle_obj.begin_fill()
        turtle_obj.color(color)
        turtle_obj.circle(radius, 60)  # Draw 60-degree arc for petal
        turtle_obj.left(120)
        turtle_obj.circle(radius, 60)  # Complete the petal shape
        turtle_obj.left(120)
        turtle_obj.end_fill()

    def draw_poppy():
        screen = turtle.Screen()
        # Create a turtle for drawing
        poppy_turtle = turtle.Turtle()
        poppy_turtle.speed(3)
        poppy_turtle.width(2)

        # Draw petals
        petal_colors = ["yellow"]
        petal_radius = 100
        num_petals = len(petal_colors)
    
        # Draw petals in a circular pattern
        for i in range(num_petals):
            draw_petal(poppy_turtle, petal_colors[i], petal_radius)
            poppy_turtle.right(360 / num_petals)  # Rotate to the next petal position
    
    # Draw the center of the poppy
        poppy_turtle.penup()
        poppy_turtle.goto(0, -20)
        poppy_turtle.pendown()
        poppy_turtle.color("black")
        poppy_turtle.begin_fill()
        poppy_turtle.circle(11)
        poppy_turtle.end_fill()
    
        # Hide the turtle and display the result
        poppy_turtle.hideturtle()
        screen.mainloop()

    # Run the function to draw the poppy flower
    draw_poppy()

def daisy():
    def draw_petal(turtle_obj, color, radius):
        turtle_obj.begin_fill()
        turtle_obj.color(color)
        turtle_obj.circle(radius, 60)  # Draw a 60-degree arc for part of the petal
        turtle_obj.left(120)
        turtle_obj.circle(radius, 60)  # Complete the petal shape
        turtle_obj.left(120)
        turtle_obj.end_fill()

    def draw_daisy():
        screen = turtle.Screen()
        screen.bgcolor("skyblue")  # Set the background color to sky blue

        # Create a turtle for drawing
        daisy_turtle = turtle.Turtle()
        daisy_turtle.speed(3)
        daisy_turtle.width(2)

        # Draw petals
        petal_color = "white"
        petal_radius = 100
        num_petals = 12
    
    # Draw petals in a circular pattern
        for _ in range(num_petals):
            draw_petal(daisy_turtle, petal_color, petal_radius)
            daisy_turtle.right(360 / num_petals)  # Rotate to the next petal position

        # Draw the center of the daisy
        daisy_turtle.penup()
        daisy_turtle.goto(0, -20)
        daisy_turtle.pendown()
        daisy_turtle.color("yellow")
        daisy_turtle.begin_fill()
        daisy_turtle.circle(30)
        daisy_turtle.end_fill()
    
        # Draw the stem
        daisy_turtle.penup()
        daisy_turtle.goto(0, -20)
        daisy_turtle.pendown()
        daisy_turtle.color("green")
        daisy_turtle.width(5)
        daisy_turtle.right(90)
        daisy_turtle.forward(200)

        # Hide the turtle and display the result
        daisy_turtle.hideturtle()
        screen.mainloop()

# Run the function to draw the daisy flower
    draw_daisy()

rose()

userinput = input("Write a Paragraph:")
flower = userinput.split(" ")
print(flower)
for i in flower: 
    if i == "rose":
        rose()
    elif i == "lily":
        print("lily")
    else:
        print("no flowers")


wn = turtle.Screen()
wn.mainloop()
