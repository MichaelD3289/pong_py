from turtle import Turtle, Screen


screen = Screen()

class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(cor)

    def move_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

    def reset(self, pos):
        self.goto(pos)

