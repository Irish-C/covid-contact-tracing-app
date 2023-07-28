import tkinter as tk
from tkinter import messagebox
import re, csv, subprocess

class Buttons:
    def __init__(self, contact_form_instance, contact_form2_instance):
        self.contact_form_instance = contact_form_instance
        self.contact_form2_instance = contact_form2_instance

    def next_window(self, event):
        subprocess.Popen(["python", "contact_form2.py"])

    def previous_window(self, event):
        subprocess.Popen(["python", "contact_form.py"])

    def save_to_csv(self, user_input):
        fieldnames = [
            "First Name", "Last Name", "Middle Initial", "Name Suffix",
            "Phone Number", "Email", "Address", "Vaccination Status",
            "COVID Symptoms", "Other Symptoms", "Tested for COVID",
            "Testing Date", "Test Result", "Emergency Name", "Emergency Phone/Email",
            "Emergency Address", "Relationship", "Travel History", "Travel Details"
        ]

        file_path = "contact_form_data.csv"

        if not user_input:
            return

        # # Check if the file exists or create a new one
        # if tk.messagebox.askyesno("File Exists", "Do you want to append to the existing file?"):
        #     file_mode = "a"
        else:
            file_mode = "w"

        with open(file_path, mode=file_mode, newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file_mode == "w":
                writer.writeheader()

            writer.writerow(user_input)

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
            if len(phone_number) != 11:
                raise ValueError("Phone number must have 11 digits.")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
                raise ValueError("Invalid email address.")

            # Save data to CSV file after form validation passes
            self.save_to_csv(user_input)

            # # Display a success message if the form is submitted successfully
            # tk.messagebox.showinfo("Success", "Form submitted successfully!")



        except Exception as e:
            # Display an error message if form validation fails or an error occurs
            tk.messagebox.showerror("Error", str(e))