from generator import gen_crescent, gen_decreasing, now, dif_time, gen_random
from bubble_sort_iterativo import bubble_sort_iterativo
from insert_sort_iterative import insert_sort_iterativo
from merge_sort_iterative import merge_sort_iterative_wrapper
from merge_sort_recursive import merge_sort_recursive_wrapper
from merge_sort_recursive_random import merge_sort_recursive_random_wrapper
from quick_sort_random import quick_sort_recursive_wrapper
from quick_sort_recursive import recursive_quick_sort
from select_sort_recursive import select_sort_recursive_wrapper
from select_sort_recursive_random import select_sort_recursive_random_wrapper
from shell_sort_base_line import shell_sort_wrapper

import csv

def exec(X):
    D = []

    a = now()
    quick_sort_recursive_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    recursive_quick_sort(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    merge_sort_iterative_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    merge_sort_recursive_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    merge_sort_recursive_random_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    select_sort_recursive_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    select_sort_recursive_random_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    bubble_sort_iterativo(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    insert_sort_iterativo(X.copy())
    b = now()
    D.append(dif_time(b,a))

    a = now()
    shell_sort_wrapper(X.copy())
    b = now()
    D.append(dif_time(b,a))

    return D

T = 100
N = 9
L = []

print('----< T = ' + str(T) + ' N = ' + str(N) + ' L = ' + str(L) + '>--------\n')

def process_and_print(gen_function, N, T):
    L = []
    print('QS1,QS2,MS1,MS2,MS3,SS1,SS2,BS,IS,BASE_LINE')
    for i in range(1, N + 1):
        X = gen_function(i * T)
        L.append(exec(X))
    for x in L:
        print(','.join(map(str, x)))

def process_and_gen_csv(gen_function, N, T, filename):
    L = []
    with open('result/' + filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['QS1','QS2','MS1','MS2','MS3','SS1','SS2','BS','IS','BASE_LINE'])
        for i in range(1, N + 1):
            X = gen_function(i * T)
            L.append(exec(X))
        for x in L:
            writer.writerow(x)

# process_and_print(gen_random, N, T)
# process_and_print(gen_decreasing, N, T)
# process_and_print(gen_crescent, N, T)

process_and_gen_csv(gen_random, N, T, 'random.csv')
process_and_gen_csv(gen_decreasing, N, T, 'decreasing.csv')
process_and_gen_csv(gen_crescent, N, T, 'crescent.csv')
