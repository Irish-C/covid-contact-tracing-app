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
    Callback function for search button click.
    '''

def display_results():
    pass

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