import random
import string


def generate_code():
    letters = string.ascii_letters
    first_three = "".join(random.choice(letters) for i in range(3))

    # Generate 7 random digits
    digits = string.digits
    last_seven = "".join(random.choice(digits) for i in range(7))

    # Combine the two parts into a single string
    result = first_three + last_seven
    return result
