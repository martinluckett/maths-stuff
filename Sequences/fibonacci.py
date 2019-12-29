# fibonacci.py
#
#  Fibonacci Numbers
#
# https://github.com/martinluckett/MathsStuff
# Martin Luckett 2019

from Sequences.Sequence import Sequence


def main():
    fib = Sequence("Fibonacci", first_term=0, second_term=1)

    result = fib.get_sequence(number_of_terms=100)
    print(result)

    term40 = fib.nth_term(n=40)
    print(term40)

    term200 = fib.nth_term(n=200)
    print(term200)

    fib.precision = 50
    ratio = fib.ratio_at_nth_term(n=1000)
    print(ratio)


if __name__ == "__main__":
    main()
