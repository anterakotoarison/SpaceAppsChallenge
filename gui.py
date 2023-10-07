import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Welcome Screen")

def open_explore_page():
    new_window = tk.Toplevel()
    new_window.title("Explore Page")
    
    choice_label = tk.Label(new_window, text="Choose Data to Explore")
    choice_label.pack()
    choice_label.place(relx=0.5, rely=0.5, anchor="center")

    image = tk.PhotoImage(file="satimage.jpg")  # Replace with the path to your image
    image_label = tk.Label(new_window, image=image)
    image_label.place(relx=0.5, rely=0.5, anchor="center")
    image_label.pack()

# Function to be called when the button is clicked
def open_new_window():
    # Close the main window

    new_window = tk.Toplevel()
    new_window.title("New Window")
    

    # Create content for the new window
    location_label = tk.Label(new_window, text="Insert your location")
    location_label.pack()
    location_label.place(relx=0.5, rely=0.27, anchor="center")

    location_entry = tk.Entry(new_window)
    location_entry.pack()
    location_entry.place(relx=0.5, rely=0.3, anchor="center")
    
    date_label = tk.Label(new_window, text="Insert your data")
    date_label.pack()
    date_label.place(relx=0.5, rely=0.53, anchor="center")

    date_entry = tk.Entry(new_window)
    date_entry.pack()
    date_entry.place(relx=0.5, rely=0.56, anchor="center")

    next_button = tk.Button(new_window, text="NEXT", command=open_explore_page)
    next_button.pack()
    next_button.place(relx=0.5, rely=0.65, anchor="center")

# Create a Label for "WELCOME"
welcome_label = tk.Label(root, text="WELCOME", font=("Helvetica", 24))
# Place it in the center of the window
welcome_label.place(relx=0.5, rely=0.4, anchor="center")

# Create a Button for "START" that opens a new window
start_button = tk.Button(root, text="START", command=open_new_window)
# Place it below the "WELCOME" label
start_button.place(relx=0.5, rely=0.45, anchor="center")

# Configure the window to be full screen
root.attributes('-fullscreen', True)

# Start the tkinter main loop
root.mainloop()
