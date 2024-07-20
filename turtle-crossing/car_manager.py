from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # when user levels up move distance increase by this increment


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            car.setheading(180)
            # car.forward(self.car_speed) no need for this guy
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def faster_cars(self):
        self.car_speed += MOVE_INCREMENT


