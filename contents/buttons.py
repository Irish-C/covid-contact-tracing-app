import tkinter as tk
from tkinter import messagebox
import re, subprocess, csv

class Buttons:
    # We treat content form 2 as the next window
    '''found in content form window'''
    def next_window(self, event):
        subprocess.Popen(["python", "contents/contact_form2.py"])

    # We treat content form as the previous window
    '''found in content form 2 window'''
    def previous_window(self, event):
        subprocess.Popen(["python", "contents/contact_form.py"])

    def save_to_csv(self, user_input):
        # Define the field names for the CSV file
        fieldnames = ["First Name", "Last Name", "Middle Initial", "Name Suffix",
                      "Phone Number", "Email", "Address", "Vaccination Status",
                      "COVID Symptoms", "Other Symptoms", "Tested for COVID",
                      "Testing Date", "Test Result", "Emergency Name", "Emergency Phone/Email",
                      "Emergency Address", "Relationship", "Travel History", "Travel Details"]

        # Get the file path where you want to save the CSV file
        file_path = "contact_form_data.csv"

        # Check if the file exists or create a new one
        file_exists = tk.messagebox("File Exists", "Do you want to append to the existing file?")
        with open(file_path, mode="a" if file_exists else "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header if the file is newly created
            if not file_exists:
                writer.writeheader()
            # Write the user input data to the CSV file
            writer.writerow(user_input)

        # Clear entry fields
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_middle_initial.delete(0, tk.END)
        self.entry_name_suffix.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def submit_form(self):
        try:
            # Get the user input
            user_input = {
                "First Name": self.first_name_entry.get(),
                "Last Name": self.last_name_entry.get(),
                "Middle Initial": self.entry_middle_initial.get(),
                "Name Suffix": self.entry_name_suffix.get(),
                "Phone Number": self.phone_entry.get(),
                "Email": self.email_entry.get(),
                "Address": self.address_entry.get(),
                "Vaccination Status": self.vaccination_choice.get(),
                "COVID Symptoms": self.symptoms_choice.get(),
                "Other Symptoms": self.other_symptoms_entry.get(),
                "Tested for COVID": self.testing_choice.get(),
                "Testing Date": self.date_entry.get(),
                "Test Result": self.result_choice.get(),
                "Emergency Name": self.emergency_name_entry.get(),
                "Emergency Phone/Email": self.emergency_phone_email_entry.get(),
                "Emergency Address": self.emergency_address_entry.get(),
                "Relationship": self.entry_name_suffix.get(),
                "Travel History": self.travel_choice_var.get(),
                "Travel Details": self.travel_details_entry.get("1.0", tk.END).strip()
            }

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

            # Save data to CSV file in "append" mode after form validation passes
            self.save_to_csv(user_input)

            # Display a success message if the form validation passes
            tk.messagebox.showinfo("Success", "Form submitted successfully!")

        except Exception as e:
            # Display an error message if form validation fails
            tk.messagebox.showerror("Error", str(e))