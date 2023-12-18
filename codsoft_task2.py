import tkinter as tk

def click_button(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for displaying the expression and result
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, justify='right', font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipadx=8, ipady=8)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and add them to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda btn=button: click_button(btn) if btn != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the GUI
window.mainloop()
