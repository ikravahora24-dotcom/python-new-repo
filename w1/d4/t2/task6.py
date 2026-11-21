
def make_validator(min_value):

    def validator(number):
        if number >= min_value:
            return True
        else:
            return False

    return validator


# Create two different validators
validate_18 = make_validator(18)
validate_50 = make_validator(50)


# Test the first validator
print("Validator 1 (Minimum value: 18)")
print(validate_18(20))
print(validate_18(15))
print(validate_18(18))

# Test the second validator
print("\nValidator 2 (Minimum value: 50)")
print(validate_50(60))
print(validate_50(40))
print(validate_50(50))
