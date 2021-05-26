from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 0.1)