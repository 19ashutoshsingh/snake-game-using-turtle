from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()

    def create_border(self):
        # self.Turtle()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-290, -290)
        self.pendown()
        for i in range(4):
            self.forward(580)
            self.left(90)
