from turtle import Screen
from rightpaddle import Rightpaddle
import time
game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("orange")
screen.title("PONG GAME")
screen.tracer(0)

rightpaddle = Rightpaddle()

screen.listen()
screen.onkey(rightpaddle.up, "Up")
screen.onkey(rightpaddle.down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)







screen.exitonclick()
