# startup_window.py
import os
import tkinter as tk
from PIL import Image, ImageTk

from main_buttons import MainButtons

class UI:
    # Initialize root window
    def __init__(self, root):
        self.__root = root
        self.__root.title("COVID-19 Contact Tracing App")
        self.__root.geometry("900x620+{}+{}".format(int(self.__root.winfo_screenwidth() / 2 - 450), 0))
        self.__root.bind("<Configure>", self.__update_image_size)

        script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the current script directory
        bg_image_path = os.path.join(script_dir, "image_widgets", "ui.png") # Load the background image
        self.__bg_image = Image.open(bg_image_path)
        self.__bg_photo = ImageTk.PhotoImage(self.__bg_image)

        # Create a label to display the background image
        self.__bg_label = tk.Label(self.__root, image=self.__bg_photo)
        self.__bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Store the reference to the label to prevent the PhotoImage object from being garbage collected
        self.__bg_label.image = self.__bg_photo

        # Use tkinter's canvas module 
        self.__canvas = tk.Canvas(self.__root)
        self.__canvas.pack(fill="both", expand=True)

        # Create title and descriptive text/contents
        self.__canvas.create_image(0, 0, image=self.__bg_photo, anchor='nw')
        self.__canvas.create_text(150,100, text="COVID-19", font=("Bold", 35, "bold italic"), fill="white")
        self.__canvas.create_text(160,140, text="CONTACT", font=("Bold", 35, "bold"), fill="blue", activefill="red")
        self.__canvas.create_text(353,140, text="TRACING", font=("Bold", 35, "bold"), fill="red", activefill="blue")
        self.__canvas.create_text(105,180, text="QUEZON CITY", font=("Arial", 12, "bold italic"), fill="light gray", activefill="orange")
        self.__canvas.create_text(270,220, text="This COVID-19 Contact Tracing App is a user-friendly and intuitive application\n"
                           "designed to help individuals track their potential exposure to COVID-19.", font=("Arial", 10), fill="light gray")
        
        '''Create functional texts'''
        # [Icons] Department and menu 
        self.__canvas.create_text(160, 20, text="Department of QC DRRMO", font=("Arial", 10, "underline"), activefill="light gray")
        self.__canvas.create_text(850, 20, text="☰", font=("Arial", 15), activefill="white")

        main_buttons = MainButtons(self.__canvas)

        # [Icons] Privacy policy, contact us, and exit
        self.__canvas.create_text(150, 550, text="Privacy Policy", font=("Arial", 10), activefill="light gray")
        self.__canvas.create_text(300, 550, text="Contact Us", font=("Arial", 10), activefill="light gray")
        exit_text = self.__canvas.create_text(800, 550, text="Exit", font="Arial", fill="black", activefill="red")
        self.__canvas.tag_bind(exit_text, "<Button-1>", self.__exit_click)
    
    def __exit_click(self, event):    # Exit main window
        self.__root.destroy()

    def __privacy_policy(self, event):
        pass

    def __contact_us(self, event):
        pass

    def __menu(self, event):
        pass

    def __update_image_size(self, event):
        '''Update image size when window is resized'''
        window_width, window_height = self.__root.winfo_width(), self.__root.winfo_height() # Get the current window size
        self.__resized_bg_image = self.__bg_image.resize((window_width, window_height), Image.LANCZOS)    # Resize the image to fill the window while maintaining the aspect ratio
        self.__bg_photo = ImageTk.PhotoImage(self.__resized_bg_image)
        self.__bg_label.config(image=self.__bg_photo)   # Update the image on the label

