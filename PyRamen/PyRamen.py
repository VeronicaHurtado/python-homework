# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath, 'r') as csv_file:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delimiter) and return the csvreader object
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Go to the next row from the start of the file
    # to skip the header
    header = next(csv_reader)

    # Read each row of data after the header
    for row in csv_reader:
        # Print the row
        print(row)
        # Transfer data to the menu list
        menu.append(row)


# Read in the sales data into the sales list
with open(sales_filepath, 'r') as csv_file:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delimiter) and return the csvreader object
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Go to the next row from the start of the file
    # to skip the header
    header = next(csv_reader)

    # Read each row of data after the header
    for row in csv_reader:
        # Print the row
        print(row)
        # Transfer data to the menu list
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object
for row in sales:

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    quantity = int(row[3])
    menu_item = row[4]

    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report:
        report[menu_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # For every row in our sales data, loop over the menu records to determine a match
    for item_row in menu:

        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
        item = item_row[0]
        price = float(item_row[3])
        cost = int(item_row[4])

        # Calculate profit of each item in the menu data
        profit = price - cost

        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking
        # metrics for that item
        if item == menu_item:

            # Print out matching menu data
            print(item_row)

            # Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity

        # Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{menu_item} does not equal {item}! NO MATCH!")

    # Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
print(f"The total number of records in the Sales data is {row_count}")

# Write out report to a text file (won't appear on the command line output)
output_path = Path('output.txt')  # Set the output file path

# Open the output_path as a file object in "write" mode ('w')
with open(output_path, 'w') as file:
    for key,record in report.items():
        print(record)
        file.write(f'{key} {record}\n')
