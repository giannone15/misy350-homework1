# MISY350 - Homework 1: Coffee Shop Kiosk Inventory & Orders

# Data Model


inventory = [
    {"item_id": 1, "name": "Espresso",        "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte",           "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew",       "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha",           "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin","unit_price": 2.95, "stock": 18},
]

orders = [
    {"order_id": "Order_101", "item_id": 2, "quantity": 2, "status": "Placed", "total": 8.50},
    {"order_id": "Order_102", "item_id": 3, "quantity": 1, "status": "Placed", "total": 3.75},
]

# Query 1: Place a new order for an item and quantity.

# Input:
item_id = int(input("\nEnter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))

# Process: Validate Stock and Create New Order
# Find the matching inventory item
matched_inventory_item = None
for inventory_item in inventory:
    if inventory_item["item_id"] == item_id:
        matched_inventory_item = inventory_item

if matched_inventory_item is None:
    print("Error: Item not found in inventory.")
elif matched_inventory_item["stock"] < quantity:
    print(f"Error: Not enough stock. Available: {matched_inventory_item['stock']}")
else:
    # Reduce the stock
    matched_inventory_item["stock"] = matched_inventory_item["stock"] - quantity

    # Calculate total price
    order_total = quantity * matched_inventory_item["unit_price"]

    # Create a new unique order ID
    new_order_id = "Order_" + str(100 + len(orders) + 1)

    # Build the new order dictionary
    new_order = {
        "order_id": new_order_id,
        "item_id": item_id,
        "quantity": quantity,
        "status": "Placed",
        "total": order_total
    }

    # Record the order
    orders.append(new_order)

    #Output:
    print(f"\nOrder placed successfully!")
    print(f"  Order ID  : {new_order_id}")
    print(f"  Item      : {matched_inventory_item['name']}")
    print(f"  Quantity  : {quantity}")
    print(f"  Total     : ${order_total:.2f}")
    print(f"  New Stock : {matched_inventory_item['stock']}")

# READ

# Query 2: View all orders placed for a particular item.
# Prompt the user for the item name.

#nput:
search_item = input("\nEnter the item name to search (e.g. 'Latte'): ")

#Process: Find Orders Matching Item Name
# First, find the item_id that matches the searched name
matching_item_id = None
for inventory_item in inventory:
    if inventory_item["name"].lower() == search_item.lower():
        matching_item_id = inventory_item["item_id"]

# Then, collect all orders for that item_id
matching_orders = []
if matching_item_id is not None:
    for customer_order in orders:
        if customer_order["item_id"] == matching_item_id:
            matching_orders.append(customer_order)

#Output:
if matching_item_id is None:
    print(f"No inventory item found with the name '{search_item}'.")
elif len(matching_orders) == 0:
    print(f"No orders found for '{search_item}'.")
else:
    print(f"\nOrders for '{search_item}':")
    for customer_order in matching_orders:
        print(f"  - Order ID: {customer_order['order_id']} | "
              f"Qty: {customer_order['quantity']} | "
              f"Status: {customer_order['status']} | "
              f"Total: ${customer_order['total']:.2f}")


# Query 3: Calculate and print the total number of orders placed for "Cold Brew".

# Input:
# Access the inventory and orders lists; target item name is hardcoded.
target_item_name = "Cold Brew"

# Process: Count Orders Placed for Cold Brew
# Find the item_id for Cold Brew
cold_brew_item_id = None
for inventory_item in inventory:
    if inventory_item["name"] == target_item_name:
        cold_brew_item_id = inventory_item["item_id"]

# Count how many orders reference that item_id
cold_brew_order_count = 0
for customer_order in orders:
    if customer_order["item_id"] == cold_brew_item_id:
        cold_brew_order_count = cold_brew_order_count + 1

#Output:
print(f"\nTotal orders placed for '{target_item_name}': {cold_brew_order_count}")

# UPDATE

# Query 4: Update item stock quantity by item id.

#Input:
item_id = int(input("\nEnter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))

#Process: Validate and Update Stock Quantity
# Search for the item in the inventory
updated_inventory_item = None
for inventory_item in inventory:
    if inventory_item["item_id"] == item_id:
        updated_inventory_item = inventory_item

if updated_inventory_item is not None:
    updated_inventory_item["stock"] = new_stock

#Output:
if updated_inventory_item is None:
    print(f"Error: No item found with ID {item_id}.")
else:
    print(f"\nStock updated successfully!")
    print(f"  Item    : {updated_inventory_item['name']}")
    print(f"  New Stock: {updated_inventory_item['stock']}")


# REMOVE / DELETE

# Query 5: Cancel an order and restore stock.

#Input:
cancel_order_id = input("\nEnter Order ID to cancel: ")

#Process: Cancel Order and Restore Inventory Stock
# Find the order to cancel
cancelled_order = None
for customer_order in orders:
    if customer_order["order_id"] == cancel_order_id:
        cancelled_order = customer_order

if cancelled_order is not None:
    if cancelled_order["status"] == "Cancelled":
        print(f"Order {cancel_order_id} is already cancelled.")
    else:
        # Change the order status to Cancelled
        cancelled_order["status"] = "Cancelled"

        # Read item_id and quantity from the order
        restored_item_id = cancelled_order["item_id"]
        restored_quantity = cancelled_order["quantity"]

        # Locate the matching item in inventory and restore stock
        for inventory_item in inventory:
            if inventory_item["item_id"] == restored_item_id:
                inventory_item["stock"] = inventory_item["stock"] + restored_quantity
                restored_item_name = inventory_item["name"]
                restored_new_stock = inventory_item["stock"]

        #Output:
        print(f"\nOrder cancelled successfully!")
        print(f"  Order ID     : {cancel_order_id}")
        print(f"  Item         : {restored_item_name}")
        print(f"  Stock Restored By: {restored_quantity}")
        print(f"  New Stock    : {restored_new_stock}")
else:
    #Output (not found case):
    print(f"Error: No order found with ID '{cancel_order_id}'.")