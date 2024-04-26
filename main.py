from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.mov_up)
screen.onkey(key="Down", fun=r_paddle.mov_down)
screen.onkey(key="w", fun=l_paddle.mov_up)
screen.onkey(key="s", fun=l_paddle.mov_down)
game_is_on = True
while game_is_on:
    time.sleep(ball.mov_speed)
    screen.update()
    ball.ball_mov()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
