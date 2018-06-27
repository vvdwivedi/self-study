# Uses Python3
numbers = [int(x) for x in input('Enter two integers separated by space: ').split()]

def get_common_divisors(num1, num2):
    common_divisors = []
    for i in range(1, int(min(num1, num2)/2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    if num1 % num2 == 0:
        common_divisors.append(num2)
    if num2 % num1 == 0:
        common_divisors.append(num1)
    return common_divisors

print("GCD of {} and {} is: {}".format(numbers[0], numbers[1], get_common_divisors(numbers[0], numbers[1])[-1]))
