from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            highest_score = int(file.read())
            self.highest_score = highest_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}    Highest Score: {self.highest_score}', align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     # goto() is same as setposition()
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def higher_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
