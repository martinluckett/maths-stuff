# goldenratio.py
#
#  Algebraic form of the golden ratio
#  PHI = 1/2 * (1 + SQRT(5))
#
# https://github.com/martinluckett/maths-stuff
# Martin Luckett 2019

from decimal import *
from Sequences.Sequence import Sequence



def phi(precision=20):
    # Using Decimal
    getcontext().prec = precision
    result = (Decimal(0.5)*(Decimal(1) + Decimal(5).sqrt()))
    return result


def gr_fibonacci(n, precision):
    fib = Sequence("Fibonacci", first_term=0, second_term=1)
    fib.precision = precision
    result = fib.ratio_at_nth_term(n)
    return result


def main():
    precision = 50
    nth_term = 100

    print("Golden Ratio to {0} decimal places\n".format(precision))

    gr = phi(precision)
    print("By Calculation:\n {0}".format(gr))

    fib_ratio = gr_fibonacci(nth_term, precision)

    print("By ratio of consecutive Fibonacci numbers (at term {0}):\n {1}".format(nth_term, fib_ratio))

    error = ((gr/fib_ratio) - 1) * 100

    print("Error: {0} %".format(error))


if __name__ == "__main__":
    main()