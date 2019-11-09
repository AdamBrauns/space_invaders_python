# Space Invaders

# Set up the screen
import turtle
import os
import math
import random
from invader import Invader
from player import Player

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("background.gif")

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

# Set the score to 0
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
score_string = f'Score: {score}'
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player
player = Player()

# Choose a number of invaders
number_of_invaders = 5

# Create an empty list of ememies
invaders = []

# Add invaders to list
for i in range(number_of_invaders):
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    invaders.append(Invader(x,y))

# Create the invader 
#invader = Invader()

item_zone_x_y = 280

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

def step_down(invader):
    y = invader.ycor()
    y -= 40
    invader.sety(y)

# Create keyboard bindings
wn.onkey(player.move_left, "Left")
wn.onkey(player.move_right, "Right")
wn.onkey(player.fire_bullet, "space")
wn.listen()

while True:

    for invader in invaders:
        x = invader.xcor()
        x += invader.movement_speed
        invader.setx(x)
        if invader.xcor() > item_zone_x_y:
            # Move all invaders down
            for i in invaders:
                step_down(i)
                i.movement_speed *= -1
        
        if invader.xcor() < -item_zone_x_y:
            # Move all invaders down
            for i in invaders:
                step_down(i)
                i.movement_speed *= -1

        if isCollision(player.bullet, invader):
            # Reset the bullet
            player.bullet.hideturtle()
            # Even though it's invisible, enimies could still hit it
            player.bullet.setposition(0,-400)
            # Reset the invader
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            invader.setposition(x, y)
            score += 10
            score_string = f'Score: {score}'
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            print("Game Over")
            break
    
    # Move the bullet
    if player.bullet.isvisible():
        y = player.bullet.ycor() + player.bullet.movement_speed
        player.bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if player.bullet.ycor() > (item_zone_x_y - 5):
        player.bullet.hideturtle()

#wn.mainloop()