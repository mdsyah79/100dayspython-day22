from turtle import Turtle

class Rightpaddle(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(x=350, y=0)
        self.color("white")
        # self.showturtle()


    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
