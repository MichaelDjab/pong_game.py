from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.x_motion = 2
        self.y_motion = 2

    def move(self):
        x_cor = self.xcor() + self.x_motion
        y_cor = self.ycor() + self.y_motion
        self.goto(x_cor, y_cor)
