import tkinter as tk
from tkinter import ttk
import csv

def read_csv_file(file_path):
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
        # If error occurs we print the csv
        print(f"Error reading the CSV file: {str(e)}")
        return None

def search_csv(search_term, csv_data):
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

def on_search_button_click():
    '''
    Callback function triggered 
    when the search button is clicked.
    '''
    search_term = search_entry.get()
    if search_term:
        results = search_csv(search_term, csv_data)
        display_results(results)

def display_results(results):
    """
    Updates the result_tree widget to display the given results.
    """
    # Clear the existing content in result_tree
    result_tree.delete(*result_tree.get_children())
    for row in results:
        # Fill in empty cells with a blank string
        for i in range(len(row)):
            if not row[i]:
                row[i] = ""
        # Insert the row into the result_tree as a new entry
        result_tree.insert("", "end", values=row)

# Navigate CSV file
csv_file_path = 'contact-tracing-data.csv'
csv_data = read_csv_file(csv_file_path)

# Create Tkinter application
root = tk.Tk()
root.title("CSV READER TABLE")

# Get screen dimensions
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

# Set window size and position (center-north)
window_width, window_height = 900, 600
x_position, y_position = (screen_width - window_width) // 2, 0
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

search_label = tk.Label(root, text="Enter search term:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=on_search_button_click)
search_button.pack()

# Define the sample headings for the table
headings = [
    "First Name", "Last Name", "Middle Initial", "Name Suffix", "Phone Number", "Email", "Address",
    "Vaccination Status", "COVID Symptoms", "Other Symptoms", "Tested for COVID", "Testing Date",
    "Test Result", "Emergency Name", "Emergency Phone/Email", "Emergency Address", "Relationship",
    "Travel History", "Travel Details"
]

# Create the Treeview widget to display the search results in a table
result_tree = ttk.Treeview(root, columns=headings, show="headings")

root.mainloop()