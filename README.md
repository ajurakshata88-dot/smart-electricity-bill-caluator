# Smart Electricity Bill Calculator

A beginner-friendly Python console program that collects customer details and
electricity use, calculates the bill, and prints a formatted receipt. It uses
only Python's built-in features; no database, files, APIs, or external
libraries are needed.

## Run the program

Open a terminal in this folder and run:

```bash
python smart_electricity_bill_calculator.py
```

## Program flow

1. `get_customer_details()` asks for the customer's name, ID, and consumed
	units. It asks again if units are not a whole number or are negative.
2. `calculate_bill(units)` calculates the energy charge using progressive
	rates, then adds the fixed Rs. 100 service charge:
	- First 100 units: Rs. 2 per unit
	- Units 101–200: Rs. 4 per unit
	- Units 201–500: Rs. 6 per unit
	- Units above 500: Rs. 8 per unit
3. `display_bill(...)` prints the customer details, units, energy charge,
	service charge, and final amount.

The provided slab text says "201 to 5000" and "above 500". This program treats
the intended boundary as 201–500 followed by above 500 units.