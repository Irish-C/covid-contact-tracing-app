# button.py
import tkinter as tk
from tkinter import messagebox
import re, subprocess


class Buttons:
    def __init__(self, contact_form_instance, contact_form2_instance):
        self.contact_form_instance = contact_form_instance
        self.contact_form2_instance = contact_form2_instance
        self.previous_window_entries = None
        self.user_data = None

    def next_window(self, event):
        subprocess.call(["python", "contact_form2.py"])
        self.previous_window_entries = None  # Reset previous window entries
        if self.contact_form_instance:
            self.previous_window_entries = self.contact_form_instance.get_entries()
        elif self.contact_form2_instance:
            self.previous_window_entries = self.contact_form2_instance.get_entries2()

    def previous_window(self, event):
        self.contact_form2_instance.second_window.destroy()  # Close the current window
        subprocess.run(["python", "contact_form.py"]) 

    def save_data(self, user_input):
        self.user_data = user_input

    def submit_form(self):
        user_input = None

        if self.contact_form_instance:
            user_input = self.contact_form_instance.get_entries()
        elif self.contact_form2_instance:
            user_input = self.contact_form2_instance.get_entries2()

        try:
            # Format and validate personal information
            first_name = user_input["First Name"]
            last_name = user_input["Last Name"]
            phone_number = re.sub(r'\D', '', user_input["Phone Number"])
            email_address = user_input["Email"]

            fullname = '{} {}'.format(first_name.capitalize(), last_name.capitalize())
            if len(phone_number) != 1:
                raise ValueError("Phone number must have 11 digits.")
            # if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
            #     raise ValueError("Invalid email address.")

            # tk.messagebox.showinfo("Success", "Alright!")

            # Save the form data and proceed to the next window
            self.save_data(user_input)

            return True

        except Exception as e:
            # Display an error message if form validation fails or an error occurs
            tk.messagebox.showerror("Error", str(e))

            return False