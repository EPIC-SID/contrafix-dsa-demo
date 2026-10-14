def largest_element(numbers):
    """Return the largest element, or None for empty input. Do not change input."""
    if not numbers:
        return None
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest
