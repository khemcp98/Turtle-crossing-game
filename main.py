import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
score = Scoreboard()
cars = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect collision with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # Detect crossing
    if player.ycor() == 280:
        player.refresh_position()
        cars.speed()
        score.update_score()

screen.exitonclick()
