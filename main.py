# NASA Space Apps Challenge 2023
# Canadian Space Agency Challenge 1 (Moonwalker)
# Written by Nicole Tan and Antenaina Rakotoarison
# October 7 - 8 2023

#import libraries
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Space Date Explore Application")

def open_final_summary():
    new_window = tk.Toplevel()
    new_window.title("Summary Page")

    initial_width = 800
    initial_height = 1000
    new_window.geometry(f"{initial_width}x{initial_height}")

    background_image = PhotoImage(file="images/Satellite Altitudes.png")  # Replace with the path to your image

    # Create a label to display the background image
    background_label = tk.Label(new_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)  

    # Create other widgets (labels, buttons, etc.) here

    # Keep a reference to the background image
    new_window.background_image = background_image

def exit_app():
        root.destroy()

def open_explore_page():
    for widget in root.winfo_children():
        widget.destroy()

    background_image = PhotoImage(file="images/explore_background.png")  # Replace with the path to your image

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  

    # Create other widgets (labels, buttons, etc.) here

    # Keep a reference to the background image
    root.background_image = background_image

    choice_label = tk.Label(root, text="Choose Data to Explore", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    choice_label.pack()
    choice_label.place(relx=0.5, rely=0.49, anchor="center")

    altitude_button = tk.Button(root, text="VIEW DIFFERENT SATELLITES ALTITUDE RANGES", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    altitude_button.pack()
    altitude_button.place(relx=0.26, rely=0.26, anchor="center")

    weather_button = tk.Button(root, text="VIEW SPACE WEATHER FORECAST", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    weather_button.pack()
    weather_button.place(relx=0.76, rely=0.26, anchor="center")

    deorbiting_button = tk.Button(root, text="VIEW DE-ORBITING SATELLITES", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    deorbiting_button.pack()
    deorbiting_button.place(relx=0.26, rely=0.76, anchor="center")

    near_button = tk.Button(root, text="VIEW NEAR-EARTH ASTERIODS AND CLOSE APPROACHES", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    near_button.pack()
    near_button.place(relx=0.76, rely=0.76, anchor="center")

    back_button = tk.Button(root, text="BACK", command=open_new_window , padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    back_button.pack()
    back_button.place(relx=0.5, rely=0.57, anchor="center")

    summary_button = tk.Button(root, text="FINAL SUMMARY REPORT", command=open_final_summary , padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    summary_button.pack()
    summary_button.place(relx=0.5, rely=0.53, anchor="center")

    exit_button = tk.Button(root, text="EXIT", command=exit_app, padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    exit_button.place(relx=0.05, rely=0.05, anchor="center")

    
    
# Function to be called when the button is clicked
def open_new_window():
    for widget in root.winfo_children():
        widget.destroy()

    background_image = Image.open("images/bgdimage.png")  # Replace with the path to your image

    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(background_image)

    # Create a Label to display the background image
    background_label = tk.Label(root, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Keep a reference to the photo to prevent it from being garbage collected
    background_label.photo = photo
    
    initial_width = 1070
    initial_height = 1050
    root.geometry(f"{initial_width}x{initial_height}")
    # Create content for the new window
    location_label = tk.Label(root, text="Insert your location", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    location_label.pack()
    location_label.place(relx=0.5, rely=0.27, anchor="center")

    location_entry = tk.Entry(root)
    location_entry.pack()
    location_entry.place(relx=0.5, rely=0.3, anchor="center")
    
    date_label = tk.Label(root, text="Insert your data", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    date_label.pack()
    date_label.place(relx=0.5, rely=0.53, anchor="center")

    date_entry = tk.Entry(root)
    date_entry.pack()
    date_entry.place(relx=0.5, rely=0.56, anchor="center")

    next_button = tk.Button(root, text="NEXT", command=open_explore_page, padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    next_button.pack()
    next_button.place(relx=0.5, rely=0.65, anchor="center")

    back_button = tk.Button(root, text="BACK", command=open_main_window, padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    back_button.pack()
    back_button.place(relx=0.05, rely=0.05, anchor="center")

def open_main_window():
    for widget in root.winfo_children():
        widget.destroy()

    background_image = Image.open("images/nextbgd.png")  # Replace with the path to your image

    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(background_image)

    # Create a Label to display the background image
    background_label = tk.Label(root, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Keep a reference to the photo to prevent it from being garbage collected
    background_label.photo = photo  

    # Create other widgets (labels, buttons, etc.) here

    # # Keep a reference to the background image
    # root.background_image = background_image
    # Create a Label for "WELCOME"
    welcome_label = tk.Label(root, text="WELCOME", padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    # Place it in the center of the window
    welcome_label.place(relx=0.5, rely=0.4, anchor="center")

    # Create a Button for "START" that opens a new window
    start_button = tk.Button(root, text="START", command=open_new_window, padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    # Place it below the "WELCOME" label
    start_button.place(relx=0.5, rely=0.45, anchor="center")

    exit_button = tk.Button(root, text="EXIT", command=exit_app, padx=0, pady=0, borderwidth=0, highlightthickness=0, compound="top")
    exit_button.place(relx=0.05, rely=0.05, anchor="center")

def main():

    initial_width = 1070
    initial_height = 1050
    root.geometry(f"{initial_width}x{initial_height}")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - initial_width) // 2
    y = (screen_height - initial_height) // 2

    # Set the window's position and size
    root.geometry(f"{initial_width}x{initial_height}+{x}+{y}")

    # Configure the window to be full screen
    #root.attributes('-fullscreen', True)

    # Start the tkinter main loop

    open_main_window()
    #style = ttk.Style('yeti')
    root.mainloop()


if __name__ == "__main__":
    main()