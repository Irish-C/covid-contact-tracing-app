import tkinter as tk
from tkinter import ttk, PhotoImage
import tkcalendar
from buttons import Buttons

class ContactForm:
    '''Contact Tracing Form'''
    def __init__(self, add_contact_window):
        self.add_contact_window = add_contact_window
        self.add_contact_window.title("Contact Tracing Form")
        self.add_contact_window.geometry("900x620+{}+{}".format(int(self.add_contact_window.winfo_screenwidth() / 2 - 450), 0))

        self.image = PhotoImage(file="image_widgets/ui.png")    # Load the image using PhotoImage

        # Create a canvas inside the add_contact_window
        self.canvas = tk.Canvas(self.add_contact_window, bd=0)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the background image on the canvas
        self.canvas.image = self.image  # Keep a reference to the image
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)

        # Heading
        self.canvas.create_text(320, 25, text="CONTACT TRACING FORM", font=("Arial", 25, "bold"), fill="blue")
        self.canvas.create_text(341, 25, text="TRACING", font=("Arial", 25, "bold"), fill="red")

        # Call personal info and health info methods
        self.personal_info()
        self.health_info()

        self.buttons_handler = Buttons(self, None)

        # Create the "NEXT" button and bind it to the next_window_and_submit_form method
        self.next_button = tk.Button(text="NEXT", width=10, height=2, activebackground="orange")
        self.next_button.pack(side="bottom", anchor="se", padx=10, pady=10)
        self.next_button.bind("<Button-1>", self.next_window_and_submit_form)

    def next_window_and_submit_form(self, event):
        # Call the submit_form method of the Buttons class to save the data to CSV
        self.buttons_handler.submit_form()
        self.buttons_handler.next_window(self.get_entries())

    def personal_info(self):
        '''Ask user of their personal information'''
        # Personal Information inside the canvas
        self.personal_info_frame = tk.Frame(self.add_contact_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.personal_info_frame.place(x=100, y=50, width=700, height=220)

        # Label for Personal Information
        self.label_personal_info = tk.Label(self.personal_info_frame, text="\nPERSONAL INFORMATION\n",
                                            font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.label_personal_info.grid(row=0, column=0, columnspan=2)

        # Create labels and entry fields for personal information
        self.name_label = tk.Label(self.personal_info_frame, text="Name:", font=("Arial", 10))
        self.name_label.grid(row=1, column=0)

        # First Name Label and Entry
        self.label_first_name = tk.Label(self.personal_info_frame, text="First Name", font=("Arial", 9, "italic"))
        self.label_first_name.grid(row=2, column=1)
        self.entry_first_name = ttk.Entry(self.personal_info_frame, justify="center")
        self.entry_first_name.grid(row=1, column=1)

        # Last Name Label and Entry
        self.label_last_name = tk.Label(self.personal_info_frame, text="Last Name", font=("Arial", 9, "italic"))
        self.label_last_name.grid(row=2, column=2)
        self.entry_last_name = ttk.Entry(self.personal_info_frame, justify="center")
        self.entry_last_name.grid(row=1, column=2)

        # Middle Initial Label and Entry
        self.label_middle_initial = tk.Label(self.personal_info_frame, text="M.I. (optional)", font=("Arial", 9, "italic"))
        self.label_middle_initial.grid(row=2, column=3)
        self.entry_middle_initial = ttk.Entry(self.personal_info_frame, justify="center", )
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
        self.address_entry.grid(row=8, column=1, columnspan=3, sticky=tk.W + tk.E)

    def health_info(self):
        # Health Information Frame
        self.health_frame = tk.Frame(self.add_contact_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.health_frame.place(x=100, y=270, width=700, height=320)

        self.label_health_info = tk.Label(self.health_frame, text="HEALTH INFORMATION",
                                          font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.label_health_info.grid(row=0, column=0, columnspan=5, padx=20, pady=5, sticky="w")

        # Vaccination status
        self.vaccination_label = ttk.Label(self.health_frame,
                                           text="\t(A.) Have you been vaccinated?")
        self.vaccination_label.grid(row=1, column=0, sticky="w")
        self.vaccination_choice = ttk.Combobox(self.health_frame,
                                               values=["Not yet", "1st shot", "2nd shot", "1st Booster", "2nd Booster"])
        self.vaccination_choice.grid(row=1, column=1)

        # COVID symptoms
        self.symptoms_label = ttk.Label(self.health_frame,
                                        text="\t(B.) Have you experienced symptoms of COVID within 14 days?")
        self.symptoms_label.grid(row=5, column=0, sticky="w")
        self.symptoms_choice = ttk.Combobox(self.health_frame, values=["Yes", "No"])
        self.symptoms_choice.grid(row=5, column=1)
        self.symptoms_label = ttk.Label(self.health_frame, text="\t\t\t\tIf YES, check all that applies:",
                                        font=("Arial", 8, "italic"))
        self.symptoms_label.grid(row=6, column=0, columnspan=2, sticky="w")

        # COVID symptoms checkboxes
        self.symptoms_checkboxes = [
            ("Fever", tk.IntVar()),
            ("Cough", tk.IntVar()),
            ("Shortness of breath", tk.IntVar()),
            ("Fatigue", tk.IntVar()),
            ("Other:", tk.IntVar())  # Additional checkbox for "Other" option
        ]

        for i, (symptom, var) in enumerate(self.symptoms_checkboxes):
            checkbox = ttk.Checkbutton(self.health_frame, text=symptom, variable=var)
            checkbox.grid(row=i + 6, column=1, sticky="w")

        # Entry field for inputting other symptoms
        self.other_symptoms_entry = ttk.Entry(self.health_frame, state="disabled", justify="center")
        self.other_symptoms_entry.grid(row=len(self.symptoms_checkboxes) + 6, column=1, sticky="w")

        # Function to enable/disable the entry field based on the "Other" checkbox state
        def enable_disable_other_symptoms_entry(*args):
            if self.symptoms_checkboxes[-1][1].get() == 1:  # If "Other" checkbox is checked
                self.other_symptoms_entry["state"] = "normal"
            else:
                self.other_symptoms_entry["state"] = "disabled"

        # Binding the enable_disable_other_symptoms_entry function to the "Other" checkbox
        self.symptoms_checkboxes[-1][1].trace("w", enable_disable_other_symptoms_entry)

        # COVID testing
        self.testing_label = ttk.Label(self.health_frame, text="\t(C.) Have you been tested for COVID-19?")
        self.testing_label.grid(row=len(self.symptoms_checkboxes) + 7, column=0, sticky="w")
        self.testing_choice = ttk.Combobox(self.health_frame, values=["Yes", "No"])
        self.testing_choice.grid(row=len(self.symptoms_checkboxes) + 7, column=1)

        # Testing date and result
        self.date_label = ttk.Label(self.health_frame, text="\t(D.) Date of testing (MM/DD/YYYY):", state="disabled")
        self.date_label.grid(row=len(self.symptoms_checkboxes) + 8, column=0, sticky="w")
        self.date_entry = tkcalendar.DateEntry(self.health_frame, date_pattern="mm/dd/yyyy", state="disabled")
        self.date_entry.grid(row=len(self.symptoms_checkboxes) + 8, column=1)
        self.result_label = ttk.Label(self.health_frame, text="\t(E.) Result of the test:", state="disabled")
        self.result_label.grid(row=len(self.symptoms_checkboxes) + 9, column=0, sticky="w")
        self.result_choice = ttk.Combobox(self.health_frame, values=["Positive", "Negative", "Pending"], state="disabled")
        self.result_choice.grid(row=len(self.symptoms_checkboxes) + 9, column=1)

        # Define a function to enable or disable the date and result fields based on the testing choice
        def enable_disable_date_result_fields(event):
            if self.testing_choice.get() == "Yes":
                self.date_label.configure(state="normal")
                self.date_entry.configure(state="normal")
                self.result_label.configure(state="normal")
                self.result_choice.configure(state="normal")
            else:
                self.date_label.configure(state="disabled")
                self.date_entry.configure(state="disabled")
                self.result_label.configure(state="disabled")
                self.result_choice.configure(state="disabled")

        # Bind the enable_disable_date_result_fields function to the testing_choice combobox event
        self.testing_choice.bind("<<ComboboxSelected>>", enable_disable_date_result_fields)

    def get_entries(self):
        '''Return the user input as a dictionary'''
        entries = {
            "First Name": self.entry_first_name.get(),
            "Last Name": self.entry_last_name.get(),
            "Middle Initial": self.entry_middle_initial.get(),
            "Name Suffix": self.entry_name_suffix.get(),
            "Phone Number": self.phone_entry.get(),
            "Email": self.email_entry.get(),
            "Address": self.address_entry.get(),
            "Vaccination Status": self.vaccination_choice.get(),
            "COVID Symptoms": self.symptoms_choice.get(),
            "Other Symptoms": self.other_symptoms_entry.get() if self.symptoms_checkboxes[-1][1].get() == 1 else "",
            "Tested for COVID": self.testing_choice.get(),
            "Testing Date": self.date_entry.get() if self.testing_choice.get() == "Yes" else "",
            "Test Result": self.result_choice.get() if self.testing_choice.get() == "Yes" else "",
        }
        return entries

if __name__ == "__main__":
    add_contact_window = tk.Tk()
    app = ContactForm(add_contact_window)
    add_contact_window.mainloop()