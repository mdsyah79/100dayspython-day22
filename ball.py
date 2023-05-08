import time
from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(x=0, y=0)
        self.dx = 10
        self.dy = 10

    def ball_move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()


