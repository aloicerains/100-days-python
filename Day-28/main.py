from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = ""
REP = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, TICK, REP
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    TICK = ""
    label_tick.config(text=TICK)
    count_text = '00:00'
    canvas.itemconfig(timer_text, text=count_text)
    REP = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    '''Starts the timer mechanism'''
    global REP
    global TICK
    if REP == 7:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text='Break', fg=RED)
        REP = 0
    elif REP % 2 == 0:
        count_down(WORK_MIN * 60)
        label_timer.config(text='Work', fg=GREEN)
        TICK = TICK + "✔"
        REP += 1
    else:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text='Break', fg=PINK)
        label_tick.config(text=TICK)
        REP += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# creating the count
def count_down(count):
    global timer, TICK
    min_count = count // 60  # or use math.floor(count)
    sec_count = count % 60
    if min_count < 10:
        min_count = f'0{min_count}'
    if sec_count < 10:
        sec_count = f'0{sec_count}'
    count_text = f'{min_count}:{sec_count}'
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodora')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# canvas uses photoimage hence must be converted as below
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Creating labels
label_timer = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

label_tick = Label(font=(FONT_NAME, 20, 'bold'), bg=YELLOW)
label_tick.config(fg=GREEN)
label_tick.grid(row=3, column=1)

# creating buttons
button_start = Button(text='Start', command=start_timer, highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(row=2, column=2)


window.mainloop()