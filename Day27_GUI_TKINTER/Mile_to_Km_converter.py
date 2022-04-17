from tkinter import *


def calculate_km():
    km = float(miles_entry.get()) * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=80)
window.config(padx=20, pady=20)

equal_to_label = Label(text="is equal to", font=("Arial", 12))
equal_to_label.grid(row=1, column=0)

miles_entry = Entry()
miles_entry.insert(END, "0")
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=0, column=2)

km_result_label = Label(text="0", font=("Arial", 12))
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
