'''Made by Dolphin-Syndrom 
27-01-2024'''
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def generate_output_filename(output_file):
    base_name, extension = os.path.splitext(output_file)
    counter = 1
    new_output_file = f"{base_name}_{counter}{extension}"
    
    while os.path.exists(new_output_file):
        counter += 1
        new_output_file = f"{base_name}_{counter}{extension}"

    return new_output_file

def extract_and_filter(input_file, output_file, allowed_domains):
    print(f"Processing {input_file}...")

    df = pd.read_excel(input_file)

    print("Filtering data based on allowed domains...")
    df_filtered = df[df['registrant_email'].str.split('@').str[1].isin(allowed_domains)]

    relevant_columns = ['domain_name', 'registrant_name', 'registrant_country', 'registrant_phone', 'registrant_email']

    if os.path.exists(output_file):
        print(f"{output_file} already exists. Generating a new name...")
        output_file = generate_output_filename(output_file)

    df_filtered[relevant_columns].to_csv(output_file, index=False)

    print(f"Data has been filtered and saved to {output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(title="Select input Excel file", filetypes=[("Excel files", "*.xlsx")])
    if not input_file:
        print("No file selected. Exiting.")
        exit()

    output_file = 'output.csv'

    allowed_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']

    extract_and_filter(input_file, output_file, allowed_domains)
