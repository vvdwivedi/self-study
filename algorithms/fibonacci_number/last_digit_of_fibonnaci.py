# Uses Python3
n = int(input('Enter the number for which you want fibonnaci: '))

def fibonnaci_last_digit(num):
    second_last = 0
    last = 1
    if num < 0:
        return 'Incorrect input'
    elif num == 0:
        return second_last
    elif num == 1:
        return last

    for i in range(1, num):
        next = ((last % 10) + (second_last % 10)) % 10
        second_last = last
        last = next
    return last

print(fibonnaci_last_digit(n))
