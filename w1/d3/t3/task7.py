
# Inventory Management System

inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

# Display original inventory
print("Original Inventory:", inventory)

# Add new stock
product = "Mouse"
quantity = 5

if product in inventory:
    inventory[product] += quantity
else:
    inventory[product] = quantity

print("\nAfter Adding Stock:", inventory)


# Sell a product
product = "Laptop"
quantity = 3

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("\n", quantity, product, "sold successfully!")
    else:
        print("\nNot enough stock available!")
else:
    print("\nProduct does not exist!")


# Try selling a product that does not exist
product = "Mobile"
quantity = 2

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("\n", quantity, product, "sold successfully!")
    else:
        print("\nNot enough stock available!")
else:
    print("\nProduct does not exist!")


# Display final inventory
print("\nFinal Inventory:", inventory)
