import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import PVP


def reset_board():
    # Clear button texts
    for i in range(3):
        for j in range(3):
            buttons[i][j].configure(text="")
    # Reset title
    root.title("Tic Tac Toe - Turno de la X")
    # clear the board
    PVP.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def button_click(row, column):
    number = row * 3 + column + 1  # Calcular el numero de boton
    print(f"Button {number} clicked!")
    button = buttons[row][column]

    if PVP.is_space_empty(row, column):
        if PVP.current_player == 1:
            PVP.tablero[row][column] = 1
            print(PVP.tablero)
            # set the button text to X
            button.configure(text="X")
            root.title("Tic Tac Toe - Turno de la O")

        else:
            PVP.tablero[row][column] = 2
            print(PVP.tablero)
            # set the button text to O
            button.configure(text="O")
            root.title("Tic Tac Toe - Turno de la X")

        if PVP.checkWinner() != 0:
            messagebox.showinfo("Ganador", f"El jugador {PVP.checkWinner()} ha ganado")
            # Clear button texts
            reset_board()

        elif PVP.isDraw():
            messagebox.showinfo("Empate", "Nadie ha ganado")
            # Clear button texts
            reset_board()

        else:
            PVP.switch_player()

    else:
        button.configure(style="Clicked.TButton")
        root.after(1000, lambda: button.configure(style="TButton"))


root = tk.Tk()

# set title
root.title("Tic Tac Toe - Turno de la X")

# Create a 3x3 grid of buttons
buttons = []
for i in range(3):
    root.grid_rowconfigure(i, weight=1)  # Expand rows evenly
    buttons.append([])
    for j in range(3):
        root.grid_columnconfigure(j, weight=1)  # Expand columns evenly
        button = ttk.Button(
            root,
            text="",
            command=lambda row=i, column=j: button_click(row, column),
            width=10,
            style="TButton",
        )  # Set the width and height of the button
        button.grid(
            row=i, column=j, sticky="nsew"
        )  # Center the button vertically and horizontally
        buttons[i].append(button)

# Set the window size and position
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Define button style
style = ttk.Style()
style.configure("Clicked.TButton", background="red")

root.mainloop()
