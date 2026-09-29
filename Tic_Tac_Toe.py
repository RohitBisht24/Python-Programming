import tkinter as tk
from tkinter import messagebox


def check_winner():
    global winner

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7],
        [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg="green")
            buttons[b].config(bg="green")
            buttons[c].config(bg="green")

            winner = True
            messagebox.showinfo(
                "Tic-Tac-Toe", f"Player {buttons[a]['text']} wins!")
            return

    # Check draw
    if all(button["text"] != "" for button in buttons):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Match Draw!")


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()

        if not winner:
            toggle_player()


def toggle_player():
    global current_player

    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False

buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

label = tk.Label(
    root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)


def reset_game():
    global current_player, winner

    current_player = "X"
    winner = False

    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

    label.config(text=f"Player {current_player}'s turn")


again_button = tk.Button(
    root,
    text="Play Again",
    font=("Arial", 10, "bold"),
    bg="#2A7C13",
    fg="white",
    command=reset_game
)

again_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
