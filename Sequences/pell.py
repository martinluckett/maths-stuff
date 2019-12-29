# pell.py
#
#  Pell Numbers
#
# https://github.com/martinluckett/MathsStuff
# Martin Luckett 2019

from Sequences.Sequence import Sequence


def main():
    pel = Sequence("Pell", first_term=0, second_term=1, multiplier_first_term=1, multiplier_second_term=2)

    result = pel.get_sequence(number_of_terms=100)
    print(result)

    term31 = pel.nth_term(n=31)
    print(term31)

    term200 = pel.nth_term(n=200)
    print(term200)

    pel.precision = 50
    ratio = pel.ratio_at_nth_term(n=1000)
    print(ratio-1)


if __name__ == "__main__":
    main()
