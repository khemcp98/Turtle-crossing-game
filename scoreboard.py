from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.display_score()

    def display_score(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)
