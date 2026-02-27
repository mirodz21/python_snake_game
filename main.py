
import time
from snake import Snake
from turtle import Screen
from food import Food
from score import ScoreBoard

wall = (-300, )
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Master")

screen.tracer(0)


snake=Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_over = False
while not game_over:
    score = ScoreBoard()
    screen.update()
    time.sleep(0.1)
    print("score")
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.food_loc()
        snake.create_snake()
        score += 1


screen.exitonclick()



