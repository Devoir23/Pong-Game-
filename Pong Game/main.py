# 1.create the screen
# 2. create and move a paddle
# 3. create another paddle
# 4.create the ball and make it move
# 5. detect collison with all and bounce_y
# 6. detect collison with paddle
# 7. detect when paddle misses
# 8. keep score

from turtle import Screen
from paddle1 import Paddle1
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(1000, 650)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)


l_paddle = Paddle1((-450, 0))
r_paddle = Paddle1((450, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collison with wall:
    if ball.ycor() > 305 or ball.ycor() < -305:
        ball.bounce_y()

    # detect collison with r_paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420 :
        ball.bounce_x()
        # print(ball.xcor())

    # detect R paddle misses
    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()