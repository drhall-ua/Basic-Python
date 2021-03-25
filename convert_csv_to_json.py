import csv
import json

# Function to convert CSV to JSON
# FilePaths are Arguments for Function
def make_json(csvFilePath, jsonFilePath):
    #Creates a dictionary
    data = {}

    # Open a CSV reader called 'DictReader'
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row of CSV file into a Dict ('data')
        for rows in csvReader:

            # Insert column name to be used as primary key
            key = rows['port']
            data[key] = rows

    # Open a JSON writer and use json.dumps() to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Input the file paths for CSV input to JSON output
csvFilePath = r'myFile.csv'
jsonFilePath = r'myNewFile.json'

# Calls the make_json function
make_json(csvFilePath, jsonFilePath)