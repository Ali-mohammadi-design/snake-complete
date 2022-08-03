from turtle import Screen, Turtle
import time
from Snake import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# screen.tracer(0) turns of the automatic update of the screen
x = 0
# timy_list = []
# position = []
# for t in range(3):
#     timy = Turtle()
#     timy.penup()
#     timy_list.append(timy)
#     timy.shape("square")
#     timy.color("white")
#     timy.goto(x, 0)
#     x = x - 20
#     print(timy.position())
#     position.append(timy.position())
d=Snake()
global list
list=d.create(12)

def up():
 d.up(list)
def down():
 d.down(list)
def left():
 d.left(list)
def right():
 d.right(list)

screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
print(list[0].position())
screen.update()

# screen.update() would update the screen right away
# time.sleep(x) would create a delay for the program for x seceonds
# = True
v = 1
position1 = [0, 0, 0]
for d1 in range(100):
 print(list[0].heading())
 d.move(list)
    # position1[0] = timy_list[0].position()
    # timy_list[0].forward(20)
    # timy_list[0].left(90)
    # screen.listen()
    #
    # for a in range(1, 3):
    #     position1[a] = timy_list[a].position()
    #     timy_list[a].goto(position1[a - 1])
    #     print(timy_list[a].position())

 time.sleep(0.5)
 screen.update()

screen.exitonclick()


