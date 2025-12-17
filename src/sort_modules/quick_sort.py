def partition(array, start, end):
    mid = (start + end) // 2
    array[start], array[mid] = array[mid], array[start]

    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return array

    p = partition(array, start, end)  # сначала сортируем меньший подмассив

    left_size = p - start
    right_size = end - p

    if left_size < right_size:  # определяем, какой подмассив меньше
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)
    else:
        quick_sort(array, p + 1, end)
        quick_sort(array, start, p - 1)

    return array
