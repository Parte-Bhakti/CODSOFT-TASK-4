import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x450")
        self.root.configure(bg="#F0F8FF")  # Light background color

        self.user_score = 0
        self.ai_score = 0
        self.history = []

        title = tk.Label(root, text="🎮 Rock Paper Scissors", font=("Arial", 16, "bold"),
                         bg="#F0F8FF", fg="#333")
        title.pack(pady=10)

        ttk.Label(root, text="Choose your move:").pack(pady=5)

        btn_frame = tk.Frame(root, bg="#F0F8FF")
        btn_frame.pack()

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10))

        for move in ["Rock", "Paper", "Scissors"]:
            btn = tk.Button(btn_frame, text=move, width=10,
                            font=("Arial", 11, "bold"),
                            bg="#90CAF9", fg="black",
                            activebackground="#42A5F5",
                            command=lambda m=move: self.play(m))
            btn.pack(pady=5)

        # Result label
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_var,
                                     font=('Arial', 12), bg="#F0F8FF", fg="#333")
        self.result_label.pack(pady=10)

        # Score label
        self.score_var = tk.StringVar()
        self.score_label = tk.Label(root, textvariable=self.score_var,
                                    font=("Arial", 11, "bold"), bg="#E3F2FD")
        self.score_label.pack(pady=5)

        # History Listbox
        tk.Label(root, text="Game History:", bg="#F0F8FF", font=("Arial", 10, "bold")).pack(pady=5)
        self.history_box = tk.Listbox(root, height=5, width=40, font=("Arial", 10))
        self.history_box.pack(pady=5)

        # Reset Button
        tk.Button(root, text="Reset Score", command=self.reset,
                  font=("Arial", 10), bg="#FFAB91", activebackground="#FF7043").pack(pady=10)

        self.update_score()

    def play(self, user_move):
        ai_move = random.choice(["Rock", "Paper", "Scissors"])
        result = ""

        if user_move == ai_move:
            result = "It's a tie!"
        elif (user_move == "Rock" and ai_move == "Scissors") or \
             (user_move == "Paper" and ai_move == "Rock") or \
             (user_move == "Scissors" and ai_move == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "AI wins!"
            self.ai_score += 1

        self.result_var.set(f"You chose {user_move}, AI chose {ai_move}. {result}")
        self.history.insert(0, f"You: {user_move}, AI: {ai_move} → {result}")
        self.update_score()

    def update_score(self):
        self.score_var.set(f"Score: You {self.user_score} - {self.ai_score} AI")
        self.history_box.delete(0, tk.END)
        for entry in self.history[:5]:
            self.history_box.insert(tk.END, entry)

    def reset(self):
        self.user_score = 0
        self.ai_score = 0
        self.history.clear()
        self.result_var.set("")
        self.update_score()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
