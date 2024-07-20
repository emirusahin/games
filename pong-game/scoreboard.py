from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 400)
        self.update_score()


    def update_score(self):
        self.write(arg=f'{self.score1} : {self.score2}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        # goto() is same as setposition()
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score1(self):
        self.clear()
        self.score1 += 1
        self.update_score()

    def increase_score2(self):
        self.clear()
        self.score2 += 1
        self.update_score()
