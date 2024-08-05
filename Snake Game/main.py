from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
EASY_TIMER = 0.3
MEDIUM_TIMER = 0.2
HARD_TIMER = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
difficulty_level = screen.textinput(title="Difficulty Level", prompt="Choose: EASY or MEDIUM or HARD").lower()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    if difficulty_level == "easy":
        time.sleep(EASY_TIMER)
    elif difficulty_level == "medium":
        time.sleep(MEDIUM_TIMER)
    elif difficulty_level == "hard":
        time.sleep(HARD_TIMER)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
