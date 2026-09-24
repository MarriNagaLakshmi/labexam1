def sum_list(numbers):
    """Returns the sum of all numbers in the list."""
    return sum(numbers)

def count_negatives(numbers):
    """Counts how many numbers in the list are strictly less than zero."""
    return sum(1 for x in numbers if x < 0)
