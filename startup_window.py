import os
import tkinter as tk
from PIL import Image, ImageTk

from main_buttons import MainButtons

class UI:
    # Initialize root window
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing App")
        self.root.geometry("900x620+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 450), 0))
        self.root.bind("<Configure>", self.update_image_size)

        script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the current script directory
        bg_image_path = os.path.join(script_dir, "image_widgets", "ui.png") # Load the background image
        self.bg_image = Image.open(bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label to display the background image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Store the reference to the label to prevent the PhotoImage object from being garbage collected
        self.bg_label.image = self.bg_photo

        # Use tkinter's canvas module 
        canvas = tk.Canvas(self.root)
        canvas.pack(fill="both", expand=True)

        # Create title and descriptive text/contents
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        canvas.create_text(150,100, text="COVID-19", font=("Bold", 35, "bold italic"), fill="white")
        canvas.create_text(160,140, text="CONTACT", font=("Bold", 35, "bold"), fill="blue", activefill="red")
        canvas.create_text(353,140, text="TRACING", font=("Bold", 35, "bold"), fill="red", activefill="blue")
        canvas.create_text(105,180, text="QUEZON CITY", font=("Arial", 12, "bold italic"), fill="light gray", activefill="orange")
        canvas.create_text(270,220, text="This COVID-19 Contact Tracing App is a user-friendly and intuitive application\n"
                           "designed to help individuals track their potential exposure to COVID-19.", font=("Arial", 10), fill="light gray")
        
        '''Create functional texts'''
        # [Icons] Department and menu 
        canvas.create_text(160, 20, text="Department of QC DRRMO", font=("Arial", 10, "underline"), activefill="light gray")
        canvas.create_text(850, 20, text="☰", font=("Arial", 15), activefill="white")

        main_buttons = MainButtons(canvas)

        # [Icons] Privacy policy, contact us, and exit
        canvas.create_text(150, 550, text="Privacy Policy", font=("Arial", 10), activefill="light gray")
        canvas.create_text(300, 550, text="Contact Us", font=("Arial", 10), activefill="light gray")
        exit_text = canvas.create_text(800, 550, text="Exit", font="Arial", fill="black", activefill="red")
        canvas.tag_bind(exit_text, "<Button-1>", self.exit_click)
    
    def exit_click(self, event):    # Exit main window
        self.root.destroy()

    def privacy_policy(self, event):
        pass

    def contact_us(self, event):
        pass

    def menu(self, event):
        pass

    def update_image_size(self, event):
        '''Update image size when window is resized'''
        window_width, window_height = self.root.winfo_width(), self.root.winfo_height() # Get the current window size
        self.resized_bg_image = self.bg_image.resize((window_width, window_height), Image.LANCZOS)    # Resize the image to fill the window while maintaining the aspect ratio
        self.bg_photo = ImageTk.PhotoImage(self.resized_bg_image)
        self.bg_label.config(image=self.bg_photo)   # Update the image on the label

if __name__ == "__main__":  
    root = tk.Tk()
    app = UI(root)
    root.mainloop()