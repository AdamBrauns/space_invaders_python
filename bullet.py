import turtle

class Bullet(turtle.Turtle):

    movement_speed = 20

    def __init__(self):
        super().__init__()
        turtle.register_shape("laser.gif")
        self.color("yellow")
        self.shape("laser.gif")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(1, 1)
        self.hideturtle()