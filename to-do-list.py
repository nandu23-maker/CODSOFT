import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task = task_var.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_var.set("")
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(tk.END, f"✔ {task}")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed!")

def clear_all():
    task_listbox.delete(0, tk.END)

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            task_listbox.delete(0, tk.END)
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Load Error", "No saved tasks found!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#2E2E2E")

fg_color = "#FFFFFF"
bg_color = "#2E2E2E"
btn_bg = "#444444"
btn_fg = "#FFFFFF"

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5, background=btn_bg, foreground=btn_fg)

frame = tk.Frame(root, bg=bg_color)
frame.pack(pady=10)

tk.Label(frame, text="Task:", fg=fg_color, bg=bg_color, font=("Arial", 12)).grid(row=0, column=0, padx=5)
task_var = tk.StringVar()
tk.Entry(frame, textvariable=task_var, bg=btn_bg, fg=btn_fg, insertbackground="white", font=("Arial", 12)).grid(row=0, column=1, padx=5)

tk.Button(root, text="Add Task", command=add_task, bg=btn_bg, fg=btn_fg, font=("Arial", 12)).pack(pady=5)

frame_list = tk.Frame(root, bg=bg_color)
frame_list.pack(pady=5, fill=tk.BOTH, expand=True)

task_listbox = tk.Listbox(frame_list, bg=btn_bg, fg=btn_fg, font=("Arial", 12), selectbackground="#555555")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

tk.Button(root, text="Mark Completed", command=mark_completed, bg=btn_bg, fg=btn_fg, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg=btn_bg, fg=btn_fg, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_all, bg=btn_bg, fg=btn_fg, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Save Tasks", command=save_tasks, bg=btn_bg, fg=btn_fg, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Load Tasks", command=load_tasks, bg=btn_bg, fg=btn_fg, font=("Arial", 12)).pack(pady=5)

root.mainloop()