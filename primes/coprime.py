# coprime.py
#
#  If the greatest common divisor of two numbers is 1 then the numbers are said to be coprime
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019

from Basics.gcd import gcd_recursive


def coprime(a, b):
    if gcd_recursive(a, b) == 1:
        return True
    else:
        return False


def main():
    print(coprime(6, 35))


if __name__ == "__main__":
    main()