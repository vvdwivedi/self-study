1. Find two largest integers in an array in 1.5n comparisons.

  The fast algorithm implementation takes about 2n - 3 comparisons. This can be further reduced in following way:
  Let's create n/2 pairs from our list of n. Find max of each pair. This will take n/2 comparisons. Now to get the largest number, we need to find the maximum among the pair maximums. This will take another n/2 - 1 comparisons. This gives our biggest number. To find the second largest, we repeat the same in remaining pairs. After getting this maximum, we compare it with the smaller number in the pair that gave us our maximum. This will be another n/2 - 1 comparisons. So, we have our maximum two numbers in about 1.5 n comparisons.
