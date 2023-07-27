import tkinter as tk
from contents.contact_form import ContactForm

class ContactForm2(ContactForm):
    '''Contact Tracing Form Part 2'''
    def __init__(self, add_contact_window):
        super().__init__(add_contact_window)

        self.emergency_info()

    def emergency_info(self):
        pass

