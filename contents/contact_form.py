import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

import re


class ContactForm:
    '''Contact Tracing Form'''
    def __init__(self, add_contact_window):
        self.add_contact_window = add_contact_window
        self.add_contact_window.title("ContacTracing Form")
        self.add_contact_window.geometry("900x620+{}+{}".format(int(self.add_contact_window.winfo_screenwidth() / 2 - 450), 0))

        self.image = PhotoImage(file="image_widgets/ui_bg.png")    # Load the image using PhotoImage
        
        # Create a canvas inside the add_contact_window
        self.canvas = tk.Canvas(self.add_contact_window, bd=0)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the background image on the canvas
        self.canvas.image = self.image  # Keep a reference to the image
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        
        '''Ask user of their personal information'''
        # Personal Information inside the canvas
        self.personal_info_frame = tk.Frame(self.canvas)
        self.personal_info_frame.pack(padx=100, pady=50)

        # Label for Personal Information
        self.label_personal_info = tk.Label(self.personal_info_frame, text="\nPERSONAL INFORMATION\n", font=("Arial", 11),justify="center")
        self.label_personal_info.grid(row=0, column=0, columnspan=5)

        # Create labels and entry fields for personal information
        self.name_label = tk.Label(self.personal_info_frame, text="Name:", font=("Arial", 11))
        self.name_label.grid(row=1, column=0)

        self.entry_first_name = tk.Entry(self.personal_info_frame, justify="center")
        self.entry_first_name.grid(row=1, column=1)
        self.entry_last_name = tk.Entry(self.personal_info_frame, justify="center")
        self.entry_last_name.grid(row=1, column=2)
        self.entry_middle_initial = tk.Entry(self.personal_info_frame, justify="center",)
        self.entry_middle_initial.grid(row=1, column=3)
        self.entry_name_suffix = ttk.Combobox(self.personal_info_frame, values=["", "Sr.", "Jr.", "III", "IV"])
        self.entry_name_suffix.grid(row=1, column=4)

        self.label_first_name = tk.Label(self.personal_info_frame, text="First Name", font=("Arial", 9, "italic"))
        self.label_first_name.grid(row=2, column=1)
        self.label_last_name = tk.Label(self.personal_info_frame, text="Last Name", font=("Arial", 9, "italic"))
        self.label_last_name.grid(row=2, column=2)
        self.label_middle_initial = tk.Label(self.personal_info_frame, text="M.I.", font=("Arial", 9, "italic"))
        self.label_middle_initial.grid(row=2, column=3)
        self.label_name_suffix = tk.Label(self.personal_info_frame, text="Suffix", font=("Arial", 9, "italic"))
        self.label_name_suffix.grid(row=2, column=4)

    # # PERSONAL INFORMATION
    # def set_personal_information(self, first_name, last_name, phone_number, email_address, address):
    #     '''
    #     Reformat and validate user input for personal information
    #     '''

    #     # Format and set the full name
    #     self.__fullname = '{} {}'.format(first_name.capitalize(), last_name.capitalize())

        # Validate email address format
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        #     raise ValueError("Invalid email address.")
        # self.__email_address = email_address

        # # Set the address
        # self.__address = address

    #     # Set the address
    #     self.__address = address

    # # A method that add close contact into lists
    # def add_close_contact(self, name, contact_details):
    #     self.close_contacts.append({'name': name, 'contact_details': contact_details})

    # # A method that add travel history into lists
    # def add_travel_history(self, location, date):
    #     self.travel_history.append({'location': location, 'date': date})

    # # A method that sets consent to TRUE
    # def give_consent(self):
    #     self.consent = True

if __name__ == "__main__":
    add_contact_window= tk.Tk()
    app = ContactForm(add_contact_window)
    add_contact_window.mainloop()