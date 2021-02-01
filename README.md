[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3989531&assignment_repo_type=AssignmentRepo)
# CMPS 2200  Recitation 01

**Names (Team Members):** Hailey Dusablon, Abe Messing, Shengkai Qin, Alexis Preston, Daniel Ellsworth 


In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment. 
- Click on your personal github repository for the assignment (e.g., https://github.com/allan-tulane/recitation-01-your_username).
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: The worst case input value for linear search is a value that is not in the list because it will have to search through the entire list to determine that it is not there. The worst case value for binary search is also a value that is not in the list because it will have to search through the entire list to determine that it is not there, though it directly searched through less values than the linear search.**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: For linear search, the best case input value is the first value in the list because it will only have to run one time. For binary search, the value in the middle of the list is the best case input value as it is the first one to be compared to the key. **

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO:Running this code in main gave us an error in code given to us by the lab., which I have pasted below.**
main.py:89: in <module>
    print_results(compare_search())
main.py:74: in print_results
    print(tabulate.tabulate(results,
/opt/virtualenvs/python3/lib/python3.8/site-packages/tabulate.py:1426: in tabulate
    list_of_lists, headers = _normalize_tabular_data(
/opt/virtualenvs/python3/lib/python3.8/site-packages/tabulate.py:1103: in _normalize_tabular_data
    rows = list(map(list, rows))
E   TypeError: 'float' object is not iterable
=========================== short test summary info ============================
ERROR main.py - TypeError: 'float' object is not iterable
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!

**The print out of our results tuple is pasted here, as I believe it is closer to the intended answer for this question.**
[10.0, 0.0030994415283203125, 0.0057220458984375, 100.0, 0.0019073486328125, 0.003814697265625, 1000.0, 0.0016689300537109375, 0.00286102294921875, 10000.0, 0.0019073486328125, 0.003337860107421875, 100000.0, 0.0019073486328125, 0.0030994415283203125, 1000000.0, 0.0021457672119140625, 0.00286102294921875, 10000000.0, 0.001430511474609375, 0.0035762786865234375]


- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**TODO: Not exactly. This does not match the big O analysis, because there are not enough iterations for us to see the difference and big O is based on worst case time complexity. However, if the lists we are searching were much longer, it would be more likely we notice the predicted runtime differences.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **TODO: O(nk) **
  + For binary search? **TODO: O(n^2) + O(logn * k) = O(n^2 + (logn \* k))**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: It makes sense to sort and use binary search when k > n.**
