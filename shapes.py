import turtle

def draw_square(brad):
    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)

def draw_art():  
    
    
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    for i in range(0, 24):
        draw_square(brad)
        brad.right(15)

    


window = turtle.Screen()
window.bgcolor("red")

draw_art()

window.exitonclick()