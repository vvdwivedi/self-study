# Uses Python3

input_length = input()
entries = input()
all_numbers = list(map(int, entries.split()))
all_numbers.sort()
length_supplied = int(input_length)

if length_supplied % 2 == 0:
    median = round(((all_numbers[(length_supplied//2)] + all_numbers[(length_supplied//2) - 1]) / 2) , 1)
else:
    median = round(all_numbers[(length_supplied//2)], 1)

print(median)
