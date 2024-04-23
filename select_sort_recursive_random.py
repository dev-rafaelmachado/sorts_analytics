from random import randrange

def partition(arr, pivot_index = 0):
    i = 0
    
    if pivot_index != 0: 
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
        
    for j in range(len(arr) - 1):
        if arr[j + 1] < arr[0]:
            arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
            i += 1
            
    arr[0], arr[i] = arr[i], arr[0]
    return arr, i

def select_sort_random(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        partitioned_arr = partition(arr, randrange(len(arr)))
        arr = partitioned_arr[0]
        j = partitioned_arr[1]
        if j == k:
            return arr[j]
        elif j > k:
            return select_sort_random(arr[:j], k)
        else:
            k = k - j - 1
            return select_sort_random(arr[(j+1):], k)

def select_sort_recursive_random_wrapper(arr, counter = 0, Q = []):
    if counter == len(arr):
        return Q
    else:
        Q.append(select_sort_random(arr, counter))
        select_sort_recursive_random_wrapper(arr, counter + 1, Q)
    return Q
