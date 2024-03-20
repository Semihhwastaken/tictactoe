import tkinter as tk
from tkinter import *
from tkinter import font
import random


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_title = "Tic-Tac-Toe"
        self.title(self.window_title)
        self.geometry("600x600")
        self.buttons = {}
        self._create_menu()
        self.create_board()
        self.create_player()
        
        
        self.winning_combs = [
            # Vertical 
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Horizantol 
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diognal 
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        self.x_current_moves = []
        self.o_current_moves = []
        
    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(
            label="Play Again",
            command=self.reset_game
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)    

    def create_board(self):
        display_fra = tk.Frame(master=self)
        display_fra.pack(fill=tk.X)
        self.display = Label(
            master=display_fra,
            text="Ready?",
            font=font.Font(size=28,weight="bold")
        )
        self.display.pack()

        button_frame = tk.Frame(master=self)
        button_frame.pack()
        for row in range(3):
            self.rowconfigure(row,weight=1,minsize=(self.winfo_width()/3))
            self.columnconfigure(row,weight=1,minsize=(self.winfo_height()/3)) 
            for col in range(3):
                button = Button(
                    master=button_frame,
                    text="",
                    font=font.Font(size=36,weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                    highlightthickness=2
                )
                self.buttons[button] = (row,col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    
                )

    def create_player(self):
        global player
        self.characters = ["X","O"]
        player = random.choice(self.characters)
        self.label = Label(text=f"{player}'s turn",font=("arial",25))
        self.label.pack()

        for button in self.buttons:
            button.config(command=lambda b=button: self.button_click(b))

    
    def button_click(self, button):
        global player
        row, col = self.buttons[button]
        if player == "X":
            self.display.config(text="Let's Play")
            self.x_current_moves.append((row,col))
            button.config(text="X",fg="green", state="disabled")
            player = "O"
        else:
            self.display.config(text="Let's Play")
            self.o_current_moves.append((row,col))
            button.config(text="O", state="disabled")
            player = "X"    
        self.label.config(text=f"{player}'s turn")

        if self.has_winner():
            self.display.config(text="X has won" if player == "O" else "O has won")
            self.label.config(text="Game Over")
            for button,row in self.buttons.items():
                button.config(state="disabled")
        elif not self.has_winner() and all(button["text"] != "" for button in self.buttons):
            self.display.config(text="Tied")
            self.label.config(text="Game Over")

    def has_winner(self):
        self.has_winne = False
        self.x_current_moves.sort()
        self.o_current_moves.sort()
        for win_con in self.winning_combs:
            if all(item in self.x_current_moves for item in win_con):
                self.has_winne = True
                return self.has_winne
            elif all(item in self.o_current_moves for item in win_con):
                self.has_winne = True
                return self.has_winne
            
        return self.has_winne
    
    def reset_game(self):
       global player
       self.x_current_moves.clear()
       self.o_current_moves.clear()
       self.has_winne = False
       self.display.config(text="Let's Play")
       self.label.config(text=f"{player}'s turn")
       for button,row in self.buttons.items():
           button.config(state="normal")
           button.config(text="")
       
board = TicTacToe()
board.mainloop()        

