import tkinter as tk
from tkinter import messagebox

def on_click(text):
    if text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

def create_button(parent, text):
    return tk.Button(parent, text=text, font=("Arial", 16), width=5, height=2, command=lambda: on_click(text))

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

tk.Label(root, text="Simple Calculator", font=("Arial", 14, "bold")).pack()

entry_var = tk.StringVar()
tk.Entry(root, textvar=entry_var, font=("Arial", 18), justify='right').pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for char in row:
        create_button(frame, char).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()

def on_click(text):
    if text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

def create_button(parent, text):
    return tk.Button(parent, text=text, font=("Arial", 16), width=5, height=2, command=lambda: on_click(text))

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

tk.Label(root, text="Simple Calculator", font=("Arial", 14, "bold")).pack()

entry_var = tk.StringVar()
tk.Entry(root, textvar=entry_var, font=("Arial", 18), justify='right').pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for char in row:
        create_button(frame, char).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()

