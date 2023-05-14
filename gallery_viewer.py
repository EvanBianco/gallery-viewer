import os
import sys
from PIL import Image, ImageTk
import tkinter as tk

# Set the directory containing the images
image_dir = "images"

# Get a list of all the image file names in the directory
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Set the initial image index to 0
current_image_index = 0

# Create a function to display the current image
def show_image():
    # Get the current image file name
    current_image_file = image_files[current_image_index]
    
    # Load the image using the Pillow library
    img = Image.open(os.path.join(image_dir, current_image_file))
    
    # Create a Tkinter window and display the image in it
    root = tk.Tk()
    root.title(current_image_file)
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.pack()
    
    # Create a function to handle key press events
    def on_key_press(event):
        global current_image_index
        
        # If the left arrow key is pressed, go to the previous image
        if event.keysym == "Left":
            if current_image_index > 0:
                current_image_index -= 1
        
        # If the right arrow key is pressed, go to the next image
        elif event.keysym == "Right":
            if current_image_index < len(image_files) - 1:
                current_image_index += 1
        
        # If the Escape key is pressed, close the window
        elif event.keysym == "Escape":
            root.destroy()
            sys.exit()
        
        # Update the image displayed in the window
        img = Image.open(os.path.join(image_dir, image_files[current_image_index]))
        tk_img.paste(img)
        root.title(image_files[current_image_index])
    
    # Bind the key press event to the window
    root.bind("<Key>", on_key_press)
    
    # Start the Tkinter main loop
    root.mainloop()

# Show the initial image
show_image()
