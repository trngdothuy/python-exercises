import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Trang's Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.more()
    car_manager.move()

    scoreboard.update()

    # if collision with cars:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        # If go to top of the screen then level up
        elif player.reach_end():
            scoreboard.increase_level()
            player.refresh()
            car_manager.level_up()









screen.exitonclick()

