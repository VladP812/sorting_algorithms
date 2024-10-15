import datetime
from insertionsort import insertion_sort
from quicksort import quick_sort_bad, quick_sort

import random
from typing import Callable
from time import perf_counter_ns
from collections import defaultdict
import json

import matplotlib.pyplot as plt


"""
Measures sorting performance of all sorting algorithms provided. Measures are conducted
on list of different, growing sizes.

@arguments:
    algorithms: a list containing function pointers, essentially the sorting algorithms
    perforamnce of which we are measuring.
    min_list_length: starting size of generated lists (inclusive)
    max_list_length: maximum size of generated lists (EXCLUSIVE)
    number_of_lists: how many lists of each size to generate and conduct measurments on
   
@returns:
    dictionary containing AVERAGE timings (in nanoseconds) each algorithm scored
    for each size of the list it was measured on.

    Format:
        { 1: {"quicksort" : 12345, "insertionsort" : 987655},
          2: ...,
         ...
         max_list_length - 1 : {"quicksort": 852924, "insertionsort" : 9798727}

        where 1, 2, 3 ... up to max_list_length - 1 are sizes of the lists

@example
    algs = [quicksort, insertionsort]
    compare_sorting_algorithms(algs, 2, 300, 85)

    Deconstruction:
    Each algortihm's performance will be measured on lists of different, growing sizes 
    starting from size=2. And for each size, there will be 85 different lists generated
    so the measurments obtained is more smooth and generic.
    In total, there will be 25245 measurments conducted for each algorithms.
    (299-2) * 85 = 25245 ; 299 instead of 300 since value 300 is EXCLUDED.

    Generated lists are identical for each algortihms, since the random seed is
    being reset for each algorithm, hence generated random values will be the same.
"""
def compare_sorting_algorithms(algorithms: list[Callable], min_list_length: int,
                               max_list_length: int, number_of_lists: int):
    results = defaultdict(dict)
    
    for algorithm in algorithms:
        random.seed(42)  # Reset random seed so arrays are the same for each algorithm
        for i in range(min_list_length, max_list_length):
            print(f"Algoritm {algorithm.__name__} : Measuring performance "
                  f"for lists of length: {i}")
            total_time = 0
            for _ in range(number_of_lists):  # generate 100 arrays of each length
                arr = [random.randint(-30, 30) for _ in range(i)]
                start_time = perf_counter_ns()
                algorithm(arr.copy())
                end_time = perf_counter_ns()
                total_time += end_time - start_time
            results[i][algorithm.__name__] = total_time / (number_of_lists) 
    return results

if __name__ == "__main__":
    algorithms: list[Callable] = [quick_sort_bad, quick_sort, insertion_sort]

    results = compare_sorting_algorithms(algorithms, 2, 350, 120)
    
    with open(f"measurments/performance_comparisons_{datetime.datetime.now()}.json", 
              "w") as file:
        json.dump(results, file, indent=4)

    sizes = list(results.keys())
    
    plt.xlabel("size of input array (unsorted)")
    plt.ylabel("time taken (nanoseconds) to sort ^6 (in power 6)")
        
    colors = ["b", "g", "r", "c", "m", "y", "k", "w"]
    current_color = 0
    line_types = ["-", "--", ":", "-."]
    current_line_type = 0

    for algorithm in algorithms:
        if current_line_type == len(line_types) - 1\
        and current_color == len(colors) - 1:
            print("Ran out of colors and line types to make algorithms look distinct!")
            break

        alg_values = []

        for key, val in results.items():
            alg_values.append(val[algorithm.__name__])
        plt.plot(sizes, alg_values, color=colors[current_color], 
                 linestyle=line_types[current_line_type],
                 label=algorithm.__name__)

        if current_color < len(colors) - 1:
            current_color += 1
        elif current_color == len(colors) - 1:
            current_color = 0
            current_line_type += 1
    plt.legend()
    #plot.show()
    plt.savefig(f"measurments/performance_comparisons_{datetime.datetime.now()}.jpeg",
                dpi=200)
