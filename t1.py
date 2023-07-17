# Turtle program
from turtle import *
speed('slowest')
pencolor('red')
pensize(3)
#speed('fast')
pencolor('red')
# range(stop)
# range(start,stop)
# range(start,stop,step)
for m in range(6):
 for m in range(6,16,5):
    fd(120)
    lt(360/6)
    dot(10,'green')
    write(m,font=('Calibri',20,'bold'))
    # reverse
    goto(100,100)
    for i in range(10,0,-1):
       fd(60)
       lt(360/10)
    dot(20,'red')
    write(i,font=('Calibri',20,'bold'))

"""fd(100)
rt(72)
fd(100)
rt(72)
fd(100)
rt(72)
fd(100)
rt(72)"""

"""fd(100)
rt(120)
fd(100)
rt(120)
fd(120)
rt(120)"""
"""fd(100)
rt(90)
fd(100)
rt(90)"""
"""fd(100)
rt(90)
fd(100)
rt(90)
fd(100)
rt(90)
fd(100)
rt(90)"""
mainloop()