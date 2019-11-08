# Space Invaders

# Set up the screen
import turtle
import os
import math

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

# Create the player towards the bottom

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Create the enemy 
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

# Create a player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

item_zone_x_y = 280

bullet_speed = 20

enemy_speed = 2

player_speed = 15

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

# Move the player left and right

def move_left():
    x = player.xcor()
    x -= player_speed
    if x >= -item_zone_x_y:
        player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x <= item_zone_x_y:
        player.setx(x)

def step_down(item):
    y = item.ycor()
    y -= 40
    item.sety(y)

# Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

while True:
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)
    if enemy.xcor() > item_zone_x_y:
        step_down(enemy)
        enemy_speed *= -1
    
    if enemy.xcor() < -item_zone_x_y:
        step_down(enemy)
        enemy_speed *= -1
    
    # Move the bullet
    if bullet.isvisible():
        y = bullet.ycor() + bullet_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > (item_zone_x_y - 5):
        bullet.hideturtle()

    if isCollision(bullet, enemy):
        # Reset the bullet
        bullet.hideturtle()
        # Even though it's invisible, enimies could still hit it
        bullet.setposition(0,-400)
        # Reset the enemy
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

#wn.mainloop()