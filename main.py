import tkinter as tk
import random
import string
import pyperclip

def generate_password():
   password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
   password_label.config(text=password)
   pyperclip.copy(password)
   return password

def copy_password():
   password = generate_password()

root = tk.Tk()

# Set the window size to be at least 30% of the screen width
screen_width = root.winfo_screenwidth()
root.geometry(f"{int(screen_width * 0.3)}x200")

welcome_label = tk.Label(root, text="WELCOME TO DAY 6", cursor="hand2")
welcome_label.pack()

password_label = tk.Label(root, text="", cursor="hand2")
password_label.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()


root.mainloop()
