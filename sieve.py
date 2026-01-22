#! /usr/bin/env python3

import time

"""
Generator to generate the series of prime numbers.
Implementation of the "sieve of Eratosthenes" from SICP 3.5.2 as a python generator.
Apparently not the real sieve of Eratosthenes, apparently actually Turner's sieve.
"""

WANT_TO_GO_HIGHER=False

def divisible(x, y):
    return x % y == 0

def integers_starting_from(n):
    while True:
        yield n
        n += 1

def sieve(stream):
    car = next(stream)
    yield car
    yield from sieve(filter(lambda x: not divisible(x, car), stream))

def primes():
    yield from sieve(integers_starting_from(2))

if __name__ == '__main__':
    if WANT_TO_GO_HIGHER:
        import sys
        print("Recursion limit:\t{}".format(sys.getrecursionlimit()))
        sys.setrecursionlimit(20000)
        print("New limit:\t{}".format(sys.getrecursionlimit()))

    for p in primes():
        print(p)
        time.sleep(1)
