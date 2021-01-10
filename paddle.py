from turtle import Turtle
import random

PADDLE_LENGTH = 5


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_LENGTH)
        self.color("white")
        self.goto(pos)
        self.left(90)
        self.paddle_speed = 25

    def up(self):
        if self.ycor() < 240:
            self.forward(self.paddle_speed)

    def down(self):
        if self.ycor() > -210:
            self.backward(self.paddle_speed)

    def auto_paddle(self, ball, coordinates):
        """
        Logic for moving the paddles if the user wants to ply against a computer:
        Automatic left paddle
        """
        self.paddle_speed = random.randint(-10, 25)
        if coordinates < 0:
            if ball.xcor() < coordinates:
                if ball.ycor() > self.ycor():
                    self.up()
                elif ball.ycor() < self.ycor():
                    self.down()

        elif coordinates > 0:
            self.paddle_speed = random.randint(-10, 25)
            if ball.xcor() > 350:
                if ball.ycor() > self.ycor():
                    self.up()
                elif ball.ycor() < self.ycor():
                    self.down()
