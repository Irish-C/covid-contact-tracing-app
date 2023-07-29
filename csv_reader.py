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
    pass

def display_results():
    pass
