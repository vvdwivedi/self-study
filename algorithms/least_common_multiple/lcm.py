# Uses Python3
numbers = [int(x) for x in input('Enter two integers(non zero) separated by space: ').split()]

def gcd_euclid(a, b):
    if a == 0:
        return b
    return gcd_euclid(b%a, a)

lcm = int(numbers[0] * numbers[1] / gcd_euclid(numbers[0], numbers[1]))
print("LCM of {} and {} is: {}".format(numbers[0], numbers[1], lcm))
