"""
Quicksort implementations.
"""


"""
This is not good implementation of quick sort, my first attempt.
The biggest issue is that it creates a bunch of separate list objects (when slicing),
insead of operating on the one passed as argument. This overhead decreases it's
performance a lot.
"""
def quick_sort_bad(arr) -> list[int | float]:
    if len(arr) <= 1:
        return arr

    partitioned = partition_left_right_bad(arr)
    left_side = quick_sort_bad(partitioned[0][:partitioned[1]])
    right_size = quick_sort_bad(partitioned[0][partitioned[1] + 1:])
    arr[:partitioned[1]] = left_side
    arr[partitioned[1] + 1:] = right_size
    return arr

def partition_left_right_bad(arr: list[int | float]) -> tuple[list[int | float], int]:
    def swap(i1: int, i2:int):
        temp: int | float = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = temp

    if len(arr) == 1:
        return (arr, -1)
    if len(arr) == 0:
        raise Exception("Cannot partition empty array")
    
    i: int = 0;
    j: int = len(arr) - 1;
    p: int = len(arr) - 1;
    while i < j:
        if arr[i] < arr[p]:
            i += 1
        elif arr[i] >= arr[p] and arr[j] < arr[p]:
            swap(i, j)
            i += 1
        elif arr[i] >= arr[p] and arr[j] >= arr[p]:
            j -= 1
    
    swap(i, p)
    return (arr, i)

"""
Good implementation of quicksort.
"""
def quick_sort(arr, l=None, r=None):
    if l == None:
        l = 0
    if r == None:
        r = len(arr) - 1

    if l >= r or r <= l:
        return

    partition_pivot = partition_left_right(arr, l, r)
    quick_sort(arr, l, partition_pivot - 1)
    quick_sort(arr, partition_pivot + 1, r)

def partition_left_right(arr: list[int | float], l, r) -> int:
    def swap(i1: int, i2:int):
        temp: int | float = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = temp

    if len(arr) == 1:
        return 0
    if len(arr) == 0:
        raise Exception("Cannot partition empty array")
    
    i: int = l;
    j: int = r;
    p: int = r;
    while i < j:
        if arr[i] < arr[p]:
            i += 1
        elif arr[i] >= arr[p] and arr[j] < arr[p]:
            swap(i, j)
            i += 1
        elif arr[i] >= arr[p] and arr[j] >= arr[p]:
            j -= 1
    
    swap(i, p)
    return i

