# Uses Python3
input_length = input()
entries = input()
all_numbers = list(map(int, entries.split()))

mean = round(sum(all_numbers)/length_supplied, 1)

print(mean)
