from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 40, 'bold')
flip_timer = '3000'
word_set = {}


# ---------------------------DATA ---------------------------#
try:
    dataset = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    dataset = pd.read_csv('data/french_words.csv')
finally:
    words_to_learn = dataset.to_dict(orient='records')

def correct_card():
    """Eliminatest the known word from the list of words to learn"""
    global words_to_learn
    words_to_learn.remove(word_set)
    data = pd.DataFrame(words_to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    random_card()



def random_card():
    """Generates a random French word"""
    global flip_timer, word_set
    window.after_cancel(flip_timer)
    word_set = random.choice(words_to_learn)
    french_word = word_set['French']
    english_word = word_set['English']
    canvas.itemconfig(canvas_img, image=CANVAS_FRONT_IMG)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=french_word, fill='black')
    # After 3 seconds, show the english translation
    flip_timer = window.after(3000, flip_card, english_word)

def flip_card(english_word):
    '''Flips the other side of the card and show the english translation'''
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_img, image=CANVAS_BACK_IMG)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=english_word, fill='white')

# ---------------------------UI SETUP ------------------------#

window = Tk()
window.title('flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
CANVAS_FRONT_IMG = PhotoImage(file='images/card_front.png')
CANVAS_BACK_IMG = PhotoImage(file='images/card_back.png')


# canvas
canvas = Canvas()
canvas.config(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

canvas_img = canvas.create_image(400, 263)
title_text = canvas.create_text(400, 150, font=TITLE_FONT)
word_text = canvas.create_text(400, 263, font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
x_img = PhotoImage(file='images/wrong.png')
x_button = Button(image=x_img, highlightthickness=0, command=random_card)
check_img = PhotoImage(file='images/right.png')
check_button = Button(image=check_img, highlightthickness=0, command=correct_card)

# positions
x_button.grid(row=1, column=0)
check_button.grid(row=1, column=1)

random_card()


window.mainloop()
