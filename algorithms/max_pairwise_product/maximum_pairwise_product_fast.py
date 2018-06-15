# Uses Python3

n = int(input())
a = [int(x) for x in input().split()]
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
print(product)
