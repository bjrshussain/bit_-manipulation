"""
QUESTION: Given an array A of N numbers, where every element
occurs even number of times, except one element
(which occurs odd number of times), find the unique
element, which occurs odd number of times.
"""


# Find unique
def find_unique(arr):
    unique = 0
    for each in arr:
        unique = unique ^ each
        print(unique)
    return unique


# in the input array 2 occurs 4 times, 5 occurs 4 times, only 3 occurs 3 times, odd number of time
''' The Xor operator exclusively returns the exclusive bits only'''
res = find_unique([2, 3, 2, 2, 3, 3, 2, 5, 5, 5, 5])
print(res)
