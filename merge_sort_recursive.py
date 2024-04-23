
def merge(array, left_array, right_array):
    i, j, k = 0, 0, 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        else:
            array[k] = right_array[j]
            j = j + 1
        k = k + 1

    while i < len(left_array):
        array[k] = left_array[i]
        i = i + 1
        k = k + 1

    while j < len(right_array):
        array[k] = right_array[j]
        j = j + 1
        k = k + 1

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        merge(array, left_array, right_array)

def merge_sort_recursive_wrapper(array):
    merge_sort(array)
    return array
