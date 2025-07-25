from turtle import Turtle,Screen
import time
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
from line import Center_line
screen = Screen()


screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



scoreboard = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
line = Center_line()
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed )
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325 :
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
