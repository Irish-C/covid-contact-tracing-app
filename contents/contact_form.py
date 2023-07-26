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

        # Create a label with the loaded image as the background
        self.background_label = tk.Label(self.add_contact_window, image=self.image)
        self.background_label.pack(fill=tk.BOTH, expand=tk.YES)

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