
# Dictionary containing products and their prices
products = {
    "Pen": 20,
    "Notebook": 80,
    "Bag": 500,
    "Laptop": 45000,
    "Mouse": 150,
    "Keyboard": 90
}

# Dictionary comprehension to filter products above 100
expensive_products = {
    product: price
    for product, price in products.items()
    if price > 100
}

# Print results
print("All Products:", products)
print("Products priced above 100:", expensive_products)
