import pdb

def quick_sort1(arr) -> list[int | float]:
    if len(arr) <= 1:
        return arr

    partitioned = partition_left_right1(arr)
    left_side = quick_sort1(partitioned[0][:partitioned[1]])
    right_size = quick_sort1(partitioned[0][partitioned[1] + 1:])
    arr[:partitioned[1]] = left_side
    arr[partitioned[1] + 1:] = right_size
    return arr

def partition_left_right1(arr: list[int | float]) -> tuple[list[int | float], int]:
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
            # i += 1 ??
        elif arr[i] >= arr[p] and arr[j] >= arr[p]:
            j -= 1
    
    swap(i, p)
    return (arr, i)

def quick_sort2(arr, l=None, r=None):
    #pdb.set_trace()
    if l == None:
        l = 0
    if r == None:
        r = len(arr) - 1

    if l >= r or r <= l:
        return

    partition_pivot = partition_left_right2(arr, l, r)
    quick_sort2(arr, l, partition_pivot - 1)
    quick_sort2(arr, partition_pivot + 1, r)

def partition_left_right2(arr: list[int | float], l, r) -> int:
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
            # i += 1 ??
        elif arr[i] >= arr[p] and arr[j] >= arr[p]:
            j -= 1
    
    swap(i, p)
    return i

