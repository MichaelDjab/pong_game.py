from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Score(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
