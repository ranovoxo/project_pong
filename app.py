from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboad
import time

UP = "Up"
DOWN = "Down"
W_UP = "w"
W_DOWN = "s"

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboad()

screen.listen()

screen.onkey(right_paddle.go_up, UP)
screen.onkey(right_paddle.go_down, DOWN)
screen.onkey(left_paddle.go_up, W_UP)
screen.onkey(left_paddle.go_down, W_DOWN)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # ball collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball collision with right paddle.
    if ball.distance(right_paddle) < 40 and ball.xcor() > 340 or ball.distance(left_paddle) < 40 and ball.xcor() < -340:
        ball.bounce_x()

    # ball going past paddle
    if ball.xcor() > 450:
        scoreboard.left_point()
        ball.reset_ball()
    
    
    if ball.xcor() < -450:
        scoreboard.right_point()
        ball.reset_ball()

    if scoreboard.left_score == 5:
        game_is_on = False
        scoreboard.game_over("left")

    if scoreboard.right_score == 5:
        game_is_on = False
        scoreboard.game_over("right")



screen.exitonclick()