import random
import tkinter as tk
from tkinter import messagebox

def start_game():
    global TargetNumber, Guesses
    TargetNumber = random.randint(1, 100)
    Guesses = 0
    guess_entry.config(state='normal')
    submit_button.config(state='normal')
    status_label.config(text="I'm thinking of a number between 1 and 100. Try to guess it!")

def check_guess():
    global Guesses
    try:
        UserNumber = int(guess_entry.get())
        Guesses += 1
        if UserNumber < TargetNumber:
            status_label.config(text='Your guess is lower than my number.')
        elif UserNumber > TargetNumber:
            status_label.config(text='Your guess is higher than my number.')
        else:
            messagebox.showinfo('Congratulations', f'You have guessed the number {TargetNumber} in {Guesses} guesses!')
            guess_entry.config(state='disabled')
            submit_button.config(state='disabled')
    except ValueError:
        messagebox.showerror('Invalid Input', 'Please enter a valid integer.')

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create and place widgets
instructions = tk.Label(root, text="Guess the number I'm thinking of between 1 and 100.")
instructions.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

start_button = tk.Button(root, text="Start New Game", command=start_game)
start_button.pack()

# Initialize game
start_game()

# Run the application
root.mainloop()