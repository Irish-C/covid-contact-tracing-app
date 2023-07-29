# csv_reader.py
import tkinter as tk
from tkinter import ttk
import csv

class CsvReader:
    def __init__(self):
        # Navigate CSV file
        self.csv_file_path = 'contact-tracing-data.csv'
        self.csv_data = self.read_csv_file(self.csv_file_path)

        # Create Tkinter application
        self.root = tk.Tk()
        self.root.title("CSV READER TABLE")
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # Set window size and position (center-north)
        window_width, window_height = 900, 600
        x_position, y_position = (screen_width - window_width) // 2, 0
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        search_label = tk.Label(self.root, text="Enter search term:")
        search_label.pack()

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        search_button = tk.Button(self.root, text="Search", command=self.on_search_button_click)
        search_button.pack()

        # Define the sample headings for the table
        headings = [
            "First Name", "Last Name", "Middle Initial", "Name Suffix", "Phone Number", "Email", "Address",
            "Vaccination Status", "COVID Symptoms", "Other Symptoms", "Tested for COVID", "Testing Date",
            "Test Result", "Emergency Name", "Emergency Phone/Email", "Emergency Address", "Relationship",
            "Travel History", "Travel Details"
        ]

        # Create the Treeview widget to display the search results in a table
        self.result_tree = ttk.Treeview(self.root, columns=headings, show="headings")

        # Set up the column headings and width with proper alignment
        for col, heading in enumerate(headings):
            self.result_tree.heading(heading, text=heading)
            self.result_tree.column(heading, width=150)

        # Define the maximum number of rows to display
        self.max_display_rows = 20

        # Displaying data with proper alignment by row
        if self.csv_data is not None:
            for row in self.csv_data:
                # Fill in empty cells with a blank string
                for i in range(len(row)):
                    if not row[i]:
                        row[i] = ""
                self.result_tree.insert("", "end", values=row)

                # Limit the number of rows displayed
                if self.result_tree.get_children().__len__() >= self.max_display_rows:
                    break

        self.result_tree.pack(fill="both", expand=True)

        # Add a vertical scrollbar to navigate through the rows
        vertical_slider = ttk.Scrollbar(self.root, orient="vertical", command=self.result_tree.yview)
        vertical_slider.pack(side="right", fill="y")
        self.result_tree.configure(yscrollcommand=vertical_slider.set)

        # Add a horizontal scrollbar to navigate through the columns
        horizontal_slider = ttk.Scrollbar(self.root, orient="horizontal", command=self.result_tree.xview)
        horizontal_slider.pack(side="bottom", fill="x")
        self.result_tree.configure(xscrollcommand=horizontal_slider.set)

        self.root.mainloop()

    def read_csv_file(self, file_path):
        '''
        This function reads data from a CSV file 
        and returns it as a list of lists.
        '''
        try:
            data = []
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the first row (header row)
                for row in csv_reader:
                    data.append(row)
            return data
        except Exception as e:
            # If an error occurs, print the csv
            print(f"Error reading the CSV file: {str(e)}")
            return None

    def search_csv(self, search_term, csv_data):
        '''
        Find rows in the CSV data that contain 
        the given search term (case-insensitive).
        '''
        results = []
        for row in csv_data:
            for cell in row:
                if search_term.lower() in cell.lower():
                    results.append(row)
                    break
        return results

    def on_search_button_click(self):
        '''
        Callback function triggered 
        when the search button is clicked.
        '''
        search_term = self.search_entry.get()
        if search_term:
            results = self.search_csv(search_term, self.csv_data)
            self.display_results(results)

    def display_results(self, results):
        """
        Updates the result_tree widget to display the given results.
        """
        # Clear the existing content in result_tree
        self.result_tree.delete(*self.result_tree.get_children())
        for row in results:
            # Fill in empty cells with a blank string
            for i in range(len(row)):
                if not row[i]:
                    row[i] = ""
            # Insert the row into the result_tree as a new entry
            self.result_tree.insert("", "end", values=row)

if __name__ == "__main__":
    app = CsvReader()