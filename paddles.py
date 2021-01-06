from turtle import Turtle

PADDLE_Y_POSITIONS = [-20, 0, 20, 40, 60]
PADDLE_LENGTH = 5


def add_paddle_pieces(paddle, x_pos):
    """
    Adds paddle pieces to a given paddle given a constant y-position and a given x position
    """
    for i in range(PADDLE_LENGTH):
        paddle.append(Turtle(shape="square"))
        paddle[i].color("white")
        paddle[i].penup()
        paddle[i].goto(x_pos, PADDLE_Y_POSITIONS[i])


def move(paddle, heading):
    """
    Moves the paddles up or down depending on the heading
    """
    for paddle_piece in paddle:
        paddle_piece.setheading(heading)
        paddle_piece.forward(20)


class Paddles:
    """
    Initializes right and left paddles and calls add_paddle_pieces() for both paddles
    """
    def __init__(self):
        self.right_paddle = []
        self.left_paddle = []
        add_paddle_pieces(self.right_paddle, 450)
        add_paddle_pieces(self.left_paddle, -450)

    def right_up(self):
        move(self.right_paddle, 90)

    def right_down(self):
        move(self.right_paddle, -90)

    def left_up(self):
        move(self.left_paddle, 90)

    def left_down(self):
        move(self.left_paddle, -90)
