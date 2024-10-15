import random
from typing import Callable

from quicksort import quick_sort_bad, quick_sort
from insertionsort import insertion_sort


def test_sorting_algorithm(algorithm: Callable):
    for i in range (2, 21): # generate arrays of length in range from 2 to 20
        for _ in range(0, 1001): # how many such arrays generate
            listt: list[int | float] = [random.randint(-15, 15) for _ in range(0, i)]
            listt_copy = listt.copy()
            print("Array before sorting: " + str(listt))
            algorithm(listt)
            listt_copy.sort()
            print("Array sorted by quicksort: " + str(listt))
            print(f"Is array sorted correctly?: {listt == listt_copy}")
            if listt != listt_copy:
                print("Array is incorrectly sorted!")
                return


if __name__ == "__main__":
    test_sorting_algorithm(quick_sort)
    test_sorting_algorithm(quick_sort_bad)
    test_sorting_algorithm(insertion_sort)
