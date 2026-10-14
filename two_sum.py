def two_sum(numbers, target):
    """Return two distinct indices adding to target, or None. Do not change input."""
    seen = {}
    for index, number in enumerate(numbers):
        seen[number] = index
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
    return None
