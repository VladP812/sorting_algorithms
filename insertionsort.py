import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i 
        while j > 0 and key < arr[j - 1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr


if __name__ == "__main__":
    arr = list(range(1,1000))
    random.shuffle(arr)
    print(insertion_sort(arr))
