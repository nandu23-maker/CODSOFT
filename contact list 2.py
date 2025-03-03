import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    if name and phone:
        contacts[name] = phone
        update_contact_list()
        name_var.set("")
        phone_var.set("")
    else:
        messagebox.showwarning("Input Error", "Both fields are required!")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected)
        del contacts[name]
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete!")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        contact_listbox.insert(tk.END, name)

def show_details():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected)
        phone = contacts[name]
        messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {phone}")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to view details!")

root = tk.Tk()
root.title("Contact Book")
root.geometry("350x400")
root.configure(bg="#2E2E2E")

fg_color = "#FFFFFF"
bg_color = "#2E2E2E"
btn_bg = "#444444"
btn_fg = "#FFFFFF"

tk.Label(root, text="Name:", fg=fg_color, bg=bg_color).pack()
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var, bg=btn_bg, fg=btn_fg, insertbackground="white").pack()

tk.Label(root, text="Phone:", fg=fg_color, bg=bg_color).pack()
phone_var = tk.StringVar()
tk.Entry(root, textvariable=phone_var, bg=btn_bg, fg=btn_fg, insertbackground="white").pack()

tk.Button(root, text="Add Contact", command=add_contact, bg=btn_bg, fg=btn_fg).pack()
contact_listbox = tk.Listbox(root, bg=btn_bg, fg=btn_fg)
contact_listbox.pack(fill=tk.BOTH, expand=True)

tk.Button(root, text="Show Details", command=show_details, bg=btn_bg, fg=btn_fg).pack()
tk.Button(root, text="Delete Contact", command=delete_contact, bg=btn_bg, fg=btn_fg).pack()

root.mainloop()