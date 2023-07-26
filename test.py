import os
import tkinter as tk
from PIL import Image, ImageTk

class BackgroundUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing App")
        self.root.geometry("900x620+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 450), 0))
        self.root.bind("<Configure>", self.update_image_size)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        bg_image_path = os.path.join(script_dir, "image_widgets", "app_bg.png")
        self.bg_image = Image.open(bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.image = self.bg_photo

        canvas = tk.Canvas(self.root)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        canvas.create_text(150,100, text="COVID-19", font=("Bold", 35, "bold italic"), fill="white")
        canvas.create_text(160,140, text="CONTACT", font=("Bold", 35, "bold"), fill="blue", activefill="red")
        canvas.create_text(353,140, text="TRACING", font=("Bold", 35, "bold"), fill="red", activefill="blue")
        canvas.create_text(105,180, text="QUEZON CITY", font=("Arial", 12, "bold italic"), fill="light gray", activefill="orange")
        canvas.create_text(270,220, text="This COVID-19 Contact Tracing App is a user-friendly and intuitive application\n"
                           "designed to help individuals track their potential exposure to COVID-19.", font=("Arial", 10), fill="light gray")

        canvas.create_text(160, 20, text="Department of QC DRRMO", font=("Arial", 10, "underline"), activefill="light gray")
        canvas.create_text(850, 20, text="☰", font=("Arial", 15), activefill="white")

        # Function to change button appearance on enter and leave
        def on_button_hover(event):
            if event.type == '7':  # Enter event
                event.widget.config(foreground="black", background="orange")
                event.widget.master.config(background="orange")  # Update the frame's background
            elif event.type == '8':  # Leave event
                event.widget.config(foreground="blue", background=event.widget.original_bg_color)
                event.widget.master.config(background=event.widget.original_bg_color)  # Reset the frame's background

        # Add contact button with background
        add_contact_frame = tk.Frame(canvas, bg="white", padx=5, pady=5)
        canvas.create_window(180, 300, window=add_contact_frame, anchor='nw')

        add_contact_label = tk.Label(add_contact_frame, text="ADD CONTACT", font=("Arial", 12, "bold"))
        add_contact_label.pack(fill="both", expand=True)
        add_contact_label.original_bg_color = "light blue"  # Store the original background color
        add_contact_label.bind("<Enter>", on_button_hover)
        add_contact_label.bind("<Leave>", on_button_hover)

        # Search contact button with background
        search_contact_frame = tk.Frame(canvas, bg="white", padx=5, pady=5)
        canvas.create_window(170, 370, window=search_contact_frame, anchor='nw')

        search_contact_label = tk.Label(search_contact_frame, text="SEARCH CONTACT", font=("Arial", 12, "bold"))
        search_contact_label.pack(fill="both", expand=True)
        search_contact_label.original_bg_color = "light blue"  # Store the original background color
        search_contact_label.bind("<Enter>", on_button_hover)
        search_contact_label.bind("<Leave>", on_button_hover)

    def update_image_size(self, event):
        window_width, window_height = self.root.winfo_width(), self.root.winfo_height()
        self.resized_bg_image = self.bg_image.resize((window_width, window_height), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(self.resized_bg_image)
        self.bg_label.config(image=self.bg_photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundUI(root)
    root.mainloop()
