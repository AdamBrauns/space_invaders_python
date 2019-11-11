import turtle

class Bullet(turtle.Turtle):

    movement_speed = 20

    def __init__(self):
        super().__init__()
        turtle.register_shape("images/laser.gif")
        self.color("yellow")
        self.shape("images/laser.gif")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(1, 1)
        self.setposition(-500, -500)
        self.hideturtle()