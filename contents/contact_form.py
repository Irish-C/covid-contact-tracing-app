import tkinter as tk
from bg_UI import BackgroundUI
import re

class ContactForm(BackgroundUI):
    """ 
    Contact Tracing Form class
    """
    def __init__(self, root):
        # Call the constructor of the parent class (ContactFormUI)
        super().__init__(root)
        self.root.title("Contact Tracing Form")

    # PERSONAL INFORMATION
    def set_personal_information(self, first_name, last_name, phone_number, email_address, address):
        '''
        Reformat and validate user input for personal information
        '''

        # Format and set the full name
        self.__fullname = '{} {}'.format(first_name.capitalize(), last_name.capitalize())

        # Remove non-digit characters from phone number and validate its length
        phone_number = re.sub(r'\D', '', phone_number)
        if len(phone_number) != 11:
            raise ValueError("Phone number must have 11 digits.")
        self.__phone_number = phone_number

        # Validate email address format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
            raise ValueError("Invalid email address.")
        self.__email_address = email_address

        # Set the address
        self.__address = address

    # HEALTH INFORMATION
    def set_health_information(self, symptoms, symptom_onset, tested_positive, test_date="", test_result=""):
        self.__symptoms = symptoms
        self.__symptom_onset = symptom_onset
        self.__tested_positive = tested_positive
        self.__test_date = test_date
        self.__test_result = test_result

    # A method that add close contact into lists
    def add_close_contact(self, name, contact_details):
        self.close_contacts.append({'name': name, 'contact_details': contact_details})

    # A method that add travel history into lists
    def add_travel_history(self, location, date):
        self.travel_history.append({'location': location, 'date': date})

    # A method that sets consent to TRUE
    def give_consent(self):
        self.consent = True

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactForm(root)
    root.mainloop()