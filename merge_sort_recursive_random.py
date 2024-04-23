from random import randint

def merge(array, left_part, right_part):
    i, j, k = 0, 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i = i + 1
        else:
            array[k] = right_part[j]
            j = j + 1
        k = k + 1

    while i < len(left_part):
        array[k] = left_part[i]
        i = i + 1
        k = k + 1

    while j < len(right_part):
        array[k] = right_part[j]
        j = j + 1
        k = k + 1


def merge_sort_random(array):
    N = len(array)
    if N > 1:
        divide = randint(1, N - 1)
        left_part = array[:divide]
        right_part = array[divide:]

        merge_sort_random(left_part)
        merge_sort_random(right_part)

        merge(array, left_part, right_part)

def merge_sort_recursive_random_wrapper(array):
    merge_sort_random(array)
    return array
