import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player((0, -280))
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.you_lose()


    # detect turtle at finish line
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_score()

screen.exitonclick()
