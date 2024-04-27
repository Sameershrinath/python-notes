import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        password_result.set("Password length should be at least 4 characters")
        return

    # Characters to be used in generating the password (excluding special characters and operators)
    characters = string.ascii_letters + string.digits  # Only letters (both cases) and digits

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Update result label with the generated password
    password_result.set(password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entry widgets
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = ttk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
length_entry.insert(0, "12")  # Default length

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_result = tk.StringVar()
password_label = ttk.Label(root, textvariable=password_result, wraplength=300)
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
