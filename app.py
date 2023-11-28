from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")


left_paddle = Paddle()
right_paddle = Paddle()
left_paddle.goto(-350, 0)
right_paddle.goto(350, 0)

screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")












screen.exitonclick()