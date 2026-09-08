import turtle
import time

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

direction = "stop"

def up():
    global direction
    direction = "up"

def down():
    global direction
    direction = "down"

def left():
    global direction
    direction = "left"

def right():
    global direction
    direction = "right"

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

while True:
    x = snake.xcor()
    y = snake.ycor()

    if direction == "up":
        snake.sety(y + 20)
    elif direction == "down":
        snake.sety(y - 20)
    elif direction == "left":
        snake.setx(x - 20)
    elif direction == "right":
        snake.setx(x + 20)

    time.sleep(0.1)

screen.mainloop()