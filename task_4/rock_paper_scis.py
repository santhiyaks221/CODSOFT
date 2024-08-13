import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("400x500")
        self.root.config(bg="#f5f5f5")

        # Title Label
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333333")
        self.title_label.pack(pady=20)

        # Instructions Label
        self.instruction_label = tk.Label(root, text="Choose one:", font=("Helvetica", 14), bg="#f5f5f5", fg="#333333")
        self.instruction_label.pack(pady=10)

        # Emoji Buttons for Rock, Paper, Scissors
        button_frame = tk.Frame(root, bg="#f5f5f5")
        button_frame.pack(pady=20)

        button_style = {
            "font": ("Helvetica", 18, "bold"),
            "width": 5,
            "height": 2,
            "bd": 3,
            "relief": "raised",
            "bg": "#e0e0e0",
            "fg": "#333333",
            "activebackground": "#d0d0d0"
        }

        self.rock_button = tk.Button(button_frame, text="✊", command=lambda: self.play("Rock"), **button_style)
        self.rock_button.grid(row=0, column=0, padx=10, pady=5)

        self.paper_button = tk.Button(button_frame, text="✋", command=lambda: self.play("Paper"), **button_style)
        self.paper_button.grid(row=0, column=1, padx=10, pady=5)

        self.scissors_button = tk.Button(button_frame, text="✌️", command=lambda: self.play("Scissors"), **button_style)
        self.scissors_button.grid(row=0, column=2, padx=10, pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#d32f2f")
        self.result_label.pack(pady=20)

        # Scores
        self.user_score = 0
        self.computer_score = 0
        self.score_label = tk.Label(root, text=f"Score: You - {self.user_score} | Computer - {self.computer_score}", 
                                    font=("Helvetica", 14), bg="#f5f5f5", fg="#333333")
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, font=("Helvetica", 14, "bold"),
                                           width=15, bd=3, relief="raised", bg="#d0d0d0", fg="#333333", activebackground="#b0b0b0")
        self.play_again_button.pack(pady=20)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        # Update the result and score labels
        emoji_map = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
        self.result_label.config(text=f"You: {emoji_map[user_choice]} | Computer: {emoji_map[computer_choice]}\n{result}")
        self.score_label.config(text=f"Score: You - {self.user_score} | Computer - {self.computer_score}")

    def reset_game(self):
        self.result_label.config(text="")
        self.play("")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
