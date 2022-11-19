# Import the pathlib and csv libraries
from pathlib import Path
import csv

# Set the file path
csv_path = Path('Resources/budget_data.csv')

# Initialise variables
months_count = 0  # The total number of months included in the dataset
total_amount = 0  # The net total amount of Profit/Losses over the entire period
avg_change = 0.0  # The average of the changes in Profit/Losses over the entire period
great_increase = {'date': '', 'amount': 0}  # The greatest increase in profits (date and amount) over the entire period
great_decrease = {'date': '', 'amount': 0}  # The greatest decrease in losses (date and amount) over the entire period
budget_data = {}  # Dictionary to store data from the csv file

# Open the input path as a file object
with open(csv_path, 'r') as csv_file:

    # Pass in the csv file to the csv.reader() function and return the csv_reader object
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Go to the next row from the start of the file in order to skip the header
    header = next(csv_reader)

    # Read each row of data after the header
    for row in csv_reader:
        # Print the row
        # print(row)
        # Transfer data to the budget_data dictionary
        budget_data[row[0]] = int(row[1])

