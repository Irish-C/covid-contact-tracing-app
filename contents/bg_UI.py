import os
import tkinter as tk
from PIL import Image, ImageTk

class BackgroundUI:
    # Initialize root window
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing App")
        self.root.geometry("800x620+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 400), 0))
        self.root.bind("<Configure>", self.update_bg_image)

        # Get the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the background image
        bg_image_path = os.path.join(script_dir, "image_widgets", "app_bg.png")
        self.bg_image = Image.open(bg_image_path)
        self.update_bg_image()  # Call the function to resize and update the background image

        
    def update_bg_image(self, event=None):
        # Get the current window size
        window_width, window_height = self.root.winfo_width(), self.root.winfo_height()

        # Resize the background image to match the window size
        self.resized_bg_image = self.bg_image.resize((window_width, window_height), Image.ANTIALIAS)

        # Convert the image to PhotoImage to use with Label
        self.bg_photo = ImageTk.PhotoImage(self.resized_bg_image)

        # Create a label to display the background image
        if hasattr(self, 'bg_label'):
            # If the label already exists, update the image
            self.bg_label.config(image=self.bg_photo)
        else:
            # If the label does not exist, create it
            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundUI(root)
    root.mainloop()