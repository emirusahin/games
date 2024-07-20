from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(-280, 260)
        self.update_score()

    def update_score(self):
        self.write(arg=f'Level {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        # goto() is same as setposition()
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.update_score()
