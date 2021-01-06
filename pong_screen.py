from turtle import Turtle, Screen

SCREEN_DIMENSIONS = (1000, 600)


class PongScreen:

    def __init__(self):
        """
        Initialize screen and net and call setup_screen() as well as setup_net()
        """
        super().__init__()
        self.screen = Screen()
        self.net = Turtle()
        self.setup_screen()
        self.setup_net()

    def setup_screen(self):
        """
        Setup_screen() uses a constant dimensions, colors it in black and removes the tracer.
        """
        self.screen.setup(SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1])
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def setup_net(self):
        """
        Setup_net() draws the net in the middle of the screen depending on the constant dimensions.
        """
        self.net.hideturtle()
        self.net.goto(0, SCREEN_DIMENSIONS[1]/2 - 20)
        self.net.color("white")
        self.net.setheading(-90)

        for x in range(SCREEN_DIMENSIONS[1]//20 - 2):
            self.net.forward(10)
            self.net.penup()
            self.net.forward(10)
            self.net.pendown()
