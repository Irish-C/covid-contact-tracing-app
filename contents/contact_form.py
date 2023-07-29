# contact_form.py
import tkinter as tk
from tkinter import ttk, PhotoImage
import tkcalendar, subprocess
from buttons import Buttons
from contact_form2 import ContactForm2

class ContactForm:
    '''Contact Tracing Form'''
    def __init__(self, add_contact_window):
        self.__add_contact_window = add_contact_window
        self.__add_contact_window.title("Contact Tracing Form")
        self.__add_contact_window.geometry("900x620+{}+{}".format(int(self.__add_contact_window.winfo_screenwidth() / 2 - 450), 0))

        self.__image = PhotoImage(file="image_widgets/ui.png")    # Load the image using PhotoImage

        # Create a canvas inside the add_contact_window
        self.__canvas = tk.Canvas(self.__add_contact_window, bd=0)
        self.__canvas.pack(fill="both", expand=True)

        # Load and display the background image on the canvas
        self.__canvas.image = self.__image  # Keep a reference to the image
        self.__canvas.create_image(0, 0, anchor='nw', image=self.__image)

        # Heading
        self.__canvas.create_text(320, 25, text="CONTACT TRACING FORM", font=("Arial", 25, "bold"), fill="blue")
        self.__canvas.create_text(352, 25, text="TRACING", font=("Arial", 25, "bold"), fill="red")

        # Call personal info and health info methods
        self.__personal_info()
        self.__health_info()

        self.__buttons_handler = Buttons(self, None)

        # Create the "NEXT" button and bind it to the next_window_and_submit_form method
        self.__next_button = tk.Button(text="NEXT", width=10, height=2, activebackground="orange")
        self.__next_button.pack(side="right", padx=10, pady=10)
        self.__next_button.bind("<Button-1>", self.__next_window_and_submit_form)

        # Create an "EXIT" button and bind it to the exit_application method
        self.__exit_button = tk.Button(self.__add_contact_window, text="EXIT", width=10, height=2, bg="light pink", activebackground="orange", command=self.__exit_application)
        self.__exit_button.pack(side="right", padx=10, pady=10)

    def __exit_application(self):
        self.__add_contact_window.destroy()

    def __next_window_and_submit_form(self, event):
        user_input = self.__buttons_handler.submit_form()
        if user_input == True:
            self.__second_window = tk.Toplevel(self.__add_contact_window)
            app2 = ContactForm2(self.__second_window)

            # Keep the second window on top
            self.__second_window.attributes("-topmost", True)
            self.__second_window.focus_force()
            self.__second_window.attributes("-topmost", False)
    
    def __personal_info(self):
        '''Ask user of their personal information'''
        # Personal Information inside the canvas
        self.__personal_info_frame = tk.Frame(self.__add_contact_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.__personal_info_frame.place(x=100, y=50, width=700, height=220)

        # Label for Personal Information
        self.__label_personal_info = tk.Label(self.__personal_info_frame, text="\nPERSONAL INFORMATION\n",
                                            font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.__label_personal_info.grid(row=0, column=0, columnspan=2)

        # Create labels and entry fields for personal information
        self.__name_label = tk.Label(self.__personal_info_frame, text="Name:", font=("Arial", 10))
        self.__name_label.grid(row=1, column=0)

        # First Name Label and Entry
        self.__label_first_name = tk.Label(self.__personal_info_frame, text="First Name", font=("Arial", 9, "italic"))
        self.__label_first_name.grid(row=2, column=1)
        self.__entry_first_name = ttk.Entry(self.__personal_info_frame, justify="center")
        self.__entry_first_name.grid(row=1, column=1)

        # Last Name Label and Entry
        self.__label_last_name = tk.Label(self.__personal_info_frame, text="Last Name", font=("Arial", 9, "italic"))
        self.__label_last_name.grid(row=2, column=2)
        self.__entry_last_name = ttk.Entry(self.__personal_info_frame, justify="center")
        self.__entry_last_name.grid(row=1, column=2)

        # Middle Initial Label and Entry
        self.__label_middle_initial = tk.Label(self.__personal_info_frame, text="M.I. (optional)", font=("Arial", 9, "italic"))
        self.__label_middle_initial.grid(row=2, column=3)
        self.__entry_middle_initial = ttk.Entry(self.__personal_info_frame, justify="center", )
        self.__entry_middle_initial.grid(row=1, column=3)

        # Name Suffix Label and Entry
        self.__label_name_suffix = tk.Label(self.__personal_info_frame, text="Suffix", font=("Arial", 9, "italic"))
        self.__label_name_suffix.grid(row=2, column=4)
        self.__entry_name_suffix = ttk.Combobox(self.__personal_info_frame, values=["", "Sr.", "Jr.", "III", "IV"])
        self.__entry_name_suffix.grid(row=1, column=4)

        # Phone number, email, and address fields
        self.__phone_label = ttk.Label(self.__personal_info_frame, text="\tPhone Number:", font=("Arial", 10))
        self.__phone_label.grid(row=6, column=0)
        self.__phone_entry = ttk.Entry(self.__personal_info_frame, justify="center")
        self.__phone_entry.grid(row=6, column=1)

        self.__email_label = ttk.Label(self.__personal_info_frame, text="\tEmail:", font=("Arial", 10))
        self.__email_label.grid(row=7, column=0)
        self.__email_entry = ttk.Entry(self.__personal_info_frame, justify="center")
        self.__email_entry.grid(row=7, column=1)

        self.__address_label = ttk.Label(self.__personal_info_frame, text="\tAddress:", font=("Arial", 10))
        self.__address_label.grid(row=8, column=0)
        self.__address_entry = ttk.Entry(self.__personal_info_frame, justify="center")
        self.__address_entry.grid(row=8, column=1, columnspan=3, sticky=tk.W + tk.E)

    def __health_info(self):
        # Health Information Frame
        self.__health_frame = tk.Frame(self.__add_contact_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.__health_frame.place(x=100, y=270, width=700, height=320)

        self.__label_health_info = tk.Label(self.__health_frame, text="HEALTH INFORMATION",
                                          font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.__label_health_info.grid(row=0, column=0, columnspan=5, padx=20, pady=5, sticky="w")

        # Vaccination status
        self.__vaccination_label = ttk.Label(self.__health_frame,
                                           text="\t(A.) Have you been vaccinated?")
        self.__vaccination_label.grid(row=1, column=0, sticky="w")
        self.__vaccination_choice = ttk.Combobox(self.__health_frame,
                                               values=["Not yet", "1st shot", "2nd shot", "1st Booster", "2nd Booster"])
        self.__vaccination_choice.grid(row=1, column=1)

        # COVID symptoms
        self.__symptoms_label = ttk.Label(self.__health_frame,
                                        text="\t(B.) Have you experienced symptoms of COVID within 14 days?")
        self.__symptoms_label.grid(row=5, column=0, sticky="w")
        self.__symptoms_choice = ttk.Combobox(self.__health_frame, values=["Yes", "No"])
        self.__symptoms_choice.grid(row=5, column=1)
        self.__symptoms_label = ttk.Label(self.__health_frame, text="\t\t\t\tIf YES, check all that applies:",
                                        font=("Arial", 8, "italic"))
        self.__symptoms_label.grid(row=6, column=0, columnspan=2, sticky="w")

        # COVID symptoms checkboxes
        self.__symptoms_checkboxes = [
            ("Fever", tk.IntVar()),
            ("Cough", tk.IntVar()),
            ("Shortness of breath", tk.IntVar()),
            ("Fatigue", tk.IntVar()),
            ("Other:", tk.IntVar())  # Additional checkbox for "Other" option
        ]

        for i, (symptom, var) in enumerate(self.__symptoms_checkboxes):
            checkbox = ttk.Checkbutton(self.__health_frame, text=symptom, variable=var)
            checkbox.grid(row=i + 6, column=1, sticky="w")

        # Entry field for inputting other symptoms
        self.__other_symptoms_entry = ttk.Entry(self.__health_frame, state="disabled", justify="center")
        self.__other_symptoms_entry.grid(row=len(self.__symptoms_checkboxes) + 6, column=1, sticky="w")

        # Function to enable/disable the entry field based on the "Other" checkbox state
        def enable_disable_other_symptoms_entry(*args):
            if self.__symptoms_checkboxes[-1][1].get() == 1:  # If "Other" checkbox is checked
                self.__other_symptoms_entry["state"] = "normal"
            else:
                self.__other_symptoms_entry["state"] = "disabled"

        # Binding the enable_disable_other_symptoms_entry function to the "Other" checkbox
        self.__symptoms_checkboxes[-1][1].trace("w", enable_disable_other_symptoms_entry)

        # COVID testing
        self.__testing_label = ttk.Label(self.__health_frame, text="\t(C.) Have you been tested for COVID-19?")
        self.__testing_label.grid(row=len(self.__symptoms_checkboxes) + 7, column=0, sticky="w")
        self.__testing_choice = ttk.Combobox(self.__health_frame, values=["Yes", "No"])
        self.__testing_choice.grid(row=len(self.__symptoms_checkboxes) + 7, column=1)

        # Testing date and result
        self.__date_label = ttk.Label(self.__health_frame, text="\t(D.) Date of testing (MM/DD/YYYY):", state="disabled")
        self.__date_label.grid(row=len(self.__symptoms_checkboxes) + 8, column=0, sticky="w")
        self.__date_entry = tkcalendar.DateEntry(self.__health_frame, date_pattern="mm/dd/yyyy", state="disabled")
        self.__date_entry.grid(row=len(self.__symptoms_checkboxes) + 8, column=1)
        self.__result_label = ttk.Label(self.__health_frame, text="\t(E.) Result of the test:", state="disabled")
        self.__result_label.grid(row=len(self.__symptoms_checkboxes) + 9, column=0, sticky="w")
        self.__result_choice = ttk.Combobox(self.__health_frame, values=["Positive", "Negative", "Pending"], state="disabled")
        self.__result_choice.grid(row=len(self.__symptoms_checkboxes) + 9, column=1)

        # Define a function to enable or disable the date and result fields based on the testing choice
        def enable_disable_date_result_fields(event):
            if self.__testing_choice.get() == "Yes":
                self.__date_label.configure(state="normal")
                self.__date_entry.configure(state="normal")
                self.__result_label.configure(state="normal")
                self.__result_choice.configure(state="normal")
            else:
                self.__date_label.configure(state="disabled")
                self.__date_entry.configure(state="disabled")
                self.__result_label.configure(state="disabled")
                self.__result_choice.configure(state="disabled")

        # Bind the enable_disable_date_result_fields function to the testing_choice combobox event
        self.__testing_choice.bind("<<ComboboxSelected>>", enable_disable_date_result_fields)

    def get_entries(self):
        '''Return the user input as a dictionary'''
        entries = {
            "First Name": self.__entry_first_name.get(),
            "Last Name": self.__entry_last_name.get(),
            "Middle Initial": self.__entry_middle_initial.get(),
            "Name Suffix": self.__entry_name_suffix.get(),
            "Phone Number": self.__phone_entry.get(),
            "Email": self.__email_entry.get(),
            "Address": self.__address_entry.get(),
            "Vaccination Status": self.__vaccination_choice.get(),
            "COVID Symptoms": self.__symptoms_choice.get(),
            "Other Symptoms": self.__other_symptoms_entry.get() if self.__symptoms_checkboxes[-1][1].get() == 1 else "",
            "Tested for COVID": self.__testing_choice.get(),
            "Testing Date": self.__date_entry.get() if self.__testing_choice.get() == "Yes" else "",
            "Test Result": self.__result_choice.get() if self.__testing_choice.get() == "Yes" else "",
        }
        return entries

if __name__ == "__main__":
    add_contact_window = tk.Tk()
    app = ContactForm(add_contact_window)
    add_contact_window.mainloop()