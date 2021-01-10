from turtle import Turtle
import random
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_motion = random.randint(1, 15)
        self.y_motion = random.randint(1, 15)

    def move(self):
        x_cor = self.xcor() + self.x_motion
        y_cor = self.ycor() + self.y_motion
        self.goto(x_cor, y_cor)

    def bounce(self, right_paddle, left_paddle):
        # if ball touches ceiling or floor
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_motion *= -1

        # if ball touches paddles
        if self.distance(right_paddle) < 50 and self.xcor() >= 430:
            self.x_motion *= -1
        if self.distance(left_paddle) < 50 and self.xcor() <= -430:
            self.x_motion *= -1
