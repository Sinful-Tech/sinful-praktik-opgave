from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data: A larger list of orders
orders = [
    {"id": 1, "item": "Vibrator", "quantity": 2, "state": "new"},
    {"id": 2, "item": "Lingerie Set", "quantity": 1, "state": "picked"},
    {"id": 3, "item": "Massage Oil", "quantity": 3, "state": "fulfilled"},
    {"id": 4, "item": "Blindfold", "quantity": 5, "state": "new"},
    {"id": 5, "item": "Handcuffs", "quantity": 2, "state": "canceled"},
    {"id": 6, "item": "Lubricant", "quantity": 4, "state": "picked"},
    {"id": 7, "item": "Feather Tickler", "quantity": 1, "state": "fulfilled"},
    {"id": 8, "item": "Body Stocking", "quantity": 2, "state": "new"},
    {"id": 9, "item": "Massage Candle", "quantity": 3, "state": "fulfilled"},
    {"id": 10, "item": "Bondage Rope", "quantity": 1, "state": "canceled"},
    {"id": 11, "item": "Couples Vibrator", "quantity": 1, "state": "new"},
    {"id": 12, "item": "Cock Ring", "quantity": 5, "state": "picked"},
]

# Endpoint: Get all orders (with optional filtering by state)
@app.route('/orders', methods=['GET'])
def get_orders():
    state = request.args.get('state')
    if state:
        filtered_orders = [order for order in orders if order['state'] == state]
        return jsonify(filtered_orders)
    return jsonify(orders)

# Endpoint: Get a single order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

# Endpoint: Update order state
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    new_state = request.json.get('state')
    if new_state not in ['new', 'picked', 'fulfilled', 'canceled']:
        return jsonify({"error": "Invalid state"}), 400

    for order in orders:
        if order['id'] == order_id:
            order['state'] = new_state
            return jsonify({"message": f"Order {order_id} updated successfully", "order": order})
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)