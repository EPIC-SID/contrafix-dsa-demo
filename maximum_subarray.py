def maximum_subarray(numbers):
    """Return maximum contiguous nonempty subarray sum; return 0 for empty input."""
    best = current = 0
    for number in numbers:
        current = max(number, current + number)
        best = max(best, current)
    return best
