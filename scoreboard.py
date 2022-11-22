from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.l_score, align="center", font=('Courier', 60, "normal"))
        self.goto(100, 210)
        self.write(self.r_score, align="center", font=('Courier', 60, "normal"))

    def award_point(self, player):
        if player == 'right':
            self.r_score += 1
        elif player == 'left':
            self.l_score += 1
        self.update_scoreboard()

    def print_winner(self, player):
        self.goto((0, 0))
        self.write(f"{player.title()} player wins!", align="center", font=('Courier', 36, "normal"))