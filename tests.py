import random

from quicksort import quick_sort1, partition_left_right1,\
                      partition_left_right2, quick_sort2


def test_partition1():
    for i in range (2, 21): # generate arrays of length in range from 2 to 20
        for _ in range(0, 1001): # how many such arrays generate
            arr: list[int | float] = [random.randint(-15, 15) for j in range(0, i)]
            print(f"Array before partition: {arr}")
            partitioned = partition_left_right1(arr)
            print(f"Array partitioned: {partitioned}\n"
                  "Checking parititon...")
            for k, num in enumerate(partitioned[0]):
                if partitioned[1] == -1:
                    print(f"Partition with no pivot! : {partitioned}")
                    continue
                if k == partitioned[1]:
                    continue
                if k < partitioned[1] and num >= partitioned[0][partitioned[1]]:
                    print(f"Partition did not work for {partitioned}"
                          " - number at the left side of the pivot is greater or "
                          "equal to the pivot and should be at the right side instead")
                    return
                if k > partitioned[1] and num < partitioned[0][partitioned[1]]:
                    print(f"Partition did not work for {partitioned}"
                          " - number at the right side of the pivot is less "
                          "than pivot and should be at the left side instead")
                    return
            print("Partition correct!")


def test_quicksort1():
    for i in range (2, 21): # generate arrays of length in range from 2 to 20
        for _ in range(0, 1001): # how many such arrays generate
            arr: list[int | float] = [random.randint(-15, 15) for j in range(0, i)]
            print("Array before sorting: " + str(arr))
            arr_quick_sorted = quick_sort1(arr)
            arr.sort()
            print("Array sorted by quicksort: " + str(quick_sort1(arr)))
            print(f"Is array sorted correctly?: {arr == arr_quick_sorted}")
            if arr != arr_quick_sorted:
                print("Array is incorrectly sorted!")
                return

if __name__ == "__main__":
    arr = [1, 4, 6, 2, 8, 3]
    quick_sort2(arr)
    print(arr)
