# while Loops:--
from turtle import *

speed('fastest')
pencolor('Blue')
bgcolor('#303030')
pensize(3)

i = 200
while i > 0:
    fd(i)
    lt(180)
    i -=4
    dot(10,'red')
    write(i, font=('Calibri', 14, 'bold'))


    mainloop()