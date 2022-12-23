from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1200, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_names = ['Tim', 'Ben', 'Rick', 'Beth', 'Jule', 'Ruth']
locations = [(-550,-150), (-550,-100), (-550,-50), (-550,0), (-550,50), (-550,100)]


def prepare_to_start(name, location, t_color):
    name = Turtle(shape='turtle')
    name.color(t_color)
    name.penup()
    name.setposition(location)


for i in range(len(turtle_names)):
    prepare_to_start(turtle_names[i], (locations[i]), colors[i])


screen.exitonclick()