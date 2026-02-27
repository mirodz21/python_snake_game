
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
score = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # extend/eat
    if snake.head.distance(food) < 15:
        food.food_loc()
        snake.extend()
        score.increase_score()

    # collide with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        score.display_game_over()
    #colide with body
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_over = True
            score.display_game_over()



screen.exitonclick()



