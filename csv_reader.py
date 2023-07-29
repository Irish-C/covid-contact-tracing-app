import tkinter as tk
from tkinter import ttk
import csv

def read_csv_file(file_path):
    try:
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the first row (header row)
            for row in csv_reader:
                data.append(row)
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {str(e)}")
        return None

def search_csv(search_term, csv_data):
    results = []
    for row in csv_data:
        for cell in row:
            if search_term.lower() in cell.lower():
                results.append(row)
                break
    return results

def on_search_button_click():
    search_term = search_entry.get()
    if search_term:
        results = search_csv(search_term, csv_data)
        display_results(results)

def display_results(results):
    result_tree.delete(*result_tree.get_children())
    for row in results:
        # Fill in empty cells with a blank string
        for i in range(len(row)):
            if not row[i]:
                row[i] = ""
        # Insert the first name in the first column
        result_tree.insert("", "end", values=row)

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'contact-tracing-data.csv'
csv_data = read_csv_file(csv_file_path)

# Create the Tkinter application
root = tk.Tk()
root.title("CSV Search Tool")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position it at the center of the screen (north)
window_width = 900
window_height = 600
x_position = (screen_width - window_width) // 2
y_position = 0  # Position at the top of the screen (north)
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

# Set up the column headings and width with proper alignment
for col, heading in enumerate(headings):
    result_tree.heading(heading, text=heading)
    result_tree.column(heading, width=150)

# Define the maximum number of rows to display
max_display_rows = 20

# Displaying data with proper alignment by row
if csv_data is not None:
    for row in csv_data:
        # Fill in empty cells with a blank string
        for i in range(len(row)):
            if not row[i]:
                row[i] = ""
        result_tree.insert("", "end", values=row)

        # Limit the number of rows displayed
        if result_tree.get_children().__len__() >= max_display_rows:
            break

result_tree.pack()

result_tree.pack(fill="both", expand=True)

# Add a vertical scrollbar to navigate through the rows
vsb = ttk.Scrollbar(root, orient="vertical", command=result_tree.yview)
vsb.pack(side="right", fill="y")
result_tree.configure(yscrollcommand=vsb.set)

# Add a horizontal scrollbar to navigate through the columns
hsb = ttk.Scrollbar(root, orient="horizontal", command=result_tree.xview)
hsb.pack(side="bottom", fill="x")
result_tree.configure(xscrollcommand=hsb.set)

root.mainloop()
