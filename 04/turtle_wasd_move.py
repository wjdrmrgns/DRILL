import turtle

def move_w_turtle():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
    
def move_a_turtle():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
    
def move_s_turtle():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
    
def move_d_turtle():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(move_w_turtle, 'w')
turtle.onkey(move_a_turtle, 'a')
turtle.onkey(move_s_turtle, 's')
turtle.onkey(move_d_turtle, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
    
