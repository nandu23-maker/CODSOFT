import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_var.set("Invalid length")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        password_var.set("Enter a number")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

password_var = tk.StringVar()

# Label and Entry for password length
tk.Label(root, text="Enter Password Length:", font=("Arial", 10)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), bd=2, width=10)
length_entry.pack()

# Label
tk.Label(root, text="Generated Password:", font=("Arial", 10)).pack(pady=5)

# Entry to display password
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), bd=2, width=25)
password_entry.pack()

# Small button
tk.Button(root, text="Generate", command=generate_password, font=("Arial", 10), width=10, height=1).pack(pady=10)

root.mainloop()
