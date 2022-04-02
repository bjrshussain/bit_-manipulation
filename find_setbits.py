""" This programs finds the number of ones set bits for a given integer value."""


def find_bits(n):
    bits = 0
    while n:
        if n & 1:
            bits += 1
        n = n >> 1
    return bits


number = 45
res = find_bits(number)
print("decimal representation ", bin(number))
# ans=>3
print("RESULT", res)
