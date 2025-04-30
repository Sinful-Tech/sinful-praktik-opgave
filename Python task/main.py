from fastapi import FastAPI
import json
from datetime import date
from pydantic import BaseModel

class Order(BaseModel):
    id: int; item: str; quantity: int; state: str

skipped_items = 0
processed_orders = []

def reset():
    global skipped_items, processed_orders
    skipped_items = 0
    processed_orders = []

# Process each order
def process(location):
    global skipped_items
    global processed_orders
    for order in location:
        if order['quantity'] > 0:
            order['state'] = 'picked'  # Transform state
            order['order_date'] = str(date.today())  # Add today's date
            order["processed_by"] = "intern_name"
            if order['item'] == 'Massage Oil':
                order['quantity'] = int(round(order['quantity'] * 1.1, 0))
            processed_orders.append(order)
        else:
            skipped_items = skipped_items + 1


app = FastAPI()
@app.get("/")

async def somethingotherthanroot(): 
    # Read new orders from JSON file
    with open('new_orders.json', 'r') as file:
        new_orders = json.load(file)
        reset()
        process(new_orders)

    # Write processed orders to another JSON file
    with open('processed_orders.json', 'w') as file:
        json.dump(processed_orders, file, indent=2)
    
    
    skipped_count = f"{skipped_items} items skipped"

    return {"processed_orders": processed_orders, "skipped_count": skipped_count}

@app.post("/")

async def create_order(order: Order): 
    process([order.dict()])

    with open('processed_orders.json', 'w') as file:
        json.dump(processed_orders, file, indent=3)
    return order