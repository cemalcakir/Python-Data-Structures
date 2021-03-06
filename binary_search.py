def bs_recursive(array, x):
    "Initializing recursive function for binary search."
    left = 0
    right = len(array) - 1
    return recursive_helper(array, x, left, right)


def recursive_helper(array, x, left, right):
    "Helper function for bs_recursive, calculates mid value with low and high and performs search."
    if left > right:
        return "The value has not been found."
    mid = (left + right) // 2
    if array[mid] == x:
        return mid
    elif x < array[mid]:
        return recursive_helper(array, x, left, mid - 1)
    else:
        return recursive_helper(array, x, mid + 1, right)


def bs_iterative(array, x):
    "Iterative implementation of binary search."
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return "The value has not been found."
