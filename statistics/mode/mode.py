# Uses Python3

input_length = input()
entries = input()
all_numbers = list(map(int, entries.split()))

def get_mode(numbers):
    counts = {k:numbers.count(k) for k in set(numbers)}
    modes = sorted(dict(filter(lambda x: x[1] == max(counts.values()), counts.items())).keys())
    return modes[0]

mode = get_mode(all_numbers)

print(mode)
