import turtle
from bullet import Bullet

class Player(turtle.Turtle):

    movement_speed = 15
    item_zone_x_y = 280

    def __init__(self):
        super().__init__()
        turtle.register_shape("ship.gif")
        self.bullet = Bullet()
        self.color("blue")
        self.shape("ship.gif")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
    
    # Move the player right
    def move_right(self):
        item_zone_x_y = 280
        x = self.xcor()
        x += self.movement_speed
        if x <= item_zone_x_y:
            self.setx(x)

    # Move the player left
    def move_left(self):
        x = self.xcor()
        x -= self.movement_speed
        if x >= -self.item_zone_x_y:
            self.setx(x)

    def fire_bullet(self):
        if not self.bullet.isvisible():
            x = self.xcor()
            y = self.ycor() + 10
            self.bullet.setposition(x, y)
            self.bullet.showturtle()