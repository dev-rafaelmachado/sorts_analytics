from bubble_sort_iterativo import bubble_sort_iterativo
from insert_sort_iterativo import insert_sort_iterativo
from gerador import gerar_dados_decrescente, agora, dif_time, gerar_dados_random
from merge_sort_interativo import Merge_Sort_interativo_wapper
from merge_sort_recursivo import merge_sort__recursivo_wapper
from merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from quick_sort_random import quick_sort_recursive_wrapper
from quick_sort_recursivo import recursive_quick_sort
from select_sort_recursivo import select_sort_recursivo_wapper
from select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sellSort_base_line import shellSort_Wapper



def execucao(X):
    D = []

    a = agora()
    QS1 = quick_sort_recursive_wrapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    QS2 = recursive_quick_sort(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    MS1 = Merge_Sort_interativo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    MS2 = merge_sort__recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    MS3 = merge_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    SS1 = select_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    SS2 = select_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    BS = bubble_sort_iterativo(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    IS = insert_sort_iterativo(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    BASE_LINE = shellSort_Wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    return D

T = 230
N = 4
L = []

for i in range(1, N + 1, 1):
    X = gerar_dados_random( i * T )
    L.append( execucao(X) )

print('QS1,QS2,MS1,MS2,MS3,SS1,SS2,BASE_LINE')
for x in L:
    for y in x:
        print(y, end=',')
    print()

