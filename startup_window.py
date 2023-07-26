import os
import tkinter as tk
from PIL import Image, ImageTk

class BackgroundUI:
    # Initialize root window
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing App")
        self.root.geometry("900x620+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 450), 0))
        self.root.bind("<Configure>", self.update_image_size)

        script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the current script directory
        bg_image_path = os.path.join(script_dir, "image_widgets", "app_bg.png") # Load the background image
        self.bg_image = Image.open(bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label to display the background image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Store the reference to the label to prevent the PhotoImage object from being garbage collected
        self.bg_label.image = self.bg_photo

        # Add Texts
        canvas = tk.Canvas(self.root)
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        canvas.create_text(150, 20, text="Department of QC DRRMO", font=("Arial", 10))
        canvas.create_text(150,100, text="COVID-19", font=("Bold", 35, "bold italic"), fill="white")
        canvas.create_text(160,135, text="CONTACT", font=("Bold", 35, "bold"), fill="blue")
        canvas.create_text(353,135, text="TRACING", font=("Bold", 35, "bold"), fill="red")
        canvas.create_text(105,180, text="QUEZON CITY", font=("Arial", 12, "bold italic"), fill="gray")
        canvas.create_text(265,210, text="This COVID-19 Contact Tracing App is a user-friendly and intuitive application", font=("Arial", 10), fill="gray")
        canvas.create_text(255,225, text="designed to help individuals track their potential exposure to COVID-19.", font=("Arial", 10), fill="gray")
        canvas.pack(fill="both", expand=True)

    def update_image_size(self, event):
        '''Update image size when window is resized'''
        window_width, window_height = self.root.winfo_width(), self.root.winfo_height() # Get the current window size
        self.resized_bg_image = self.bg_image.resize((window_width, window_height), Image.ANTIALIAS)    # Resize the image to fill the window while maintaining the aspect ratio
        self.bg_photo = ImageTk.PhotoImage(self.resized_bg_image)
        self.bg_label.config(image=self.bg_photo)   # Update the image on the label

if __name__ == "__main__":  
    root = tk.Tk()
    app = BackgroundUI(root)
    root.mainloop()