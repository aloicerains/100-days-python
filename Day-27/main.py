"""Miles to Km converter"""
from tkinter import *
# from playground import add

# creating the window
window = Tk()
# to change title
window.title('Miles to KM converter')
# to change the size of the window
window.minsize(width=400, height=300)
# add padding
window.config(padx=100, pady=70)

# Creating a label
label_desc = Label(text="equal to", font=('Arial', 14))
# placing the label in the screen layout
label_desc.grid(row=1, column=0)

label_km = Label(text="0", font=('Arial', 14))
label_km.grid(row=1, column=1)

label_miles = Label(text="Miles", font=('Arial', 14))
label_miles.grid(row=0, column=2)

label_kms = Label(text="Km", font=('Arial', 14))
label_kms.grid(row=1, column=2)

def button_clicked():
    miles = float(in_put.get())
    km = round(miles * 1.60934)
    label_km.config(text=str(km))


# Entry component
in_put = Entry(width=10)
in_put.grid(row=0, column=1)

# Creating button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# Ensure the screen is always visible
window.mainloop()
