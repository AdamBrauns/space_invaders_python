import turtle

class Bullet(turtle.Turtle):

    movement_speed = 20

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()