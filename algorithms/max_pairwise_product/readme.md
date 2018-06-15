# Max pairwise product
Given some `n` non-negative integers, we have to find the maximum product of two distinct numbers.

## Run it yourself
This code uses Python 3. There are two algorithms mentioned here, naive and fast. Both can be executed from terminal as:

`python3 <filename.py>`

Enter the value of `n` on the terminal, which is the number of non-negative integers that you will supply. Press enter/return key and then enter `n` non-negative integers separated by space. Press enter/return key again. The program will output the maximum product of pair.  

# Stress Tester
While the test cases can be entered by hand, we can't be sure about a lot of situations. The stress tester included will automate the process of testing out code for a wide variety of inputs. A stress test needs to consider 4 things:

1. Your implementation of the algorithm
2. A naive solution that is known to work for sure, will act as source of truth.
3. A Random test case generator
4. An infinite loop that takes the test generator and keeps on calling your implementation and naive one. It compares the result from both and stop when the results are not the same. To run the stress tester here, run `stress_tester.py` from terminal. It takes two inputs, the max length of inputs to generate, and the maximum value an input can have. Once you provide those two, it will generate random test cases and execute them.

## Additional questions
1. Find two largest integers in an array in 1.5n comparisons.

[Answers](./answers.md) can be found here for above questions.
