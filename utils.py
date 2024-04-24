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

algorithms = ['QS1','QS2','MS1','MS2','MS3','SS1','SS2','BS','IS','BASE_LINE']

functions = [quick_sort_recursive_wrapper, recursive_quick_sort, merge_sort_iterative_wrapper, merge_sort_recursive_wrapper, merge_sort_recursive_random_wrapper, select_sort_recursive_wrapper, select_sort_recursive_random_wrapper, bubble_sort_iterativo, insert_sort_iterativo, shell_sort_wrapper]


T = 100
N = 9