import turtle

class Invader(turtle.Turtle):

    movement_speed = 2

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.setposition(-200, 250)