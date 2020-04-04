from turtle import Turtle
from random import randint
import turtle
import time
# WINDOW

window = turtle.Screen()
window.title('Turtle race')
turtle.bgcolor('purple')
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write('Turtle race',font=('Arial',30,'bold'))
turtle.penup()

#
turtle.setpos(-1200,-180)
turtle.color('red')
turtle.begin_fill()
turtle.pendown()
turtle.forward(3000)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(3000)
turtle.right(90)
turtle.forward(500)
turtle.end_fill()


# finish line

stamp_size=20
square_size=15
finish_line = 200
turtle.color('black')
turtle.shape('square')
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line,(150 - (i*square_size*2)))
    turtle.stamp()
turtle.hideturtle()


# turtles
t1 = Turtle()
t1.speed(0)
t1.color('blue')
t1.shape('turtle')
t1.penup()
t1.goto(-250,100)
t1.pendown()

# 2nd
t2 = Turtle()
t2.speed(0)
t2.color('green')
t2.shape('turtle')
t2.penup()
t2.goto(-250,50)
t2.pendown()


#3rd
t3 = Turtle()
t3.speed(0)
t3.color('orange')
t3.shape('turtle')
t3.penup()
t3.goto(-250,0)
t3.pendown()


#4th
t4 = Turtle()
t4.speed(0)
t4.color('red')
t4.shape('turtle')
t4.penup()
t4.goto(-250,-50)
t4.pendown()

time.sleep(1)

# start the race

for i in range(145):
    t1.forward(randint(1,5))
    t2.forward(randint(1, 5))
    t3.forward(randint(1, 5))
    t4.forward(randint(1, 5))

turtle.exitonclick()

turtle.Screen().mainloop()

turtle.done()
