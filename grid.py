import turtle

count = 5
while (count >= 0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0,count * 100)
    turtle.pendown()
    count -= 1

count = 5
turtle.left(90)

while (count >= 0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(count * 100,0)
    turtle.pendown()
    count -= 1
    
turtle.exitonclick()
