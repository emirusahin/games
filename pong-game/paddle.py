from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)

