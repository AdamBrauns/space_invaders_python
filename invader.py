import turtle

class Invader(turtle.Turtle):

    movement_speed = 2

    def __init__(self, x, y):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.setposition(x, y)