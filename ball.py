from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 7.5
        self.goto(new_x, new_y)