# collatz.py
#
# If even, a is divided by 2
# If odd, a is multiplied by 3 and add 1 (3n + 1)
#
# The Collatz conjecture is:
# "...that no matter what value of n, the sequence will always reach 1"
#
# https://github.com/martinluckett/MathsStuff
# Martin Luckett 2019


def collatz(number, max_iterations=10000):

    a = number
    counter = 0

    while a != 1 and counter < max_iterations:
        counter += 1
        if a % 2 == 0:
            a = int(a/2)
        else:
            a = a * 3 + 1

    if counter < max_iterations:
        return counter
    else:
        return "Maximum iteration limit reached"


def test():
    n = 333
    col = collatz(number=n, max_iterations=1000)
    print("Collatz: {0} reached 1 in {1} steps".format(n, col))


if __name__ == "__main__":
    test()





