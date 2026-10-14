def binary_search(numbers, target):
    """Return target's index in a sorted distinct list, or -1. Do not change input."""
    left, right = 0, len(numbers) - 1
    while left < right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
