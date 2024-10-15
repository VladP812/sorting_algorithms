from insertionsort import insertion_sort
from quicksort import quick_sort

"""

- Clone repository 
- Create a new project in PyCharm pointing to root direcory of cloned repository
- Open ```run.py``` file
- With ```run.py``` file opened press CONTROL+SHIFT+F10 to automatically add configuration
- Place breakpoints
- Press debug button to run the file in the debug mode (button with a bug icon next to the play (run) button)
- Follow instructions in the ```run.py``` file

Assuming you run it within an IDE:

To debug an algorithm and see how it works under the hood, place a breakpoint (red dot)
right on the line when desired algorithm is called and run the file (in debug mode).

Once the breakpoint is hit (program will stop and wait) press "Step Into" in your 
debugger to go inside the function (algorithm) and follow it's flow of execution.

Then, you can use "Step" or in some IDEs "Next" button, to execute algorithm line by
line.

In the bottom window (usually) you will see a window with locals and other 
variables used by the algorithm. While stepping through the algorithm, look how these
variables change after each step - this will give you a deep understanding of how
algorithm works.
"""
if __name__ == "__main__":
    array = [2, 7, 6, 1, 8, 3, 4]
    insertion_sort(array) # place breakpoint on this line before running the file
    array = [2, 7, 6, 1, 8, 3, 4] # reset the array so it is not sorted again
    quick_sort(array) # place breakpoint on this line before running the file
