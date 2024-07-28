# JSON TO CSV CONVERTER

import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        
        # Write the header row
        header = ['Serial No', 'Username', 'Password']
        csv_writer.writerow(header)
        
        # Write the data rows
        for index, row in enumerate(data, start=1):
            csv_writer.writerow([index, row['Username'], row['Password']])

# Example usage
json_file_path = 'users.json'
csv_file_path = 'data.csv'
json_to_csv(json_file_path, csv_file_path)
