from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard
snake = Snake()
food = Food()
score = Scoreboard()
# ________________________ Screen Setup ________________________

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ________________________ Snake Startup ________________________

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        score.the_score += 1
        score.update()

screen.exitonclick()
