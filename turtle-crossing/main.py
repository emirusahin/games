import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

# TODO.1: continuously create cars +
# TODO.2: make cars faster after level_up

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()



    # detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 21:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > FINISH_LINE_Y:
        scoreboard.level_up()
        player.goto(STARTING_POSITION)
        car_manager.faster_cars()

screen.exitonclick()
