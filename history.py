from datetime import datetime

# Add a new product to the inventory
def add_product(inventory):
    product_name = input("Please enter the name of the product: ")

    # Validate price input
    valid = False
    while valid == False:
        try:
            price = float(input("Please enter the price of the product: "))
            valid = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Validate quantity input
    valid = False
    while valid == False:
        try:
            amount = int(input("Please enter the quantity of the product: "))
            valid = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create product dictionary and add it to inventory
    product = {
        "name": product_name,
        "price": price,
        "amount": amount
    }

    inventory.append(product)
    print("Product added successfully")


# Show all products in the inventory
def show_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        # Loop through and print each product
        for product in inventory:
            print(f"Product: {product['name']} | Price: {product['price']} | Amount: {product['amount']}")


# Calculate total value and total quantity of products
def calculate_statistics(inventory):
    if len(inventory) == 0:
        print("No data to calculate")
        return

    total_value = 0
    total_products = 0

    # Sum all values and quantities
    for product in inventory:
        total_value = total_value + (product["price"] * product["amount"])
        total_products = total_products + product["amount"]

    print("Total inventory value:", str(total_value).replace(".", ""))
    print("Total products:", total_products)