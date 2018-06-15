# Uses Python3
import sys

def sum_two(num_first, num_second):
    return num_first + num_second

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

print(sum_two(a, b))
