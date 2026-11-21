def apply_discount(price, percent=10):

    discount = price * percent / 100
    final_price = price - discount

    print("Original Price:", price)
    print("Discount:", percent, "%")
    print("Discount Amount:", discount)
    print("Final Price:", final_price)


# 1. Calling with only price (default discount = 10%)
apply_discount(1000)

print("--------------------")

# 2. Calling with both arguments using keyword argument
apply_discount(2000, percent=20)