from tkinter import *
from tkinter import messagebox
import pyperclip
LABEL_FONT = ('Arial', 9)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password import pass_gen

def populate_pass():
    '''Populates newly generated password and copis it to clipboard'''
    pass_word = pass_gen()
    pass_entry.insert(END, string=pass_word)
    # for copying
    pyperclip.copy(pass_word)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    '''Adds the generated password to data file'''
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    # confirm the details
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops!', message="One of the fields is left blank!")
    else:
        confirmed = messagebox.askokcancel(title=website, message=f"Are these the correct details?\n"
                                                  f"email: {email}\n"
                                                  f"password: {password}\n")

        if confirmed:
            with open('data.txt', 'a+') as f:
                f.write(f"{website} | {email} | {password}" + "\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text='Website:', font=LABEL_FONT)
email_label = Label(text="Email/Username:", font=LABEL_FONT)
pass_label = Label(text="Password", font=LABEL_FONT)

# positioning labels
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=50, highlightthickness=0, highlightcolor='blue')
email_entry = Entry(width=50)
pass_entry = Entry(width=34)

# positioning entries
web_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)

# buttons
generate_button = Button(text="Generate", width=12, command=populate_pass)
add_button = Button(text="Add", width=42, command=save_password)

# position the buttons
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

# initializations
web_entry.focus()
email_entry.insert(END, 'aloiceokoth98@gmail.com')






window.mainloop()