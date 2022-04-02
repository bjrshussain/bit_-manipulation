""" find if nth bit in array is 0 or 1. We will use add first bit
    and use shift left bit operators to left by n-1 places. Once we have the mask
    we can then use & bit operator to see if it returns true. if yes its 1"""
''' shift n-1 zeros, add n-1 zeros to the right of insignificant bit. and compare the 
    nth to see if it   returns zero or true e.g. if bits = 11001101 n=4, then we create 
    1 and then add n-1 zero to right by shifting to left so mask becomes 1000, then we 
    compare 4th bit in mask and bits with & operator, if both are 1s
    it will return the value else returns zero'''


def find_bit(bits, n):
    x = 0b1 << (n-1)
    return x & bits


b = 0b011010

n = 6
res = find_bit(b, n)
print(res)

