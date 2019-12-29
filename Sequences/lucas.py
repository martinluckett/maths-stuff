# lucas.py
#
#  Lucas Numbers
#
# https://github.com/martinluckett/MathsStuff
# Martin Luckett 2019

from Sequences.Sequence import Sequence


def main():
    luc = Sequence("Lucas", first_term=2, second_term=1)

    result = luc.get_sequence(number_of_terms=100)
    print(result)

    term38 = luc.nth_term(n=38)
    print(term38)

    term200 = luc.nth_term(n=200)
    print(term200)

    luc.precision = 50
    ratio = luc.ratio_at_nth_term(n=1000)
    print(ratio)


if __name__ == "__main__":
    main()
