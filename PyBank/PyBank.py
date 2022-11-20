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
previous_month_pnl = 0  # Variable to keep track of the previous month pnl
historical_change = []  # List to store change over time

# Open the input path as a file object
with open(csv_path, 'r') as csv_file:

    # Pass in the csv file to the csv.reader() function and return the csv_reader object
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Go to the next row from the start of the file to skip the header
    header = next(csv_reader)

    # Read each row of data after the header
    for row in csv_reader:
        # Transfer data to the budget_data dictionary
        budget_data[row[0]] = int(row[1])

# Iterate over each "month" of the budget_data dictionary
for date, pnl in budget_data.items():
    months_count += 1  # Add up 1 to the months count
    total_amount += pnl  # Sum up the pnl to the total_amount

    # Logic to determine the Greatest Increase and Greatest Decrease
    if great_decrease['amount'] == 0:
        great_decrease['amount'] = pnl
        great_decrease['date'] = date
    elif pnl < great_decrease['amount']:
        great_decrease['amount'] = pnl
        great_decrease['date'] = date
    elif pnl > great_increase['amount']:
        great_increase['amount'] = pnl
        great_increase['date'] = date

    # Logic to calculate the Monthly Change (prev vs current)
    if previous_month_pnl != 0:  # Skip the first iteration as there is nothing to compare to
        monthly_change = pnl - previous_month_pnl
        historical_change.append(monthly_change)

    # Update previous_month_pnl after Monthly Change calculation
    previous_month_pnl = pnl

# Calculate the Average Change, round to the nearest 2 decimal places
avg_change = round(sum(historical_change) / len(historical_change), 2)

# Print the metrics
print('Financial Analysis')
print('---------------------------------------------------')
print(f'Total months: {months_count}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {great_increase["date"]} (${great_increase["amount"]})')  # ToDo: Double check
print(f'Greatest Decrease in Profits: {great_decrease["date"]} (${great_decrease["amount"]})')  # ToDo: Double check

# Generate and export report
output_path = Path('output.txt')  # Set the output file path

# Open the output_path as a file object in "write" mode ('w')
with open(output_path, 'w') as file:
    # Write a header
    file.write('Financial Analysis\n')
    file.write('---------------------------------------------------\n')
    # write the content
    file.write(f'Total months: {months_count}\n')
    file.write(f'Total: ${total_amount}\n')
    file.write(f'Average Change: ${avg_change:.2f}\n')
    file.write(f'Greatest Increase in Profits: {great_increase["date"]} (${great_increase["amount"]})\n')
    file.write(f'Greatest Decrease in Profits: {great_decrease["date"]} (${great_decrease["amount"]})\n')
