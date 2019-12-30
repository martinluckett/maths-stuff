# gcd.py
#
#  Greatest Common Divisor using Euclid's Algorithm
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def main():
    result = gcd(252, 105)
    print(result)
    result2 = gcd_recursive(252, 105)
    print(result2)


if __name__ == "__main__":
    main()

