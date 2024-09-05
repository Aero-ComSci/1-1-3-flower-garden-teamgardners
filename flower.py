import turtle

ninjaTurtle = turtle.Turtle()

def draw_rect():
    ninjaTurtle.forward(100)
    ninjaTurtle.right(90)
    ninjaTurtle.forward(100)
    ninjaTurtle.right(90)


def rose():
        ninjaTurtle.penup()
        ninjaTurtle.left(90)
        ninjaTurtle.fd(200)
        ninjaTurtle.pendown()
        ninjaTurtle.right(90)

    # Flower base
        ninjaTurtle.fillcolor("red")
        ninjaTurtle.begin_fill()
        ninjaTurtle.circle(10, 180)
        ninjaTurtle.circle(25, 110)
        ninjaTurtle.left(50)
        ninjaTurtle.circle(60, 45)
        ninjaTurtle.circle(20, 170)
        ninjaTurtle.right(24)
        ninjaTurtle.fd(30)
        ninjaTurtle.left(10)
        ninjaTurtle.circle(30, 110)
        ninjaTurtle.fd(20)
        ninjaTurtle.left(40)
        ninjaTurtle.circle(90, 70)
        ninjaTurtle.circle(30, 150)
        ninjaTurtle.right(30)
        ninjaTurtle.fd(15)
        ninjaTurtle.circle(80, 90)
        ninjaTurtle.left(15)
        ninjaTurtle.fd(45)
        ninjaTurtle.right(165)
        ninjaTurtle.fd(20)
        ninjaTurtle.left(155)
        ninjaTurtle.circle(150, 80)
        ninjaTurtle.left(50)
        ninjaTurtle.circle(150, 90)
        ninjaTurtle.end_fill()

    # Petal 1
        ninjaTurtle.left(150)
        ninjaTurtle.circle(-90, 70)
        ninjaTurtle.left(20)
        ninjaTurtle.circle(75, 105)
        ninjaTurtle.setheading(60)
        ninjaTurtle.circle(80, 98)
        ninjaTurtle.circle(-90, 40)

    # Petal 2
        ninjaTurtle.left(180)
        ninjaTurtle.circle(90, 40)
        ninjaTurtle.circle(-80, 98)
        ninjaTurtle.setheading(-83)

    # Leaves 1
        ninjaTurtle.fd(30)
        ninjaTurtle.left(90)
        ninjaTurtle.fd(25)
        ninjaTurtle.left(45)
        ninjaTurtle.fillcolor("green")
        ninjaTurtle.begin_fill()
        ninjaTurtle.circle(-80, 90)
        ninjaTurtle.right(90)
        ninjaTurtle.circle(-80, 90)
        ninjaTurtle.end_fill()
        ninjaTurtle.right(135)
        ninjaTurtle.fd(60)
        ninjaTurtle.left(180)
        ninjaTurtle.fd(85)
        ninjaTurtle.left(90)
        ninjaTurtle.fd(80)

    # Leaves 2
        ninjaTurtle.right(90)
        ninjaTurtle.right(45)
        ninjaTurtle.fillcolor("green")
        ninjaTurtle.begin_fill()
        ninjaTurtle.circle(80, 90)
        ninjaTurtle.left(90)
        ninjaTurtle.circle(80, 90)
        ninjaTurtle.end_fill()
        ninjaTurtle.left(135)
        ninjaTurtle.fd(60)
        ninjaTurtle.left(180)
        ninjaTurtle.fd(60)
        ninjaTurtle.right(90)
        ninjaTurtle.circle(200, 60)

        
# Call the function to draw the flower

def lily():
    radius= 11
    pedals=6
    """
    Draws a flower using arcs of a circle with ninjaTurtle graphics.
The length of the pedal is 0.5 * pi * radius. The second argument
specifies the number of pedals to be drawn.
"""
    
    for p in range(pedals):
        pedals=0
        radius=0
        # Draws a flower pedal
        ninjaTurtle.circle(radius,90)
        ninjaTurtle.left(90)
        ninjaTurtle.circle(radius,90)
        ninjaTurtle.left(90)
        
        # Rotates the ninjaTurtle 
        ninjaTurtle.left(360/pedals)


def poppy():
    def draw_petal(ninjaTurtle_obj, color, radius):
        ninjaTurtle_obj.begin_fill()
        ninjaTurtle_obj.color(color)
        ninjaTurtle_obj.circle(radius, 60)  # Draw 60-degree arc for petal
        ninjaTurtle_obj.left(120)
        ninjaTurtle_obj.circle(radius, 60)  # Complete the petal shape
        ninjaTurtle_obj.left(120)
        ninjaTurtle_obj.end_fill()

    def draw_poppy():
        screen = ninjaTurtle.Screen()
        # Create a ninjaTurtle for drawing
        poppy_ninjaTurtle = ninjaTurtle.ninjaTurtle()
        poppy_ninjaTurtle.speed(3)
        poppy_ninjaTurtle.width(2)

        # Draw petals
        petal_colors = ["yellow"]
        petal_radius = 100
        num_petals = len(petal_colors)
    
        # Draw petals in a circular pattern
        for i in range(num_petals):
            draw_petal(poppy_ninjaTurtle, petal_colors[i], petal_radius)
            poppy_ninjaTurtle.right(360 / num_petals)  # Rotate to the next petal position
    
    # Draw the center of the poppy
        poppy_ninjaTurtle.penup()
        poppy_ninjaTurtle.goto(0, -20)
        poppy_ninjaTurtle.pendown()
        poppy_ninjaTurtle.color("black")
        poppy_ninjaTurtle.begin_fill()
        poppy_ninjaTurtle.circle(11)
        poppy_ninjaTurtle.end_fill()
    
        # Hide the ninjaTurtle and display the result
        poppy_ninjaTurtle.hideninjaTurtle()
        screen.mainloop()

    # Run the function to draw the poppy flower
    draw_poppy()

def daisy():
    def draw_petal(ninjaTurtle_obj, color, radius):
        ninjaTurtle_obj.begin_fill()
        ninjaTurtle_obj.color(color)
        ninjaTurtle_obj.circle(radius, 60)  # Draw a 60-degree arc for part of the petal
        ninjaTurtle_obj.left(120)
        ninjaTurtle_obj.circle(radius, 60)  # Complete the petal shape
        ninjaTurtle_obj.left(120)
        ninjaTurtle_obj.end_fill()

    def draw_daisy():
        screen = ninjaTurtle.Screen()
        screen.bgcolor("skyblue")  # Set the background color to sky blue

        # Create a ninjaTurtle for drawing
        daisy_ninjaTurtle = ninjaTurtle.ninjaTurtle()
        daisy_ninjaTurtle.speed(3)
        daisy_ninjaTurtle.width(2)

        # Draw petals
        petal_color = "white"
        petal_radius = 100
        num_petals = 12
    
    # Draw petals in a circular pattern
        for _ in range(num_petals):
            draw_petal(daisy_ninjaTurtle, petal_color, petal_radius)
            daisy_ninjaTurtle.right(360 / num_petals)  # Rotate to the next petal position

        # Draw the center of the daisy
        daisy_ninjaTurtle.penup()
        daisy_ninjaTurtle.goto(0, -20)
        daisy_ninjaTurtle.pendown()
        daisy_ninjaTurtle.color("yellow")
        daisy_ninjaTurtle.begin_fill()
        daisy_ninjaTurtle.circle(30)
        daisy_ninjaTurtle.end_fill()
    
        # Draw the stem
        daisy_ninjaTurtle.penup()
        daisy_ninjaTurtle.goto(0, -20)
        daisy_ninjaTurtle.pendown()
        daisy_ninjaTurtle.color("green")
        daisy_ninjaTurtle.width(5)
        daisy_ninjaTurtle.right(90)
        daisy_ninjaTurtle.forward(200)

        # Hide the ninjaTurtle and display the result
        daisy_ninjaTurtle.hideninjaTurtle()
        screen.mainloop()

# Run the function to draw the daisy flower
    #draw_daisy()

rose()
lily()
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