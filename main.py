import turtle as t
import numpy as np

lengde_list = [1,5,1,5]
lengde_list = np.array(lengde_list)
lengde_list = lengde_list * 1
speed = 10000

tu = t.Turtle()
tu.color('green')
tu.speed(speed)
tu.left(0)
def drawShape(sides):
    for i in range(0,sides):
        tu.forward(1)
        tu.left(360/sides)
        if not i % (360/10):
            petal(i)
            print(i)
def rectangle():
    for lengde in lengde_list:
        tu.forward(lengde)
        tu.right(90)

def petal(current_angle):
    tu.begin_fill()
    tu.right(145)
    tu.circle(60,90)
    tu.left(90)
    tu.circle(60,90)
    tu.setheading(current_angle)
    tu.end_fill()
Start = -300
move = Start*-1
def draw(Start,move,y):
    for i in range(3):
        tu.penup()
        tu.goto(Start,y)
        tu.pendown()
        drawShape(360)
        Start += move

draw(Start,move,-300)
draw(Start,move, 0)
draw(Start,move, 300)

t.exitonclick()