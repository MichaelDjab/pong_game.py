from turtle import Turtle

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

    def up(self):
        if self.ycor() < 240:
            self.forward(10)

    def down(self):
        if self.ycor() > -230:
            self.backward(10)
