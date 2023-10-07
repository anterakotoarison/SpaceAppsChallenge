# NASA Space Apps Challenge 2023
# Canadian Space Agency Challenge 1 (Moonwalker)
# Written by Nicole Tan and Antenaina Rakotoarison
# October 7 - 8 2023
#gui.py

#This file contains the gui code


#import libraries
import tkinter as tk

# Create the main application window
root = tk.Tk()

root.title("Title of Window")
# Maximize the window to fill the screen
root.attributes('-fullscreen', True)

welcome_label = tk.Label(root, text="WELCOME", font=("Helvetica", 24))
welcome_label.pack(pady=20)  # Add padding to space it from the button
welcome_label.place(relx=0.5, rely=0.4, anchor="center")

# Function to be called when the button is clicked
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("400x300")

    # Create content for the new window
    new_label = tk.Label(new_window, text="This is the new window!")
    new_label.pack()

# Create a clickable button
start_button = tk.Button(root, text="START", command=open_new_window)
start_button.pack()
start_button.place(relx=0.5, rely=0.5, anchor="center")


# Start the tkinter main loop
root.mainloop()

