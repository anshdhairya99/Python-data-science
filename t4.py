# Turtle program
from turtle import *
speed('fastest')
pensize(2)
bgcolor('black') 
pencolor('white')
colors =['red','yellow','blue','green','orange','purple']
side = 6
for i in range(side):
    fd(200)
    lt(360/side)
    begin_fill()
    fillcolor(color[i%6])
    for i in range(side):
        fd(50)
        lt(360/side)
        end_fill()
        lt(360/side)
mainloop()