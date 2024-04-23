
def shell_sort(array, size):
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            key = array[i]
            j = i
            while j >= gap and array[j - gap] > key:
                array[j] = array[j - gap]
                j -= gap
            array[j] = key
        gap //= 2
    return array

def shell_sort_wrapper(array):
    return shell_sort(array, len(array))
