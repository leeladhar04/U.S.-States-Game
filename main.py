import turtle
import pandas

screen = turtle.Screen()
screen.title(("US States Game"))
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")


all_states = data.state.to_list()
all_x = data.x.to_list()
all_y = data.y.to_list()
count = 0
state = set()

while count != 50:

    answer_state = (
        (screen.textinput(title=f"States Guessed {count}/50", prompt="What's another states name? ")).lower()).title()

    if answer_state == "Exit":
        missing_states = []
        for i in all_states:
            if i not in state:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for i in range(len(all_states)):
        if (answer_state == all_states[i]) and answer_state not in state:
            count += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(all_x[i], all_y[i])
            t.write(answer_state)
            state.add(answer_state)
