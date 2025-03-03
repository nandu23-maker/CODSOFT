import tkinter as tk
import random

# Choices and Scores
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

# Function to play the game
def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "You Lose! 😢"
        computer_score += 1

    user_choice_var.set(f"Your Choice: {choice}")
    computer_choice_var.set(f"Computer: {computer_choice}")
    result_var.set(result)
    score_var.set(f"Score: You {user_score} - {computer_score} Computer")

# GUI Setup
root = tk.Tk()
root.title("Rock, Paper, Scissors - Ultimate Battle")
root.geometry("400x400")

# Variables
user_choice_var = tk.StringVar()
computer_choice_var = tk.StringVar()
result_var = tk.StringVar()
score_var = tk.StringVar(value="Score: You 0 - 0 Computer")

# Large, Bold Headline
tk.Label(root, text="ROCK PAPER SCISSORS", font=("Arial", 18, "bold"), fg="blue").pack(pady=10)

# Labels for Choices & Result
tk.Label(root, textvariable=user_choice_var, font=("Arial", 12)).pack()
tk.Label(root, textvariable=computer_choice_var, font=("Arial", 12)).pack()
tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(root, textvariable=score_var, font=("Arial", 12, "bold")).pack(pady=5)

# Buttons for Choices
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

for choice in choices:
    tk.Button(
        btn_frame, text=choice, font=("Arial", 12, "bold"), width=12, bg="black", fg="white",
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=10)

root.mainloop()
