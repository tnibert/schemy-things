#! /usr/bin/env python

from math import sqrt


def fib(n):
    """
    Find fibonacci numbers in O(1) via solved recurrence relation.
    round() is just used to remove floating point precision error.
    """
    return round((1/sqrt(5)) * ((1+sqrt(5))/2) ** n - (1/sqrt(5)) * ((1-sqrt(5))/2) ** n)


if __name__ == '__main__':
    for i in range(1, 100):
        print(fib(i))
