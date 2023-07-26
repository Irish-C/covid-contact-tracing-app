import tkinter as tk
from tkinter import PhotoImage

import re


class ContactForm:
    '''Contact Tracing Form'''
    def __init__(self, add_contact_window):
        self.add_contact_window = add_contact_window
        self.add_contact_window.title("ContacTracing Form")
        self.add_contact_window.geometry("900x620+{}+{}".format(int(self.add_contact_window.winfo_screenwidth() / 2 - 450), 0))

        self.image = PhotoImage(file="image_widgets/app_bg.png")    # Load the image using PhotoImage
        
                            # # Create a label with the loaded image as the background
                            # self.background_label = tk.Label(self.add_contact_window, image=self.image)
                            # self.background_label.pack(fill=tk.BOTH, expand=tk.YES)

        # Create a canvas inside the add_contact_window
        self.canvas = tk.Canvas(self.add_contact_window, bd=0)
        self.canvas.pack(fill="both", expand=True)

        # Personal Information inside the canvas
        self.personal_info_frame = tk.Frame(self.canvas, bg="")
        self.personal_info_frame.pack()

        # Load and display the background image on the canvas
        self.canvas.image = self.image  # Keep a reference to the image
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        
        # Create labels and entry fields for personal information
        self.label_first_name = tk.Label(self.personal_info_frame, text="First Name:")
        self.label_first_name.grid(row=0, column=0)
        self.entry_first_name = tk.Entry(self.personal_info_frame)
        self.entry_first_name.grid(row=0, column=1)

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