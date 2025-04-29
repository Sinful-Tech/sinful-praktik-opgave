# 📦 Simple Order Management API

Welcome to your first backend project at **Sinful**! 🎉

In this project, you'll build and extend a small API that manages **orders** for an ecommerce shop. You'll get a chance to work with **Python** and **Flask**, a lightweight web framework used to build backend services.

You'll learn how to:

- Create API endpoints
- Work with data in Python (lists & dictionaries)
- Handle HTTP requests and responses

Don't worry if you've never done this before—take it step by step, and feel free to ask questions!

---

## 🚀 Getting Started

### 1. Install Python (if not installed)

You need **Python 3.10+**. Check your version:

```bash
python --version
```

If you don’t have it installed, we can help set it up.

---

### 2. Set up your environment

Install **Flask**:

```bash
pip install flask
```

---

### 3. Run the server

Start the Flask app:

```bash
python app.py
```

You should see something like:

```
Running on http://127.0.0.1:5000/
```

Open your browser and go to [**http://localhost:5000/orders**](http://localhost:5000/orders) to see the orders!

---

## 📝 Tasks

### 1. Explore the Code

- Look through the `app.py` file.
- Understand how:
  - The **list of orders** is structured.
  - The **API endpoints** work (focus on `GET /orders`).

---

### 2. Test the API

Use your browser or a tool like **Postman** to:

- View **all orders**:\
  `http://localhost:5000/orders`
- Filter **orders by state**:\
  `http://localhost:5000/orders?state=new`
- Get a **specific order by ID**:\
  `http://localhost:5000/orders/1`

---

### 3. Create a New Order (`POST /orders`)

- Add a **new endpoint** to **create an order**:
  - Path: `POST /orders`

  - Body (example):

    ```json
    {
      "item": "New Item Name",
      "quantity": 2,
      "state": "new"
    }
    ```

  - Automatically assign a **new unique ID** to the order.

---

### 4. Improve the Update Order Endpoint (`PUT /orders/<id>`)

- Make sure the endpoint:
  - Returns a **clear success message**.
  - Rejects **invalid states** like `"delivered"` or `"in_progress"`.

---

### 5. Add a New Field: `order_date`

- Add an `` field to each order.
- It can be a simple string like `"2025-04-28"`.
- Add it to **existing orders** in the mock data.
- Make sure it's included in the API responses.

---

### 6. BONUS: Add a Stats Endpoint (`GET /orders/stats`)

- Create a new endpoint:
  - Path: `GET /orders/stats`
- It should return a **summary of how many orders are in each state**.
- Example output:
  ```json
  {
    "new": 4,
    "picked": 3,
    "fulfilled": 3,
    "canceled": 2
  }
  ```

---

### 7. BONUS: Delete an Order (`DELETE /orders/<id>`)

- Add an endpoint to **delete an order** by its ID:
  - Path: `DELETE /orders/<id>`
  - Return a message like `"Order deleted successfully"`.

---

## 🌟 Stretch Goals

If you finish early and want more challenges, try these!

---

### 8. Filter Orders by Multiple States

- Modify the `/orders` endpoint to support **filtering by multiple states**.
- Example:\
  `GET /orders?state=new,fulfilled`\
  Should return **orders with state **``** or **``.

---

### 9. Sort Orders by Date

- Modify the `/orders` endpoint to allow sorting by **order\_date**.
- Example:\
  `GET /orders?sort=asc` (ascending)\
  `GET /orders?sort=desc` (descending)

---

### 10. Search Orders by Item Name

- Add a query parameter to search orders by **item name**.
- Example:\
  `GET /orders?search=Vibrator`\
  Should return all orders that include the word **"Vibrator"** in the item name.

---

### 11. Add Pagination

- Modify `/orders` to support **pagination**:
  - Query parameters: `page` and `limit`.
  - Example:\
    `GET /orders?page=1&limit=5`\
    Returns the **first 5 orders**.

---

## 💡 Tips

- **Ask for help** anytime—this is a learning experience!
- If you get stuck, break down the problem:
  - What do you want the API to do?
  - What data should it return?
- Test **small changes** often.

---

Have fun! 🎉 You're already on your way to becoming a backend developer! 🚀

