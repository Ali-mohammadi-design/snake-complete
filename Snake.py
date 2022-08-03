from turtle import Turtle,Screen
class Snake():
    from turtle import Turtle
    def __init__(self):
        self.s=0
        self.position=0



    def create(self,number):

        x=0
        timy_list = []
        for t in range(number):
            self = Turtle()
            self.penup()
            timy_list.append(self)
            self.shape("square")
            self.color("white")
            self.goto(x, 0)
            x = x - 20
            print(self.position())


        return timy_list

    def up(self,list):
        if list[0].heading() !=270:
          list[0].setheading(90)
    def down(self,list):
        if list[0].heading() !=90:
          list[0].setheading(270)
    def left(self,list):
        if list[0].heading() !=0:
          list[0].setheading(180)
    def right(self,list):
        if list[0].heading() !=180:
         list[0].setheading(0)




    def move(self,list):
            print(len(list))
            pos=[]

            for number in range(len(list)):
                pos.append(0)

            pos[0]= list[0].position()
            list[0].forward(20)

            for a in range(1, len(list)):
                 pos[a] = list[a].position()
                 list[a].goto(pos[a-1])
            #     print(timy_list[a].position())
