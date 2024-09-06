import turtle

ninjaTurtle = turtle.Turtle()
def daisy():
    ninjaTurtle. fillcolor()       
    ninjaTurtle.begin_fill()
    ninjaTurtle.penup()
    ninjaTurtle.goto(-200,200)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(15)
    ninjaTurtle.end_fill()

    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.penup()
    ninjaTurtle.goto(-170,190)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()

    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.goto(-170,230)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)  
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()

    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.goto(-198,245)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()

    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.goto(-225,230)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()

    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.goto(-230,200)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()
    
    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.goto(-220,178)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()

    ninjaTurtle.fillcolor("#ffbddf")
    ninjaTurtle.begin_fill()
    ninjaTurtle.goto(-193,175)
    ninjaTurtle.pendown()
    ninjaTurtle.circle(9)
    ninjaTurtle.penup()
    ninjaTurtle.end_fill()



def sunflower():


    ninjaTurtle.color("yellow")


    def draw_petal():
        ninjaTurtle.circle(100, 60)
        ninjaTurtle.left(120)
        ninjaTurtle.circle(100, 60)
        ninjaTurtle.left(120)


    ninjaTurtle.penup()
    ninjaTurtle.goto(0, -100)
    ninjaTurtle.pendown()
    ninjaTurtle.begin_fill()
    for _ in range(6):
        draw_petal()
        ninjaTurtle.right(60)
    ninjaTurtle.end_fill()


    ninjaTurtle.color("orange")
    ninjaTurtle.penup()
    ninjaTurtle.goto(0, -120)
    ninjaTurtle.pendown()
    ninjaTurtle.begin_fill()
    ninjaTurtle.circle(20)
    ninjaTurtle.end_fill()

   
def poppy():

    ninjaTurtle.speed(10)
    ninjaTurtle.color("red")


    def draw_petal():
        ninjaTurtle.circle(100, 60)
        ninjaTurtle.left(120)
        ninjaTurtle.circle(100, 60)
        ninjaTurtle.left(120)


    ninjaTurtle.penup()
    ninjaTurtle.goto(0, -100)
    ninjaTurtle.pendown()
    ninjaTurtle.begin_fill()
    for _ in range(7):
        draw_petal()
        ninjaTurtle.right(50)
    ninjaTurtle.end_fill()



    ninjaTurtle.color("yellow")
    ninjaTurtle.penup()
    ninjaTurtle.goto(0, -120)
    ninjaTurtle.pendown()
    ninjaTurtle.begin_fill()
    ninjaTurtle.circle(20)
    ninjaTurtle.end_fill()


person = input("Write a paragraph with flower names (e.g., 'rose', 'lily'): ")
flower_list = person.split()

for flower in flower_list:
    if flower == "sunflower":
        sunflower()
    elif flower == "daisy":
        daisy()
    
    elif flower == "poppy":
        poppy()

    else:
        print(f"No function to draw {flower}")
wn = turtle.Screen()
wn.mainloop()
