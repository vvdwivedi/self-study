# Uses Python3
from random import randint

def max_pairwise_product_naive(n, a):
    product = 0;
    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, a[i] * a[j])
    return product

def max_pairwise_product_fast(n, a):
    largest_index = 0
    second_largest_index = 0
    for i in range(0, n):
        if a[i] > a[largest_index]:
            largest_index = i

    largest, last = a[largest_index], a[n - 1]
    a[largest_index] = last
    a[n - 1] = largest

    for i in range(0, n - 1):
        if a[i] > a[second_largest_index]:
            second_largest_index = i

    #This is not required as we already have largest and second largest numbers, but if we had a situation to search for three of the biggest numbers, this would be the way to go.
    second_largest, last = a[second_largest_index], a[n - 2]
    a[second_largest_index] = last
    a[n - 2] = second_largest

    product = a[n - 1] * a[n -2]
    return product


def stress_test(max_input_length, max_input_size):
    while True:
        input_length = randint(3, max_input_length)
        array_length = input_length - 1
        input_to_test = []
        for i in range(array_length):
            input_to_test.append(randint(0, max_input_size))

        algo_under_test_result = max_pairwise_product_fast(array_length, input_to_test)
        known_result = max_pairwise_product_naive(array_length, input_to_test)
        if algo_under_test_result == known_result:
            print("OK")
        else:
            print("wrong answer from algo: {} , it should be: {}" .format(algo_under_test_result, known_result))
            print("Test cases are: {}".format(input_to_test))
            return False

max_input_length_to_test = int(input())
max_input_size_to_test = int(input())

stress_test(max_input_length_to_test, max_input_size_to_test)
