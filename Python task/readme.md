# 📦 Simple Order Processor (Python Version)

Welcome to your first backend project at **Sinful**! 🎉

In this project, you'll build a simple **order processor** that reads data from a **JSON file**, transforms it, and writes the output to another JSON file. This project is a great way to learn **backend data processing** without needing to run servers or use tools like Postman.

You'll learn how to:

- Read data from a JSON file
- Transform data (change order states, add fields)
- Write data back to a new JSON file

---

## 🚀 Getting Started

### 1. Install Python (if not installed)

You need **Python 3.10+**. Check your version:

```bash
python --version
```

If you don’t have it installed, we can help set it up.

---

### 2. Explore the Files

- `new_orders.json`: Contains **new orders** that need processing.
- `processed_orders.json`: Will be created after running your script.
- `process_orders.py`: The Python script where you'll write your code.

---

### 3. Example Data

#### new_orders.json

```json
[
  { "id": 1, "item": "Vibrator", "quantity": 2, "state": "new" },
  { "id": 2, "item": "Lingerie Set", "quantity": 1, "state": "new" },
  { "id": 3, "item": "Massage Oil", "quantity": 3, "state": "new" }
]
```

#### processed_orders.json (after running the script)

```json
[
  {
    "id": 1,
    "item": "Vibrator",
    "quantity": 2,
    "state": "picked",
    "order_date": "2025-04-28"
  },
  {
    "id": 2,
    "item": "Lingerie Set",
    "quantity": 1,
    "state": "picked",
    "order_date": "2025-04-28"
  },
  {
    "id": 3,
    "item": "Massage Oil",
    "quantity": 3,
    "state": "picked",
    "order_date": "2025-04-28"
  }
]
```

---

## 📝 Tasks

### 1. Run the Starter Script

- The script reads **new orders** from `new_orders.json`.
- It transforms each order:
  - Changes `state` from `"new"` to `"picked"`.
  - Adds `order_date` (today's date).
- It writes the processed orders to `processed_orders.json`.

---

### 2. Add a New Transformation

- Add a new field to each order:  
  `"processed_by": "intern_name"`

- **BONUS:** If the item is **"Massage Oil"**, increase the quantity by **10%** (round up).

---

### 3. BONUS: Validate Orders

- Make sure **all orders have a quantity > 0**.
- Skip or flag any invalid orders.

---

## 🌟 Stretch Goals

If you finish early and want more challenges, try these!

### 4. Add an API Layer (Optional)

- Use **Flask** to create a small API:
  - **GET /orders**: Return the contents of `processed_orders.json`.
  - **POST /orders**: Add a new order to `new_orders.json`.
- This will help you connect your data processing with **real backend services**.

---

## 💡 Tips

- **Ask for help** anytime—this is a learning experience!
- Test **small changes** often.
- Use `print()` to debug and see what's happening inside your script.

---

Have fun! 🎉 You're already on your way to becoming a backend developer! 🚀