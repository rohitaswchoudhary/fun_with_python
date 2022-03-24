# Python program to draw star
# using Turtle Package
import turtle
star = turtle.Turtle()
 
star.pencolor("red")
star.width(5)
star.right(85)
star.forward(200)     
 
for i in range(8):
    star.right(160)
    star.forward(200)

turtle.delay(10000)
turtle.exitonclick()