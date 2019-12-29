# mersenne.py
#
#  Mersenne Numbers
#
# https://github.com/martinluckett/MathsStuff
# Martin Luckett 2019

from Sequences.Sequence import Sequence


def main():
    mer = Sequence("Mersenne", first_term=0, second_term=1,
                   multiplier_first_term=0, multiplier_second_term=2, constant_factor=1)

    result = mer.get_sequence(number_of_terms=100)
    print(result)

    term32 = mer.nth_term(n=32)
    print(term32)

    term200 = mer.nth_term(n=200)
    print(term200)

    mer.precision = 50
    ratio = mer.ratio_at_nth_term(n=1000)
    print(ratio)


if __name__ == "__main__":
    main()
