import turtle

turtle.setup(600, 600)
turtle.colormode(255)
turtle.bgcolor(135, 206, 250)

# Setting up the boundary
t = turtle.Turtle()
t.pencolor('navy')
t.penup()
t.goto(-200, 200)
t.pendown()


def borders():
    for i in range(4):
        t.forward(400)
        t.right(90)


borders()
t.hideturtle()

# Players
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle2 = turtle1.clone()

turtle1.pencolor('crimson')
turtle2.pencolor('teal')

turtle1.penup()
turtle2.penup()

speed1 = 3
speed2 = 3


# Increasing or decreasing speed
def increase_speed():
    global speed1
    if not (speed1 + 1 > 6):
        speed1 = speed1 + 1
        turtle1.speed(speed1)


def decrease_speed():
    global speed1
    if not (speed1 - 1 < 1):
        speed1 = speed1 - 1
        turtle1.speed(speed1)


def increase_speed2():
    global speed2
    if not (speed2 + 1 > 6):
        speed2 = speed2 + 1


def decrease_speed2():
    global speed2
    if not (speed2 - 1 < 1):
        speed2 = speed2 - 1


# Turning left or right
def turn_left():
    turtle1.left(90)


def turn_right():
    turtle1.right(90)


def turn_left_2():
    turtle2.left(90)


def turn_right_2():
    turtle2.right(90)


# Player 1
turtle.onkey(increase_speed, "w")
turtle.onkey(turn_left, "a")
turtle.onkey(decrease_speed, "s")
turtle.onkey(turn_right, "d")

# Player 2
turtle.onkey(increase_speed2, "Up")
turtle.onkey(turn_left_2, "Left")
turtle.onkey(decrease_speed2, "Down")
turtle.onkey(turn_right_2, "Right")

turtle.listen()

leaf = turtle.Turtle()
# coordinates to draw leaf shape
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
turtle.register_shape("leaf", leaf_shape)
leaf.shape("leaf")
leaf.color("green")
leaf.penup()

# Second leaf
leaf2 = leaf.clone()

# Random locations of leaves
import random


def leaf_generation(leaves):
    leaves_location_x = random.randint(-180, 180)
    leaves_location_y = random.randint(-180, 180)
    leaves.goto(leaves_location_x, leaves_location_y)


leaf_generation(leaf)
leaf_generation(leaf2)

# Scorekeeper
score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle2 = score_turtle.clone()
score1 = 0
score2 = 0


def update_score():
    global score1
    score_turtle.clear()
    score_turtle.goto(-200, 215)
    score_turtle.pencolor('crimson')
    score_turtle.write("Player 1 Score: " + str(score1), font=("Arial", 10, "bold"))


def update_score2():
    global score2
    score_turtle2.clear()
    score_turtle2.pencolor('teal')
    score_turtle2.goto(0, 215)
    score_turtle2.write("Player 2 Score: " + str(score2), font=("Arial", 10, "bold"))


update_score()
update_score2()

# Turtles' movement and scorekeeping
while True:
    turtle1.forward(speed1)
    turtle2.forward(speed2)

    if turtle1.xcor() < -200 or turtle1.xcor() > 200 or turtle1.ycor() < -200 or turtle1.ycor() > 200:
        turtle1.right(180)

    if turtle2.xcor() < -194 or turtle2.xcor() > 194 or turtle2.ycor() < -194 or turtle2.ycor() > 194:
        turtle2.right(180)

    if turtle1.distance(leaf) < 25 or turtle1.distance(leaf2) < 25:
        score1 = score1 + 1
        update_score()
    if turtle2.distance(leaf) < 25 or turtle2.distance(leaf2) < 25:
        score2 = score2 + 1
        update_score2()

    if turtle1.distance(leaf) < 25 or turtle2.distance(leaf) < 25:
        leaf_generation(leaf)
    if turtle1.distance(leaf2) < 25 or turtle2.distance(leaf2) < 25:
        leaf_generation(leaf2)

    if score1 == 10 or score2 == 10:
        break

# Win screen
t.color("teal")
t.begin_fill()
borders()
t.end_fill()
t.goto(-160, 0)
t.pencolor("White")
if score1 == 10:
    t.write("Player 1 wins!", font=("Arial", 30, "bold"))
else:
    t.write("Player 2 wins!", font=("Arial", 30, "bold"))
