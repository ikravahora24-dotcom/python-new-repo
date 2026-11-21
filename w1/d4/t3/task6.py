
def process_order(order):
    try:
        item = order["item"]
        price = order["price"]

    except KeyError as error:
        print("Error: Missing order detail:", error)

    else:
        print("Order Details:")
        print("Item:", item)
        print("Price:", price)

    finally:
        print("Processing complete")


# Valid order
order1 = {
    "item": "Laptop",
    "price": 45000
}

# Order with a missing key
order2 = {
    "item": "Keyboard"
}

print("First Order:")
process_order(order1)

print("\nSecond Order:")
process_order(order2)
