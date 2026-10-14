def bubble_sort(numbers):
    """Return a new ascending sorted list without changing input."""
    result = list(numbers)
    for _ in range(len(result)):
        for index in range(len(result) - 2):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
    return result
