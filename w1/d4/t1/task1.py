def build_invoice(customer_name, *args, **kwargs):

    print("Customer Name:", customer_name)

    total = sum(args)
    print("Total Amount:", total)

    print("\nExtra Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


# Function calling
build_invoice(
    "Ikra",
    500, 200, 300,
    discount=100,
    tax=50,
    payment_method="Cash"
)