# contact_form2.py
import tkinter as tk
from tkinter import ttk, PhotoImage
from buttons import Buttons

class ContactForm2:
    '''Contact Tracing Form - Second Window'''
    def __init__(self, second_window):
        self.__buttons_handler = Buttons(None, self)
        self.__second_window = second_window
        self.__second_window.title("Contact Tracing Form")
        self.__second_window.geometry("900x620+{}+{}".format(int(self.__second_window.winfo_screenwidth() / 2 - 450), 0))

        self.__image = PhotoImage(file="image_widgets/ui.png")    # Load the image using PhotoImage

        # Create a canvas inside the second_window
        self.__canvas = tk.Canvas(self.__second_window, bd=0)
        self.__canvas.pack(fill="both", expand=True)

        # Load and display the background image on the canvas
        self.__canvas.image = self.__image  # Keep a reference to the image
        self.__canvas.create_image(0, 0, anchor='nw', image=self.__image)

        # Heading
        self.__canvas.create_text(320,25, text="CONTACT TRACING FORM", font=("Arial", 25, "bold"), fill="blue")
        self.__canvas.create_text(352,25, text="TRACING", font=("Arial", 25, "bold"), fill="red")

        # Call emergency_info and travel_history methods
        self.__emergency_info()
        self.__travel_history()

        # Create a "SUBMIT" button and bind it to the submit_form method of the Buttons class
        self.__submit_button = tk.Button(self.__second_window, text="SUBMIT", width=10, height=2, bg="light blue", activebackground="orange")
        self.__submit_button.pack(side="right", padx=10, pady=10)
        self.__submit_button.bind("<ButtonRelease-1>", lambda event: self.__buttons_handler.submit_form2())

        # Create a "PREVIOUS" button and bind it to the previous_window method of the Buttons class
        self.__previous_button = tk.Button(self.__second_window, text="PREVIOUS", width=10, height=2, activebackground="orange")
        self.__previous_button.pack(side="left", padx=10, pady=10)
        self.__previous_button.bind("<Button-1>", self.__buttons_handler.previous_window)

        # Create an "EXIT" button and bind it to the exit_application method
        self.__exit_button = tk.Button(self.__second_window, text="EXIT", width=10, height=2, bg="light pink", activebackground="orange", command=self.exit_application)
        self.__exit_button.pack(side="right", padx=10, pady=10)

    def exit_application(self):
        self.__second_window.destroy()

    def __emergency_info(self):
        # Emergency Contact Information Frame
        self.__emergency_frame = tk.Frame(self.__second_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.__emergency_frame.place(x=100, y=50, width=700, height=220)

        # Label for Emergency Contact Information
        self.__label_emergency_info = tk.Label(self.__emergency_frame, text="\nEMERGENCY CONTACT PERSON\n", 
                                            font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.__label_emergency_info.grid(row=0, column=0, columnspan=2)

        # Name label and entry
        self.__other_name_label = tk.Label(self.__emergency_frame, text="\tName:", font=("Arial", 10))
        self.__other_name_label.grid(row=1, column=0, sticky="w")
        self.__other_name_entry = ttk.Entry(self.__emergency_frame, justify="center")
        self.__other_name_entry.grid(row=1, column=1)

        # Phone number/email label and entry
        self.__phone_email_label = tk.Label(self.__emergency_frame, text="\tPhone Number/Email:", font=("Arial", 10))
        self.__phone_email_label.grid(row=2, column=0, sticky="w")
        self.__phone_email_entry = ttk.Entry(self.__emergency_frame, justify="center")
        self.__phone_email_entry.grid(row=2, column=1)

        # Address label and entry
        self.__other_address_label = tk.Label(self.__emergency_frame, text="\tAddress:", font=("Arial", 10))
        self.__other_address_label.grid(row=3, column=0, sticky="w")
        self.__other_address_entry = ttk.Entry(self.__emergency_frame, width=50, justify="center")
        self.__other_address_entry.grid(row=3, column=1, columnspan=4, padx=38)

        # Relationship label and entry
        self.__relationship_label = tk.Label(self.__emergency_frame, text="\tRelationship:", font=("Arial", 10))
        self.__relationship_label.grid(row=4, column=0, sticky="w")
        self.__entry_name_suffix = ttk.Combobox(self.__emergency_frame, values=["Parent", "Guardian", "Sibling", "Relative", "Acquaintance", "Romantic Partner"])
        self.__entry_name_suffix.grid(row=4, column=1)

    def __travel_history(self):
        # Travel History Frame
        self.__travel_frame = tk.Frame(self.__second_window, borderwidth=10, highlightthickness=1, highlightbackground="gray")
        self.__travel_frame.place(x=100, y=260, width=700, height=310)

        # Label for Travel History
        self.__label_travel_history = tk.Label(self.__travel_frame, text="TRAVEL HISTORY", 
                                            font=("Arial", 14, "bold underline"), foreground="dark blue")
        self.__label_travel_history.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        # Have you traveled outside of your local area in the past 14 days?
        self.__travel_question_label = ttk.Label(self.__travel_frame, text="\t(F.) Have you traveled outside of your local area in the past 14 days?")
        self.__travel_question_label.grid(row=1, column=0, columnspan=2, sticky="w")

        # Radio Buttons for Yes and No options
        self.__travel_choice_var = tk.StringVar()
        self.__travel_choice_var.set("No")  # Set the default value to "No"
        self.__travel_choice_yes = ttk.Radiobutton(self.__travel_frame, text="Yes", variable=self.__travel_choice_var, value="Yes")
        self.__travel_choice_yes.grid(row=2, column=0)
        self.__travel_choice_no = ttk.Radiobutton(self.__travel_frame, text="No", variable=self.__travel_choice_var, value="No")
        self.__travel_choice_no.grid(row=3, column=0)

        # If yes, provide details
        self.__travel_details_label = ttk.Label(self.__travel_frame, text="\n\t(G.) If yes, please provide a brief details of the locations and dates visited:")
        self.__travel_details_label.grid(row=4, column=0, pady=5)
        self.__travel_details_entry = tk.Text(self.__travel_frame, height=5, width=50, padx=20, wrap="word", font=("times", 10))
        self.__travel_details_entry.grid(row=5, column=0, pady=5)

    def get_entries2(self):
        '''Return the user input as a dictionary'''
        entries2 = {
            "Emergency Name": self.__other_name_entry.get(),
            "Emergency Phone/Email": self.__phone_email_entry.get(),
            "Emergency Address": self.__other_address_entry.get(),
            "Relationship": self.__entry_name_suffix.get(),
            "Travel History": self.__travel_choice_var.get(),
            "Travel Details": self.__travel_details_entry.get("1.0", "end-1c"),
        }
        return entries2

if __name__ == "__main__":
    second_window = tk.Tk()
    app2 = ContactForm2(second_window)
    second_window.mainloop()