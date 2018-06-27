# Getting `n`th number of Fibonnaci series
Given some non-negative integer `n`, what will be the `n`th term in the fibonnaci series with seed 0 and 1.

## Run it yourself
This code uses Python 3. There are two algorithms mentioned here, naive and fast. Both can be executed from terminal as:

`python3 <filename.py>`

Note that naive algorithm is just for reference and can result in a long waiting for numbers greater than 30.

# Stress Tester
Fibonnaci results are standard, so there was no need for stress test here.

# Companion problems

## Find the last digit of a large fibonnaci number
This is very similar to finding the `n`th term, but since the requirement is just to get the last digit, we need not keep the entire number. Last digit of `n`th number will be sum of last digits of two previous number `mod` 10.
