# Uses Python3
n = int(input('Enter the number for which you want fibonnaci: '))

def fibonnaci(num):
    if num < 0:
        return 'Incorrect input'
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonnaci(num - 1) + fibonnaci(num - 2)

print(fibonnaci(n))
