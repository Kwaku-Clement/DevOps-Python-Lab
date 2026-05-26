def square(num):
    """Returns the square of a number."""
    return num * num


def is_even(num):
    """Returns True if the number is even, False otherwise."""
    if num % 2 == 0:
        return True
    else:
        return False

def sum_list(numbers):
    """Returns the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total


print(f"Square of 5: {square(5)}")
print(f"Is 4 even? {is_even(4)}")
print(f"Sum of [1, 2, 3, 4, 5]: {sum_list([1, 2, 3, 4, 5])}")