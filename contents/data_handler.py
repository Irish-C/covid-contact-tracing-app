# data_handler.py
import pandas as pd

class DataHandler:
    def __init__(self):
        self.data = []

    def add_data(self, user_data, user_data2):
        self.data.append({**user_data, **user_data2})

    def save_to_csv(self):
        if not self.data:
            return

        df = pd.DataFrame(self.data)
        df.to_csv('contact_tracing_data.csv', index=False)

    def clear_data(self):
        self.data = []
