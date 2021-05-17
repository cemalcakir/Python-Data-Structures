def quick_sort(array):
    "Main function, calls the helper function with default parameters."
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, start, end):
    "Partitions the array in two and recursively calls itself for each part."
    if start < end:
        index = partition(array, start, end)
        quick_sort_helper(array, start, index - 1)
        quick_sort_helper(array, index + 1, end)


def partition(array, start, end):
    """Selects the pivot element and sorts the array, elements on the left
    side of the pivot will be less than pivot while elements on the right bigger than it."""
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) - 1 and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end
