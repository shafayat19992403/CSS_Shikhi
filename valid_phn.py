def isValid(str):
    if len(str) == 10 and str.isdigit():
        return True
    elif len(str) == 12 and str[:3].isdigit() and str[4:7].isdigit() and str[8:].isdigit():
        return True

    return False

#  (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)


def isValidTwo(str):
    if len(str) == 14 and str[1:4].isdigit() and str[0] == "(" and str[4] == ")" and str[5]==" " and str[6:9].isdigit() and str[9] == "-" and str[10:]:
        return True
    elif len(str) == 12 and str[:3].isdigit() and str[3] == "-" and str[4:7] and str[7] == "-" and str[8:].isdigit():
        return True
    return False

test_cases = [
    "123-456-7890",  # Valid
    "(123) 456-7890",  # Valid
    "123 456 7890",  # Invalid
    "(123) 456-789",  # Invalid
    "123-456-78901",  # Invalid
]

# Testing the function with test cases
for phone in test_cases:
    print(f"Phone number '{phone}' is valid: {isValidTwo(phone)}")