import turtle, random

s = turtle.Screen()
s.bgcolor("black")

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-250,250), random.randint(-250,250))

def move():
    snake.forward(20)

    if snake.distance(food) < 20:
        food.goto(random.randint(-250,250),
                  random.randint(-250,250))

    s.ontimer(move, 100)

def up(): snake.setheading(90)
def down(): snake.setheading(270)
def left(): snake.setheading(180)
def right(): snake.setheading(0)

s.listen()
s.onkey(up,"Up")
s.onkey(down,"Down")
s.onkey(left,"Left")
s.onkey(right,"Right")

move()
s.mainloop()