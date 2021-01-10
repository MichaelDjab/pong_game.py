from turtle import Turtle
import random
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_motion = random.randint(5, 15)
        self.y_motion = random.randint(5, 15)


    def move(self):
        x_cor = self.xcor() + self.x_motion
        y_cor = self.ycor() + self.y_motion
        self.goto(x_cor, y_cor)
