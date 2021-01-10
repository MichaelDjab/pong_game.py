from ball import Ball
from paddle import Paddle
from pong_screen import PongScreen

scr = PongScreen()
right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()
scr.screen.update()


scr.screen.listen()

game_over = False

while not game_over:
    # Move ball
    ball.move()

    # if ball touches ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_motion *= -1

    # if ball touches paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() >= 430) or (ball.distance(left_paddle) < 50 and ball.xcor() <= -430):
        ball.x_motion *= -1

    # Left paddle motion
    scr.screen.onkey(left_paddle.up, "w")
    scr.screen.onkey(left_paddle.down, "s")

    # Right paddle motion
    scr.screen.onkey(right_paddle.up, "Up")
    scr.screen.onkey(right_paddle.down, "Down")

    # Logic for moving the paddles if the user wants to ply against a computer
    if ball.xcor() < -350:
        if ball.ycor() > left_paddle.ycor():
            left_paddle.up()
        elif ball.ycor() < left_paddle.ycor():
            left_paddle.down()

    if ball.xcor() > 350:
        if ball.ycor() > right_paddle.ycor():
            right_paddle.up()
        elif ball.ycor() < right_paddle.ycor():
            right_paddle.down()



    scr.screen.update()


scr.screen.exitonclick()


