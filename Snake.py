from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for segment in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(segment)
            self.snake_body.append(snake)
    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.snake_body[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)
    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)