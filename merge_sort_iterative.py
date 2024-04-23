def merge(arr, temp, start, mid, end):

    left = start
    right = start
    right_end = mid + 1

    while right <= mid and right_end <= end:
        if arr[right] < arr[right_end]:
            temp[left] = arr[right]
            right = right + 1
        else:
            temp[left] = arr[right_end]
            right_end = right_end + 1
        left = left + 1

    while right < len(arr) and right <= mid:
        temp[left] = arr[right]
        left = left + 1
        right = right + 1

    for i in range(start, end + 1):
        arr[i] = temp[i]


def merge_sort(arr):

    low = 0
    high = len(arr) - 1

    temp = arr.copy()

    gap = 1
    while gap <= high - low:

        for i in range(low, high, 2*gap):
            start = i
            mid = i + gap - 1
            end = min(i + 2*gap - 1, high)
            merge(arr, temp, start, mid, end)

        gap = 2*gap
    return arr

def merge_sort_iterative_wrapper(arr):
    return merge_sort(arr)
