import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.config(bg="#3a3a3a")

        # Number 1 Label and Entry
        self.label1 = tk.Label(root, text="Enter first number:", font=("Helvetica", 12), bg="#3a3a3a", fg="#ffffff")
        self.label1.pack(pady=10)
        self.num1_entry = tk.Entry(root, width=15, font=("Helvetica", 12), bd=2, relief="solid", bg="#5a5a5a", fg="#ffffff")
        self.num1_entry.pack(pady=5)

        # Number 2 Label and Entry
        self.label2 = tk.Label(root, text="Enter second number:", font=("Helvetica", 12), bg="#3a3a3a", fg="#ffffff")
        self.label2.pack(pady=10)
        self.num2_entry = tk.Entry(root, width=15, font=("Helvetica", 12), bd=2, relief="solid", bg="#5a5a5a", fg="#ffffff")
        self.num2_entry.pack(pady=5)

        # Buttons for Operations
        button_frame = tk.Frame(root, bg="#3a3a3a")
        button_frame.pack(pady=20)

        button_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 5,
            "bd": 3,
            "relief": "raised",
            "bg": "#7a7a7a",
            "fg": "#ffffff",
            "activebackground": "#5a5a5a"
        }

        self.add_button = tk.Button(button_frame, text="+", command=lambda: self.set_operation("+"), **button_style)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.sub_button = tk.Button(button_frame, text="-", command=lambda: self.set_operation("-"), **button_style)
        self.sub_button.grid(row=0, column=1, padx=5, pady=5)

        self.mul_button = tk.Button(button_frame, text="*", command=lambda: self.set_operation("*"), **button_style)
        self.mul_button.grid(row=0, column=2, padx=5, pady=5)

        self.div_button = tk.Button(button_frame, text="/", command=lambda: self.set_operation("/"), **button_style)
        self.div_button.grid(row=0, column=3, padx=5, pady=5)

        # Equals Button
        self.eq_button = tk.Button(root, text="=", command=self.calculate, **button_style)
        self.eq_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#3a3a3a", fg="#d32f2f")
        self.result_label.pack(pady=20)

        # Operation Variable
        self.operation = None

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            if not self.operation:
                raise ValueError("No operation selected.")

            if self.operation == "+":
                result = num1 + num2
            elif self.operation == "-":
                result = num1 - num2
            elif self.operation == "*":
                result = num1 * num2
            elif self.operation == "/":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
            self.num1_entry.delete(0, tk.END)
            self.num2_entry.delete(0, tk.END)
            self.operation = None
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
