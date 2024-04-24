from charts import plot_algorithm_progression
from generator import gen_crescent, gen_decreasing, now, dif_time, gen_random
from utils import functions, algorithms, T, N

import csv

def exec(X):
    D = []
    for func in functions:
        a = now()
        func(X.copy())
        b = now()
        D.append(dif_time(b,a))
    return D
L = []

def process(gen_function, N, T):
    L = []
    for i in range(1, N + 1):
        X = gen_function(i * T)
        L.append(exec(X))
    return L

def print_result(L):
    print('----< T = ' + str(T) + ' N = ' + str(N) + ' L = ' + str(L) + '>--------\n')
    for x in L:
        print(x)
    
def gen_csv(L, filename):
    with open('result/csv/' + filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(algorithms)
        for x in L:
            writer.writerow(x)


crescent = process(gen_crescent, N, T)
plot_algorithm_progression(crescent, 'Crescent Data', 'crescent')

decreasing = process(gen_decreasing, N, T)
plot_algorithm_progression(decreasing, 'Decreasing Data', 'decreasing')

random = process(gen_random, N, T)
plot_algorithm_progression(random, 'Random Data', 'random')

