import tkinter as tk
from tkinter import ttk, PhotoImage

import re

class ContactForm:
    '''Contact Tracing Form'''
    def __init__(self, add_contact_window):
        self.add_contact_window = add_contact_window
        self.add_contact_window.title("ContacTracing Form")
        self.add_contact_window.geometry("900x620+{}+{}".format(int(self.add_contact_window.winfo_screenwidth() / 2 - 450), 0))

        self.image = PhotoImage(file="image_widgets/ui_bg.png")    # Load the image using PhotoImage
        
        # Call personal info and health info methods
        self.personal_info()
        self.health_info()

    def personal_info(self):
        # Create a canvas inside the add_contact_window
        self.canvas = tk.Canvas(self.add_contact_window, bd=0)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the background image on the canvas
        self.canvas.image = self.image  # Keep a reference to the image
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        
        '''Ask user of their personal information'''
        # Personal Information inside the canvas
        self.personal_info_frame = tk.Frame(self.canvas, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.personal_info_frame.place(x=100, y=50, width=700, height=220)

        # Label for Personal Information
        self.label_personal_info = tk.Label(self.personal_info_frame, text="\nPERSONAL INFORMATION\n", 
                                            font=("Arial", 14, "bold"), foreground="dark blue", justify="center")
        self.label_personal_info.grid(row=0, column=0, columnspan=2)

        # Create labels and entry fields for personal information
        self.name_label = tk.Label(self.personal_info_frame, text="Name:", font=("Arial", 10))
        self.name_label.grid(row=1, column=0)

        # First Name Label and Entry
        self.label_first_name = tk.Label(self.personal_info_frame, text="First Name", font=("Arial", 9, "italic"))
        self.label_first_name.grid(row=2, column=1)
        self.entry_first_name = tk.Entry(self.personal_info_frame, justify="center")
        self.entry_first_name.grid(row=1, column=1)

        # Last Name Label and Entry
        self.label_last_name = tk.Label(self.personal_info_frame, text="Last Name", font=("Arial", 9, "italic"))
        self.label_last_name.grid(row=2, column=2)
        self.entry_last_name = tk.Entry(self.personal_info_frame, justify="center")
        self.entry_last_name.grid(row=1, column=2)

        # Middle Initial Label and Entry
        self.label_middle_initial = tk.Label(self.personal_info_frame, text="M.I. (optional)", font=("Arial", 9, "italic"))
        self.label_middle_initial.grid(row=2, column=3)
        self.entry_middle_initial = tk.Entry(self.personal_info_frame, justify="center",)
        self.entry_middle_initial.grid(row=1, column=3)

        # Name Suffix Label and Entry
        self.label_name_suffix = tk.Label(self.personal_info_frame, text="Suffix", font=("Arial", 9, "italic"))
        self.label_name_suffix.grid(row=2, column=4)
        self.entry_name_suffix = ttk.Combobox(self.personal_info_frame, values=["", "Sr.", "Jr.", "III", "IV"])
        self.entry_name_suffix.grid(row=1, column=4)

        # Phone number, email, and address fields
        self.phone_label = ttk.Label(self.personal_info_frame, text="\tPhone Number:", font=("Arial", 10))
        self.phone_label.grid(row=6, column=0)
        self.phone_entry = ttk.Entry(self.personal_info_frame, justify="center")
        self.phone_entry.grid(row=6, column=1)

        self.email_label = ttk.Label(self.personal_info_frame, text="\tEmail:", font=("Arial", 10))
        self.email_label.grid(row=7, column=0)
        self.email_entry = ttk.Entry(self.personal_info_frame, justify="center")
        self.email_entry.grid(row=7, column=1)

        self.address_label = ttk.Label(self.personal_info_frame, text="\tAddress:", font=("Arial", 10))
        self.address_label.grid(row=8, column=0)
        self.address_entry = ttk.Entry(self.personal_info_frame, justify="center")
        self.address_entry.grid(row=8, column=1, columnspan=3, sticky=tk.W+tk.E)

    def health_info(self):
        # Health Information Frame
        self.health_frame = tk.Frame(self.add_contact_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.health_frame.place(x=100, y=270, width=700, height=320)

        self.label_health_info = tk.Label(self.health_frame, text="\nHEALTH INFORMATION", 
                                            font=("Arial", 14, "bold"), foreground="dark blue", justify="center")
        self.label_health_info.grid(row=0, column=0)

        # Vaccination status
        self.vaccination_label = ttk.Label(self.health_frame, 
                                           text="\t(A.) Have you been vaccinated?")
        self.vaccination_label.grid(row=1, column=0, sticky="w")
        self.vaccination_choice = ttk.Combobox(self.health_frame, 
                                               values=["1st shot", "2nd shot", "Not yet", "1st Booster", "2nd Booster"])
        self.vaccination_choice.grid(row=1, column=1)

        # COVID symptoms
        self.symptoms_label = ttk.Label(self.health_frame, 
                                        text="\t(B.) Have you experienced symptoms of COVID within 14 days?")
        self.symptoms_label.grid(row=5, column=0, sticky="w")
        self.symptoms_choice = ttk.Combobox(self.health_frame, values=["YES", "NO"])
        self.symptoms_choice.grid(row=5, column=1)
        self.symptoms_label = ttk.Label(self.health_frame, text="\t\t\t\tIf YES, check all that applies:", 
                                        font=("Arial", 8, "italic"))
        self.symptoms_label.grid(row=6, column=0, sticky="w")

        # COVID symptoms checkboxes
        symptoms_checkboxes = [
            ("Fever", tk.IntVar()),
            ("Cough", tk.IntVar()),
            ("Shortness of breath", tk.IntVar()),
            ("Fatigue", tk.IntVar()),
        ]

        for i, (symptom, var) in enumerate(symptoms_checkboxes):
            checkbox = ttk.Checkbutton(self.health_frame, text=symptom, variable=var)
            checkbox.grid(row=i+6, column=1, sticky="w")

        # COVID testing
        self.testing_label = ttk.Label(self.health_frame, text="\t(C.) Have you been tested for COVID-19?")
        self.testing_label.grid(row=len(symptoms_checkboxes)+5, column=0, sticky="w")
        self.testing_choice = ttk.Combobox(self.health_frame, values=["Yes", "No"])
        self.testing_choice.grid(row=len(symptoms_checkboxes)+5, column=1)

        # Testing date and result
        self.date_label = ttk.Label(self.health_frame, text="\t(D.) Date of testing (MM/DD/YYYY):")
        self.date_label.grid(row=len(symptoms_checkboxes)+7, column=0, sticky="w")
        self.date_entry = ttk.Entry(self.health_frame)
        self.date_entry.grid(row=len(symptoms_checkboxes)+7, column=1)

        self.result_label = ttk.Label(self.health_frame, text="\t(E.) Result of the test:")
        self.result_label.grid(row=len(symptoms_checkboxes)+8, column=0, sticky="w")
        self.result_choice = ttk.Combobox(self.health_frame, values=["Positive", "Negative", "Pending"])
        self.result_choice.grid(row=len(symptoms_checkboxes)+8, column=1)

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