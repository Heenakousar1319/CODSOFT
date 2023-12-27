import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Please enter a positive length.")
            return

        password = generate_password(length)
        result_label.config(text="Generated Password: " + password)

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number for the length.")

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(window, text="Enter password length:")
length_label.grid(row=0, column=0, pady=5)

length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, pady=5)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display the generated password
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

# Run the GUI
window.mainloop()

