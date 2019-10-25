import turtle

def draw_triangle(kinda_turtle):
    for i in range (1,4): #for loop
        kinda_turtle.left(120)
        kinda_turtle.forward(100)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")

    sue = turtle.Turtle()
    sue.shape ("turtle")
    sue.color("red", "purple")
    sue.speed(10)
    draw_triangle(sue)

    for i in  range (1,4):
        draw_triangle(sue)
        sue.left(120)
        sue.forward(100)
        sue.forward(100)











    window.exitonclick()
draw_art()