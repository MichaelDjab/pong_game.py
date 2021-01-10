from ball import Ball
from paddle import Paddle
from pong_screen import PongScreen
from scoreboard import Score
import random
import time

scr = PongScreen()
right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()
left_score = Score((100, 250))
right_score = Score((-100, 250))
scr.screen.update()


scr.screen.listen()

game_over = False


while not game_over:
    # Move ball
    ball.move()

    # if ball touches ceiling, floor or paddles, it will bounce
    ball.bounce(right_paddle, left_paddle)
    ball.x_motion *= 1.001
    ball.y_motion *= 1.001

    # if ball gets away from the paddles
    if ball.xcor() > 530:
        right_score.score += 1
        right_score.write_score()
        time.sleep(1)
        ball = Ball()
    elif ball.xcor() < -530:
        left_score.score += 1
        left_score.write_score()
        time.sleep(1)
        ball = Ball()
        ball.x_motion *= -1


    # Left paddle motion
    scr.screen.onkey(left_paddle.up, "w")
    scr.screen.onkey(left_paddle.down, "s")

    # Right paddle motion
    scr.screen.onkey(right_paddle.up, "Up")
    scr.screen.onkey(right_paddle.down, "Down")

    left_paddle.auto_paddle(ball, random.randint(-400, 0))
    right_paddle.auto_paddle(ball, random.randint(0, 400))

    scr.screen.update()


scr.screen.exitonclick()


