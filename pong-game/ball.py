from turtle import Turtle
from random import choice, randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(0)
        self.x_move = 40
        self.y_move = 40
        self.move_speed = 0.15

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9





