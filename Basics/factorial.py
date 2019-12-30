# factorial.py
#
#  Factorial
#
# https://github.com/martinluckett/MathsPlay
# Martin Luckett 2019


def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result


def main():
    f1 = factorial(52)

    print(f1)


if __name__ == "__main__":
    main()

