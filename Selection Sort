def selection_sort(array):
    for i in range(0, len(array)):
        swap(array, i, index_of_smallest(array, i))


def index_of_smallest(array, start):
    index = start
    smallest = float("inf")
    for i in range(start, len(array)):
        if array[i] < smallest:
            index = i
            smallest = array[index]
    return index


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
