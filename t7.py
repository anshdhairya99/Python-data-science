# Turtle program of making a flower :----

"""import turtle as tur
import colorsys as cs 
tur.setup(800,800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
        tur.hideturtle()
        tur.done()"""


# Python program to draw square
# using Turtle Programming

"""import turtle
skk = turtle.Turtle()

for i in range(4):
	skk.forward(50)
	skk.right(90)
	
turtle.done()"""

# Python program to draw star
# using Turtle Programming

"""import turtle
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
	star.right(144)
	star.forward(100)
	
turtle.done()"""

# Python program to draw hexagon
# using Turtle Programming

"""import turtle
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
	polygon.forward(side_length)
	polygon.right(angle)
	
turtle.done()"""

# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming

"""import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

turtle.exitonclick()"""





