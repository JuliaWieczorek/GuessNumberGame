"""
GUESS NUMBER GAME
The computer randomly generates a number.
The user enters a number, and the computer will tell you
if you are too high, or too low.
Then keep guessing until you guess the number.
https://www.epythonguru.com/2020/02/5-Python-projects-for-beginners.html
"""

import tkinter as tk
from tkinter import *
from ttkthemes import ThemedTk
import random

class window(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, root)
        root.title("Guess number game")
        # Gets the requested values of the height and width.
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
        # Positions the window in the center of the page.
        root.geometry("300x130+{}+{}".format(positionRight, positionDown))
        # screen.geometry("210x170")
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self.button = tk.Button(text="Generate new number", command=self.generate).pack()
        self.label = tk.Label(text="Guess number from 0 to 100").pack()
        self.entry = tk.Entry()
        self.entry.pack()
        self.button = tk.Button(text="Click", command=self.guess).pack()
        self.statusbar = tk.Label(text='Welcome', relief=SUNKEN, anchor=W, font='Times 10 italic')
        self.statusbar.pack(side=BOTTOM, fill=X)


    def guess(self):
        try:
            number = int(self.entry.get())
            if number == self.random_number:
                self.statusbar['text'] = "It's your lucky day! You are the winner!"
            elif number > self.random_number:
                self.statusbar['text'] = "It's too much. Try again :)"
            else:
                self.statusbar['text'] = "It's not enough. Try again."
        except:
            self.statusbar['text'] = "First you should generate a number ;)"

    def generate(self):
        self.random_number = random.randint(0, 100)
        print(self.random_number)


if __name__ == "__main__":
    root = ThemedTk(theme="clearlooks")
    window(root).pack(fill="both", expand=True)
    root.mainloop()