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
root.geometry("600x500")
root.configure(bg="#2C3E50")

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=10)

tk.Label(frame, text="Name", bg="#2C3E50", fg="white").grid(row=0, column=0)
name_var = tk.StringVar()
tk.Entry(frame, textvariable=name_var, bg="#ECF0F1").grid(row=0, column=1)

tk.Label(frame, text="Phone", bg="#2C3E50", fg="white").grid(row=1, column=0)
phone_var = tk.StringVar()
tk.Entry(frame, textvariable=phone_var, bg="#ECF0F1").grid(row=1, column=1)

tk.Label(frame, text="Email", bg="#2C3E50", fg="white").grid(row=2, column=0)
email_var = tk.StringVar()
tk.Entry(frame, textvariable=email_var, bg="#ECF0F1").grid(row=2, column=1)

tk.Label(frame, text="Address", bg="#2C3E50", fg="white").grid(row=3, column=0)
address_var = tk.StringVar()
tk.Entry(frame, textvariable=address_var, bg="#ECF0F1").grid(row=3, column=1)

tk.Button(frame, text="Add", command=add_contact, bg="#3498DB", fg="white").grid(row=4, column=0)
tk.Button(frame, text="Update", command=update_contact, bg="#F39C12", fg="white").grid(row=4, column=1)
tk.Button(frame, text="Delete", command=delete_contact, bg="#E74C3C", fg="white").grid(row=4, column=2)
tk.Button(frame, text="Export", command=export_contacts, bg="#27AE60", fg="white").grid(row=4, column=3)

search_var = tk.StringVar()
tk.Entry(root, textvariable=search_var, bg="#ECF0F1").pack(pady=5)
tk.Button(root, text="Search", command=search_contact, bg="#9B59B6", fg="white").pack()

columns = ("ID", "Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    contact_list.heading(col, text=col)
contact_list.pack(pady=5)

setup_db()
load_contacts()
root.mainloop()