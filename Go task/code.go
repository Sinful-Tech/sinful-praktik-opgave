package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

// Order represents the structure of an order
type Order struct {
	ID       int    `json:"id"`
	Item     string `json:"item"`
	Quantity int    `json:"quantity"`
	State    string `json:"state"`
	// TODO: Add more fields here (like order_date, processed_by)
}

func main() {
	// Step 1: Read new_orders.json
	data, err := ioutil.ReadFile("new_orders.json")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	var orders []Order
	err = json.Unmarshal(data, &orders)
	if err != nil {
		fmt.Println("Error parsing JSON:", err)
		return
	}

	// Step 2: Process each order
	for i := range orders {
		// TODO: Transform each order
		// - Change state from "new" to "picked"
		// - Add order_date (today's date)
		// - Add processed_by ("intern_name")
		// - Bonus: If item is "Massage Oil", increase quantity by 10%
	}

	// Step 3: Write to processed_orders.json
	output, err := json.MarshalIndent(orders, "", "  ")
	if err != nil {
		fmt.Println("Error encoding JSON:", err)
		return
	}

	err = ioutil.WriteFile("processed_orders.json", output, 0644)
	if err != nil {
		fmt.Println("Error writing file:", err)
		return
	}

	fmt.Println("Orders processed successfully!")
}
