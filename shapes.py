import turtle

def draw_square(some_turtle):

    for i in range (1,5): # for loop
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(kinda_turtle):
    for i in range (1,4): #for loop
        kinda_turtle.left(120)
        kinda_turtle.forward(100)
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")

    # create the turtle brad - Draws a square

    brad = turtle.Turtle()
    brad.shape ("turtle")
    brad.color("green", "purple")
    brad.speed(2)
    draw_square(brad)

    # create the turtle tom - Draws a circle
    
    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.color("brown", "black")
    tom.speed(2)
    tom.circle(100)

    # create the turtle sue - Draws a triangle

    sue = turtle.Turtle()
    sue.shape ("turtle")
    sue.color("red", "purple")
    sue.speed(2)
    draw_triangle(sue)

    window.exitonclick()
draw_art()






# start-up code (unsimplified)

# def draw_square():
#     window = turtle.Screen()
#     window.bgcolor("yellow")

#     brad = turtle.Turtle()
#     brad.shape("turtle")
#     brad.color("white", "purple")
#     brad.speed(2)

#     brad.forward(100) #Forward brad by 100 units
#     brad.right(90) #Turn brad by 90 degree
#     brad.forward(100) 
#     brad.right(90)
#     brad.forward(100) 
#     brad.right(90)
#     brad.forward(100) 
#     brad.right(90)
#     brad.forward(100)

#     tom = turtle.Turtle()
#     tom.shape("arrow")
#     tom.color("brown", "purple")
#     tom.speed(2)
#     tom.circle(100)


#     window.exitonclick()

#draw_square()



