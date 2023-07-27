import tkinter as tk
import re

class ContactFormGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Tracing Form")

        # Create labels and entry fields for personal information
        self.lbl_first_name = tk.Label(self, text="First Name:")
        self.lbl_first_name.pack()
        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.pack()

        self.lbl_last_name = tk.Label(self, text="Last Name:")
        self.lbl_last_name.pack()
        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.pack()

        self.lbl_phone_number = tk.Label(self, text="Phone Number:")
        self.lbl_phone_number.pack()
        self.entry_phone_number = tk.Entry(self)
        self.entry_phone_number.pack()

        self.lbl_email_address = tk.Label(self, text="Email Address:")
        self.lbl_email_address.pack()
        self.entry_email_address = tk.Entry(self)
        self.entry_email_address.pack()

        self.lbl_address = tk.Label(self, text="Address:")
        self.lbl_address.pack()
        self.entry_address = tk.Entry(self)
        self.entry_address.pack()

        # Create a button to submit the form
        self.btn_submit = tk.Button(self, text="Submit", command=self.submit_form)
        self.btn_submit.pack()

    def submit_form(self):
        try:
            # Get the user input
            first_name = self.entry_first_name.get()
            last_name = self.entry_last_name.get()
            phone_number = self.entry_phone_number.get()
            email_address = self.entry_email_address.get()
            address = self.entry_address.get()

            # Format and validate personal information
            fullname = '{} {}'.format(first_name.capitalize(), last_name.capitalize())
            phone_number = re.sub(r'\D', '', phone_number)
            if len(phone_number) != 11:
                raise ValueError("Phone number must have 11 digits.")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
                raise ValueError("Invalid email address.")

            # Display a success message if the form validation passes
            tk.messagebox.showinfo("Success", "Form submitted successfully!")
        except Exception as e:
            # Display an error message if form validation fails
            tk.messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = ContactFormGUI()
    app.mainloop()









import tkinter as tk
from PIL import Image
class ContactFormGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Contact Tracing Form")
        
        # Create labels and entry fields for personal information
        personal_info_label = tk.Label(root, text="Personal Information")
        personal_info_label.pack()

        first_name_label = tk.Label(root, text="First Name:")
        first_name_label.pack()
        self.first_name_entry = tk.Entry(root)
        self.first_name_entry.pack()

        last_name_label = tk.Label(root, text="Last Name:")
        last_name_label.pack()
        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.pack()

        phone_label = tk.Label(root, text="Phone Number:")
        phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        email_label = tk.Label(root, text="Email Address:")
        email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        address_label = tk.Label(root, text="Address:")
        address_label.pack()
        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        # Create labels and entry fields for health information
        health_info_label = tk.Label(root, text="Health Information")
        health_info_label.pack()

        symptoms_label = tk.Label(root, text="Symptoms:")
        symptoms_label.pack()
        self.symptoms_entry = tk.Entry(root)
        self.symptoms_entry.pack()

        symptom_onset_label = tk.Label(root, text="Symptom Onset Date:")
        symptom_onset_label.pack()
        self.symptom_onset_entry = tk.Entry(root)
        self.symptom_onset_entry.pack()

        tested_positive_label = tk.Label(root, text="Tested Positive:")
        tested_positive_label.pack()
        self.tested_positive_var = tk.BooleanVar(root, value=False)
        self.tested_positive_checkbox = tk.Checkbutton(root, variable=self.tested_positive_var)
        self.tested_positive_checkbox.pack()

        test_date_label = tk.Label(root, text="Test Date:")
        test_date_label.pack()
        self.test_date_entry = tk.Entry(root)
        self.test_date_entry.pack()

        test_result_label = tk.Label(root, text="Test Result:")
        test_result_label.pack()
        self.test_result_entry = tk.Entry(root)
        self.test_result_entry.pack()

        # Create button for submitting the form
        submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        submit_button.pack()

    def submit_form(self):
        # Get values from the entry fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_entry.get()
        email_address = self.email_entry.get()
        address = self.address_entry.get()

        symptoms = self.symptoms_entry.get()
        symptom_onset = self.symptom_onset_entry.get()
        tested_positive = self.tested_positive_var.get()
        test_date = self.test_date_entry.get()
        test_result = self.test_result_entry.get()

        # Create a ContactForm instance and set the form values
        contact_form = ContactFormGUI()
        contact_form.set_personal_information(first_name, last_name, phone_number, email_address, address)
        contact_form.set_health_information(symptoms, symptom_onset, tested_positive, test_date, test_result)

        # Print the form values (you can modify this to store the values or perform other operations)
        print("Personal Information:")
        print("First Name:", contact_form.first_name)
        print("Last Name:", contact_form.last_name)
        print("Phone Number:", contact_form.phone_number)
        print("Email Address:", contact_form.email_address)
        print("Address:", contact_form.address)
        print()
        print("Health Information:")
        print("Symptoms:", contact_form.symptoms)
        print("Symptom Onset Date:", contact_form.symptom_onset)
        print("Tested Positive:", contact_form.tested_positive)
        print("Test Date:", contact_form.test_date)
        print("Test Result:", contact_form.test_result)

        # Clear the entry fields after submitting the form
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.symptoms_entry.delete(0, tk.END)
        self.symptom_onset_entry.delete(0, tk.END)
        self.test_date_entry.delete(0, tk.END)
        self.test_result_entry.delete(0, tk.END)

root = tk.Tk()
contact_form_gui = ContactFormGUI(root)
root.mainloop()