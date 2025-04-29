import json
from datetime import date

# Read new orders from JSON file
with open('new_orders.json', 'r') as file:
    new_orders = json.load(file)

# Process each order
processed_orders = []
for order in new_orders:
    order['state'] = 'picked'  # Transform state
    order['order_date'] = str(date.today())  # Add today's date
    processed_orders.append(order)

# Write processed orders to another JSON file
with open('processed_orders.json', 'w') as file:
    json.dump(processed_orders, file, indent=2)

print("Orders processed successfully!")