def linear_search(numbers, target):
    """Return the first matching index, or -1. Do not change input."""
    for index in range(len(numbers) - 1):
        if numbers[index] == target:
            return index
    return -1
