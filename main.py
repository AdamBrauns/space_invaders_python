# Space Invaders

# Set up the screen
import turtle
import os
import math
from invader import Invader
from player import Player
from bullet import Bullet

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw boarder
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player
player = Player()

# Create the invader 
invader = Invader()

# Create a player bullet
bullet = Bullet()

item_zone_x_y = 280

def fire_bullet():
    if not bullet.isvisible():
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

def step_down(item):
    y = item.ycor()
    y -= 40
    item.sety(y)

# Create keyboard bindings
wn.onkey(player.move_left, "Left")
wn.onkey(player.move_right, "Right")
wn.onkey(fire_bullet, "space")
wn.listen()

while True:
    x = invader.xcor()
    x += invader.movement_speed
    invader.setx(x)
    if invader.xcor() > item_zone_x_y:
        step_down(invader)
        invader.movement_speed *= -1
    
    if invader.xcor() < -item_zone_x_y:
        step_down(invader)
        invader.movement_speed *= -1
    
    # Move the bullet
    if bullet.isvisible():
        y = bullet.ycor() + bullet.movement_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > (item_zone_x_y - 5):
        bullet.hideturtle()

    if isCollision(bullet, invader):
        # Reset the bullet
        bullet.hideturtle()
        # Even though it's invisible, enimies could still hit it
        bullet.setposition(0,-400)
        # Reset the invader
        invader.setposition(-200, 250)

    if isCollision(player, invader):
        player.hideturtle()
        invader.hideturtle()
        print("Game Over")
        break

#wn.mainloop()