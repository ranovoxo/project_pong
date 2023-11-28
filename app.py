from turtle import Screen, Turtle
from paddle import Paddle
UP = "Up"
DOWN = "Down"
W_UP = "W"
W_DOWN = "S"

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))


screen.listen()

screen.onkey(right_paddle.go_up, UP)
screen.onkey(right_paddle.go_down, DOWN)
screen.onkey(left_paddle.go_up, W_UP)
screen.onkey(left_paddle.go_down, W_DOWN)

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()