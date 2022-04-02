""" Find magic number with base 5. which is sum of powers of 
    binary number. Given a number generate a magic
    number bsed on bits in given number. if n==1, magic 
    number will be 5*1, if n==2, magic num is 25"""


''' if n==3 bits are 11 least bit==1 so 5^0 == 5....
    then shift right and get least bit,,, it's 1, so 
    ans = ans+ 5^2'''


def find_magic(n):
    ans = 0
    base = 5
    while n > 0:
        least = n & 1
        ans = ans + (least * base)
        n = n >> 1
        base = base * 5
    print(ans)


if __name__ == "__main__":
    find_magic(4)

