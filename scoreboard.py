from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.the_score = 0
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.color("white")
        self.write(f"Score: {self.the_score}", False, 'center', ('Arial', 15, 'normal'))


    def update(self):
        self.clear()
        self.write(f"Score: {self.the_score}", False, 'center', ('Arial', 15, 'normal'))