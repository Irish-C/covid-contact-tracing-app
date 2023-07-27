import os, subprocess, sys
import tkinter as tk
from PIL import Image, ImageTk

class MainButtons:
    '''constains add contact and search contact buttons'''
    def __init__(self, canvas):
        # Add contact button with background
        add_contact_frame = tk.Frame(canvas, bg="white", padx=5, pady=5)
        canvas.create_window(180, 300, window=add_contact_frame, anchor='nw')

        add_contact_label = tk.Label(add_contact_frame, text="ADD CONTACT", font=("Arial", 12, "bold"))
        add_contact_label.pack(fill="both", expand=True)
        add_contact_label.original_bg_color = "light blue"  # Store the original background color
        add_contact_label.bind("<Enter>", self.on_button_hover)
        add_contact_label.bind("<Leave>", self.on_button_hover)
        add_contact_label.bind("<Button-1>", self.open_contact_form)
    
        # Search contact button with background
        search_contact_frame = tk.Frame(canvas, bg="white", padx=5, pady=5)
        canvas.create_window(165, 370, window=search_contact_frame, anchor='nw')

        search_contact_label = tk.Label(search_contact_frame, text="SEARCH CONTACT", font=("Arial", 12, "bold"))
        search_contact_label.pack(fill="both", expand=True)
        search_contact_label.original_bg_color = "light blue"  # Store the original background color
        search_contact_label.bind("<Enter>", self.on_button_hover)
        search_contact_label.bind("<Leave>", self.on_button_hover)

    def on_button_hover(self, event):
        if event.type == '7':  # Enter event
            event.widget.config(foreground="black", background="orange")
            event.widget.master.config(background="orange")  # Update the frame's background
        elif event.type == '8':  # Leave event
            event.widget.config(foreground="blue", background=event.widget.original_bg_color)
            event.widget.master.config(background=event.widget.original_bg_color)  # Reset the frame's background

    def open_contact_form(self, event):
        # Open the contact form using subprocess
        subprocess.Popen(["python", "contents/contact_form.py"])

    def open_search_data():
        pass