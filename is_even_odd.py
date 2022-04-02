# check to see if given number is even or odd
def isodd(n):

    # use bitwise & operator which returns need both to be true to return true. so if given number + 1 bit gives true
    # it means the number had first bit 2^0 set to 1 which means it was odd. and when we added another bit it returns
    # 1, meaning number had first bit set to 1. so the answer was odd. T
    x = "Odd" if (n & 1) == 1 else "Even"
    return x


res = isodd(22)
print(res)
