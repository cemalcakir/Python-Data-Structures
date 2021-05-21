def bubble_sort(array):
    last_unsorted = len(array) - 1
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(last_unsorted):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                unsorted = True
        last_unsorted -= 1
