import os
import tkinter as tk
from PIL import Image, ImageTk

class ContactFormGUI:
    # Initialize root window
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing App")
        self.root.geometry("800x620+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 400), 0))

        # Get the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the background image
        bg_image_path = os.path.join(script_dir, "image_widgets", "app_bg.png")
        self.bg_image = Image.open(bg_image_path)
