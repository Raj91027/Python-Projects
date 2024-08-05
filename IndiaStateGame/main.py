import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian States Game")
image = "IndiaStateGame\India.svg.gif"
turtle.addshape(image)

turtle.shape(image)

data = pandas.read_csv("IndiaStateGame\india_states.csv")
all_sates = data.state.to_list()
guessed_state = []

while len(guessed_state) <= 30:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/30 States Correct", prompt="What's another state names").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_sates if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('IndiaStateGame\state_to_learn.csv')
        break
    if answer_state in guessed_state:
        continue
    if answer_state in all_sates:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# def get(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get)

turtle.mainloop()
