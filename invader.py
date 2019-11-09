import turtle

class Invader(turtle.Turtle):

    movement_speed = 2

    def __init__(self, x, y):
        super().__init__()
        turtle.register_shape("invader.gif")
        self.color("red")
        self.shape("invader.gif")
        self.penup()
        self.speed(0)
        self.shapesize(1, 1)
        self.setposition(x, y)