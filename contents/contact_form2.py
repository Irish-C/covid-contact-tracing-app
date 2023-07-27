import tkinter as tk
from tkinter import ttk, PhotoImage
import tkcalendar

class ContactForm:
    '''Contact Tracing Form'''
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
        # Emergency Contact Information Frame
        self.emergency_frame = tk.Frame(self.add_contact_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.emergency_frame.place(x=100, y=50, width=700, height=220)

        # Label for Emergency Contact Information
        self.label_emergency_info = tk.Label(self.emergency_frame, text="\nEMERGENCY CONTACT INFORMATION\n", 
                                            font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.label_emergency_info.grid(row=0, column=0, columnspan=2)

        # Name label and entry
        other_name_label = tk.Label(self.emergency_frame, text="\tName:", font=("Arial", 10))
        other_name_label.grid(row=1, column=0, sticky="w")
        other_name_entry = ttk.Entry(self.emergency_frame, justify="center")
        other_name_entry.grid(row=1, column=1)

        # Phone number/email label and entry
        phone_email_label = tk.Label(self.emergency_frame, text="\tPhone Number/Email:", font=("Arial", 10))
        phone_email_label.grid(row=2, column=0, sticky="w")
        phone_email_entry = ttk.Entry(self.emergency_frame, justify="center")
        phone_email_entry.grid(row=2, column=1)

        # Address label and entry
        other_address_label = tk.Label(self.emergency_frame, text="\tAddress:", font=("Arial", 10))
        other_address_label.grid(row=3, column=0, sticky="w")
        other_address_entry = ttk.Entry(self.emergency_frame, width=50, justify="center")
        other_address_entry.grid(row=3, column=1, columnspan=4, padx=38)

        # Relationship label and entry
        relationship_label = tk.Label(self.emergency_frame, text="\tRelationship:", font=("Arial", 10))
        relationship_label.grid(row=4, column=0, sticky="w")
        self.entry_name_suffix = ttk.Combobox(self.emergency_frame, values=["Parent", "Guardian", "Sibling", "Relative", "Acquaintance", "Romantic Partner"])
        self.entry_name_suffix.grid(row=4, column=1)

    def travel_history(self):
        pass

if __name__ == "__main__":
    add_contact_window = tk.Tk()
    app = ContactForm(add_contact_window)
    add_contact_window.mainloop()