import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.config(bg="#f0f0f0")

        self.tasks = []

        # Frame for listbox and scrollbar
        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=10)

        # Listbox to display tasks with styling
        self.listbox = tk.Listbox(self.frame, height=15, width=50, selectmode=tk.SINGLE, 
                                  bg="#e0f7fa", fg="#00796b", font=("Helvetica", 12, "bold"), 
                                  bd=2, relief="solid", highlightcolor="#004d40", highlightthickness=1)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=5)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Configuring listbox to work with scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry widget for adding new tasks
        self.task_entry = tk.Entry(root, width=52, font=("Helvetica", 12), 
                                   bg="#ffffff", fg="#000000", bd=2, relief="solid")
        self.task_entry.pack(pady=10)

        # Button styling
        button_style = {
            "width": 50,
            "font": ("Helvetica", 10, "bold"),
            "bg": "#00897b",
            "fg": "#ffffff",
            "bd": 2,
            "relief": "raised",
            "activebackground": "#00796b"
        }

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, **button_style)
        self.add_button.pack(pady=5)

        self.mark_button = tk.Button(root, text="Mark Task as Done", command=self.mark_task_done, **button_style)
        self.mark_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, **button_style)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks, **button_style)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " (Done)" if task['completed'] else ""
            self.listbox.insert(tk.END, task['task'] + status)

    def mark_task_done(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]['completed'] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
