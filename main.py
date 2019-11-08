# Space Invaders

# Set up the screen
import turtle
import os

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

item_zone_x_y = 280

enemy_speed = 2

player_speed = 15

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

#wn.mainloop()