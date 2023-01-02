FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-270, 240)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
