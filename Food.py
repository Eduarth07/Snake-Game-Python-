from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        new_x = random.randrange(-255,255)
        new_y = random.randrange(-255, 255)
        self.setpos(new_x,new_y)