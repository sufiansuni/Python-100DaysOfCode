import turtle
import pandas
from pandas._libs import missing
from pandas.core.frame import DataFrame

screen = turtle.Screen()
screen.title("50 US States Game")
image_path = "day-25-50StatesGame/blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

states_data = pandas.read_csv("day-25-50StatesGame/50_states.csv")
all_states = states_data.state.tolist()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 US States Guessed", 
        prompt="What's another states' name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("day-25-50StatesGame/states_to_learn.csv")
        break
    
    # if answer_state in list of states
    if answer_state in all_states:
        # write the state name at state's coords
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
