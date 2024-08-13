import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        self.root.config(bg="#f5f5f5")

        # Create or connect to the database
        self.conn = sqlite3.connect("contacts.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT
            )"""
        )
        self.conn.commit()

        # Title Label
        self.title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333333")
        self.title_label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(root, bg="#f5f5f5")
        button_frame.pack(pady=20)

        button_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 20,
            "bd": 3,
            "relief": "raised",
            "bg": "#d0d0d0",
            "fg": "#333333",
            "activebackground": "#b0b0b0"
        }

        self.add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact, **button_style)
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.view_button = tk.Button(button_frame, text="View Contacts", command=self.view_contacts, **button_style)
        self.view_button.grid(row=1, column=0, padx=10, pady=5)

        self.search_button = tk.Button(button_frame, text="Search Contact", command=self.search_contact, **button_style)
        self.search_button.grid(row=2, column=0, padx=10, pady=5)

        self.update_button = tk.Button(button_frame, text="Update Contact", command=self.update_contact, **button_style)
        self.update_button.grid(row=3, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, **button_style)
        self.delete_button.grid(row=4, column=0, padx=10, pady=5)

        self.exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit, **button_style)
        self.exit_button.grid(row=5, column=0, padx=10, pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:", parent=self.root)
        phone = simpledialog.askstring("Input", "Enter Phone Number:", parent=self.root)
        email = simpledialog.askstring("Input", "Enter Email (Optional):", parent=self.root)
        address = simpledialog.askstring("Input", "Enter Address (Optional):", parent=self.root)

        if name and phone:
            self.cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                                (name, phone, email, address))
            self.conn.commit()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required!")

    def view_contacts(self):
        self.cursor.execute("SELECT name, phone FROM contacts")
        contacts = self.cursor.fetchall()
        if contacts:
            contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts found!")

    def search_contact(self):
        search_query = simpledialog.askstring("Search", "Enter Name or Phone Number:", parent=self.root)
        if search_query:
            self.cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{search_query}%", f"%{search_query}%"))
            contacts = self.cursor.fetchall()
            if contacts:
                contact_info = "\n".join([f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}\n" 
                                          for _, name, phone, email, address in contacts])
                messagebox.showinfo("Search Results", contact_info)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found!")
        else:
            messagebox.showerror("Error", "Search query cannot be empty!")

    def update_contact(self):
        search_query = simpledialog.askstring("Update", "Enter Name or Phone Number to Update:", parent=self.root)
        if search_query:
            self.cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{search_query}%", f"%{search_query}%"))
            contact = self.cursor.fetchone()
            if contact:
                name = simpledialog.askstring("Input", "Enter New Name (Leave blank to keep current):", parent=self.root, initialvalue=contact[1])
                phone = simpledialog.askstring("Input", "Enter New Phone Number (Leave blank to keep current):", parent=self.root, initialvalue=contact[2])
                email = simpledialog.askstring("Input", "Enter New Email (Leave blank to keep current):", parent=self.root, initialvalue=contact[3])
                address = simpledialog.askstring("Input", "Enter New Address (Leave blank to keep current):", parent=self.root, initialvalue=contact[4])

                if name and phone:
                    self.cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?",
                                        (name, phone, email, address, contact[0]))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Contact updated successfully!")
                else:
                    messagebox.showerror("Error", "Name and Phone Number are required!")
            else:
                messagebox.showinfo("Update", "No matching contact found!")
        else:
            messagebox.showerror("Error", "Search query cannot be empty!")

    def delete_contact(self):
        search_query = simpledialog.askstring("Delete", "Enter Name or Phone Number to Delete:", parent=self.root)
        if search_query:
            self.cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{search_query}%", f"%{search_query}%"))
            contact = self.cursor.fetchone()
            if contact:
                confirm = messagebox.askyesno("Delete", f"Are you sure you want to delete {contact[1]}?")
                if confirm:
                    self.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact[0],))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Delete", "No matching contact found!")
        else:
            messagebox.showerror("Error", "Search query cannot be empty!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
