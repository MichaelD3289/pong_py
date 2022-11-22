from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, dir):
        if dir == 'y':
            self.y_move *= -1
        elif dir == 'x':
            self.x_move *= -1
            self.increase_speed()

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1

    def increase_speed(self):
        self.move_speed *= 0.9
