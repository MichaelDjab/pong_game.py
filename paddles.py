from turtle import Turtle

PADDLE_LENGTH = 5


class Paddles:
    """
    Initializes right and left paddles and calls add_paddle_pieces() for both paddles
    """
    def __init__(self):
        self.right_paddle = Turtle()
        self.right_paddle.shape("square")
        self.right_paddle.shapesize(stretch_wid=1, stretch_len=PADDLE_LENGTH)
        self.right_paddle.color("white")
        self.right_paddle.goto(450, 0)
        self.right_paddle.left(90)
        
        self.left_paddle = Turtle()
        self.left_paddle.shape("square")
        self.left_paddle.shapesize(stretch_wid=1, stretch_len=PADDLE_LENGTH)
        self.left_paddle.color("white")
        self.left_paddle.goto(-450, 0)
        self.left_paddle.left(90)

    def right_up(self):
        x_cor = self.right_paddle.xcor()
        y_cor = self.right_paddle.ycor()
        self.right_paddle.goto(x_cor, y_cor + 10)

    def right_down(self):
        x_cor = self.right_paddle.xcor()
        y_cor = self.right_paddle.ycor()
        self.right_paddle.goto(x_cor, y_cor - 10)

    def left_up(self):
        x_cor = self.left_paddle.xcor()
        y_cor = self.left_paddle.ycor()
        self.left_paddle.goto(x_cor, y_cor + 10)

    def left_down(self):
        x_cor = self.left_paddle.xcor()
        y_cor = self.left_paddle.ycor()
        self.left_paddle.goto(x_cor, y_cor - 10)