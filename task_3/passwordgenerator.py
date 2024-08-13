import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x250")
        self.root.config(bg="#f5f5f5")

        # Password Length Label and Entry
        self.label = tk.Label(root, text="Enter password length:", font=("Helvetica", 12), bg="#f5f5f5", fg="#333333")
        self.label.pack(pady=10)
        self.length_entry = tk.Entry(root, width=15, font=("Helvetica", 12), bd=2, relief="solid", bg="#e0e0e0", fg="#333333")
        self.length_entry.pack(pady=5)

        # Generate Button
        self.gen_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12, "bold"), 
                                    width=20, bd=3, relief="raised", bg="#d0d0d0", fg="#333333", activebackground="#b0b0b0")
        self.gen_button.pack(pady=20)

        # Password Display
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#d32f2f")
        self.result_label.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be greater than zero.")

            # Character set for password generation
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            # Display the generated password
            self.result_label.config(text=f"Password: {password}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
