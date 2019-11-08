import turtle

class Player(turtle.Turtle):

    movement_speed = 15

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)