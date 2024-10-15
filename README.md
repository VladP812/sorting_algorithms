Collection of sorting algorithms implemented in Python
=

<h4>How to debug (PyCharm):</h4>

- Clone repository 
- Create a new project in PyCharm pointing to root direcory of cloned repository
- Open ```run.py``` file
- With ```run.py``` file opened press CONTROL+SHIFT+F10 - this will automatically add a configuration so you can easily run the file
- Place breakpoints
- Press debug button to run the file in the debug mode (button with a bug icon next to the play (run) button)
- Follow detailed instructions in the ```run.py``` file
---


<h4>How to run performance comparisons:</h4>

- Clone the repository
- Run ```pip install -r requirements.txt``` (better do it in a new virtual environment)
- Run ```python performance_comparisons.py```
- After it completed, you will see two files created in the <b>measurments directory</b>, where .json file is a json representation of the performance measurments, and the .jpeg file is the actual chart you can open with an image viewer.

<h4>How to add/remove algorithms:</h4>

*! This is temporary, not very convenient method, it will be changed in the future*

- In the ```performance_comparisons.py``` file there is a list containing functions (algorithms) to be measured:
``` python
  if __name__ == "__main__":
    algorithms: list[Callable] = [quick_sort, insertion_sort]
```
- To add or remove algorithms you want to measure, simply delete/append a function from/to this list.

<h4>Optional:</h4>

- If you are running the script within an IDE, you can uncomment ```plot.show()``` in the main method so that the plotted chart will be shown automatically.
