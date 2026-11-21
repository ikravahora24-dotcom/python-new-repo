
class InvalidRangeError(Exception):
    pass


while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            raise InvalidRangeError(
                "Error: Number must be between 1 and 10!"
            )

    except ValueError:
        print("Error: Please enter a valid numeric value!")

    except InvalidRangeError as error:
        print(error)

    else:
        print("Valid number entered:", number)
        break
