import csv

# Sample data
data = [
    ['Miras', 87752378298],
    ['Ayana', 87779878732],
    ['Malika', 87709857019]
]

# Open the CSV file in write mode
with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['first_name', 'phone_number'])

    # Write the data rows
    for row in data:
        writer.writerow(row)