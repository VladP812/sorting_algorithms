import datetime
from insertionsort import insertion_sort
from quicksort import quick_sort1, quick_sort2

import random
from typing import Callable
from time import perf_counter_ns
from collections import defaultdict
import json

import matplotlib.pyplot as plt
import numpy as np

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
                arr_tuple = tuple(arr)  # convert to tuple to use as dictionary key
                start_time = perf_counter_ns()
                algorithm(arr.copy())
                end_time = perf_counter_ns()
                total_time += end_time - start_time
            results[i][algorithm.__name__] = total_time / (number_of_lists) 
    return results

if __name__ == "__main__":
    algorithms: list[Callable] = [quick_sort1, quick_sort2, insertion_sort]
    results = compare_sorting_algorithms(algorithms, 2, 350, 85)
    
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
    plt.savefig(f"measurments/performance_comparisons_{datetime.datetime.now()}.jpeg",
                dpi=200)
