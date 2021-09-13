import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
print(f"Your bet is on: {user_bet} turtle")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []  # to store multiple turtle instances. Each instances having different states.

# Or we can create many objects having same name using for loop as follows.
# here 6 objects named timmy will be created.
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # each turtle object is a 40x40 object.
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# to prevent the racing to start before the user bet.
if user_bet:  # if user_bet has some values this condition will be true
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:  # 230 because half of the turtle's body should cross the winning line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
