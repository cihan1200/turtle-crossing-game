from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(x=-250, y=280)

    def clean_scoreboard(self):
        self.clear()

    def write_score(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over_message(self):
        self.goto(x=0, y=280)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
