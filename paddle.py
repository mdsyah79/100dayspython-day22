from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_positions):
        self.paddle_positions = paddle_positions
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(paddle_positions)
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
