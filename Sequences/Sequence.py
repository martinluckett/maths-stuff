# sequences.py
#
# create a sequence such with initial terms: first_term and second_term
# generate new terms by:
#
# new term = (first_term ** (exponent)) * (multiplier)
#               + (second_term ** (exponent)) * (multiplier)
#               + constant_factor
#
# default multiplier is 1
# default exponent is 1
# default constant is 0
#
# https://github.com/martinluckett/MathsStuff
# Martin Luckett 2019

from decimal import *


class Sequence:
    def __init__(self, name, first_term=0, second_term=1,
                 multiplier_first_term=1, multiplier_second_term=1,
                 exponent_first_term=1, exponent_second_term=1, constant_factor=0):
        self.name = name
        self.first_term = first_term
        self.second_term = second_term
        self.multiplier_first_term = multiplier_first_term
        self.multiplier_second_term = multiplier_second_term
        self.exponent_first_term = exponent_first_term
        self.exponent_second_term = exponent_second_term
        self.constant_factor = constant_factor
        self.number_of_terms = 100
        self.result = []
        self.precision = 20
        #self.test()

    def generate_sequence(self):
        self.result = []

        a = self.first_term
        b = self.second_term
        c = self.multiplier_first_term
        d = self.multiplier_second_term
        e = self.exponent_first_term
        f = self.exponent_second_term
        g = self.constant_factor

        # print(a,b, c, d, e, f, g)

        # add the first term
        self.result.append(a)

        # generate the sequence
        while len(self.result) < self.number_of_terms + 1:
            self.result.append(b)

            # new a = old b, new b = calculated term
            a, b = b, (c * (a ** e)) + (d * (b ** f)) + g

        return

    def get_sequence(self, number_of_terms):

        if number_of_terms > len(self.result):
            self.number_of_terms = number_of_terms
            self.generate_sequence()
            return self.result
        else:
            return self.result[0:number_of_terms]

    def nth_term(self, n):
        if n > len(self.result):
            self.number_of_terms = n
            self.generate_sequence()

        return self.result[n]

    def ratio_at_nth_term(self, n):
        getcontext().prec = self.precision

        nth_term = Decimal(self.nth_term(n))
        previous_term = Decimal(self.nth_term(n-1))

        result = nth_term / previous_term

        return result



    def test(self):
        result = self.get_sequence(100)
        print(result)
