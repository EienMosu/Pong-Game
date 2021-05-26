from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)


    def move_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)


    def move_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
