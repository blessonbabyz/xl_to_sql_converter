import openpyxl
import sqlite3
import os

# Get the path of the input Excel file
input_file = 'database.xlsx'
input_dir = os.path.dirname(input_file)

# Set the path of the output SQLite file
output_file = os.path.join(input_dir, 'database.db')

# Load the workbook
workbook = openpyxl.load_workbook(input_file)
sheet = workbook.active

# Connect to the SQLite database
conn = sqlite3.connect(output_file)
c = conn.cursor()

# Create the table
c.execute('''
    CREATE TABLE IF NOT EXISTS bank_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Country TEXT, 
        SWIFT TEXT,
        Code TEXT,
        Bank TEXT
    )
''')

# Iterate through the rows in the sheet and insert the data into the database
for row in sheet.iter_rows(min_row=2):
    country = row[0].value
    swift = row[1].value
    code = row[2].value
    bank = row[3].value

    c.execute('INSERT INTO bank_details (Country, SWIFT, Code, Bank) VALUES (?, ?, ?, ?)', (country, swift, code, bank))

# Commit the changes and close the connection
conn.commit()
conn.close()
