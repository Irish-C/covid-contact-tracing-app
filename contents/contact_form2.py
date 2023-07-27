import tkinter as tk
from tkinter import ttk, PhotoImage
import tkcalendar

class ContactForm:
    '''Contact Tracing Form Part 2'''
    def __init__(self, add_contact_window):
        self.add_contact_window = add_contact_window
        self.add_contact_window.title("Contact Tracing Form")
        self.add_contact_window.geometry("900x620+{}+{}".format(int(self.add_contact_window.winfo_screenwidth() / 2 - 450), 0))

        self.image = PhotoImage(file="image_widgets/ui.png")    # Load the image using PhotoImage

        # Create a canvas inside the add_contact_window
        self.canvas = tk.Canvas(self.add_contact_window, bd=0)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the background image on the canvas
        self.canvas.image = self.image  # Keep a reference to the image
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)

        # Heading
        self.canvas.create_text(320,25, text="CONTACTRACINGFORM", font=("Arial", 25, "bold"), fill="blue")
        self.canvas.create_text(341,25, text="TRACING", font=("Arial", 25, "bold"), fill="red")
        # Call personal info and health info methods

        self.emergency_info()
        self.travel_history()

    def emergency_info(self):
        pass

    def travel_history(self):
        pass