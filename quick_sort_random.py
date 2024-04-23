from random import randint

def swap_elements(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def partition(array, low, high):
    pivot_index = randint(low, high)
    swap_elements(array, pivot_index, high)
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            swap_elements(array, i, j)
    swap_elements(array, i + 1, high)
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)

def quick_sort_recursive_wrapper(array):
    size = len(array) - 1
    quick_sort(array, 0, size)
    return array
