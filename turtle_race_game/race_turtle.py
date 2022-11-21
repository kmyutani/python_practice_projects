import turtle as tr
import random as rd

is_race_on = False
screen = tr.Screen()
screen.setup(width=500, height=400)
all_turtle = []
colors = ["red", "orange", "yellow", "green", "blue", "yellow"]
y_position = [-50, -25, 0, 25, 50, 75]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0,6):
    new_turtle = tr.Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = rd.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()