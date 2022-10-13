import math
import sys

def char(digit):
    return chr(digit + 48)


def digit(charachter):
    return ord(charachter) - 48


def int_to_str(n):
    digits = []
    while True:
        n, r = divmod(n ,10)
        digits.append(char(r))
        if n == 0:
            break

    return "".join(reversed(digits))


def str_to_int(s):
    n = 0
    for ch in s:
        n = 10 * n + digit(ch)
    return n



def main():
    answer = math.factorial(10000)
    print({answer})


if __name__ == "__main__":
    main()