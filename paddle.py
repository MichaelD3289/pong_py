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
        self.update()

    def update(self):
        screen.update()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.update()

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.update()


