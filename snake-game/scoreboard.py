from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.score = 0

    def score_count(self):
        self.clear()
        self.write(arg=f"Score = {self.score}",align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.hideturtle()
        self.home()
        self.color("white")
        self.write(arg= "GAME OVER", align= ALIGNMENT, font= FONT)
