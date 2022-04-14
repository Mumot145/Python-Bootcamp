import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

is_game_on = True
correct_answers = 0
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()

guessed_states = []

while correct_answers < len(states_data):
    answer_state = screen.textinput(title=f"Guess the State({len(guessed_states)}/50)",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_not_guessed = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(states_not_guessed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = states_data[states_data.state == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(answer_state, align="center")
