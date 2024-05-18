import csv

def create_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

# Example usage:
filename = "example.csv"
data = [
    ["Name", "Age", "Country"],
    ["John", 30, "USA"],
    ["Alice", 25, "Canada"],
    ["Bob", 35, "UK"]
]

create_csv(filename, data)
print(f"CSV file '{filename}' created successfully.")

import csv

def clean_data(csv_file):
    cleaned_data = []

    # Read data from CSV file
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header
        cleaned_data.append(header)  # Append the header to the cleaned data

        # Remove duplicates and handle missing values
        unique_rows = set()  # To store unique rows
        for row in reader:
            # Skip rows with missing values
            if any(cell.strip() == '' for cell in row):
                continue
            
            # Check for duplicates and add only unique rows
            if tuple(row) not in unique_rows:
                cleaned_data.append(row)
                unique_rows.add(tuple(row))

    return cleaned_data

# Example usage:
csv_file = "example.csv"  # Replace "data.csv" with the path to your CSV file
cleaned_data = clean_data(csv_file)
print("Cleaned Data:")
for row in cleaned_data:
    print(row)

