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

# # first object instance
# aayam = Turtle(shape="turtle")
# aayam.color(colors[0])
# aayam.penup()
# aayam.goto(x=-235, y=-150)
#
# # second object instance
# kanchan = Turtle(shape="turtle")
# kanchan.color(colors[5])
# kanchan.penup()
# kanchan.goto(x=-235, y=-90)
#
# # third object instance
# brinda = Turtle(shape="turtle")
# brinda.color(colors[1])
# brinda.penup()
# brinda.goto(x=-235, y=-30)
#
# # forth object instance
# bishnu = Turtle(shape="turtle")
# bishnu.color(colors[2])
# bishnu.penup()
# bishnu.goto(x=-235, y=30)
#
# # fifth object instance
# gopal = Turtle(shape="turtle")
# gopal.color(colors[3])
# gopal.penup()
# gopal.goto(x=-235, y=90)
#
# # sixth object instance
# rojina = Turtle(shape="turtle")
# rojina.color(colors[4])
# rojina.penup()
# rojina.goto(x=-235, y=150)


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
