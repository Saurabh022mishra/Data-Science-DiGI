from turtle import *


def polygon(side, dis):
    for i in range(side):
        fd(dis)
        lt(360/side)

polygon(3, 100)

polygon(4, 100)
for i in range(5, 11):
    polygon(i, 100)
hideturtle()
mainloop()
