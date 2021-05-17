
def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, start, end):
    if start < end:
        index = partition(array, start, end)
        quick_sort_helper(array, start, index - 1)
        quick_sort_helper(array, index + 1, end)


def partition(array, start, end):
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


# Driver code
array = [10, 7, 8, 9, 1, 5]
print(f'Original array: {array}')
quick_sort(array)
print(f'Sorted array: {array}')
