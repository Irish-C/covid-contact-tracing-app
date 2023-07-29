# button.py
import tkinter as tk
from tkinter import messagebox
import re, subprocess, csv, os

class Buttons:
    def __init__(self, contact_form_instance, contact_form2_instance):
        self.contact_form_instance = contact_form_instance
        self.contact_form2_instance = contact_form2_instance
        self.previous_window_entries = None
        
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


    def submit_form(self):
        user_input = None
        if self.contact_form_instance:
            user_input = self.contact_form_instance.get_entries()
        elif self.contact_form2_instance:
            user_input = self.contact_form2_instance.get_entries2()
        try:

            dictlist = []
            for key, value in user_input.items():
                entry_dict = {'key': key, 'value': value}
                dictlist.append(entry_dict)

            # Check if the CSV file already exists
            file_path = os.path.join(os.getcwd(), 'contact-tracing-data.csv')
            file_exists = os.path.isfile(file_path)

            with open('contact-tracing-data.csv', 'a', newline='') as file:
                writer = csv.writer(file)

                # If the file doesn't exist, write the header row
                if not file_exists:
                    writer.writerow(list(user_input.keys()) + [''])

                # Write the data row
                writer.writerow(list(user_input.values()) + [''])
                tk.messagebox.showinfo("Success", "Saved Succesfully!")

            return True

        except Exception as e:
            # Display an error message if form validation fails or an error occurs
            tk.messagebox.showerror("Error", str(e))

            return False