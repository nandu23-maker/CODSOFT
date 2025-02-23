import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import csv

# Database setup
def setup_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      phone TEXT NOT NULL UNIQUE,
                      email TEXT,
                      address TEXT)''')
    conn.commit()
    conn.close()

# Add Contact
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()
    if name and phone:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                           (name, phone, email, address))
            conn.commit()
            messagebox.showinfo("Success", "Contact added successfully!")
            clear_entries()
            load_contacts()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Phone number already exists!")
        conn.close()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

# Load Contacts
def load_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, email, address FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    contact_list.delete(*contact_list.get_children())
    for contact in contacts:
        contact_list.insert("", "end", values=contact)

# Search Contact
def search_contact():
    query = search_var.get()
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, email, address FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{query}%", f"%{query}%"))
    contacts = cursor.fetchall()
    conn.close()
    contact_list.delete(*contact_list.get_children())
    for contact in contacts:
        contact_list.insert("", "end", values=contact)

# Delete Contact
def delete_contact():
    selected = contact_list.selection()
    if selected:
        contact_id = contact_list.item(selected[0])['values'][0]
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
        load_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to delete")

# Update Contact
def update_contact():
    selected = contact_list.selection()
    if selected:
        contact_id = contact_list.item(selected[0])['values'][0]
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()
        if name and phone:
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?", (name, phone, email, address, contact_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated", "Contact updated successfully!")
            clear_entries()
            load_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")
    else:
        messagebox.showerror("Error", "Select a contact to update")

# Export Contacts to CSV
def export_contacts():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone, email, address FROM contacts")
        contacts = cursor.fetchall()
        conn.close()
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address"])
            writer.writerows(contacts)
        messagebox.showinfo("Success", "Contacts exported successfully!")

# UI Setup
root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x600")

tk.Label(root, text="Name").pack()
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Phone").pack()
phone_var = tk.StringVar()
tk.Entry(root, textvariable=phone_var).pack()

tk.Label(root, text="Email").pack()
email_var = tk.StringVar()
tk.Entry(root, textvariable=email_var).pack()

tk.Label(root, text="Address").pack()
address_var = tk.StringVar()
tk.Entry(root, textvariable=address_var).pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()
tk.Button(root, text="Export Contacts", command=export_contacts).pack()

search_var = tk.StringVar()
tk.Entry(root, textvariable=search_var).pack()
tk.Button(root, text="Search", command=search_contact).pack()

columns = ("ID", "Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    contact_list.heading(col, text=col)
contact_list.pack()

setup_db()
load_contacts()
root.mainloop()
