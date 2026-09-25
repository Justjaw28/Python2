import tkinter as tk
import random

root = tk.Tk()

# Setting some window properties
root.title("Tk Example")
root.configure(background="black")
root.minsize(200, 200)
root.geometry("900x500+50+50")

tk.Label(root, text="Hello! I am a window!", font=("Arial", 24), fg="white", bg="black").pack(pady=20)

def reroll():
    # Rolling a number
    dice_roll = random.randint(1, 100)
    tk.Label(root, text=f"You rolled: {dice_roll}", font=("Arial", 15), fg="white", bg="black").pack(pady=10)

reroll()

def key_pressed(event):
    reroll()

root.bind("<space>", key_pressed)

root.mainloop()