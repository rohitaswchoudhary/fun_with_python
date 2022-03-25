# Digital clock using python

import time
import datetime as dt
import turtle

# using two turtle to create this clock.
	
# create a turtle to display time
t = turtle.Turtle()

# create a turtle to create rectangle box
t1 = turtle.Turtle()

# create screen
src = turtle.Screen()

# set background color of the screen
src.bgcolor("light green")

# we are using system time to display time
# obtain current hour, minute and second
# from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(3)
t1.color('black')
t1.penup()

# set the position of turtle
t1.goto(-110, 0)
t1.pendown()

# create rectangular box
for i in range(2):
	t1.forward(300)
	t1.left(90)
	t1.forward(90)
	t1.left(90)
	
# hide the turtle
t1.hideturtle()

t.goto(-80,0)

# displaying time in 24 hour format
# running the while loop to display time while the screen is open
while True:
	t.hideturtle()
	t.clear()



	# display the time
	t.write(str(hr).zfill(2)
			+":"+str(min).zfill(2)+":"
			+str(sec).zfill(2),
			font =("Arial Narrow", 50, "bold"))
	time.sleep(1)
	sec+= 1
	
	if sec == 60:
		sec = 0
		min+= 1
	
	if min == 60:
		min = 0
		hr+= 1
	
	if hr == 13:
		hr = 1
