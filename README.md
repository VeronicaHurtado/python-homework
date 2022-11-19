# Python Challenge
This repository contains two scrips:

## I. PyBank
Python script that analyses the records in [budget_data.csv](PyBank/Resources/budget_data.csv) to calculate:
- The total number of months included in the dataset
- The net total amount of Profit/Losses over the entire period
- The average of the changes in Profit/Losses over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

Additionally, a text file is generated with the results. The output of the script looks like this example:
```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

## II. PyRamen
Python script to support the analysis of a business' financial performance by cross-referencing the sales data 
[sales_data.csv](PyRamen/Resources/sales_data.csv) with the internal menu data [menu_data.csv](PyRamen/Resources/menu_data.csv) 
to figure out revenues and costs for the year.

In addition, the script assesses sales by product and generates a report with each product type and the following metrics:
- Count
- Revenue
- Cogs
- Profit

The output of the script looks like this example:
```text
  spicy miso ramen {'01-count': 9238, '02-revenue': 110856.0, '03-cogs': 46190.0, '04-profit': 64666.0}
  tori paitan ramen {'01-count': 9156, '02-revenue': 119028.0, '03-cogs': 54936.0, '04-profit': 64092.0}
  truffle butter ramen {'01-count': 8982, '02-revenue': 125748.0, '03-cogs': 62874.0, '04-profit': 62874.0}
  tonkotsu ramen {'01-count': 9288, '02-revenue': 120744.0, '03-cogs': 55728.0, '04-profit': 65016.0}
  vegetarian spicy miso {'01-count': 9216, '02-revenue': 110592.0, '03-cogs': 46080.0, '04-profit': 64512.0}
  shio ramen {'01-count': 9180, '02-revenue': 100980.0, '03-cogs': 45900.0, '04-profit': 55080.0}
  miso crab ramen {'01-count': 8890, '02-revenue': 106680.0, '03-cogs': 53340.0, '04-profit': 53340.0}
  nagomi shoyu {'01-count': 9132, '02-revenue': 100452.0, '03-cogs': 45660.0, '04-profit': 54792.0}
  soft-shell miso crab ramen {'01-count': 9130, '02-revenue': 127820.0, '03-cogs': 63910.0, '04-profit': 63910.0}
  burnt garlic tonkotsu ramen {'01-count': 9070, '02-revenue': 126980.0, '03-cogs': 54420.0, '04-profit': 72560.0}
  vegetarian curry + king trumpet mushroom ramen {'01-count': 8824, '02-revenue': 114712.0, '03-cogs': 61768.0, '04-profit': 52944.0}
 ```