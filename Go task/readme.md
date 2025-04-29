# 📦 Simple Order Processor (Go Version)

Welcome to your first backend project at **Sinful**! 🎉

In this project, you'll build a simple **order processor** using **Golang**. Instead of running a server, you'll work directly with **JSON files**. Your task is to read orders from one file, process them, and write the results to another file.

You'll learn how to:

- Read data from a JSON file
- Transform data (change order states, add fields)
- Write data back to a new JSON file

This will help you get familiar with **Go structs**, **slices**, and **file handling**.

---

## 🚀 Getting Started

### 1. Install Go (if not installed)

Check your Go version:

```bash
go version
```

If you don’t have it installed, we can help set it up.

---

### 2. Explore the Files

- `new_orders.json`: Contains **new orders** that need processing.
- `processed_orders.json`: Will be created after running your Go program.
- `process_orders.go`: The Go script where you'll write your code.

---

### 3. Example Data

#### new_orders.json

```json
[
  { "id": 1, "item": "Vibrator", "quantity": 2, "state": "new" },
  { "id": 2, "item": "Lingerie Set", "quantity": 1, "state": "new" },
  { "id": 3, "item": "Massage Oil", "quantity": 3, "state": "new" },
  { "id": 4, "item": "Blindfold", "quantity": 5, "state": "new" },
  { "id": 5, "item": "Handcuffs", "quantity": 2, "state": "new" },
  { "id": 6, "item": "Lubricant", "quantity": 4, "state": "new" },
  { "id": 7, "item": "Feather Tickler", "quantity": 1, "state": "new" },
  { "id": 8, "item": "Body Stocking", "quantity": 2, "state": "new" },
  { "id": 9, "item": "Massage Candle", "quantity": 3, "state": "new" },
  { "id": 10, "item": "Bondage Rope", "quantity": 1, "state": "new" },
  { "id": 11, "item": "Couples Vibrator", "quantity": 1, "state": "new" },
  { "id": 12, "item": "Cock Ring", "quantity": 5, "state": "new" }
]
```

---

## 📝 Tasks

### 1. Run the Starter Program

- The program reads **new orders** from `new_orders.json`.
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

- Use **Gorilla Mux** to create a small API:
  - **GET /orders**: Return the contents of `processed_orders.json`.
  - **POST /orders**: Add a new order to `new_orders.json`.
- This will help you connect your data processing with **real backend services**.

---

## 💡 Tips

- **Ask for help** anytime—this is a learning experience!
- Test **small changes** often.
- Use `fmt.Println()` to debug and see what's happening inside your program.

---

Have fun! 🎉 You're already on your way to becoming a backend developer! 🚀

