# buttons.py
import tkinter as tk
from tkinter import messagebox
import re, subprocess, csv, os
import shutil

class Buttons:
    def __init__(self, contact_form_instance, contact_form2_instance):
        self.__contact_form_instance = contact_form_instance
        self.__contact_form2_instance = contact_form2_instance
        self.__previous_window_entries = None
        self.__user_data = None

    def __next_window(self, event):
        subprocess.call(["python", "contact_form2.py"])
        self.__previous_window_entries = None  # Reset previous window entries
        if self.__contact_form_instance:
            self.__previous_window_entries = self.__contact_form_instance.get_entries()
        elif self.__contact_form2_instance:
            self.__previous_window_entries = self.__contact_form2_instance.get_entries2()

    def __previous_window(self, event):
        self.__contact_form2_instance.second_window.destroy()  # Close the current window
        subprocess.run(["python", "contact_form.py"]) 


    def submit_form(self):
        user_input = None
        if self.__contact_form_instance:
            user_input = self.__contact_form_instance.get_entries()
        elif self.__contact_form2_instance:
            user_input = self.__contact_form2_instance.get_entries2()
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
                tk.messagebox.showinfo("Success", "Saved Successfully!")

            return True

        except Exception as e:
            # Display an error message if form validation fails or an error occurs
            tk.messagebox.showerror("Error", str(e))

            return False

    def submit_form2(self):
        user_input2 = None

        if self.__contact_form_instance:
            user_input2 = self.__contact_form_instance.get_entries()
        elif self.__contact_form2_instance:
            user_input2 = self.__contact_form2_instance.get_entries2()

        try:
            dictlist2 = []
            for key, value in user_input2.items():
                entry_dict = {'key': key, 'value': value}
                dictlist2.append(entry_dict)

            # Save the form data and proceed to the next window
            self.__save_data2(dictlist2)
            self.__save_data_to_csv('contact-tracing-data.csv')

            return True

        except Exception as e:
            # Display an error message if form validation fails or an error occurs
            tk.messagebox.showerror("Error", str(e))

            return False

    def __save_data2(self, user_input):
        # Save the input data for later use
        self.__user_data = user_input

    def __save_data_to_csv(self, filename):
        # Save the user data to a CSV file
        if self.__user_data is not None:
            current_directory = os.getcwd()  # Get the current directory
            csv_file_path = os.path.join(current_directory, '..', 'contact-tracing-data.csv')

        with open(csv_file_path, 'a', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Key', 'Value'])  # Write header row
            for entry in self.__user_data:
                writer.writerow([entry['key'], entry['value']])
        
        tk.messagebox.showinfo("Success", "Saved Successfully!")