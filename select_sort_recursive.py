
def min_index(arr, start, end):
    if start == end:
        return start
    mid = min_index(arr, start + 1, end)
    return start if arr[start] < arr[mid] else mid

def select_sort(arr, size, index=0):
    if index == size:
        return
    min_idx = min_index(arr, index, size - 1)
    if min_idx != index:
        arr[min_idx], arr[index] = arr[index], arr[min_idx]
    select_sort(arr, size, index + 1)
    return arr

def select_sort_recursive_wrapper(arr):
    return select_sort(arr, len(arr))
