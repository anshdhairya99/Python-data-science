from turtle import *

# define a function
def hexagon():
    for i in range(4):
        fd(100)
        lt(360/6)
#calling the function
hexagon()
penup()
goto(100,100)
pendown()
hexagon()
penup()
goto(-100,100)
pendown()
hexagon()
penup()
goto(-100,-100)
pendown()
hexagon()
penup()
goto(100,-100)
pendown()
hexagon()
penup()
hideturtle()
mainloop()
 