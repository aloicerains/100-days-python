# Importing modules
import turtle
from turtle import Turtle, Screen
import pandas as pd
from pen import Pen

# Processing data
dataset = pd.read_csv('50_states.csv')
# states = list(dataset.state.values) # or dataset.state.to_list()
states = dataset.state.to_list()


def get_cord(state_input):
    """Obtain the coordinates of the given state"""
    result = dataset[dataset.state == state_input]  # similar to dataset.loc[dataset.state==state_input]
    x = result.iloc[0, 1]  # or int(result['x'])
    y = result.iloc[0, 2]  # or int(result['y'])
    return x, y


# Create turtle screen
screen = Screen()
screen.title('Us. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
# give tim the image shape background
turtle.shape(image)

# method to get the mouseclick coordinates
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop() # prevents the screen from going off even after clicking it


score = 0
correct_states = []
while len(correct_states) < 50:
    # user input and prompt
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's the next state?").title()
    if answer == 'Exit':
        break
    if answer in states and answer not in correct_states:
        # get coordinates of the state
        coord = get_cord(answer)
        pen = Pen(coord, answer)
        correct_states.append(answer)
        score += 1
states_to_learn = [state for state in states if state not in correct_states]
states_remaining = pd.DataFrame({
    "State": states_to_learn
})
states_remaining.to_csv('states_to_learn.csv')
