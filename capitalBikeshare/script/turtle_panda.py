import turtle
import math

# setup the screen
# (width=200, height=200, startx=0, starty=0)
turtle.setup(1000, 1800)
# the pen size
turtle.pensize(5)
# speed
turtle.speed(10)

# the pen always starts from the center by default. which is 0,0
# eye
def pandaeye(x,y,size=50,color='black',fill_color='white'):
	eye = turtle
	eye.penup()
	eye.goto(x,y)
	eye.pendown()
	eye.begin_fill()
	eye.pencolor(color)  # head side color
	eye.circle(size)
	eye.fillcolor(fill_color)  # face color
	eye.end_fill()
	eye.penup



def pandanose(x,y,color='black'):

	nose = turtle
	nose.pencolor(color)
	nose.penup()
	nose.goto(x,y)
	nose.pendown()
	nose.begin_fill()
	nose.forward(40)
	nose.right(120)
	nose.forward(80)
	nose.right(120)
	nose.forward(80)
	nose.right(120)
	nose.forward(40)
	nose.fillcolor('black')
	nose.end_fill()
	nose.penup()



# and mouth part

	arc_n = turtle
	arc_n.pencolor('black')
	arc_n.penup()
	arc_n.goto(x,y-60)
	arc_n.pendown()
	arc_n.right(90)
	arc_n.circle(50,180)
	arc_n.penup()

	arc_n.goto(0,y-60)

	arc_n.pendown()
	arc_n.right(180)
	arc_n.circle(-50,180)
	arc_n.penup()


pandaeye(-100,100, fill_color='black')
pandaeye(-100,100, 25, fill_color='white')
pandaeye(100,100, fill_color='black')
pandaeye(100,100, 25, fill_color='white')
pandanose(0,80)

# # head
chin_arc = turtle

left_x = -100
right_x = 100
mouth_y = -50
chin_arc.setheading(0)
chin_arc.pencolor('black')


# left side
chin_arc.penup()
chin_arc.goto(left_x,mouth_y)
chin_arc.pendown()
# turn 180 degree, which is turn to the opposite
chin_arc.left(180)
# radius positive, counterclockwise
chin_arc.circle(-120, 120)
chin_arc.setheading(0)
chin_arc.penup()
chin_arc.pendown()
# chin_arc.begin_fill()
chin_arc.left(90)
chin_arc.circle(-300,30)
chin_arc.penup()
# x,y position for ear
xL, yL = chin_arc.pos()

# ear part
chin_arc.backward(50)
chin_arc.left(120)
chin_arc.pendown()
chin_arc.begin_fill()
chin_arc.circle(-80, 270)
chin_arc.fillcolor('black')
chin_arc.end_fill()
chin_arc.penup()

# head
chin_arc.setheading(0)
chin_arc.goto(xL,yL)
chin_arc.left(40)
chin_arc.pendown()
chin_arc.circle(-255,40)

############
# right side

chin_arc.penup()
chin_arc.setheading(0)
chin_arc.goto(right_x,mouth_y)
chin_arc.pendown()
# chin_arc.right(45)
chin_arc.circle(120, 120)
chin_arc.penup()

chin_arc.setheading(0)

chin_arc.pendown()
chin_arc.left(90)
chin_arc.circle(300,30)
chin_arc.penup()
# x,y position for ear
xR, yR = chin_arc.pos()

# ear part
chin_arc.backward(50)
chin_arc.right(120)
chin_arc.pendown()
chin_arc.begin_fill()
chin_arc.circle(80, 270)
chin_arc.fillcolor('black')
chin_arc.end_fill()
chin_arc.penup()

# head
chin_arc.setheading(0)
chin_arc.goto(xR,yR)
chin_arc.left(140)
chin_arc.pendown()
chin_arc.circle(255,40)
chin_arc.penup()

# lower jaw
chin_arc.setheading(0)
chin_arc.goto(right_x, mouth_y)
chin_arc.pendown()
chin_arc.right(150)
chin_arc.circle(left_x*2, 60)
chin_arc.penup()


chin_arc.goto(-100,-170)

chin_arc.write("grades don't matter", font=("Arial", 32, "normal"))

chin_arc.goto(100,-210)
chin_arc.write("--- Wieland", font=("Arial", 32, "normal"))


turtle.done()










