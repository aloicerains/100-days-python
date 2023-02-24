from tkinter import *
from tkinter import messagebox
import json
import pyperclip
LABEL_FONT = ('Arial', 9)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password import pass_gen, check_website

def find_password():
    """Function searches for password"""
    website = web_entry.get().capitalize()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            try:  # you could use if website in data instead of the second try block
                result = data[website]
            except KeyError:
                messagebox.showerror(title='404', message="Website not found")
            else:
                messagebox.showinfo(title=website, message=f"email: {result['email']}\n"
                                                           f"password: {result['password']}\n")
                pyperclip.copy(result['password'])
    except FileNotFoundError:
        messagebox.showerror(title='404', message="Website not found")

def populate_pass():
    '''Populates newly generated password and copis it to clipboard'''
    pass_word = pass_gen()
    pass_entry.insert(END, string=pass_word)
    # for copying
    pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(website, password, email):
    """Verifies the password and dumps to a file"""
    confirmed = messagebox.askokcancel(title=website, message=f"Are these the correct details?\n"
                                                              f"email: {email}\n"
                                                              f"password: {password}\n")

    if confirmed:
        new_data = {
            website: {
                'email': email,
                'password': password
            }
        }

        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- CHECK PASSWORD ------------------------------- #
def check_password():
    '''checks if password exists'''
    website = web_entry.get().capitalize()
    email = email_entry.get()
    password = pass_entry.get()
    # confirm the details
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops!', message="One of the fields is left blank!")
    elif check_website(website):
        feedback = messagebox.askyesno(title=website, message="The website already exist\n"
                                                   "Do you want to update the password?")
        if feedback:
            save(website, password, email)

    else:
        save(website, password, email)


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
web_entry = Entry(width=33, highlightthickness=2, highlightcolor='sky blue')
email_entry = Entry(width=50, highlightthickness=2, highlightcolor='sky blue')
pass_entry = Entry(width=34, highlightthickness=2, highlightcolor='sky blue')

# positioning entries
web_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)

# buttons
generate_button = Button(text="Generate", width=12, command=populate_pass, activebackground='blue')
add_button = Button(text="Add", width=42, command=check_password, activebackground='blue')
search_button = Button(text="Search", width=12, command=find_password, activebackground='blue')

# position the buttons
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

# initializations
web_entry.focus()
email_entry.insert(END, 'aloiceokoth98@gmail.com')


window.mainloop()