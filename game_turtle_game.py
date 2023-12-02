import random
from turtle import Turtle, Screen

is_game_on = False
screen = Screen()
screen.setup(width=650, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
distance = [-120, -70, -20, 20, 70, 120]
all_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-300, y=distance[turtle])
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True
while is_game_on:

    for turtl in all_turtles:
        if turtl.xcor() > 325:
            is_game_on = False
            winner_turtle = turtl.pencolor()
            if winner_turtle == user_bet:
                print(f"You have won! The {winner_turtle} is winner turtle.")
            else:
                print(f"You have lost! The {winner_turtle} is winner turtle.")

        rand_distance = random.randint(0,10)
        turtl.forward(rand_distance)


screen.exitonclick()
