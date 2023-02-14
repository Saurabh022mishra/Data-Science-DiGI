from turtle import *
pencolor('black')
fillcolor('yellow')
pensize(5)
side = 6
for i in range(side):
    fd(200)
    begin_fill()
    for j in range(side):
        fd(100)
        left(360/side)
        dot(20)
    end_fill()
    lt(360/side)
hideturtle()
mainloop()
