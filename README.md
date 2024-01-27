# ExcelFilter Python Repository

## Overview

The ExcelFilter repository provides a Python script that allows users to extract specific columns from an Excel (xlsx) file based on specified rows' names. The extracted data is then saved in a new CSV file ('output.csv'). The script supports customization, allowing users to define relevant columns and filter data based on specific domain names.

## Usage

### 1. Clone the Repository

Clone the ExcelFilter repository to your local machine:

```bash
git clone https://github.com/Dolphin-Syndrom/excelfilter.git
```

### 2. Install Dependencies

Ensure you have the required dependencies installed:

```bash
pip install pandas openpyxl
```

### 3. Modify Configuration

Open the `excelfilter.py` file and locate the following sections:

```python
# Specify the relevant columns to extract
relevant_columns = ["Column1", "Column2", "Column3"]

# Specify the allowed domains for filtering
allowed_domains = ["gmail.com", "yahoo.com", "hotmail.com"]
```

Modify the `relevant_columns` list with the names of the columns you want to extract. Adjust the `allowed_domains` list to include the domain names you want to filter.

### 4. Run the Script

Execute the script by running the following command in the terminal:

```bash
python excelfilter.py
```

The script will prompt you to select/open the Excel file you want to filter.

### 5. View Output

Once the script completes execution, the filtered data will be saved in a new CSV file named `output.csv`. You can find this file in the same directory as the script.

## Customization

### Adding/Removing Relevant Columns

To add or remove columns for extraction, update the `relevant_columns` list in the script.

```python
relevant_columns = ["NewColumn1", "NewColumn2", "NewColumn3"]
```

### Modifying Allowed Domains

To change the allowed domains for filtering, update the `allowed_domains` list in the script.

```python
allowed_domains = ["example.com", "customdomain.com", "anotherdomain.com"]
```

## Notes

- The script uses the `pandas` library for handling Excel and CSV data.
- Make sure the Excel file you want to filter is in the same directory as the script.
- The output CSV file will be created in the same directory as the script.
